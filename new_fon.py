import sys
import pygame
from fon_two import FonTwo

class Fon():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        self.bg_color = (0,0,255)
        pygame.display.set_caption("Фон")
        self.fon_two = FonTwo(self)
    def run_fon(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            self.fon_two.miss_me()        
            pygame.display.flip()
if __name__ == '__main__':
    fs = Fon()
    fs.run_fon()
