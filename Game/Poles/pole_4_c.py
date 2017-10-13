import pygame,random
pygame.init()

class Pole_4(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Poles/pole2.png")
          self.image = self.image.convert()
          self.rect = self.image.get_rect()
          self.rect.center = (265+1000+65,480)
          self.dx = -5

      def update(self,pole3):
          self.x = pole3.rect.centerx
          self.y = pole3.rect.centery
          
          self.rect.centerx += self.dx
          self.checkbound()
 

      def checkbound(self):
          if self.rect.right <= 0:
             self.rect.centerx = self.x
             self.rect.centery = self.y + 170 + 140 + 170
  