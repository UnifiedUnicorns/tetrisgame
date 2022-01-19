from itertools import cycle
import pygame as pg
import string


def wrap_text(text, char_limit, separator=" "):
    """Splits a string into a list of strings no longer than char_limit."""
    words = text.split(separator)
    lines = []
    current_line = []
    current_length = 0
    for word in words:
        if len(word) + current_length <= char_limit:
            current_length += len(word) + len(separator)
            current_line.append(word)
        else:
            lines.append(separator.join(current_line))
            current_line = [word]
            current_length = len(word) + len(separator)
    if current_line:
        lines.append(separator.join(current_line))
    return lines


def _parse_color(color):
    if color is not None:
        try:
            return pg.Color(color)
        except ValueError:
            return pg.Color(*color)
    return color


class Label(object):
    """
    Parent class all labels inherit from. Color arguments can use color names
    or an RGB tuple. rect_center takes tuple in the form of x,y which is the
    center of the rectangle in which the text is in.

    Creates a surface with text blitted to it (self.image) and an associated
    rectangle (self.rect). Label will have a transparent bg if
    bg is not passed to __init__.
    """
    def __init__(self, text, font_size, color, rect_center, font="freesansbold.ttf", bg=None):
        self.bg = _parse_color(bg)
        self.color = _parse_color(color)
        self.rect_center = rect_center
        self.font = pg.font.Font(font, font_size)
        self.set_text(text)

    def set_text(self, text):
        """Set the text to display."""
        self.text = text
        self.update_text()

    def update_text(self):
        """Update the surface using the current properties and text."""
        if self.bg:
            render_args = (self.text, True, self.color, self.bg)
        else:
            render_args = (self.text, True, self.color)
        self.image = self.font.render(*render_args)
        self.rect = self.image.get_rect()
        self.rect.center = self.rect_center

    def draw(self, surface):
        """Blit self.image to target surface."""
        surface.blit(self.image, self.rect)


class MultiLineLabel(object):
    """Creates a single surface with multiple labels blitted to it."""
    def __init__(self, text, font_size, color, rect_center, font="freesansbold.ttf", bg=None, char_limit=42, align="left", vert_space=0):
        attr = {"center": (0, 0)}
        lines = wrap_text(text, char_limit)
        labels = [Label(line, font_size, color, rect_center, font, bg) for line in lines]
        width = max([label.rect.width for label in labels])
        spacer = vert_space*(len(lines)-1)
        height = sum([label.rect.height for label in labels])+spacer
        self.image = pg.Surface((width, height)).convert()
        self.image.set_colorkey(pg.Color("black"))
        self.image.fill(pg.Color("black"))
        self.rect = self.image.get_rect()
        self.rect.center = rect_center
        aligns = {"left"  : {"left": 0},
                  "center": {"centerx": self.rect.width//2},
                  "right" : {"right": self.rect.width}}
        y = 0
        for label in labels:
            label.rect = label.image.get_rect(**aligns[align])
            label.rect.top = y
            label.draw(self.image)
            y += label.rect.height+vert_space

    def draw(self, surface):
        surface.blit(self.image, self.rect)
