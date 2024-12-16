import pygame as pg
import moderngl as mgl
import sys

class GraphicsEngine:
    def __init__(self, winsize=(1600, 900)):
        # Inicializa o Pygame
        pg.init()
        # Tamanho da janela
        self.WIN_SIZE = winsize
        # Set openGL attr
        pg.display.gl_get_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_get_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Create openGL context
        