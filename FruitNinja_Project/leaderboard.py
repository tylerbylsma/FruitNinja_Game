from guizero import App, Text, TitleBox, PushButton, Box 


class LeaderBoard:
    def __init__(self, screen, dictionary = ()):
        self.screen = screen
        self.dictionary = dictionary
        
        self.u1 = ["",""]
        self.u2 = ["",""]
        self.u3 = ["",""]
        self.u4 = ["",""]
        self.u5 = ["",""]
        self.u6 = ["",""]
        self.u7 = ["",""]
        self.u8 = ["",""]
        self.u9 = ["",""]
        self.u10 = ["",""]
        
        self.line()
        self.bb()
    
        
    def line(self):
        '''Adjusts the leaderboard depending on the length of the dictionary. '''
        if len(self.dictionary) > 0:
            self.u1 = [self.dictionary[0][0],self.dictionary[0][1]]
            if len(self.dictionary) > 1:
                self.u2 = [self.dictionary[1][0],self.dictionary[1][1]]
                if len(self.dictionary) >2:
                    self.u3 = [self.dictionary[2][0],self.dictionary[2][1]]
                    if len(self.dictionary) >3:
                        self.u4 = [self.dictionary[3][0],self.dictionary[3][1]]
                        if len(self.dictionary) >4:
                            self.u5 = [self.dictionary[4][0],self.dictionary[4][1]]
                            if len(self.dictionary)>5:
                                self.u6 = [self.dictionary[5][0],self.dictionary[5][1]]
                                if len(self.dictionary) >6:
                                    self.u7 = [self.dictionary[6][0],self.dictionary[6][1]]
                                    if len(self.dictionary)>7:
                                        self.u8 = [self.dictionary[7][0],self.dictionary[7][1]]
                                        if len(self.dictionary) >8:
                                            self.u9 = [self.dictionary[8][0],self.dictionary[8][1]]
                                            if len(self.dictionary)>9:
                                                self.u10 = [self.dictionary[9][0],self.dictionary[9][1]]
                                
                                
        
    def bb(self):
        ''' Stores the dictionary values in the leaderboard. '''
        self.leaderboard_lines("#FA5F8F", ranknum = "#", u_name = "NAME", u_time = "TIME")
        self.blankbox()
        self.leaderboard_lines(ranknum = 1, u_name = self.u1[0], u_time = self.u1[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 2, u_name = self.u2[0], u_time = self.u2[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 3, u_name = self.u3[0], u_time = self.u3[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 4, u_name = self.u4[0], u_time = self.u4[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 5, u_name = self.u5[0], u_time = self.u5[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 6, u_name = self.u6[0], u_time = self.u6[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 7, u_name = self.u7[0], u_time = self.u7[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 8, u_name = self.u8[0], u_time = self.u8[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 9, u_name = self.u9[0], u_time = self.u9[1])
        self.blankbox()
        self.leaderboard_lines(ranknum = 10, u_name = self.u10[0], u_time = self.u10[1])
    
    def leaderboard_lines(self, color = "#FE9176", ranknum = "", u_name= "", u_time = ""):
        '''Draws the leaderboard. '''
        box1 = Box(self.screen, width = 500, height = 35, layout = "grid")
        box1.bg = color
        namebox = Box(box1, grid = [0,0] ,width = 100, height = 35, border = True)
        user_name = Text(namebox, text= ranknum, align = "right", size = 30)
        rank_box = Box(box1, grid=[1,0], width = 300, height = 35, border = True)
        rank = Text(rank_box, text = u_name , align = "left", size = 30)
        time_box = Box(box1, grid=[2,0], width = 100, height = 35, border = True)
        inish_time = Text(time_box, text = u_time , align = "left", size = 30)
        
    def blankbox(self):
        blankbox1 = Box(self.screen, width = 500, height = 5)
        


