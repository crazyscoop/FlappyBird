import pygame
pygame.init()

class Ball(pygame.sprite.Sprite):
      def __init__(self,screen):
          pygame.sprite.Sprite.__init__(self)
          self.screen = screen
          self.image = pygame.Surface((30,30))
          self.image.fill((255,255,255))
          pygame.draw.circle(self.image,(255,50,50),(15,15),15,0)
          transcolor = self.image.get_at((1,1))
          self.image.set_colorkey(transcolor)
          self.rect = self.image.get_rect()
          self.rect.center = (100,430)
          self.gravity1 = 1
          self.gravity2 = 1
          self.acc = -8
          self.truth = False         
          self.frame1 = 0
          self.frame2 = 0

      def update(self):
          if self.truth == True:
             if self.acc < 0:
                self.up()
             elif self.acc >= 0:
                  self.down()

             

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
