"""Check that every notebook runs on the standard "python3" kernel.

A notebook saved from a custom kernel (e.g. one named "pyleo") records that
name in its metadata. Nobody else has a kernel by that name, so CI (nbmake)
and readers' Jupyter installations fail to start it. Notebooks must either
declare a kernelspec named "python3" or declare none (Jupyter then uses the
default kernel, which is python3).

Usage, from the repository root:

    python .github/scripts/check_kernelspec.py          # report, exit 1 on problems
    python .github/scripts/check_kernelspec.py --fix    # rewrite offending notebooks

--fix edits only the kernelspec block of the raw file, so the rest of the
notebook (outputs, formatting) is left exactly as it was.
"""

import json
import re
import sys
from pathlib import Path

KERNEL = 'python3'
DISPLAY = 'Python 3 (ipykernel)'
SKIP_DIRS = {'.ipynb_checkpoints', '.virtual_documents', '_build', '.git'}

# The kernelspec block holds only flat string fields, so no nested braces.
BLOCK = re.compile(r'("kernelspec"\s*:\s*\{)([^{}]*)(\})')


def notebooks(root):
    for path in sorted(root.rglob('*.ipynb')):
        if not SKIP_DIRS.intersection(path.parts):
            yield path


def fix_block(match):
    body = re.sub(r'("name"\s*:\s*)"[^"]*"', rf'\1"{KERNEL}"', match.group(2))
    body = re.sub(r'("display_name"\s*:\s*)"[^"]*"', rf'\1"{DISPLAY}"', body)
    return match.group(1) + body + match.group(3)


def main(fix=False):
    root = Path('.')
    bad = []
    for path in notebooks(root):
        raw = path.read_text(encoding='utf-8')
        try:
            spec = json.loads(raw).get('metadata', {}).get('kernelspec')
        except json.JSONDecodeError as err:
            print(f'::error file={path}::not valid JSON ({err})')
            bad.append(path)
            continue
        if spec is None or spec.get('name') == KERNEL:
            continue
        name = spec.get('name')
        if fix:
            new, n = BLOCK.subn(fix_block, raw, count=1)
            if n == 1 and json.loads(new)['metadata']['kernelspec'].get('name') == KERNEL:
                path.write_text(new, encoding='utf-8')
                print(f'fixed {path}: kernel "{name}" -> "{KERNEL}"')
                continue
            print(f'could not fix {path} automatically; set its kernel to "{KERNEL}" by hand')
        else:
            # ::error makes GitHub annotate the file in the PR
            print(f'::error file={path}::kernelspec name is "{name}", expected "{KERNEL}"')
        bad.append(path)

    if bad:
        print(f'\n{len(bad)} notebook(s) do not use the "{KERNEL}" kernel.')
        if not fix:
            print('Run: python .github/scripts/check_kernelspec.py --fix  (then commit)')
        return 1
    print(f'All notebooks use the "{KERNEL}" kernel (or the default).')
    return 0


if __name__ == '__main__':
    sys.exit(main(fix='--fix' in sys.argv[1:]))
