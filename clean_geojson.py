import pandas as pd
import geopandas as gpd
import numpy as np

grid_cells_gdf = gpd.read_file('grid_cells_orig.geojson')

grid_cell_ids = grid_cells_gdf['layer'].astype(str).values.tolist()
grid_cell_ids = [id.replace('_shape', '') for id in grid_cell_ids]

grid_cells_gdf['grid_cell_id'] = grid_cell_ids
grid_cells_gdf.drop(columns=['layer', 'path'], inplace=True)

grid_cells_gdf.to_file('grid_cells.geojson', driver='GeoJSON')
