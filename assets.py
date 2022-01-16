from itertools import cycle

import pygame as pg
import string

LOADED_FONTS = {}

#Helper function for MultiLineLabel class
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
    or an RGB tuple. rect_attr should be a dict with keys of pygame.Rect
    attribute names (strings) and the relevant position(s) as values.
    Creates a surface with text blitted to it (self.image) and an associated
    rectangle (self.rect). Label will have a transparent bg if
    bg is not passed to __init__.
    """
    def __init__(self, path, size, text, color, rect_attr, bg=None):
        self.path, self.size = path, size
        if (path, size) not in LOADED_FONTS:
            LOADED_FONTS[(path, size)] = pg.font.Font(path, size)
        self.font = LOADED_FONTS[(path, size)]
        self.bg = _parse_color(bg)
        self.color = _parse_color(color)
        self.rect_attr = rect_attr
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
        self.rect = self.image.get_rect(**self.rect_attr)

    def draw(self, surface):
        """Blit self.image to target surface."""
        surface.blit(self.image, self.rect)
