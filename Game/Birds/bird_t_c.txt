import pygame
pygame.init()


class Bird_title(pygame.sprite.Sprite):
      def __init__(self):
          pygame.sprite.Sprite.__init__(self)
          self.image = pygame.image.load("Birds/flappy2.png")
          self.rect = self.image.get_rect()
          self.rect.center = (330,90)
          self.frame = 0
          self.pause = 0
          self.delay = 6
          self.count = 0
          self.pause2 = 0
          self.delay2 = 2
          self.dy = 1 
          self.truth = True        
           
      def update(self):
          self.pause += 1
          if self.pause >= self.delay:
             self.pause = 0

             self.loadimg()

             self.frame += 1
  
             if self.frame >= len(self.list):
                self.frame = 0

             self.image = self.list[self.frame]

          self.pause2 += 1
          if self.pause2 >= self.delay2 and self.truth == True:
             self.pause2 = 0
             self.count += 1
             self.rect.centery += self.dy
                    
             if self.count >= 35:
                self.dy *= -1
                self.count = 0

           
      def loadimg(self):
          self.list = []
          for c in range(1,4):
              bird = pygame.image.load("Birds/flappy%s.png"%(c))
              self.list.append(bird)