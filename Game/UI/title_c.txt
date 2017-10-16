import pygame
pygame.init()

class Title(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("UI/logo.png")
          self.rect = self.image.get_rect()
          self.rect.center = (160.5,90)
          self.dy = 1
          self.count = 0 
          self.pause = 0
          self.delay = 2         

      def update(self):
         self.pause += 1
         if self.pause >= self.delay:
            self.pause = 0
            self.count += 1
            self.rect.centery += self.dy
                    
            if self.count >= 35:
               self.dy *= -1
               self.count = 0