# Quidditch Moves

## Chasers [Score goals by throwing the Quaffle through the opponent's hoops.]

### /Dodge_Player opponent_name
- _Evade an incoming player._
- Activate: After Snatch by Opponent.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Dodge_Bludger
- _Evade an incoming bludger._
- Activate: After Beat Bludger, Double Hit by Opponent.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- _Disrupt a player's focus._
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Pass teammate_name
- _Pass the Quaffle to a teammate._
- Activate: If has Quaffle.  
- Counter: None  
- Effect: Increase scoring chance.  
- Chance of Warning: No  
- Cooldown: None  

### /Shoot
- _Attempt to score in a goalpost._
- Activate: If has Quaffle.  
- Counter: Block  
- Effect: Reduces strength.  
- Chance of Warning: No  
- Cooldown: None  

### /Dunk
- _Attempt a powerful or tricky shot to score._
- Activate: If has Quaffle.  
- Counter: None  
- Effect: Decreases strength and defense.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Snatch or /Snatch opponent_name
- _Attempt to pick up dropped Quaffle or snatch Quaffle from opponent._
- Activate: If not has Quaffle. No ongoing snatch event.  
- Counter: Dodge Player  
- Effect: Reduces opponent morale  
- Chance of Warning: No  
- Cooldown: None  

### /Wait
- _Wait for another action to be enabled._
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

## Beaters [Use Bludgers to disrupt the opposing team's players]

### /Namecall opponent_name
- _Disrupt a player's focus._  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Defend teammate_name
- _Protect other players._  
- Activate: After Beat Bludger, Double Hit by Opponent.  
- Counter: None  
- Effect: Prevent bludger hit.  
- Chance of Warning: No  
- Cooldown: None  

### /Beat_Bludger opponent_name
- _Hit a bludger towards an opponent._  
- Counter: Dodge Bludger, Defend, Beat Bludger  
- Effect: Reduces opponent’s handling.  
- Chance of Warning: No  
- Cooldown: 1 Action  

### /Double_Hit opponent_name
- _Beat two bludgers in rapid succession._  
- Activate: No incoming bludger towards beater  
- Counter: Dodge Bludger, Defend  
- Effect: Reduces defense and handling.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Wait
- _Wait for another action to be enabled._  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

## Keepers [Guard the hoops to prevent the opposing team from scoring.]

### /Dodge_Bludger
- _Evade a bludger._  
- Activate: After Beat Bludger, Double Hit.  
- Counter: None  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- _Disrupt a player's focus._  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Defend
- _Set up a defensive strategy._  
- Counter: None  
- Effect: Increases defense for the team.  
- Chance of Warning: No  
- Cooldown: 2 Actions  

### /Block
- _Block a shot at the goalposts._  
- Activate: After Shoot by Opponent.  
- Counter: None  
- Effect: Increases defense.  
- Chance of Warning: No  
- Cooldown: None  

### /Wait
- _Wait for another action to be enabled._  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  

### /Slow_Hover
- _Hover slowly in front of goal posts._  
- Counter: None  
- Effect: Increases defense, increases strength, decreases speed.  
- Chance of Warning: No  
- Cooldown: 1 Action

### /Pass teammate_name
- _Pass the Quaffle to a teammate._  
- Activate: If has Quaffle.  
- Counter: None  
- Effect: No additional effect.  
- Chance of Warning: No  
- Cooldown: None  

## Seekers [Catch the Golden Snitch to end the game and score 150 points for their team.]

### /Dive
- _Attempt to capture the Snitch._  
- Activate: If snitch spotted.  
- Counter: Dodge Bludger  
- Effect: Reduces defense. Increase chance of losing sight of snitch.  
- Chance of Warning: No  
- Cooldown: None  

### /Dodge_Bludger
- _Evade an incoming bludger._  
- Activate: After Beat Bludger, Double Hit.  
- Counter: Dodge Bludger  
- Effect: Reduces handling.  
- Chance of Warning: No  
- Cooldown: None  

### /Namecall opponent_name
- _Disrupt a player's focus._  
- Counter: None  
- Effect: Reduces opponent’s morale.  
- Chance of Warning: Yes  
- Cooldown: 1 Action  

### /Slow_Hover
- _Hover slowly to anticipate the Snitch's movements._  
- Activate: If snitch not spotted.  
- Counter: None  
- Effect: Increases agility, reduces speed. Increases chance of spotting snitch.  
- Chance of Warning: No  
- Cooldown: 1 Action  

### /Wait
- _Wait for another action to be enabled._  
- Counter: None  
- Effect: No additional effect  
- Chance of Warning: No  
- Cooldown: None  
- Cooldown: None
