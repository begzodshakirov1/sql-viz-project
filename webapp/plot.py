import altair as alt
import pandas as pd
from vega_datasets import data

def plot_wells(well_locations):
	states = alt.topo_feature(data.us_10m.url, feature='states')

	# US states background
	background = alt.Chart(states).mark_geoshape(
	    fill='lightgray',
	    stroke='white'
	).properties(
	    width=500,
	    height=300
	).project('albersUsa')

	wells_df = pd.DataFrame(well_locations, columns = ['latitude', 'longitude', 'depth', 'gradient'])

	wells = (alt.Chart(wells_df).mark_circle()
            .encode(latitude = 'latitude', longitude = 'longitude', 
                    color = alt.Color('gradient', scale = alt.Scale(scheme='inferno'), title='Gradient (°C/m)'),
                    tooltip = [alt.Tooltip('depth', title = 'Depth (m)'),
                              alt.Tooltip('gradient', title = 'Gradient (°C/m)'
                                         , format = '0.3f')])
            .properties(title = 'Well locations')
        	)
	well_map = background + wells

	return well_map.to_json()