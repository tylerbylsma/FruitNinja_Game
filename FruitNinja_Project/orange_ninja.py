"""Fruit Ninja Gui - Final Project

Fruit Ninja is a game where fruit will fly up accross the screen, and the user is supposed to slice through each fruit in order to get points.
If the fruit falls to the bottom of the screen, the user loses a life. The user begins with three lives, and when all three lives are gone
the game will end. The user will then have the option to save their score if they desire.

@author: Ben Kosters (bak32)
@author: Tyler Bylsma (tjb65)
@date: December, 2022

"""
from guizero import App, Drawing, Text, TextBox, Box, PushButton, Window, Picture
from random import randint
import random
from orange import Fruit
from player import Player
from timer import Timer
from guizero.utilities import GUIZeroImage



def add_image_to_drawing(drawing, image, x, y, anchor="nw", **kwargs):
    '''
    Method taken directly from the ui_images file created by kvlinden.
    Draws an image on a canvas at a given location.

    drawing: a GuiZero Drawing widget
    image:   a GUIZeroImage object
    x, y:    coordinates of the top left corner of where to draw the image
    anchor:  defaults to "nw" (northwest); alternatives include "center", "ne", "sw", "se", "e", ...
    '''
    return drawing.tk.create_image(x, y, image=image.tk_image, anchor=anchor, **kwargs)

class FruitNinja:
    """The FruitNinja class runs the gui application for the game. The ParticleSimulation class was used as a template for this class.
    """


    def __init__(self, app):
        """Instantiate the simulation GUI app."""
        self.app = app
        app.hide()
        #Instanciates a opening window
        self.window = Window(app, title='Player Info', width = 300, height = 400)
        info_window_box = Box(self.window, layout = 'grid')
        welcome_message = Text(info_window_box, text='Welcome to Fruit Ninja', grid = [0,0], align='top', size = 20, color = 'Black')
        self.name = TextBox(info_window_box,grid = [0,1], align='right')
        self.window.bg = '#FF8C00'
        enter_name = Text(info_window_box, text='Enter a Name:',grid = [0,1], align='left')
        picture = Picture(info_window_box,grid = [0,2],align = 'bottom', image ="fruit_ninja_picture.jpg")
        if app.hide == True:
            self.window.visible = True
        #Play and quit buttons underneath the image
        quit_button = PushButton(info_window_box, image='real_x_button.PNG', command = app.destroy, grid = [0,4], align='right', width = 52, height =50)
#         play_button = PushButton(info_window_box, text='Play', command = self.start_game, grid = [0,3],align = 'left')
        scores_button = PushButton(info_window_box, text = "See High Scores", command = self.see_scores, args = ['scores.txt'],grid = [0,4], align='left')
        play_button = PushButton(info_window_box, image = 'play_picture.PNG', command = self.start_game, grid = [0,3], width = 132, height = 40)
        
        self.app.bg ='#FF8C00'
        
        self.name.bg = 'light gray'
        self.name.width = 13
        self.name.text_size = 12
        
        quit_button.bg = 'red'
        play_button.bg = 'black'
        
        scores_button.text_color = 'black'
        scores_button.text_size = 10
        scores_button.bg = 'sky blue'
        scores_button.width = 11
        scores_button.font = 'Roboto'
        
        welcome_message.bg = '#FF8C00'
        welcome_message.width = 18
        welcome_message.font = 'Roboto'
        #wigets for GUI app
        app.title = 'fruit Ninja'
        UNIT = 500
        CONTROL_UNIT = 50
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT

        # Add the widgets.
        box = Box(app, layout='grid', width=UNIT, height=UNIT + CONTROL_UNIT)
        self.drawing = Drawing(box, width=UNIT, height=UNIT, grid=[0,0,2,1])
        #This object is used to store information about the player
        self.player_information = Player()
        self.fruit_list = []
        
        self.player_name_text = Text(box, text = "", grid = [0,1], align = 'left')
        self.player_score = Text(box, text = "Score:", grid = [0,1], align = 'right')
        self.player_lives = Text(box, text = f'Lives: {self.player_information.get_lives()}', grid = [1,1])
        
        self.player_score.text_color = '#413bf7'
        self.player_score.text_size = 15
        
        self.player_lives.text_size = 15
        self.player_lives.text_color = '#413bf7'
        
        self.timer = Timer()
        self.timer_text = Text(box, text = f'Time:{self.timer.get_time()}', grid = [0,1])
        #self.update_clock()
        self.quit = PushButton(box, image = 'x_button.PNG', command = app.destroy, grid = [1,1], align = 'right', width = 50, height = 52)
        
        self.timer_text.text_size = 15
        self.timer_text.text_color = '#413bf7'
        #self.drawing.when_clicked = self.check_remove_fruit
        self.drawing.when_mouse_dragged = self.check_remove_fruit
        self.drawing.when_mouse_leaves = self.check_remove_fruit
        app.repeat(50,self.draw_frame)
        
        #loading images into memory
        self.watermelon_picture = GUIZeroImage("Watermelon.PNG", width = 75, height = 75)
        self.banana_picture = GUIZeroImage("banana.PNG", width = 75, height = 75)
        self.apple_picture = GUIZeroImage("apple.PNG", width = 75, height = 75)
        #self.bomb_picture = GUIZeroImage("fruit_ninja_bomb.PNG", width = 100, height = 100)
        self.background_image = GUIZeroImage("fruit_ninja_background_game_picture.JPG" , width = UNIT, height = UNIT)
        
        self.pictures = {"Watermelon": self.watermelon_picture, "Banana" : self.banana_picture, "Apple" : self.apple_picture}

    
    def update_clock(self):
        """
            Here, we update the value of the timer display on the GUI.
            This method is taken directly from the timer module by k
        """
        
        self.timer_text.value = '{:.1f}'.format(self.timer.get_time())

    def draw_frame(self):
        """This method handles drawing each frame by clearing, moving each fruit in the list, redrawing the fruit, and checking
            if each fruit is in range of the screen. This code was lightly modified from the draw_frame method in the ParticleSimulation class

        """
              
        self.drawing.clear()
        add_image_to_drawing(drawing = self.drawing, image = self.background_image, x = 0, y = 0)
        for fruit in self.fruit_list:
            fruit.move(self.drawing)
            #fruit.draw(self.drawing)
            add_image_to_drawing(drawing = self.drawing, image = self.pictures[fruit.fruit_type], x = fruit.x, y = fruit.y)
            self.in_range()
            
        
    def add_fruit(self):
        """creates an instance of the particle class when the add particle button is pressed
        """
        x = randint(25,self.drawing.width)
        y = self.drawing.height
        #using the initial starting point of the widget determines which direction the widget moves
        starting_point = x
        if starting_point < self.drawing.height/2:
            self.pos_direction = False
            
        y_velocity = randint(2,5)
        x_velocity = randint(2,5)
        if x > 250:
            x_velocity*=-1
            
        fruit_type = self.get_random_fruit()
    
        fruit = Fruit(x, y, x_velocity,y_velocity, 0.25,3 , 25, fruit_type = fruit_type)
        if self.player_information.get_lives() != 0:
            self.fruit_list.append(fruit)
        else:
            self.end_game()
        
    def get_random_fruit(self):
        """This method randomly picks which image will be used for each fruit object
        """
        return random.choice(["Watermelon","Banana","Apple"])
        
    def in_range(self):
        """This method checks to see if each fruit object is within the range of the window each time the frame is drawn.
            If the fruit falls below the canvas, the fruit is removed from the fruit list and a life is taken away and updated on the screen
            The check_remove_particle method in the ParticleSimulation class was used as a reference for this method.
        """
        
        copy = self.fruit_list[:]
        for fruit in copy:
            if fruit.y > app.height:
                #and remove a life
                self.fruit_list.remove(fruit)
                
                self.player_information.remove_life()
        self.player_lives.value = "Lives:" + str(self.player_information.get_lives())
        
                
    def check_remove_fruit(self, event):
        """ This method is used to check if the user drags the mouse across a fruit object. If the user does so, the fruit is removed and the
            user's score increases and is updated on the canvas. The check_remove_particle from the ParticleSimulation class was used as a base
            for this method.
        """
        
        copy = self.fruit_list[:]
        for fruit in copy:
            if fruit.slices(event.x, event.y,self.watermelon_picture):
                self.fruit_list.remove(fruit)
                
                self.player_information.increment_score()
            self.player_score.value = 'Score:'+ str(self.player_information.get_score())
    
                #use set_score to change
