"""
Main module for block breaker.

Written by serinlee9@gmail.com
"""

import pygame
import math

import constants
import levels
import block as b
from player import Player
from ball import Ball

def dist(x, y):
  d = math.sqrt((x*x) + (y*y))
  return d

def hardblock_collision(block, current_level):
  if type(block) is b.HardBlock and block.collision_count > 1:
    block.collision_count -= 1
    if block.collision_count == 1:
      current_level.inner_list.remove(block.inner)
    return True
  else:
    return False

def init_levellist(player):
  level_list = []
  level_list.append(levels.Level_1(player))
  level_list.append(levels.Level_2(player))
  return level_list

def main():
  pygame.init()

  # Set the height and width of the screen
  size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
  screen = pygame.display.set_mode(size)

  pygame.display.set_caption("Block Break Game :D ")

  # Create the player
  player = Player()

  # Create the ball
  ball = Ball()

  # Create all the levels
  level_list = init_levellist(player)

  # Set the current level
  current_level_no = 0
  current_level = level_list[current_level_no]

  active_sprite_list = pygame.sprite.Group()

  player.level = current_level
  player.rect.x = (constants.SCREEN_WIDTH - player.rect.width) /2
  active_sprite_list.add(player)

  # Loop until the user clicks the close button
  done = False
  game_over = False

  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()

  # ============= Main program loop ==============
  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          player.move_left()

        if event.key == pygame.K_RIGHT:
          player.move_right()

      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
          player.stop()
        if event.key == pygame.K_RIGHT:
          player.stop()

      if event.type == pygame.MOUSEBUTTONDOWN:
        if game_over:
          ball.reset()
          player.rect.x = (constants.SCREEN_WIDTH - player.rect.width) /2
          level_list.clear()
          level_list = init_levellist(player)
          current_level = level_list[current_level_no]
          player_level = current_level
          game_over = False


    # Update the player
    active_sprite_list.update()

    # Update items in the level
    current_level.update()
    ball.update()
   
    if (ball.bottom >= player.rect.top) and (ball.x >= player.rect.x) and (ball.x <= player.rect.x+player.rect.w):
      ball.change_y *= -1
      ball.speed += 0.1
      ball.y = player.rect.top - ball.size + ball.change_y

    for block in current_level.block_list:
      # right side of block
      y = block.rect.y
      x = block.rect.x + block.rect.w
      if (ball.x >= x and ball.x <= x + ball.size and
          ball.y >= y and ball.y <= y + block.rect.h):
        ball.change_x *= -1
        ball.speed += 0.1
        if not hardblock_collision(block, current_level):
          current_level.block_list.remove(block)

      # left side of block
      y = block.rect.y
      x = block.rect.x
      if (ball.x >= x-ball.size and ball.x <= x and
          ball.y >= y and ball.y <= y + block.rect.h):
        ball.change_x *= -1
        ball.speed += 0.1
        if not hardblock_collision(block, current_level):
          current_level.block_list.remove(block)

      # bottom of block
      y = block.rect.y + block.rect.h
      x = block.rect.x
      if ((ball.x >= x and ball.x <= x + block.rect.w and 
         ball.y >= y and ball.y <= y + ball.size) or
         (dist(ball.x - x, ball.y - y) <= ball.size) or
         (dist(ball.x - (x + block.rect.w), ball.y - y) <=  ball.size)):
        ball.change_y *= -1
        ball.speed += 0.1
        ball.y = y + ball.size + ball.change_y
        if not hardblock_collision(block, current_level):
          current_level.block_list.remove(block)

      # top of block
      y = block.rect.y
      x = block.rect.x
      if ((ball.x >= x and ball.x <= x + block.rect.w and
          ball.y >= y - ball.size and ball.y <= y) or
          (dist(ball.x - x, ball.y - y) <= ball.size) or
          (dist(ball.x - (x + block.rect.w), ball.y - y) <= ball.size)):
        ball.change_y *= -1
        ball.speed += 0.1
        ball.y = y - ball.size + ball.change_y
        if not hardblock_collision(block, current_level):
          current_level.block_list.remove(block)

    # Ball fell down
    if ball.y - ball.size > constants.SCREEN_HEIGHT:
      screen.fill(constants.BLACK)
      font = pygame.font.Font(None, 50, bold=True)
      text = font.render("Game Over, click to restart", True, constants.CORAL)
      center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
      center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
      screen.blit(text, [center_x, center_y])
      game_over = True
    else:
      # Go to next level
      if len(current_level.block_list) == 0:
        if current_level_no == 1:
          screen.fill(constants.BLACK)
          font = pygame.font.Font(None, 50, bold=True)
          text = font.render("Congratulations!! You are the champion :)", True, constants.CORAL)
          center_x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
          center_y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
          screen.blit(text, [center_x, center_y])
        else:
          ball.reset()
          current_level_no += 1
          current_level = level_list[current_level_no]

      # ALL CODE TO DRAW
      current_level.draw(screen)
      active_sprite_list.draw(screen)
      ball.display(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn
    pygame.display.flip()

  pygame.quit()



if __name__ == "__main__":
  main()
