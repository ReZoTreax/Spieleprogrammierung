import pygame
import os
from pygame.constants import (QUIT, KEYDOWN, KEYUP, K_ESCAPE, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE)
import random  

class Settings(object):
    def __init__(self):
        self.width = 800                                                    #Fensterbreite
        self.height = 600                                                   #Fensterhöhe
        self.fps = 60                                                       #60 fps
        self.title = "Wild Life"                                            #Name/Titel
        self.image_path = os.path.dirname(os.path.abspath(__file__))       
def size(self):                                                             
        return (self.width, self.height)     

class Adventurer(pygame.sprite.Sprite):                                                                             
    def __init__(self, settings):
        pygame.sprite.Sprite.__init__(self)                                                                     #Die Sprite-Optionen werden zur Verfügung gestellt
        self.settings = settings
        self.image = pygame.image.load(os.path.join(self.settings.image_path, "Mewtwo.jpg")).convert()          #Spieler-Bild
        self.image = pygame.transform.scale(self.image, (90, 60))                                               #Spieler-Größe
        self.image.set_colorkey((254,254,254))                                                                  #Weißen Hintergrund eliminieren
        self.rect = self.image.get_rect()                                                                       #Größe des Bildes
        self.rect.left = (settings.width - self.rect.width) // 2                                                #x position des Adventurer
        self.rect.top = settings.height - self.rect.height - 10                                                 #y position des Adventurer
        self.left_or_right = 0
        self.up_or_down = 0
        self.speed = 6
        
        def teleport(self):                                                                                     #zufällige Positiuon
            self.rect.left = random.randrange(0,(settings.width - self.rect.width))
            self.rect.top = random.randrange(0,(settings.height - self.rect.height))

        def update(self):                                                                                       #die Bewegung der Figur/des Adventurer
            newleft = self.rect.left + (self.left_or_right * self.speed)
            newright = newleft + self.rect.width
            if newleft > 0 and newright < settings.width:
                self.rect.left = newleft
            newtop = self.rect.top + (self.up_or_down * self.speed)
            newbottom = newtop + self.rect.height
            if newtop > 0 and newbottom < settings.height:
                self.rect.top = newtop

if __name__ == '__main__':                                    
    settings = Settings()                               
    pygame.init()                                       #Pygame Funktionen bereitstellen
    game = Game(pygame, settings)                       
    game.run()                                          #Hauptschleife
    pygame.quit()                                       #beendet pygame



class Game(object):
    def __init__(self, pygame, settings):
        self.pygame = pygame
        self.settings = settings
        self.screen = pygame.display.set_mode(settings.size())                                                      
        self.pygame.display.set_caption(self.settings.title)                                                        
        self.background = self.pygame.image.load(os.path.join(self.settings.image_path, "Background.jpg")).convert()     
        self.background = pygame.transform.scale(self.background, (800, 600))                                       
        self.background_rect = self.background.get_rect()
        self.Adventurer = Adventurer(settings)                                                                              
        self.clock = pygame.time.Clock()
        self.done = False

        self.the_Adventurer = pygame.sprite.Group()                                     #Adventurer in der Sprite Gruppe
        self.the_Adventurer.add(self.Adventurer)

    def run(self):
        while not self.done:                                                            #Hauptprogrammschleife   
            self.clock.tick(self.settings.fps)                                          #60 fps festlegen  
            for event in self.pygame.event.get():                                       
                if event.type == QUIT:                                                  #wenn man das "X" drückt wird das Fenster geschlossen
                    self.done = True                    
                elif event.type == KEYDOWN:                                             #ereignis/event einer Taste wenn diese gedrückt wird
                    if event.key == K_ESCAPE:
                        self.done = True
                    if event.key == K_LEFT:                                             #Nach links bewegen
                        self.Adventurer.left_or_right = -1
                    if event.key == K_RIGHT:                                            #Nach rechts bewegen
                        self.Adventurer.left_or_right = 1
                    if event.key == K_UP:                                               #Nach oben bewegen
                        self.Adventurer.up_or_down = -1
                    if event.key == K_DOWN:                                             #Nach unten bewegen
                        self.Adventurer.up_or_down = 1
                elif event.type == KEYUP:                                               #nachdem die Taste losgelassen wird...
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        self.Adventurer.left_or_right = 0
                    if event.key == K_UP or event.key == K_DOWN:
                        self.Adventurer.up_or_down = 0
                    if event.key == K_SPACE:                                            #wenn die Leertaste losgelassen wird, wird der Adventurer an eine zufällige Position gesetzt
                        self.Adventurer.teleport()

            self.update()                                                               #Spieler updated sein Zustand
            self.draw()                                                                 #Spieler wird gemalt/generiert

 
    def draw(self):
        self.screen.blit(self.background, self.background_rect)
        self.the_Adventurer.draw(self.screen)                                           #Spieler wird im Fenster angezeigt
        self.pygame.display.flip()                                                      #Aktualisiert das Fenster

    def update(self):                                                                   #Update für den Adventurer
        self.the_Adventurer.update()