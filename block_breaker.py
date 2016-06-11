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
  level_list = []
  level_list.append(levels.Level_1(player))
  level_list.append(levels.Level_2(player))

  # Set the current level
  current_level_no = 0
  current_level = level_list[current_level_no]

  active_sprite_list = pygame.sprite.Group()

  player.level = current_level
  player.rect.x = (constants.SCREEN_WIDTH - player.rect.width) /2
  active_sprite_list.add(player)

  # Loop until the user clicks the close button
  done = False

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

    # Update the player
    active_sprite_list.update()

    # Update items in the level
    current_level.update()
    ball.update()
   
    if (ball.bottom >= player.rect.top) and (ball.x >= player.rect.x) and (ball.x <= player.rect.x+player.rect.w):
      ball.change_y *= -1
      ball.y = player.rect.top - ball.size + ball.change_y

    for block in current_level.block_list:
      # right side of block
      y = block.rect.y
      x = block.rect.x + block.rect.w
      for i in range(block.rect.h):
        distance = dist(ball.x - x, ball.y - y)
        if distance <= ball.size:
          ball.change_x *= -1
          if type(block) is b.HardBlock and block.collision_count > 1:
            block.collision_count -= 1
            if block.collision_count == 1:
              current_level.inner_list.remove(block.inner)
            break
          current_level.block_list.remove(block)
          is_collide = True
          break
        y += 1

      # left side of block
      y = block.rect.y
      x = block.rect.x
      for i in range(block.rect.h):
        distance = dist(ball.x - x, ball.y - y)
        if distance <= ball.size:
          ball.change_x *= -1
          if type(block) is b.HardBlock and block.collision_count > 1:
            block.collision_count -= 1
            if block.collision_count == 1:
              current_level.inner_list.remove(block.inner)
            break
          current_level.block_list.remove(block)
          is_collide = True
          break
        y += 1

      # bottom of block
      y = block.rect.y + block.rect.h
      x = block.rect.x
      for i in range(block.rect.w):
        distance = dist(ball.x - x, ball.y - y)
        if distance <= ball.size:
          ball.change_y *= -1
          ball.y = y + ball.size
          if type(block) is b.HardBlock and block.collision_count > 1:
            block.collision_count -= 1
            if block.collision_count == 1:
              current_level.inner_list.remove(block.inner)
            break
          current_level.block_list.remove(block)
          break
        x += 1

      # top of block
      y = block.rect.y
      x = block.rect.x
      for i in range(block.rect.w):
        distance = dist(ball.x - x, ball.y - y)
        if distance <= ball.size:
          ball.change_y *= -1
          ball.y = y - ball.size
          if type(block) is b.HardBlock and block.collision_count > 1:
            block.collision_count -= 1
            if block.collision_count == 1:
              current_level.inner_list.remove(block.inner)
            break
          current_level.block_list.remove(block)
          is_collide = True
          break
        x += 1

    # Go to next level
    if len(current_level.block_list) == 0:
      if current_level_no == 1:
        done = True
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
