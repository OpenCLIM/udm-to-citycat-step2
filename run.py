import geopandas as gpd
import os
from citycatio.inputs import Buildings
from citycatio.inputs import GreenAreas

# move files to output dir
result_data_dir = '/data/inputs'
output_data_dir = '/data/outputs'

# make output dir if not exists
os.makedirs(output_data_dir, exist_ok=True)

# Reading in the buildings shapefile
gdf = gpd.read_file(os.path.join(result_data_dir,'all_buildings.shp'))
Buildings(gdf).write(output_data_dir)

# Just printing the output of the file to show what's in it
with open(os.path.join(output_data_dir,'Buildings.txt')) as f:
  print(*f.readlines()[:50])

# Reading in the greenspaces shapefile
gdf = gpd.read_file(os.path.join(result_data_dir,'all_greenareas.shp'))
GreenAreas(gdf).write(output_data_dir)

# Just printing the output of the file to show what's in it
with open(os.path.join(output_data_dir,'GreenAreas.txt')) as f:
    print(*f.readlines()[:50])