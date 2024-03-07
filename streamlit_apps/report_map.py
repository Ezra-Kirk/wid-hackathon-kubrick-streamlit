# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
import pandas as pd
import numpy as np
from snowflake.snowpark.functions import col, to_decimal
import pydeck as pdk
 
# Write directly to the app
st.title("Crime Heatmap by Crime Type")
 
 
# Get the current credentials
session = get_active_session()
# carto_crime = session.table('WID_HACKATHON_PRIVATE_DATASETS.CARTO.DEMOGRAPHICS_CRIME_LONDON_LATLON_V1_QUARTERLY_V1')
# reported_crime = session.table('FACTS_AND_DIMENSIONS_ALL_DATA."Police"')
incident_map = session.table('WID_HACKATHON.DATA.INCIDENT_MAP_AGG')
crime_types = session.table('WID_HACKATHON.DATA.INCIDENT_MAP_AGG').select('crime_type').distinct().toPandas()
# st.table(table)
 
# Type of crime selector
# option = st.selectbox(
#     'Show map by certain crime type',
#     (carto_crime.select("crime_type").distinct().toPandas()))
 
# st.write('The map below filters for:', option)
 
crime_type = st.selectbox(label='Select a crime type to filter'
             , options=crime_types)
 
data = incident_map.select("latitude", "longitude", "number_of_incidents").dropna().filter(col("crime_type") == crime_type).collect()
# st.write(data)
 
# map_df = form_data.select(to_pandas().
#     to_decimal("longitude", 10, 8).alias("lon"),
#     to_decimal("latitude", 10, 8).alias("lat")
# ).limit(100).to_pandas()
 
st.map(data)