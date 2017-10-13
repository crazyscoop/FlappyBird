import pygame,random
pygame.init()

class Pole_3(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Poles/pole1.png")
          self.image = self.image.convert()
          self.rect = self.image.get_rect()
          self.rect.center = (265+1000+65,0)
          self.dx = -5
          self.truth = False

      def update(self,pole1):
          self.x = pole1.rect.centerx
          self.rect.centerx += self.dx
          self.checkbound()

      def checkbound(self):
          if self.rect.right <= 0:
             self.truth = True
             self.rect.centery = random.randint(-80,150)
             self.rect.centerx = self.x + 165 + 65
