 Chaser Actions:
1. Dodge Player: Evade an incoming player.  
   Activate: After Snatch by Opponent.
   Counter: None
   Effect: Reduces handling by 10%.
   Success Rate: `(Handling + Defense + Agility) / 3`
   Chance of Warning: 0%
   Cooldown: None

2. Dodge Bludger: Evade an incoming bludger.  
   Activate: After Beat Bludger, Double Hit by Opponent.
   Counter: None
   Effect: Reduces handling by 10%.  
   Success Rate: `(Handling + Defense + Agility) / 3`
   Chance of Warning: 0%
   Cooldown: None

3. Namecall: Disrupt a player's focus.
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

4. Pass: Pass the Quaffle to a teammate. 
   Activate: If has Quaffle. 
   Counter: None
   Effect: Increase scoring chance and snatch chance.
   Success Rate: `(Accuracy + Handling) / 2`
   Chance of Warning: 0%
   Cooldown: None

5. Shoot: Attempt to score in a goalpost.  
   Activate: If has Quaffle. 
   Counter: Block
   Effect: Reduces strength by 3%.  
   Success Rate: `(Accuracy * 0.4) + (Handling * 0.3) + (Strength * 0.2) + (Agility * 0.1) + (Morale * 0.05)`
   Chance of Warning: 0%
   Cooldown: None

6. Dunk: Attempt a powerful or tricky shot to score. 
   Activate: If has Quaffle. 
   Counter: None 
   Effect: Decreases strength and defense by 7%.  
   Success Rate: `(Accuracy * 0.1) + (Handling * 0.1) + (Strength * 0.1) + (Agility * 0.1) + (Morale * 0.1)`
   Chance of Warning: 0%
   Cooldown: 2 Actions

7. Snatch: Attempt to snatch quaffle from opponent.
   Activate: If not has Quaffle. 
   Counter: Dodge Player
   Effect: Reduces opponent morale by 2% (if Success)
   Success Rate: `(Handling * 0.3) + (Strength * 0.2) + (Agility * 0.1)`
   Chance of Warning: 0%
   Cooldown: None

8. Sneak and Snatch: Sneak behind the opponent and swiftly snatch the quaffle.
   Activate: If not has Quaffle. 
   Counter: None
   Effect: Reduces opponent morale by 2% (if Success)
   Success Rate: `(Handling * 0.2) + (Strength * 0.1) + (Agility * 0.05)`
   Chance of Warning: 0%
   Cooldown: 2 Actions

9. Wait: Wait for another action to be enabled.
   Counter: None
   Effect: Any random trait becomes 1.1 times
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

---
 Beater Actions:

1. Namecall: Disrupt a player's focus.  
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

2. Defend: Protect other players.
   Activate: After Beat Bludger, Double Hit by Opponent.
   Counter: None
   Effect: Prevent bludger hit.
   Success Rate: `(Strength + Morale) / 2`
   Chance of Warning: 0%
   Cooldown: None

3. Beat Bludger: Hit a bludger towards an opponent.
   Counter: Dodge Bludger
   Effect: Reduces opponent’s handling by 5% (if Success).
   Success Rate: `(Accuracy + Handling - Agility) / 2`
   Injury Rate: 3%
   Wound Rate: 1%
   Chance of Warning: 0%
   Cooldown: None

4. Double Hit: Beat two bludgers in rapid succession.
   Counter: Dodge Bludger
   Effect: Reduces defense and handling by 10% (if Success).
   Success Rate: `(Speed + Defense) / 2`
   Injury Rate: 5.9%
   Wound Rate: 1.7%
   Chance of Warning: 0%
   Cooldown: 3 Actions

5. Wait: Wait for another action to be enabled.
   Counter: None
   Effect: Any random trait becomes 1.1 times
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

---

 Seeker Actions:
1. Dive: Attempt to capture the Snitch. 
   Activate: If snitch spotted.
   Counter: Dodge Bludger
   Effect: Reduces defense by 10%.  
   Success Rate: `(Speed + Handling) / 2`
   Chance of Warning: 0%
   Cooldown: None

2. Dodge Bludger: Evade an incoming bludger. 
   Activate: After Beat Bludger, Double Hit.
   Counter: Dodge Bludger 
   Effect: Reduces handling by 10%.    
   Success Rate: `(Handling + Defense - Agility) / 2`
   Chance of Warning: 0%
   Cooldown: None

3. Namecall: Disrupt a player's focus.  
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

4. Slow Hover: Hover slowly to anticipate the Snitch's movements.  
   Effect: Increases agility by 10%, reduces speed by 10%. Increases chance of spotting snitch by 2%.
   Success Rate: `(Agility + Handling) / 2`
   Chance of Warning: 0%
   Cooldown: None

5. Wait: Wait for another action to be enabled.
   Counter: None
   Effect: Any random trait becomes 1.1 times
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

---

 Keeper Actions:
1. Dodge Bludger: Evade a bludger.  
   Activate: After Beat Bludger, Double Hit.
   Effect: Reduces handling by 10%. 
   Success Rate: `(Handling + Defense - Agility) / 2`
   Chance of Warning: 0%
   Cooldown: None

2. Namecall: Disrupt a player's focus.  
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

3. Defend: Set up a defensive strategy.  
   Effect: Increases defense for the team by 5%.  
   Success Rate: `(Agility + Morale) / 2`
   Chance of Warning: 0%
   Cooldown: 2 Actions.

4. Block: Block a shot at the goalposts.  
   Effect: Increases defense by 15%.  
   Success Rate: `(Strength + Morale + Defense) / 3`
   Chance of Warning: 0%
   Cooldown: None

5. Wait: Wait for another action to be enabled.
   Counter: None
   Effect: Any random trait becomes 1.1 times
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None