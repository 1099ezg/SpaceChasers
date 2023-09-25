# SpaceChasers
#### Video Demo: https://youtu.be/Bts-jk8hSow

#### How to play:
The player will begin the game by pressing the start game button. Once in the game, the user has control of the spacecraft using the UP and Down arrow keys to dodge the oncoming asteroids. The Asteroids will start very slow to give the user time to understand the mechanics of the game and how to dodge. However every 20 seconds, the screen will flash "Speeding Up" to indicate to the player that the difficulty has been increased, as asteroids will come 25% faster. This may seem easy, however once minutes past, the game will get very difficult trying to dodge the asteroids fast enough to survive.
#### Description:
The game SpaceChasers is a python game with around 400 lines of code making a 2D pixel asteroid dodging spacecraft game. This game includes collision detection, difficulty timers, health, bullet mechanics, complex generation depending on the difficulty, as well as main menu, game over screen, and score tracking.

The game uses a collision detection system that will detect if the Spaceship touches the asteroid in any spot. If the system does detect collision, the game will end and a game over screen displaying your score will pop up. You will be able to play again after you press back to menu on the game over screen. 

I have organized the code to include sections for defining asteroid and space ship variables, defining and drawing the menu screens, a section to set font colors and text, as well as the main game loop. The main game loop runs after it checks that the main menu is no longer showing after clicking start game, and will start the generation of asteroids and the difficulty timer.

There is also a music 8bit track on repeat throughout the game, and in the future I will be adding a volume slider and toggle to adjust sound effects.

