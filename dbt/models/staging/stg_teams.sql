select 
cast("NAME" as text) as team_name,
cast(debut as bigint) as debut_year,
cast(id as text) as team_id,
cast(abbrev as text) as team_abbrev

from {{ source('raw', 'teams') }}
