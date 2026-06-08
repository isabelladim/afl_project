select 
cast("name" as text) as team_name,
cast(rank as integer) as rank,
cast(goals_for as integer) as goals_for,
cast(draws as integer) as draws,
cast(pts as integer) as points,
cast("percentage" as float) as percentage,
cast(id as text) as team_id,
cast(behinds_for as integer) as behinds_for,
cast(wins as integer) as wins,
cast(goals_against as integer) as goals_against,
cast(behinds_against as integer) as behinds_against,
cast(against as integer) as against,
cast(losses as integer) as losses,
cast(played as integer) as played,
cast("for" as integer) as for_points

from {{ source('raw', 'standings') }}
