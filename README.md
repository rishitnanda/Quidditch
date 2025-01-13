# Quidditch Moves

## Chasers [Score goals throwing the Quaffle through opponent's hoops.]

### /Dodge_Player opponent_name
- <ins>Evade an incoming player.</ins>
- Activate: After Snatch by Opponent.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Dodge_Bludger
- <ins>Evade an incoming bludger.</ins>
- Activate: After Beat Bludger, Double Hit by Opponent.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- <ins>Disrupt a player's focus.</ins>
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Pass teammate_name
- <ins>Pass the Quaffle to a teammate.</ins>
- Activate: If has Quaffle.  
- Counter: None  
- Effect: Increase scoring chance.  
- Chance of Warning: No  
- Cooldown: None  

### /Shoot
- <ins>Attempt to score in a goalpost.</ins>
- Activate: If has Quaffle.  
- Counter: Block  
- Effect: Reduces strength.  
- Chance of Warning: No  
- Cooldown: None  

### /Dunk
- <ins>Attempt a powerful or tricky shot to score.</ins>
- Activate: If has Quaffle.  
- Counter: None  
- Effect: Decreases strength and defense.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Snatch or /Snatch opponent_name
- <ins>Attempt to pick up dropped Quaffle or snatch Quaffle from opponent.</ins>
- Activate: If not has Quaffle. No ongoing snatch event.  
- Counter: Dodge Player  
- Effect: Reduces opponent morale  
- Chance of Warning: No  
- Cooldown: None  

### /Wait
- <ins>Wait for another action to be enabled.</ins>
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

## Beaters [Use Bludgers to disrupt the opposing team's players]

### /Namecall opponent_name
- <ins>Disrupt a player's focus.</ins>  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Defend teammate_name
- <ins>Protect other players.</ins>  
- Activate: After Beat Bludger, Double Hit by Opponent.  
- Counter: None  
- Effect: Prevent bludger hit.  
- Chance of Warning: No  
- Cooldown: None  

### /Beat_Bludger opponent_name
- <ins>Hit a bludger towards an opponent.</ins>  
- Counter: Dodge Bludger, Defend, Beat Bludger  
- Effect: Reduces opponent’s handling.  
- Chance of Warning: No  
- Cooldown: 1 Action  

### /Double_Hit opponent_name
- <ins>Beat two bludgers in rapid succession.</ins>  
- Activate: No incoming bludger towards beater  
- Counter: Dodge Bludger, Defend  
- Effect: Reduces defense and handling.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Wait
- <ins>Wait for another action to be enabled.</ins>  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

## Keepers [Guard the hoops to prevent the opposing team from scoring.]

### /Dodge_Bludger
- <ins>Evade a bludger.</ins>  
- Activate: After Beat Bludger, Double Hit.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- <ins>Disrupt a player's focus.</ins>  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Defend
- <ins>Set up a defensive strategy.</ins>  
- Counter: None  
- Effect: Increases defense for the team.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Block
- <ins>Block a shot at the goalposts.</ins>  
- Activate: After Shoot by Opponent.  
- Counter: None  
- Effect: Increases defense.  
- Chance of Warning: No  
- Cooldown: None  

### /Wait
- <ins>Wait for another action to be enabled.</ins>  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

### /Slow_Hover
- <ins>Hover slowly in front of goal posts.</ins>  
- Counter: None  
- Effect: Increases defense, increases strength, decreases speed.  
- Chance of Warning: No  
- Cooldown: 1 Action

### /Pass teammate_name
- <ins>Pass the Quaffle to a teammate.</ins>  
- Activate: If has Quaffle.  
- Counter: None  
- Effect: No additional effect.  
- Chance of Warning: No  
- Cooldown: None  

## Seekers [Catch the Golden Snitch to end the game and score 150 points.]

### /Dive
- <ins>Attempt to capture the Snitch.</ins>  
- Activate: If snitch spotted.  
- Counter: Dodge Bludger  
- Effect: Reduces defense. Increase chance of losing sight of snitch.  
- Chance of Warning: No  
- Cooldown: None  

### /Dodge_Bludger
- <ins>Evade an incoming bludger.</ins>  
- Activate: After Beat Bludger, Double Hit.  
- Counter: Dodge Bludger  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- <ins>Disrupt a player's focus.</ins>  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Slow_Hover
- <ins>Hover slowly to anticipate the Snitch's movements.</ins>  
- Activate: If snitch not spotted.  
- Counter: None  
- Effect: Increases agility, reduces speed. Increases chance of spotting snitch.  
- Chance of Warning: No  
- Cooldown: 1 Action  

### /Wait
- <ins>Wait for another action to be enabled.</ins>  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  
- Cooldown: None
