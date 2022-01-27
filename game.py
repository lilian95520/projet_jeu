from distutils.spawn import spawn
from email.policy import default
import pygame
import pytmx
import pyscroll
from map import Mapmanager

from player import Player

class Game:
    
    def __init__(self) :
        self.map = "world"
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Mon aventure")     
        
        self.player = Player(0,0)
        self.map_manager = Mapmanager(self.screen,self.player)
        
        
    
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
            #print(self.player.position[0],self.player.position[1])
            
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
            #print(self.player.position[0],self.player.position[1])
        
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            #print(self.player.position[0],self.player.position[1])
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            #print(self.player.position[0],self.player.position[1])      
        
    def update(self):
        self.map_manager.update()
        
        
            
    def run(self):
        
        clock = pygame.time.Clock()
        
        running = True
        
        while running:
            
            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            clock.tick(60)
                    
        pygame.quit()