--homne perspective

select
    game_id, season, round, 
    home_team_id as team_id,
    home_team as team_name,
    home_score as score,
    away_score as opponent_score,
    away_team as opponent,
    winner,
        case when winner is null then null
        when winner = home_team then true
        else false 
        end as won_game
from {{ ref('stg_games') }}

union all 

-- away perspective
select
    game_id, season, round, 
    away_team_id as team_id,
    away_team as team_name,
    away_score as score,
    home_score as opponent_score,
    home_team as opponent,
    winner,
    case when winner is null then null
        when winner = away_team then true
        else false 
        end as won_game
from {{ ref('stg_games') }}