#     def check_remove_bomb(self, event):
#         copy = self.fruit_list[:]
#         for fruit in copy:
#             if fruit.slices(event.x, event.y, self.bomb_picture):
#                 
#                 self.player_information.remove_life()
                
    def start_game(self):
        """This method is called when the play button on the welcome window is pressed. It sets the name of the user, makes the welcome window
            invisible, starts the timer and the fruit starts appearing on the screen.
        """
        
        value = self.name.value
        self.player_information.set_name(value)
        self.player_name_text.value += value
        self.window.visible = False
        app.visible = True
        app.repeat(1500, self.add_fruit)
        self.timer.reset()
        app.repeat(10, self.update_clock)
        #FIXME - change name of this method and add a quit button to the GUI
        
    def end_game(self):
        """ This method is called when the number of player lives reaches zero. It stopps the app and timer, and a popup window appears asking
            the user if they wish to save their score.
        """
        
        self.app.cancel(self.draw_frame)
        self.app.cancel(self.add_fruit)
        self.app.cancel(self.update_clock)
        if app.yesno('Game over', 'Game over!\nSave Score?'):
            self.save_score('scores.txt')
            self.reset()
        else:
            app.destroy()
        
    def reset(self):
        """ This method is called when the game ends and after the user decides if they wish to save their score or not.
            This will reset the values of the player object and clear the screen.
        """        
        #need to reset player information, empty fruit list, and make opening window visible
        self.window.visible = True
        self.player_information = Player()
        self.player_name_text.value = 'Player Name:'
        self.player_score.value = 'Score:'
        self.fruit_list = []
        self.drawing.clear()
        app.repeat(50,self.draw_frame)
        app.show()
        #app.repeat(10, self.update_clock)
        
    def see_scores(self, filename):
        """ Elements taken from CS 108 lecture slides week 7, slide 19. This method allows the user to see scores in descending order.
            Thank you to Prof. Wieringa for helping us with ordering the scores!
        """

        scores = {}
        with open(filename, 'r') as file:
            
            for line in file:
                x = line.strip().split(',')
                scores[int(x[0])] = x[1]
            
            print(f'{"Scores":<16}{"Player Name":<16}')
            print('-' * 30)
            for player in sorted(scores, reverse=True):
                print( f'Score: {player:<16}{scores[player]:<16}')
            
    def save_score(self, filename):
        """Saves the scores to a file so it can be referenced when the user wishes to see the scores.
        """
        with open(filename, 'a') as file:
            file.write(f'{self.player_information.get_score()},{self.player_information.get_name()}\n')
            
        
#if __name__ == "__main__":        
    #assert         
    


app = App()
#app.hide()
FruitNinja(app)
#app.display()

