# SpaceChasers
#### Video Demo: https://www.youtube.com/watch?v=1FcqSjJJVIo&ab_channel=EthanGabriel
#### Description:
The game SpaceChasers is a python game with around 250 lines of code making a 2D pixel asteroid dodging spacecraft game. This game includes collision detection, difficulty timers, complex generation depending on the difficulty, as well as main menu, game over screen, and score tracking.

The main menu comprises of a quick tutorial of how to play the game as well as a section that keeps track of the high score for the player. The player will begin the game by pressing the start game button. Once in the game, the user has control of the spacecraft using the UP and Down arrow keys to dodge the oncoming asteroids. The Asteroids will start very slow to give the user time to understand the mechanics of the game and how to dodge. However every 20 seconds, the screen will flash "Speeding Up" to indicate to the player that the difficulty has been increased, as asteroids will come 25% faster. This may seem easy, however once minutes past, the game will get very difficult trying to dodge the asteroids fast enough to survive.

The game uses a collision detection system that will detect if the Spaceship touches the asteroid in any spot. If the system does detect collision, the game will end and a game over screen displaying your score will pop up. You will be able to play again after you press back to menu on the game over screen.

The game comprises of only 5 images, a sprite for the spaceship and asteroid, a background screen for the menu screen that includes the text of how to play, a title that shows the logo of the game "Space Chasers V1", as well as the main background for the game loop.

I have organized the code to include sections for defining asteroid and space ship variables, defining and drawing the menu screens, a section to set font colors and text, as well as the main game loop. The main game loop runs after it checks that the main menu is no longer showing after clicking start game, and will start the generation of asteroids and the difficulty timer.

There is also a music 8bit track on repeat throughout the game, and in the future I will be adding a volume slider and toggle to adjust sound effects.

In the future I am hoping to add AI bosses that will spawn every minute that the user will have to shoot at and the AI will be also shooting at the spacecraft. The shooting mechanic will also allow the user to shoot up to 5 asteroids every minute, as they will have limited ammo until it is refilled.

I decided on making a game for my final project as I will be able to use it toward displaying to hiring managers that I have what it takes to make a full scale application using python. I also thought a game would be more fun than writing a automation task or a command line program as there is something to be seen from your creation that actually could be used in real life. I thought of this game after thinking about flappy bird, as it uses similar 2D 8bit designs and mechanisms, but I wanted to do something also unique and different, and that is how spacechasers game to life. 
