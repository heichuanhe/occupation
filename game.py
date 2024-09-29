import pygame
import random

# 初始化 pygame
pygame.init()

# 屏幕尺寸
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("躲弹幕游戏")

# 玩家类
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.speed = 5

    def move_left(self):
        if self.x > 0:
            self.x -= self.speed

    def move_right(self):
        if self.x < SCREEN_WIDTH:
            self.x += self.speed

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < SCREEN_HEIGHT:
            self.y += self.speed

# 弹幕类
class Bullet:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = 0
        self.speed = random.randint(3, 6)

    def update(self):
        self.y += self.speed

# 创建玩家对象
player = Player()

# 弹幕列表
bullets = []

# 游戏时钟
clock = pygame.time.Clock()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            elif event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()

    # 生成新的弹幕
    if random.randint(1, 50) == 1:
        bullet = Bullet()
        bullets.append(bullet)

    # 更新弹幕位置
    for bullet in bullets:
        bullet.update()

    # 绘制
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, 50, 50))
    for bullet in bullets:
        pygame.draw.circle(screen, (255, 255, 255), (bullet.x, bullet.y), 5)

    # 检查碰撞
    for bullet in bullets:
        if (player.x < bullet.x < player.x + 50 and player.y < bullet.y < player.y + 50):
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()