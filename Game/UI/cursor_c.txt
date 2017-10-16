import pygame
pygame.init()

class Cursor(pygame.sprite.Sprite):
      def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("UI/cursor.png")
          self.rect = self.image.get_rect()
          self.rect.center = (0,0)
      
      def update(self):
          self.rect.center = pygame.mouse.get_pos()
