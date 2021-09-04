import pygame

class FonTwo():
    def __init__(self, feofil):
        self.screen = feofil.screen
        self.screen_rect = feofil.screen.get_rect()
        self.image = pygame.image.load('images/fon.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def miss_me(self):
        self.screen.blit(self.image, self.rect)
