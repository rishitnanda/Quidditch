 Chaser Actions:
1. Dodge Player: Evade an incoming player.  
   Activate: After Snatch by Opponent.
   Counter: None
   Effect: Reduces handling by 10%.
   Success Rate: `(Handling + Defense + Agility) / 3`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "With a swift sidestep, {player} skillfully evades {opponent}’s pursuit, gracefully maintaining control of the Quaffle. Their handling proves exceptional as they regain their momentum."
   - Failure: "{player} attempts to dodge but fails to shake off {opponent}, their movements too predictable. {opponent} closes in, forcing {player} to lose possession of the Quaffle."

   *{quaffle_owner} has the quaffle*

2. Dodge Bludger: Evade an incoming bludger.  
   Activate: After Beat Bludger, Double Hit by Opponent.
   Counter: None
   Effect: Reduces handling by 10%.  
   Success Rate: `(Handling + Defense + Agility) / 3`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "{player} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback."
   - Failure + No Effect: "A well-timed bludger strikes {player} squarely, knocking them off course. Their handling falters as they struggle to regain their footing."
   - Wounded:
   - Injured:

3. Namecall: Disrupt a player's focus.
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

   - Success + Warn: "{player} delivers a biting taunt to {opponent}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {player}."
   - Success + No Warn: "{Opponent} looks fazed, wonder what happened."
   - Failure + Warn: "{player} delivers a biting taunt to {opponent}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {player}."
   - Failure + No Warn: "{opponent} swoops past {player}."

4. Pass: Pass the Quaffle to a teammate. 
   Activate: If has Quaffle. 
   Counter: None
   Effect: Increase scoring chance and snatch chance.
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

   - "{player} releases a perfect pass, the Quaffle soaring through the air with pinpoint accuracy. {teammate} catches it effortlessly, continuing the offensive without missing a beat."

   *{quaffle_owner} has the quaffle*

5. Shoot: Attempt to score in a goalpost.  
   Activate: If has Quaffle. 
   Counter: Block
   Effect: Reduces strength by 3%.  
   Success Rate: `(Accuracy * 0.4) + (Handling * 0.3) + (Strength * 0.2) + (Agility * 0.1) + (Morale * 0.05)`
   Chance of Warning: 0%
   Cooldown: None

   - "{player} lines up and fires a calculated shot. The Quaffle arcs gracefully through the air, a flawless display of precision and strength."

6. Dunk: Attempt a powerful or tricky shot to score. 
   Activate: If has Quaffle. 
   Counter: None 
   Effect: Decreases strength and defense by 7%.  
   Success Rate: `(Accuracy * 0.1) + (Handling * 0.05) + (Strength * 0.1) + (Agility * 0.1) + (Morale * 0.1)`
   Chance of Warning: 0%
   Cooldown: 2 Actions

   - Success: "In a stunning display of athleticism, {player} leaps towards the hoop, executing a perfect dunk that leaves the crowd roaring. Their timing and power were immaculate, making the keeper's block impossible."
   - Failure: "{player} jumps to dunk, but the keeper anticipates the move and blocks it just in time. Their strength wasn't enough, and they’re left disappointed."

   *{quaffle_owner} has the quaffle*

7. Snatch: Attempt to snatch quaffle from opponent.
   Activate: If not has Quaffle. No ongoing snatch event.
   Counter: Dodge Player
   Effect: Reduces opponent morale by 2% (if Success)
   Success Rate: `(Handling * 0.3) + (Strength * 0.2) + (Agility * 0.1)`
   Chance of Warning: 0%
   Cooldown: None

8. Wait: Wait for another action to be enabled.
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

   - Success + Warn: "{player} delivers a biting taunt to {opponent}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {player}."
   - Success + No Warn: "{Opponent} looks fazed, wonder what happened."
   - Failure + Warn: "{player} delivers a biting taunt to {opponent}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {player}."
   - Failure + No Warn: "{opponent} swoops past {player}."

2. Defend: Protect other players.
   Activate: After Beat Bludger, Double Hit by Opponent.
   Counter: None
   Effect: Prevent bludger hit.
   Success Rate: `(Strength + Morale) / 2`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "{player} steps in front of {teammate} with impeccable timing, using their strength to block an incoming bludger. Their defensive play keeps the team safe and the offense in motion."
   - Failure + No Effect: "A well-timed bludger strikes {teammate} squarely, knocking them off course. Their handling falters as they struggle to regain their footing."
   - Wounded:
   - Injured:

3. Beat Bludger: Hit a bludger towards an opponent.
   Counter: Dodge Bludger, Defend, Beat Bludger
   Effect: Reduces opponent’s handling by 5% (if Success).
   Success Rate: `(Accuracy + Handling - Agility) / 2`
   Wound Rate: 3%
   Injury Rate: 1%
   Chance of Warning: 0%
   Cooldown: 1 Action

   - Success: "With a powerful swing, {player} sends a bludger flying directly towards {opponent}."
   - Failure: "{player} misses their target, the bludger sailing off course. Their aim is off, and the opposing player continues without hindrance, maintaining their offensive drive unhindered."

