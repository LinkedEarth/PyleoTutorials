"""Save a local backup of the ERSSTv6 data used in notebooks/L2_correlations.ipynb.

The notebook reads NOAA ERSSTv6 monthly SST from the NOAA PSL THREDDS server,
which is sometimes rate-limited or down. This script saves the only part the
notebook uses (the tropical Pacific box, all months) to a small netCDF file,
so the notebook can fall back on it.

Run it from the repository root, when the THREDDS server is up:

    python data/make_ersstv6_subset.py

Output: data/ersstv6_tropical_pacific.nc
"""

from datetime import date
from pathlib import Path

import xarray as xr

URL = 'https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v6/sst.mnmean.nc'
OUT = Path(__file__).parent / 'ersstv6_tropical_pacific.nc'

# Same box as the notebook. ERSST latitudes run north to south and longitudes
# 0-360, so the slices keep that order and the notebook's own .sel() still works.
LAT = slice(15, -15)
LON = slice(140, 280)

ds = xr.open_dataset(URL)
sub = ds[['sst']].sel(lat=LAT, lon=LON).load()

sub.attrs.update(ds.attrs)
sub.attrs['subset_source'] = URL
sub.attrs['subset_region'] = 'lat 15N to 15S, lon 140E to 280E (80W)'
sub.attrs['subset_date'] = date.today().isoformat()
sub.attrs['subset_script'] = 'data/make_ersstv6_subset.py (PyleoTutorials)'

encoding = {'sst': {'dtype': 'float32', 'zlib': True, 'complevel': 5}}
sub.to_netcdf(OUT, encoding=encoding)

print(f'Wrote {OUT} ({OUT.stat().st_size / 1e6:.1f} MB): '
      f'{sub.sizes["time"]} months, {sub.sizes["lat"]} x {sub.sizes["lon"]} grid, '
      f'{str(sub.time.values[0])[:7]} to {str(sub.time.values[-1])[:7]}')
