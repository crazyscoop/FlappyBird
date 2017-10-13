import pygame
pygame.init()

class Ten_digit(pygame.sprite.Sprite):
      def __init__(self,screen,count):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.count = count
          self.image = pygame.image.load("1.png") 
          self.rect = self.image.get_rect()
          self.rect.center = (150,53)

      def update(self,count):
          self.count = count
          self.strcount = str(count)
          self.lencount = len(self.strcount)
          self.tendigit = self.strcount[self.lencount - 2]
          self.image = pygame.image.load("%s.png"%(self.tendigit))