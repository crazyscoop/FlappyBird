import pygame
pygame.init()

class Play(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("UI/play1.png")
          self.rect = self.image.get_rect()
          self.rect.center = (90,500)