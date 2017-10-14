import pygame
pygame.init()

class Bird(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.image.load("Birds/flappymf1.png")
          #self.image = self.image.convert()
          self.image = pygame.transform.scale(self.image,(38,30))
          #self.image.set_colorkey((255,255,255))
          
          self.rect = self.image.get_rect()
          self.rect.center = (100,430)
          self.gravity1 = 1
          self.gravity2 = 1
          self.acc = -8
          self.truth = False         
          self.frame1 = 0
          self.frame2 = 0
          self.frame = 0
          self.delay = 3
          self.pause = 0
          self.freefall = False
          self.freefallht = 0
          self.truth2 = True

      def update(self):
          if self.truth == True:
             if self.acc < 0:
                self.up()
             elif self.acc >= 0:
                  self.down()
               
             
                
          if self.rect.centery >= self.freefallht - 30 and self.truth2 == True:
             self.freefall = True
          elif self.rect.centery < self.freefallht - 30 and self.truth2 == True:
               self.freefall = False

          self.pause += 1
          if self.pause >= self.delay and self.freefall == False and self.truth2 == True:
             self.pause = 0
               
             self.frame += 1
             self.loadimg()
              
             if self.frame >= len(self.bird):
                self.frame = 0
               
             self.image = self.bird[self.frame] 
             #self.image.set_colorkey((255,255,255))
               
          elif self.freefall == True:
               self.frame += 2
          
               self.loadimg2()

               if self.frame >= len(self.bird2):
                  self.frame = len(self.bird2) - 1

               self.image = self.bird2[self.frame]
               #self.image.set_colorkey((255,255,255))
   

      def loadimg2(self):
          self.bird2 = []
          for c in range(1,23):
              bird = pygame.image.load("Birds/flappym%s.png"%(c))
              #bird = bird.convert()
              #bird.set_colorkey((255,255,255))
              self.bird2.append(bird)


      def loadimg(self):
          self.bird = []
          for c in range(1,4):
              bird = pygame.image.load("Birds/flappymf%s.png"%(c))
              #bird = bird.convert()
              #bird.set_colorkey((255,255,255))
              self.bird.append(bird) 
             

      def up(self):
          self.frame1 += 1
          self.rect.centery += self.frame1*(self.gravity1 + self.acc)
          self.acc += 1

      def down(self):
          self.frame2 += 1
          self.rect.centery += self.frame2*(self.gravity2)
                            



      def checkbound(self):
  
          self.truth = False
          self.frame1 = 0
          self.frame2 = 0
          self.acc = -8