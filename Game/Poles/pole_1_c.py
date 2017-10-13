import pygame,random
pygame.init()

class Pole_1(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Poles/pole1.png")
          self.image = self.image.convert()
          self.rect = self.image.get_rect()
          self.rect.center = (100+1000,0)
          self.dx = -5  
          self.truth = False

      def update(self): 
          self.rect.centerx += self.dx
          self.checkbound()

      def checkbound(self):
          if self.rect.right <= 0:
             self.truth = True             
             self.rect.centery = random.randint(-80,150)
             self.rect.left = self.screen.get_width()