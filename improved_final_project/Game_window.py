from guizero import App, Drawing, Text, TextBox, Box, PushButton, Window, Picture
from random import randint
import random
from orange import Fruit
from player import Player
from timer import Timer
from guizero.utilities import GUIZeroImage

class Game:
    
    def init(self, app):
        self.app = app
        
        app.hide()
        #Instanciates a opening window
        self.window = Window(app, title='Player Info', width = 300, height = 400)
        
        


app = App()
Game(app)