"""
Allows a streamlit user to report an incident, which is stored in SELF_REPORTING_RAW table.
Should be run from the Snowflake UI!
"""

# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

session = get_active_session()

db = 'WID_HACKATHON'
schema = 'DATA'
table_name = 'SELF_REPORTING_RAW'

full_table_name = db + '.' + schema + '.' + table_name

age_buckets = [
"0-18",
"18-24",
"25-34",
"35-44",
"45-54",
"55-64",
"65+"
]
ethnicities = ["White - English, Welsh, Scottish, Northern Irish or British, Irish, Gypsy or Irish Traveller, Any other White background",
"Mixed or multiple ethnic groups - White and Black Caribbean, White and Black African, White and Asian, Any other Mixed or multiple ethnic background",
"Asian or Asian British - Indian, Pakistani, Bangladeshi, Chinese, Any other Asian background",
"Black, Black British, Caribbean, or African - African, Caribbean, Any other Black, Black British, or Caribbean background",
"Other ethnic group - Arab, Any other ethnic group"]

with st.form("report_crime"):
   st.write("Report your crime using the form below")
   incident_type = st.selectbox(
       label="Crime Type",
       options=('Cat Call','Sexual Comments','Public Staring')
   )
   description = st.text_area(
       label='Describe the incident.',
   )
   location = st.text_input(
       label="Location. Enter the town in which the incident took place."
   )
   # date = st.date_input(
   #     label='When did the incident take place?',
   #     key='date'
   # )
   # time = st.time_input(
   #     label="What time did the incident take place?",
   #     key="time"
   # )
   reported_police = st.selectbox(
       label="Was the incident reported to the police?",
       options=("Yes","No")
   )
   victim_age = st.selectbox(
       label="What was the victim's age at the time of incident?",
       options=age_buckets
   )
   victim_gender = st.selectbox(
       label='Victim gender',
       options=("Woman","Man","Non-binary","A gender not in here")
   )
   victim_ethnicity = st.selectbox(
       label='Victim ethnicity',
       options=ethnicities
   )
   perp_gender = st.selectbox(
       label='Perpatrator gender',
       options=("Woman","Man","Non-binary","A gender not in here")
   )
   perp_known = st.selectbox(
       label='Perpatrator known to victim?',
       options=('Yes','No')
   )
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
      query = f"""INSERT INTO {full_table_name} VALUES (
      '{incident_type}',
      '{description}',
      '{location}',
      '{reported_police}',
      '{victim_age}',
      '{victim_gender}',
      '{victim_ethnicity}',
      '{perp_gender}',
      '{perp_known}'
      )"""
      

      # write query to table which stores incidents
      session.sql(query).collect()
      st.write("Incident successfully submitted")
