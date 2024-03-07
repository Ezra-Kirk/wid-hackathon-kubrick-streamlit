create or replace table wid_hackathon.data.incident_map_agg as 
select round(longitude, 2) as latitude -- no location information for rape, sexual assault data, presumably due to privacy
    , round(latitude, 2) as longitude
    , crime_type
    , count(*) as number_of_incidents
from wid_hackathon.data.incident_map
where latitude is not null and longitude is not null
group by 1, 2, 3;