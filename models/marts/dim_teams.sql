select 
team_id,
team_name,
debut_year,
team_abbrev

from {{ ref('stg_teams') }}
