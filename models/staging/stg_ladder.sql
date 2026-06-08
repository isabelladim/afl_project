select 
cast(rank as integer) as rank,
cast(sourceid as text) as source_id,
cast(source as text) as source,
cast("percentage" as float) as percentage,
cast(swarms as text) as swarms,
cast(wins as integer) as wins,
cast("year" as integer) as season,
cast(updated as timestamp) as updated_at,
cast(team as text) as team_name,
cast(mean_rank as float) as mean_rank,
cast(round as integer) as round,
cast(teamid as text) as team_id,
cast(dummy as integer) as dummy


from {{ source('raw', 'ladder') }}
