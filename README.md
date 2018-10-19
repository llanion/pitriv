#Project 'piclick', a trivia-game buzz-in project driven by a Raspberry Pi

This is conceptually a really simple project to allow three players to 'buzz in' to answer trivia questions. There are four buttons (Blue, green, white, black) and three LEDs (blue, green, white). When any button except the black one is pressed, that player 'buzzes in'; a sound is played, that player's light illuminates, and other colors are locked out (and cannot buzz in). When the black button is pressed, the board is cleared; all lights are turned off and any player may buzz in.

When a player buzzes in, a sound ("jump.mp3" in the directory /home/pi/) is played.

When the system has finished booting, all three lights will illuminate.

Wiring:
There's a common power line (3.3V with a 220 Ohm resistor) and a GPIO pin in input mode for each button.
Each LED has 3.3V coming from a GPIO pin in output mode to the anode (longer leg of the LED); the cathode (short leg) is connected through a 330 Ohm resistor to a common ground.

This means we need to reserve a GPIO pin for the moderator (black) plus, for each player, one input and one output.

Using the diagrams at pinout.xyz worked really well for this.
