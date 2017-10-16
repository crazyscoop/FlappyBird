import pygame
pygame.init()

class Platform(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Platform/platform2.png")
          self.image = self.image.convert()
          self.rect = self.image.get_rect()
          self.rect.center = (395,624.5)
          self.dx = -5

      def update(self):
          self.rect.centerx += self.dx 
          self.checkbound()

      def checkbound(self):
          if self.rect.right <= self.screen.get_width():
             self.rect.left = 0   