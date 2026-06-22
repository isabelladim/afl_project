select team_name,
sum(case when 
won_game = TRUE then 4 
when score = opponent_score then 2
else 0 end) as points,
round(100.0 * sum(score) / nullif(sum(opponent_score), 0), 2) as percentage

from {{ ref('fct_games') }}
where team_name is not null
group by team_name