import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Player settings
PLAYER_SPEED = 5
PLAYER_SIZE = 30
PLAYER_LIVES = 3  # New: Player starts with 3 lives

# Bullet settings
BULLET_SPEED = 10

# Enemy settings
ENEMY_SPAWN_RATE = 60  # Frames between enemy spawns
ENEMY_TYPES = [
    {"color": RED, "size": 30, "bullet_color": RED, "bullet_radius": 5, "bullet_damage": 5, "speed": 1.5},
    {"color": BLUE, "size": 40, "bullet_color": BLUE, "bullet_radius": 7, "bullet_damage": 10, "speed": 1.0},
    {"color": YELLOW, "size": 50, "bullet_color": YELLOW, "bullet_radius": 10, "bullet_damage": 15, "speed": 0.8},
]

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter with Power-Ups")

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed = PLAYER_SPEED
        self.health = 100
        self.lives = PLAYER_LIVES  # New: Player lives
        self.bullets = []

    def move(self, dx, dy):
        self.x = max(0, min(SCREEN_WIDTH, self.x + dx * self.speed))
        self.y = max(0, min(SCREEN_HEIGHT, self.y + dy * self.speed))

    def shoot(self):
        self.bullets.append(Bullet(self.x, self.y - PLAYER_SIZE // 2, GREEN, 5, 10, -1))

    def draw(self, screen):
        pygame.draw.polygon(screen, GREEN, [
            (self.x, self.y - PLAYER_SIZE // 2),
            (self.x - PLAYER_SIZE // 2, self.y + PLAYER_SIZE // 2),
            (self.x + PLAYER_SIZE // 2, self.y + PLAYER_SIZE // 2)
        ])
        # Draw health bar
        pygame.draw.rect(screen, RED, (self.x - PLAYER_SIZE // 2, self.y + PLAYER_SIZE // 2 + 5, PLAYER_SIZE, 5))
        pygame.draw.rect(screen, GREEN, (self.x - PLAYER_SIZE // 2, self.y + PLAYER_SIZE // 2 + 5, PLAYER_SIZE * self.health // 100, 5))

    def reset_health(self):
        self.health = 100

class Bullet:
    def __init__(self, x, y, color, radius, damage, direction):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.damage = damage
        self.direction = direction
        self.speed = BULLET_SPEED

    def move(self):
        self.y += self.speed * self.direction

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

class Enemy:
    def __init__(self, enemy_type, speed_multiplier=1.0):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = -50
        self.type = enemy_type
        self.color = enemy_type["color"]
        self.size = enemy_type["size"]
        self.bullet_color = enemy_type["bullet_color"]
        self.bullet_radius = enemy_type["bullet_radius"]
        self.bullet_damage = enemy_type["bullet_damage"]
        self.speed = enemy_type["speed"] * speed_multiplier  # Adjusted for enemy speed increase
        self.shoot_timer = 0
        self.shoot_delay = random.randint(60, 120)

    def move(self):
        self.y += self.speed

    def shoot(self):
        if self.shoot_timer >= self.shoot_delay:
            self.shoot_timer = 0
            return Bullet(self.x, self.y + self.size // 2, self.bullet_color, self.bullet_radius, self.bullet_damage, 1)
        self.shoot_timer += 1
        return None

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size // 2)

class PowerUp:
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind  # 'health' or 'life'
        self.size = 20
        self.color = BLUE if kind == 'health' else YELLOW
        self.speed = 2

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.enemy_bullets = []
        self.power_ups = []  # New: List to hold power-ups
        self.score = 0
        self.level = 1
        self.level_time = 30 * FPS  # 30 seconds per level
        self.enemy_spawn_timer = 0
        self.game_over = False
        self.game_started = False  # New: Start screen control
        self.enemies_killed = 0  # New: Counter for enemies killed
        self.speed_multiplier = 1.0  # New: Speed multiplier for enemies

    def spawn_enemy(self):
        if self.enemy_spawn_timer <= 0:
            enemy_type = random.choice(ENEMY_TYPES)
            self.enemies.append(Enemy(enemy_type, self.speed_multiplier))
            self.enemy_spawn_timer = ENEMY_SPAWN_RATE
        else:
            self.enemy_spawn_timer -= 1

    def spawn_power_up(self, x, y):
        # Randomly choose between health and life power-ups
        kind = random.choice(['health', 'life'])
        self.power_ups.append(PowerUp(x, y, kind))

    def update(self):
        if not self.game_over:
            # Update player bullets
            for bullet in self.player.bullets[:]:
                bullet.move()
                if bullet.y < 0:
                    self.player.bullets.remove(bullet)

            # Update enemies
            for enemy in self.enemies[:]:
                enemy.move()
                if enemy.y > SCREEN_HEIGHT:
                    self.enemies.remove(enemy)
                bullet = enemy.shoot()
                if bullet:
                    self.enemy_bullets.append(bullet)

            # Update enemy bullets
            for bullet in self.enemy_bullets[:]:
                bullet.move()
                if bullet.y > SCREEN_HEIGHT:
                    self.enemy_bullets.remove(bullet)

            # Update power-ups
            for power_up in self.power_ups[:]:
                power_up.move()
                if power_up.y > SCREEN_HEIGHT:
                    self.power_ups.remove(power_up)

            # Check collisions
            self.check_collisions()

            # Spawn enemies
            self.spawn_enemy()

            # Update level
            self.level_time -= 1
            if self.level_time <= 0:
                self.level += 1
                self.level_time = 30 * FPS

    def check_collisions(self):
        # Player bullets hitting enemies
        for bullet in self.player.bullets[:]:
            for enemy in self.enemies[:]:
                if math.hypot(bullet.x - enemy.x, bullet.y - enemy.y) < enemy.size // 2 + bullet.radius:
                    self.player.bullets.remove(bullet)
                    self.enemies.remove(enemy)
                    self.score += 10
                    self.enemies_killed += 1

                    # Every 7 enemies down, increase enemy speed
                    if self.enemies_killed % 7 == 0:
                        self.speed_multiplier += 0.2

                    # 1 in 15 enemies drops a power-up
                    if self.enemies_killed % 15 == 0:
                        self.spawn_power_up(enemy.x, enemy.y)

                    break

        # Enemy bullets hitting player
        for bullet in self.enemy_bullets[:]:
            if math.hypot(bullet.x - self.player.x, bullet.y - self.player.y) < PLAYER_SIZE // 2 + bullet.radius:
                self.player.health = max(0, self.player.health - bullet.damage)
                self.enemy_bullets.remove(bullet)
                if self.player.health <= 0:
                    self.player.lives -= 1  # New: Lose a life
                    if self.player.lives > 0:
                        self.player.reset_health()  # Reset health if lives remain
                    else:
                        self.game_over = True  # Game over if no lives left

        # Player collecting power-ups
        for power_up in self.power_ups[:]:
            if math.hypot(power_up.x - self.player.x, power_up.y - self.player.y) < PLAYER_SIZE:
                if power_up.kind == 'health':
                    self.player.health = min(100, self.player.health + 50)  # Restore 50% health
                elif power_up.kind == 'life':
                    self.player.lives += 1  # Gain 1 extra life
                self.power_ups.remove(power_up)

    def draw(self, screen):
        screen.fill(BLACK)
        self.player.draw(screen)
        for bullet in self.player.bullets:
            bullet.draw(screen)
        for enemy in self.enemies:
            enemy.draw(screen)
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for power_up in self.power_ups:  # New: Draw power-ups
            power_up.draw(screen)

        # Draw HUD
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        time_text = font.render(f"Time: {self.level_time // FPS}", True, WHITE)
        lives_text = font.render(f"Lives: {self.player.lives}", True, WHITE)  # New: Display lives
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
        screen.blit(time_text, (10, 90))
        screen.blit(lives_text, (10, 130))  # New: Draw lives

        if self.game_over:
            game_over_text = font.render("Game Over! Press R to Restart", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2))

    def draw_start_screen(self, screen):
        font = pygame.font.Font(None, 74)
        start_text = font.render("Press Enter to Start", True, WHITE)
        screen.fill(BLACK)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2))

def main():
    clock = pygame.time.Clock()
    game = Game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if not game.game_started and event.key == pygame.K_RETURN:
                    game.game_started = True
                if game.game_started:
                    if event.key == pygame.K_SPACE:
                        game.player.shoot()
                    if game.game_over and event.key == pygame.K_r:
                        game = Game()

        if game.game_started:
            if not game.game_over:
                keys = pygame.key.get_pressed()
                dx = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
                dy = keys[pygame.K_DOWN] - keys[pygame.K_UP]
                game.player.move(dx, dy)

                game.update()

            game.draw(screen)
        else:
            game.draw_start_screen(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
