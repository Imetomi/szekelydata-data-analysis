import numpy as np
from globeplot.plotting import GlobePlot


# data and coordinates are one- or two-dimensional NumPy arrays
lats = np.array([40.7127753,  -25.78668, 38.50710])
lons = np.array([-73.989308, -116.33826, 20.73130])
values = np.array([1000, 10000, 100])

plot = GlobePlot(lats=lats, lons=lons, data=values)

# append more data to the plot if needed
#plot.append(more_lats, more_lons, more_values)

plot.show(title="Szeklers on Earth", creator='Tamas Imets', creator_addr='',
          code_link='http://...')