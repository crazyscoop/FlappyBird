import pygame
pygame.init()

class Unit_digit(pygame.sprite.Sprite):
      def __init__(self,screen,count):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.count = count
          self.image = pygame.image.load("0.png")
          self.rect = self.image.get_rect()
          self.rect.center = (207.5,50)

      def update(self,count):
          self.count = count
          self.strcount = str(count)
          self.lencount = len(self.strcount)
          self.unitdigit = self.strcount[self.lencount-1]
          self.image = pygame.image.load("%s.png"%(self.unitdigit))