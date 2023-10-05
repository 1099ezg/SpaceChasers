

*****DO NOT UPLOAD TO BRANCH*****
* BELOW SECTION IS FOR INTERNAL USE ONLY *

### DEBUG SECTION ###


###### Problems with asteroid - bullet collision #######

The problem with astroids not being removed correctly when the bullet is fired
could be due to the variable asteroid_rect. 

Lines 330 to 335 which are supposed to remove asteroid and bullets after impact seems to be correct,
making me believe that there must be a issue with the asteroid generation / collision, which could be 
due to a block of code containing asteroid_rect. 

ASTEROID RECT IS JUST THE individual asteroid of the ASTEROIDS list []

Bullets seem to be removing fine when a asteroid is removed. However sometimes when the asteroid is not removed,
the bullet will continue on, sometimes also skipping the first asteroid but deleting another asteroid that it hits afterward

At the start it seems that there is also a issue with not being able to fire the bullet immediately, NOT NECESSARILY A HUGE DEAL 

The main problem is likely between lines 295 and lines 315 regarding the asteroid collision section. 
Generation SEEMS to BE OK