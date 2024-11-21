import pygame
from circleshape import CircleShape
from constants import *
import random



class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)


    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS :
            return
        angle = random.uniform(20,50)
        negative_angle = self.velocity.rotate(-angle)
        positive_angle = self.velocity.rotate(angle)
        new_asteriod_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteriod_1 = Asteroid(self.position.x,self.position.y,new_asteriod_radius)
        new_asteriod_2 = Asteroid(self.position.x,self.position.y,new_asteriod_radius)
        new_asteriod_1.velocity += positive_angle * 1.2
        new_asteriod_2.velocity += negative_angle * 1.2









