import pygame
pygame.init()

class Ready(pygame.sprite.Sprite):
      def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("Platform/ready.png")
          self.rect = self.image.get_rect()
          self.rect.center = (197.5,140)
