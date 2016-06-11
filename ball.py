"""
This module is used to define Ball class
"""
import pygame
import math

import constants

class Ball(pygame.sprite.Sprite):

  change_x = 1
  change_y = 5

  def __init__(self):
    pygame.sprite.Sprite.__init__(self)

    self.velocity = [1,1]
    self.size = 13
    self.x = (constants.SCREEN_WIDTH - self.size) / 2
    self.y = constants.SCREEN_HEIGHT - 200
    self.colour = constants.CORAL
    self.thickness = 0
    self.speed = 3
    self.angle = math.pi/2

    self.right = self.x + self.size
    self.left = self.x - self.size
    self.top = self.y - self.size
    self.bottom = self.y + self.size

    # Instance varibles that control the edges of where we bounce
    self.left_boundary = 0
    self.right_boundary = constants.SCREEN_WIDTH
    self.top_boundary = 0
    self.bottom_boundary = constants.SCREEN_HEIGHT

  def update(self):
    self.x += self.change_x
    self.y += self.change_y

    self.right = self.x + self.size
    self.left = self.x - self.size
    self.top = self.y - self.size
    self.bottom = self.y + self.size

    if self.right >= self.right_boundary or self.left <= self.left_boundary:
      self.change_x *= -1

    if self.top <= self.top_boundary:
      self.change_y *= -1

  def display(self, screen):
    pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)

  def move(self):
    self.x += math.sin(self.angle) * self.speed
    self.y -= math.cos(self.angle) * self.speed
    (self.angle, self.speed) = addVectors((self.angle, self.speed), gravity)
    self.speed *= drag

  def reset(self):
    self.x = (constants.SCREEN_WIDTH - self.size) / 2
    self.y = constants.SCREEN_HEIGHT - 200
    change_x = 1
    change_y = 5

