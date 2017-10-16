import pygame
pygame.init()

class Hun_digit(pygame.sprite.Sprite):
      def __init__(self,screen,count):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.count = count
          self.image = pygame.image.load("Numbers/1.png")
          self.rect = self.image.get_rect()
          self.rect.center = (93,53)
     
      def update(self,count):
          self.count = count
          self.strcount = str(count)
          self.lencount = len(self.strcount)
          self.hundigit = self.strcount[self.lencount - 3]
          self.image = pygame.image.load("Numbers/%s.png"%(self.hundigit))