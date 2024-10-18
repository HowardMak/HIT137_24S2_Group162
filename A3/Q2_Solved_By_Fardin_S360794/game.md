### Game Documentation: **Space Shooter Game**

#### Overview:

This is a **Space Shooter Game** built using the `pygame` library. The player controls a spaceship, dodges enemy spaceships, and shoots bullets to destroy them. The game features multiple enemy types, each with different sizes, bullet damage, and speed.

#### Requirements:

- **Python Version:** Python 3.x (compatible with `pygame`)
- **Dependencies:**
  You will need the `pygame` library installed.

#### Installation Steps:

1. **Ensure Python is Installed:**
   Ensure you have Python installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Install the Required Packages:**
   Install the `pygame` library using the following command:

   ```bash
   pip install pygame
   ```

3. **Run the Game:**
   Navigate to the directory where `Game.py` is located, and run the following command:
   ```bash
   python Game.py
   ```

#### Game Controls:

- **Movement:**

  - **Arrow Keys**: Move the player spaceship up, down, left, or right on the screen.

- **Shooting:**
  - **Spacebar**: Shoot bullets from the spaceship to attack the enemies.

#### Gameplay Mechanics:

1. **Player:**

   - The player controls a spaceship that starts at the center-bottom of the screen.
   - **Health**: The player's health is displayed as a green bar above the spaceship, which decreases when hit by enemy bullets.
   - **Bullets**: The player can shoot bullets in the upward direction to destroy enemy ships.

2. **Enemies:**

   - There are different types of enemies with varying colors, sizes, and bullet damage.
   - Enemies spawn at regular intervals from the top of the screen and move downwards towards the player.
   - Each enemy can fire bullets toward the player.

3. **Health and Damage:**

   - Both the player and enemies have health values. When the player or enemies are hit by bullets, health decreases accordingly.

4. **Winning Condition:**

   - The objective is to survive for as long as possible by dodging enemy bullets and destroying enemy ships.

5. **Losing Condition:**
   - The game ends when the player's health reaches zero.

#### Code Overview:

- **Player Class:**
  Handles the player's movement, shooting bullets, and displaying the spaceship and health bar.

- **Bullet Class:**
  Represents the bullets shot by both the player and the enemies. The bullets have properties like position, color, damage, and speed.

- **Enemy Class:**
  Represents enemy ships that spawn at the top and shoot bullets toward the player.

- **Game Loop:**
  The game runs in a loop, handling events like player input (movement and shooting), updating positions of bullets and enemies, and checking for collisions between bullets and ships.

#### Enjoy the Game!

Once you start the game, you can control the spaceship with the arrow keys and shoot with the spacebar to destroy enemies and survive as long as possible!
