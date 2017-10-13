import pygame
pygame.init()

class Pole_2(pygame.sprite.Sprite):
      def __init__(self,screen): 
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Poles/pole2.png")
          self.image = self.image.convert()
          self.rect = self.image.get_rect()
          self.rect.center = (100+1000,480)
          self.dx = -5

      def update(self,pole1):
          
          self.y = pole1.rect.centery          
          
          self.rect.centerx += self.dx
          
          self.checkbound()

      def checkbound(self):

          if self.rect.right <= 0:
             self.rect.centery = self.y + 170 + 140 + 170
             self.rect.left = self.screen.get_width() 