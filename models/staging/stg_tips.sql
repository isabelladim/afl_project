select 
cast("DATE" as date) as tip_date,
cast(hmargin as integer) as home_margin,
cast(err as integer) as error,
cast(venue as text) as venue,
cast(hteam as text) as home_team,
cast(sourceid as text) as source_id,
cast(margin as integer) as margin,
cast(hconfidence as float) as home_confidence,
cast(correct as integer) as correct,
cast(source as text) as source,
cast(tip as text) as tip,
cast(bits as text) as bits,
cast(gameid as text) as game_id,
cast("YEAR" as integer) as season,
cast(hteamid as text) as home_team_id,
cast(Updated as timestamp) as updated_at,
cast(ateamid as text) as away_team_id,
cast(ateam as text) as away_team,
cast(tipteamid as text) as tip_team_id,
cast(confidence as float) as confidence,
cast(round as integer) as round

from {{ source('raw', 'tips') }}
