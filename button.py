# Credits to https://stackoverflow.com/a/65572422

import pygame


def pointInRectangle(px, py, rw, rh, rx, ry):
    if px > rx and px < rx  + rw:
        if py > ry and py < ry + rh:
            return True
    return False


class Button:
    def __init__(self, text: str, position: tuple
                 , size: tuple = (200, 50), color = (185,185,185), outline: bool = True) -> None:
        self.position = position
        self.size = size
        self.button = pygame.Surface(size).convert()
        self.button.fill(color)
        self.outline = outline

        # Text is about 70% the height of the button
        font = pygame.font.Font(pygame.font.get_default_font(), int((70 / 100) * self.size[1]))

        # First argument always requires a str, so f-string is used.
        self.textSurf = font.render(f"{text}", True, (0, 0, 0))

    def clicked(self, event):
        mousePos = pygame.mouse.get_pos()
        if pointInRectangle(mousePos[0], mousePos[1], self.size[0], self.size[1], self.position[0], self.position[1]):
            return True
        else:
            return False

    # Renders the button and text. Text position is calculated depending on position of button.
    # Also draws outline if self.outline is true
    def render(self, display: pygame.display) -> None:
        # calculation to centre the text in button
        textx = self.position[0] + (self.button.get_rect().width / 2) - (self.textSurf.get_rect().width / 2)
        texty = self.position[1] + (self.button.get_rect().height / 2) - (self.textSurf.get_rect().height / 2)

        # display button first then text
        display.blit(self.button, (self.position[0], self.position[1]))
        display.blit(self.textSurf, (textx, texty))

        # draw outline
        if self.outline:
            thickness = 5
            posx = self.position[0] - thickness
            posy = self.position[1] - thickness
            sizex = self.size[0] + thickness * 2
            sizey = self.size[1] + thickness * 2

            pygame.draw.rect(display, (253,252,253), (posx, posy, sizex, sizey), thickness)