4. Double Hit: Beat two bludgers in rapid succession.
   Activate: No incoming bludger towards beater
   Counter: Dodge Bludger, Defend
   Effect: Reduces defense and handling by 10% (if Success).
   Success Rate: `(Speed + Defense) / 2`
   Wound Rate: 5.9%
   Injury Rate: 1.7%
   Chance of Warning: 0%
   Cooldown: 3 Actions

   - Success: "With a powerful swing, {player} sends bludgers flying directly towards {opponent}."
   - Failure: "{player} misses their target, the bludgers sailing off course. Their aim is off, and the opposing player continues without hindrance, maintaining their offensive drive unhindered."

5. Wait: Wait for another action to be enabled.
   Counter: None
   Effect: Any random trait becomes 1.1 times
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

---

 Seeker Actions:
1. Seek: Attempt to capture the Snitch. 
   Activate: If snitch spotted.
   Counter: Dodge Bludger
   Effect: Reduces defense by 10%. Increase chance of losing sight of snitch by 5%.
   Success Rate: `0.1 + (Speed * 0.1) + (Accuracy * 0.1)`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "{player} plunges forward with impressive speed and has caught the snitch. Game Over! {winning team} wins by {score}"
   - Failure: "{player} dives, but just as they near the Snitch, it flits out of reach."

2. Dodge Bludger: Evade an incoming bludger. 
   Activate: After Beat Bludger, Double Hit.
   Counter: Dodge Bludger 
   Effect: Reduces handling by 10%.    
   Success Rate: `(Handling + Defense - Agility) / 2`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "{player} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback."
   - Failure + No Effect: "A well-timed bludger strikes {player} squarely, knocking them off course. Their handling falters as they struggle to regain their footing."
   - Wounded:
   - Injured:

3. Namecall: Disrupt a player's focus.  
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

   - Success + Warn: "{player} delivers a biting taunt to {opponent}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {player}."
   - Success + No Warn: "{Opponent} looks fazed, wonder what happened."
   - Failure + Warn: "{player} delivers a biting taunt to {opponent}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {player}."
   - Failure + No Warn: "{opponent} swoops past {player}."

4. Slow Hover: Hover slowly to anticipate the Snitch's movements.  
   Activate: If snitch not spotted.
   Counter: None
   Effect: Increases agility by 10%, reduces speed by 10%. Increases chance of spotting snitch by 2%.
   Success Rate: `(Agility + Handling) / 2`
   Chance of Warning: 0%
   Cooldown: 1 Action


   - Success: "The seeker hovers gracefully, taking a slow and calculated approach to the Snitch. Wait, is"
   - Failure: "The seeker’s slow hover drags on, leaving them vulnerable. The Snitch darts away in a burst of speed, and the seeker is left hovering aimlessly, losing valuable ground in the search."

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
   Counter: None
   Effect: Reduces handling by 10%. 
   Success Rate: `(Handling + Defense - Agility) / 2`
   Chance of Warning: 0%
   Cooldown: None

   - Success: "{player} ducks at the last second, narrowly avoiding the incoming bludger. They remain unscathed and maintain possession, their agility and quick thinking preventing any setback."
   - Failure + No Effect: "A well-timed bludger strikes {player} squarely, knocking them off course. Their handling falters as they struggle to regain their footing."
   - Wounded:
   - Injured:

2. Namecall: Disrupt a player's focus.  
   Counter: None
   Effect: Reduces opponent’s morale by 5%.  
   Success Rate: `(Morale - Strength) / 2`  
   Chance of Warning: 20%
   Cooldown: 1 Action

   - Success + Warn: "{player} delivers a biting taunt to {opponent}, throwing them off their game who hesitates, visibly shaken by the remark. A warning is issued for unsportsmanlike conduct to {player}."
   - Success + No Warn: "{Opponent} looks fazed, wonder what happened."
   - Failure + Warn: "{player} delivers a biting taunt to {opponent}, who remains unfazed. A warning is issued for unsportsmanlike conduct to {player}."
   - Failure + No Warn: "{opponent} swoops past {player}."

3. Defend: Set up a defensive strategy.  
   Counter: None
   Effect: Increases defense for the team by 5%.  
   Success Rate: `(Agility + Morale) / 2`
   Chance of Warning: 0%
   Cooldown: 2 Actions.

4. Block: Block a shot at the goalposts. 
   Activate: After Shoot by Opponent.
   Counter: None 
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

6. Slow Hover: Hover slowly in front of goal posts.  
   Counter: None
   Effect: Increases defense by 10%, increase strength by 10%. Decreases speed by 10%.
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: 2 Actions

   - "{player} hovers in front of the goal hoops watching the quaffle carefully.

7. Pass: Pass the Quaffle to a teammate. 
   Activate: If has Quaffle. 
   Counter: None
   Effect: No additional effect.
   Success Rate: `100%`
   Chance of Warning: 0%
   Cooldown: None

   - "{player} releases a perfect pass, the Quaffle soaring through the air with pinpoint accuracy. {teammate} catches it effortlessly, continuing the offensive without missing a beat."

   *{quaffle_owner} has the quaffle*