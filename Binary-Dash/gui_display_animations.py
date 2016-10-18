from tkinter.ttk import *
from tkinter import *

from PIL import Image, ImageTk

import sys, time, random, threading

################## THREADING NOTE : Try to thread only roulette and keep waterfall as main cycle!

class Main:
    def __init__(self, parent, main=None):
        self.parent = parent

        if main != None:
            self.main = main
            self.main.pack_forget()

        self.parent.title("Binary dash")
        self.parent.configure(background="#E3E3E3")
        self.parent.geometry("449x945")
        self.parent.resizable(0,0)

        self.frame = Frame(self.parent, bg="#E3E3E3", width=449, height=945)
        self.frame.place(x=0,y=0)

        image_logo = Image.open("./images/prescreen/binary-dash1.png")
        image_logo = ImageTk.PhotoImage(image_logo)
        label_logo = Label(self.frame, image=image_logo, bg="#E3E3E3", fg="#E3E3E3")
        label_logo.image = image_logo
        label_logo.place(x=68, y=73)

        image_play = Image.open("./images/prescreen/play1.png")
        image_play = ImageTk.PhotoImage(image_play)
        button_play = Button(self.frame, image=image_play, bg="#E3E3E3", fg="#e3e3e3",
                            relief=FLAT, command=lambda: Window(self.parent, self.frame))
        button_play.image = image_play
        button_play.place(x=39, y=292)

        image_sound = Image.open("./images/prescreen/sound1.png")
        image_sound = ImageTk.PhotoImage(image_sound)
        button_sound = Button(self.frame, image=image_sound, bg="#e3e3e3", fg="#e3e3e3",
                             relief=FLAT)
        button_sound.image = image_sound
        button_sound.place(x=40, y=791)

        image_highscore = Image.open("./images/prescreen/highscore1.png")
        image_highscore = ImageTk.PhotoImage(image_highscore)
        button_highscore = Button(self.frame, image=image_highscore, bg="#e3e3e3",
                                  fg="#e3e3e3", relief=FLAT)
        button_highscore.image = image_highscore
        button_highscore.place(x=246, y=791)

        self.parent.bind("<space>",lambda event: Window(self.parent,self.frame))

        self.random_block_list = ["./images/main_random_blocks/1.png","./images/main_random_blocks/2.png","./images/main_random_blocks/3.png","./images/main_random_blocks/4.png",
                                  "./images/main_random_blocks/5.png","./images/main_random_blocks/6.png","./images/main_random_blocks/7.png","./images/main_random_blocks/8.png",
                                  "./images/main_random_blocks/9.png","./images/main_random_blocks/10.png"]

        self.blocks_pos_list = [75,466]
        self.blocks_pos_tuple = (75, 466)

        self.counter = 0

        self.start()

        self.block = None

    def start(self):

        while self.counter >= 0:
            if self.counter%300==0:
                random_number = random.randint(0,9)
                self.image = Image.open(self.random_block_list[random_number])
                self.image = ImageTk.PhotoImage(self.image)
                self.block = Label(self.frame, image = self.image, bg="#e3e3e3", fg="#e3e3e3")
                self.block.image = self.image
                self.block.place(x=self.blocks_pos_list[0],y=self.blocks_pos_list[1])
                self.counter = 0

            if self.blocks_pos_list[1]<=742:
                try:
                    self.block.place(x=self.blocks_pos_list[0],y=self.blocks_pos_list[1])
                    self.blocks_pos_list[1]+=1
                except:
                    pass
                
            else:
                self.blocks_pos_list[0] = self.blocks_pos_tuple[0]
                self.blocks_pos_list[1] = self.blocks_pos_tuple[1]
                self.counter = 0
                self.block.destroy()

            self.parent.update()
                            
            self.counter += 1
            time.sleep(0.01)
        
class Window:

    def __init__(self, parent, main=None):

        #- Window configuration -#
        
        self.parent = parent

        if main != None:
            self.main = main
            self.main.pack_forget()


        self.parent.title("Binary dash")
        self.parent.configure(background="#E3E3E3")
        self.parent.geometry("449x945")
        self.parent.resizable(0,0)
        #- -#

        #- Frame and organisation -#
        self.frame = Frame(self.parent, bg="#E3E3E3", width = 449, height = 945)
        self.frame.place(x=0,y=0)

        self.frame_score = Frame(self.frame, bg="#E3E3E3", width = 449, height = 50)
        self.frame_score.place(x=0,y=0)

        self.label = Label(self.frame_score, bg="#E3E3E3", text = "0", font = ("Calibri",30),
                           fg = "#202020")
        self.label.place(relx=0.472,y=0) #472 - 1 digit, 0.45 - 2 digits, 0.43 - 3 digits  

        self.frame_roulette = Frame(self.frame, bg="#E3E3E3", width = 449, height = 92)
        self.frame_roulette.place(x=0,y=50)

        self.frame_waterfall = Frame(self.frame,bg="#E3E3E3", width=449, height = 703,relief=FLAT)
        self.frame_waterfall.place(x=0,y=144)

##        self.separator_waterfall = Frame(self.frame, height=2, width = 449, bd=1, relief=FLAT, bg='white') #relief=SUNKEN
##        self.separator_waterfall.place(x=0,y=843)

        self.frame_lake = Frame(self.frame, bg="#E3E3E3", width = 449, height = 102)
        self.frame_lake.place(x=0,y=843)

        #- -#

        #- Variables -#
        self.grey_block_1 = ["./images/1block1.png","./images/1block1.png","./images/1block1.png","./images/1block1.png","./images/1block1.png","./images/1block1.png","./images/1block1.png","./images/1block1.png"]
        self.grey_block_2 = ["./images/2block1.png",
                             "./images/2block_anim/1.png","./images/2block_anim/2.png","./images/2block_anim/3.png",
                             "./images/2block_anim/4.png","./images/2block_anim/5.png"
                             ,"./images/2block_anim/6.png","./images/2block_anim/7.png","./images/full_block_white_grey.png"]
        self.grey_block_3 = ["./images/3block1.png",
                             "./images/3block_anim/1.png","./images/3block_anim/2.png","./images/3block_anim/3.png"
                             ,"./images/3block_anim/4.png","./images/3block_anim/5.png","./images/3block_anim/6.png"
                             ,"./images/3block_anim/7.png","./images/full_block_white_grey.png"]
        self.grey_block_4 = ["./images/4block1.png",
                             "./images/4block_anim/1.png","./images/4block_anim/2.png","./images/4block_anim/3.png"
                             ,"./images/4block_anim/4.png","./images/4block_anim/5.png","./images/4block_anim/6.png"
                             ,"./images/4block_anim/7.png","./images/full_block_white_grey.png"]

        self.red_block_1 = ["./images/1block2.png","./images/1block2.png","./images/1block2.png","./images/1block2.png","./images/1block2.png","./images/1block2.png","./images/1block2.png","./images/1block2.png"]
        self.red_block_2 = ["./images/2block2.png",
                            "./images/2block_anim/11.png","./images/2block_anim/22.png","./images/2block_anim/33.png",
                             "./images/2block_anim/44.png","./images/2block_anim/55.png"
                             ,"./images/2block_anim/66.png","./images/2block_anim/77.png","./images/full_block_white_grey.png"]
        self.red_block_3 = ["./images/3block2.png",
                            "./images/3block_anim/11.png","./images/3block_anim/22.png","./images/3block_anim/33.png"
                             ,"./images/3block_anim/44.png","./images/3block_anim/55.png","./images/3block_anim/66.png"
                             ,"./images/3block_anim/77.png","./images/full_block_white_grey.png"]
        self.red_block_4 = ["./images/4block2.png",
                            "./images/4block_anim/11.png","./images/4block_anim/22.png","./images/4block_anim/33.png"
                             ,"./images/4block_anim/44.png","./images/4block_anim/55.png","./images/4block_anim/66.png"
                             ,"./images/4block_anim/77.png","./images/full_block_white_grey.png"]

        self.red_block_roulette = ["./images/5block2.png"]
        self.grey_block_roulette = ["./images/5block1.png"]

        self.all_blocks_list = [self.grey_block_1, self.red_block_1,
                                self.grey_block_2, self.red_block_2,
                                self.grey_block_3, self.red_block_3,
                                self.grey_block_4, self.red_block_4]

        self.red_block_frame = ["./images/red_squrcle_0.png",
                              "./images/red_squrcle_1.png",
                              "./images/red_squrcle_2.png",
                              "./images/red_squrcle_3.png",
                              "./images/red_squrcle_4.png",
                              "./images/red_squrcle_5.png",
                              "./images/red_squrcle_6.png"]

        self.grey_block_frame = ["./images/grey_squrcle_0.png",
                              "./images/grey_squrcle_1.png",
                              "./images/grey_squrcle_2.png",
                              "./images/grey_squrcle_3.png",
                              "./images/grey_squrcle_4.png",
                              "./images/grey_squrcle_5.png",
                              "./images/grey_squrcle_6.png"]

        self.repeat_yes = None

        self.waterfall_counter = 0

        self.order_max = 0

        self.selected_color_counter = 0

        self.reset_place = [None, None]

        self.score = 0

        self.no_replace_flag = 0


##        self.remember_first = 0 ### DELAY
        #- -#

        #- Lists & Dictionaries -#

        self.remember_color = [None, None] # used in random_color def
        self.roulette_blocks = [None, None, None, None, None, None] # stores the labels with images attached
        self.roulette_blocks_images = [None, None, None, None, None, None] # stores the images for labels
        self.roulette_blocks_pos_x = [-90, 0, 90, 180, 270, 360]

        self.roulette_colors = [None, None, None, None, None, None]

        self.anti_repeat = [None, None, None]

        self.on_screen = {1:0, 2:0, 3:0, 4:0}
        self.order = [0,0,0,0]
        self.check_list = []

        self.waterfall_blocks_pos = {1:[[0,-100]], 2:[[0,-100],[449//2,-100]], 3:[[0,-100],[449//3,-100],[(449//3)*2,-100]],
                                     4: [[0,-100],[449//4,-100],[(449//4)*2,-100],[(449//4)*3,-100]]} # the x and y to each and every block on the screen

        self.initial_waterfall_blocks_pos = {1:[(0,-100)], 2:[(0,-100),(449//2,-100)], 3:[(0,-100),(449//3,-100),((449//3)*2,-100)],
                                             4: [(0,-100),(449//4,-100),((449//4)*2,-100),((449//4)*3,-100)]} 

        self.lake_blocks_pos = {1:[[0,0]], 2:[[0,0],[449//2,0]], 3:[[0,0],[449//3,0],[(449//3)*2,0]],
                                     4: [[0,0],[449//4,0],[(449//4)*2,0],[(449//4)*3,0]]}
        self.lake_blocks = []

        self.break_animation = {1:[[0,0,None]], 2:[[0,0,None],[0,0,None]], 3:[[0,0,None],[0,0,None],[0,0,None]],
                                4:[[0,0,None],[0,0,None],[0,0,None],[0,0,None]]} # 0-yes or no, 1-frame, 3-stored image
        
##        self.block_delay = {1:[0,0],2:[0,0],3:[0,0],4:[0,0]} #0-flag if delay should be applied, 1-goes up when the flag is 1 with the waterfall counter 
        
        
        #- -#

        #- Widgets -#

            ##= ROULETTE =##
        
        for i in range(0,6):
            self.roulette_blocks[i] = Label(self.frame_roulette, image = self.random_color('small_square', True),
                                bg="#E3E3E3", fg="#E3E3E3")
            self.roulette_blocks[i].image = self.remember_color[0]
            self.roulette_blocks_images[i] = self.remember_color[0]
            self.roulette_blocks[i].place(x=self.roulette_blocks_pos_x[i], y=0)

            self.roulette_colors[i] = self.remember_color[1]

        left_image = Image.open("./images/left-white-1.png")
        left_image = ImageTk.PhotoImage(left_image)
        left_label = Label(self.frame_score, image = left_image, bg="#e3e3e3", fg="#e3e3e3")
        left_label.image = left_image
        left_label.place(relx=0.205, rely=0.5, anchor=CENTER)

        right_image = Image.open("./images/right-white-1.png")
        right_image = ImageTk.PhotoImage(right_image)
        right_label = Label(self.frame_score, image = right_image, bg="#e3e3e3", fg="#e3e3e3")
        right_label.image = right_image
        right_label.place(relx=0.8,rely=0.5, anchor=CENTER)
##        right_label_fill = Label(self.frame_score, image=right_image, bg="white", fg="white")
##        right_label_fill.image = right_image
##        right_label_fill.place(x=-120,y=0)

        spikes_image = Image.open("./images/spikes2.png")
        spikes_image = ImageTk.PhotoImage(spikes_image)
        spikes_label = Label(self.frame_lake, image=spikes_image,bg="#e3e3e3", fg="#e3e3e3")
        spikes_label.image = spikes_image
        spikes_label.place(x=0,y=0)

        self.draw_roulette_line()

            ##= =##

            ##= WATERFALL =##

        self.waterfall_blocks_dict = {1:[None], 2:[None,None], 3:[None,None,None], 4:[None,None,None,None]}

            ##= =##
        
            
        #- -#

        #- Others -#

        self.parent.bind("<space>",lambda event: self.start_game())

        #- -#

    def start_waterfall(self):
        if self.waterfall_counter % 100 == 0:
            ''' Creating the next block '''

            on_screen_random = random.randint(1,4)
            while self.on_screen[on_screen_random] == 1:
                on_screen_random = random.randint(1,4)
            self.on_screen[on_screen_random] = 1
            all_zero = 1
            for j in range(0, 4):
                if self.order[j] != 0:
                    all_zero = 0
                    break
            if all_zero == 1:
                self.order[on_screen_random - 1] = 1
                self.order_max = 1
            else:
                self.order_max += 1
                self.order[on_screen_random - 1] = self.order_max

            for i in range(0,on_screen_random):
                  self.waterfall_blocks_dict[on_screen_random][i] = Label(self.frame_waterfall, image=self.random_color(on_screen_random, False),
                                                                            bg = "#E3E3E3", fg="#E3E3E3")
                  self.waterfall_blocks_dict[on_screen_random][i].image = self.remember_color[0]
                  self.waterfall_blocks_dict[on_screen_random][i].config(relief=FLAT)
                  self.waterfall_blocks_dict[on_screen_random][i].place(x=(449//on_screen_random)*i, y=-100)
                  
                  self.check_list.append(self.remember_color[1])

        for i in range(1,5):
            if self.order[i-1] == 1: ## BREAKING ANIMATION 

                if self.break_animation[i][0][0] == 1:
                    self.break_block(i)

            if self.on_screen[i] == 1 : #or self.block_delay[i][0]==1
                for j in range(0,i):
                    self.waterfall_blocks_pos[i][j][1] += 2 #y coordinate updated - CHANGE HERE TO FIX THE LAG !!!!!!

                for k in range(0,i):
                    try:
                        self.waterfall_blocks_dict[i][k].place(x=self.waterfall_blocks_pos[i][k][0], y=self.waterfall_blocks_pos[i][k][1])
                    except:
                        print("Error in line 220")

        for i in range(0,4): # finds first block in order
            if self.order[i] == 1:
                first = i+1

        try:
            if self.waterfall_blocks_pos[first][0][1] >= 603: # and self.block_delay[first][0]==0
                print('Block reached end')
                self.lose('end')
        except:
            pass

    def breaking_animation(self, size_category, defined_color, frame):

        if defined_color == 'red':
            image = Image.open(self.all_blocks_list[size_category*2-1][frame])
        else:
            image = Image.open(self.all_blocks_list[size_category*2-2][frame])

        image = ImageTk.PhotoImage(image)

        self.remember_color[0] = image
        return image

    def break_block(self, i):

        for j in range(0,i):
            if self.break_animation[i][j][0] == 1 and self.break_animation[i][j][1] == 0:
                self.break_animation[i][j][2] = self.popped_color_of_check_list #stores the color of the popped block as 3rd element in break animation dict-list-list
                self.break_animation[i][j][1] = 1
                break

        for j in range(0,i):
            if self.break_animation[i][j][0] == 1 and self.break_animation[i][j][1] < 9:
                if self.no_replace_flag == 0:
                    self.waterfall_blocks_dict[i][j].config(image = self.breaking_animation(i, self.break_animation[i][j][2], self.break_animation[i][j][1]))
                    self.waterfall_blocks_dict[i][j].image = self.remember_color[0]
                    self.no_replace_flag = 1

                if self.waterfall_counter % 2 == 0 and self.break_animation[i][j][1] < 9:
                    self.break_animation[i][j][1] += 1
                    self.no_replace_flag = 0
        
    def start_roulette(self):
        for i in range(0,6): # moves the block
            self.roulette_blocks_pos_x[i] += 4 # SPEED - bigger number = higher speed
            self.roulette_blocks[i].place(x=self.roulette_blocks_pos_x[i], y=0)
            if i == 5: #checks if last block is out of screen
                if self.roulette_blocks_pos_x[i] >= 450:

                    self.roulette_blocks_pos_x = [-90, 0, 90, 180, 270, 360]
                        
                    for j in range(5,-1,-1):
                        if j != 0:
                            self.roulette_blocks[j] = self.roulette_blocks[j-1]
                            self.roulette_blocks_images[j] = self.roulette_blocks_images[j-1]
                            self.roulette_blocks[j].image = self.roulette_blocks_images[j]
                                
                            self.roulette_blocks[j].place(x=self.roulette_blocks_pos_x[j], y=0)

                            self.roulette_colors[j] = self.roulette_colors[j-1]
                        else:
                            self.roulette_blocks[j] = Label(self.frame_roulette, image = self.random_color('small_square', True),
                            bg="#E3E3E3", fg="#E3E3E3")
                            self.roulette_blocks_images[j] = self.remember_color[j]
                            self.roulette_blocks[j].image = self.roulette_blocks_images[j]

                            self.roulette_colors[j] = self.remember_color[1]

                    self.draw_roulette_line()

        time.sleep(0.004) #SPEED - smaller number = higher speed

    def start_game(self):
        '''STAAAAAAAAAAAAAAAAART'''
        self.parent.bind("<space>", lambda event: self.select_roulette())
        self.game_on = 1

        while self.game_on == 1:
            self.start_roulette()
            self.start_waterfall()

            self.waterfall_counter += 1

##            for i in range(1,5):
##                if self.block_delay[i][0]==1:
##                    self.block_delay[i][1]+=1

            self.parent.update()

    def select_roulette(self):

        for i in range(0,4): #Finds the size of the first block in order from waterfall
            if self.order[i] == 1:
                first_size = i+1
        
        if self.roulette_blocks_pos_x[3] <= 223: #Selects the color that is beneath the roulette line
            print("Selected : "+str(self.roulette_colors[3]))
            selected_color = self.roulette_colors[3]
        else:
            print("Selected : "+str(self.roulette_colors[2]))
            selected_color = self.roulette_colors[2]

        if selected_color == self.check_list[0]:
            self.popped_color_of_check_list = self.check_list[0]
            self.check_list.pop(0)
            self.score+=1
            self.label.config(text=str(self.score))
##            if self.score<10:
##                self.label.place(relx=0.472,y=0)
            if self.score>9 and self.score<100:
                self.label.place(relx=0.45,y=0)
            elif self.score>=100:
                self.label.place(relx=0.43,y=0)
        else:
            print('Selected wrong color')
            self.lose('color')
            

        if self.selected_color_counter < first_size:
            #desenez blockul corespunzator
##            self.lake_blocks.append(Label(self.frame_lake, image = self.not_random_color(first_size, selected_color),
##                                          bg="#E3E3E3", fg="#E3E3E3"))
##            self.lake_blocks[len(self.lake_blocks)-1].image = self.remember_color[0]
##            self.lake_blocks[len(self.lake_blocks)-1].place(x=self.lake_blocks_pos[first_size][self.selected_color_counter][0],
##                                                          y=self.lake_blocks_pos[first_size][self.selected_color_counter][1])

            self.break_animation[first_size][self.selected_color_counter][0] = 1
            
            self.selected_color_counter += 1
            
        if self.selected_color_counter == first_size: #Completed a waterfall block
##            self.block_delay[first_size][0]=1 ################
##            if self.block_delay[first_size][0]==1 and self.block_delay[first_size][1]<14:
##                self.remember_first = first_size
##            else:
            for i in range(0,first_size):
                    self.waterfall_blocks_dict[first_size][i].destroy()
                    self.break_animation[first_size][i] = [0,0,None] #Broke? - frame - color
##            self.block_delay[self.remember_first][1]=0
##            self.remember_first = 0
            self.on_screen[first_size] = 0

            self.reset_place[0] = 1
            self.reset_place[1] = first_size

            for i in range(0,self.reset_place[1]):
                for j in range(0,2):
                    self.waterfall_blocks_pos[self.reset_place[1]][i][j] = self.initial_waterfall_blocks_pos[self.reset_place[1]][i][j]
            
            for i in range(0, len(self.lake_blocks)):
                self.lake_blocks[i].destroy()

            for i in range(0,4):
                if self.order[i] != 0:
                    self.order[i] -= 1
            self.order_max -= 1
            
            self.selected_color_counter = 0
            self.lake_blocks = []

    def not_random_color(self, size_category, defined_color):
            
        if size_category == 4:
            size = (449//4,100)
        elif size_category == 3:
            size = (449//3,100)
        elif size_category == 2:
            size = (449//2,100)
        elif size_category == 1:
            size = (449,100)

        if defined_color == 'red':
            image = Image.open(self.red_block_frame[1])
            image = image.resize(size, Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)
        else:
            image = Image.open(self.grey_block_frame[1])
            image = image.resize(size, Image.ANTIALIAS)
            image = ImageTk.PhotoImage(image)

        self.remember_color[0] = image
        return image
    def random_color(self, size_category, roulette):
        
        local_random_color = random.randint(0,1)

        if local_random_color == 0:
            my_color = 'red'
        else:
            my_color = 'grey'

        if roulette != True:
            if my_color == 'red':
                image = Image.open(self.all_blocks_list[size_category*2-1][0])
                self.remember_color[1] = 'red'
            elif my_color == 'grey':
                image = Image.open(self.all_blocks_list[size_category*2-2][0])
                self.remember_color[1] = 'grey'

        if roulette == True:
            if self.repeat_yes!='red' and my_color == 'red':
                image = Image.open(self.red_block_roulette[0])
                self.remember_color[1] = 'red'
            elif self.repeat_yes=='red' and my_color == 'red':
                image = Image.open(self.grey_block_roulette[0])
                self.remember_color[1] = 'grey'
                self.repeat_yes = None
            elif self.repeat_yes!='grey' and my_color == 'grey':
                image = Image.open(self.grey_block_roulette[0])
                self.remember_color[1] = 'grey'
            elif self.repeat_yes=='grey' and my_color =='grey':
                image = Image.open(self.red_block_roulette[0])
                self.remember_color[1] = 'red'
                self.repeat_yes = None

        image = ImageTk.PhotoImage(image)
        self.remember_color[0] = image
        if roulette == True:
            self.anti_repeater(self.remember_color[1])
        return image

    def anti_repeater(self, last):
        if self.anti_repeat[0]==None or self.anti_repeat[1]==None or self.anti_repeat[2]==None:
            for i in range(0,3):
                if self.anti_repeat[i] == None:
                    self.anti_repeat[i] = last
                    break
        else:
            for i in range(2,-1,-1):
                if i != 0:
                    self.anti_repeat[i] = self.anti_repeat[i-1]
                else:
                    self.anti_repeat[i] = last

        if self.anti_repeat[0] == self.anti_repeat[1] and self.anti_repeat[0] == self.anti_repeat[2]:
            self.repeat_yes = last

    def draw_roulette_line(self):
        
        image_arrow = Image.open("./images/full_block_white_grey.png")
        image_arrow = image_arrow.resize((1,90), Image.ANTIALIAS)
        image_arrow = ImageTk.PhotoImage(image_arrow)
        self.arrow = Label(self.frame_roulette, image = image_arrow)
        self.arrow.image = image_arrow
        self.arrow.place(x=223,y=2)

    def lose(self, message):
        self.game_on = 0
        f = open('highscore.txt','a')
        f.write(str(self.score)+'\n')
        f.close()
        self.parent.bind("<space>",lambda event: print('You lost'))
        time.sleep(1)
        Post(self.parent, self.frame, self.score, message)
        self.close()
            
    def close(self):
        sys.exit()

class Post:
    def __init__(self, parent, main=None, score=0, message=None):
        self.parent = parent

        if message == 'end':
            self.message = 'You hit the spikes.'
        elif message == 'color':
            self.message = 'Wrong color.'
        if main != None:
            self.main = main
            self.main.pack_forget()

        self.parent.title("Binary dash")
        self.parent.configure(background="#E3E3E3")
        self.parent.geometry("449x945")
        self.parent.resizable(0,0)

        self.frame = Frame(self.parent, bg="#e3e3e3", width=449, height=945)
        self.frame.place(x=0,y=0)

        self.score_label = Label(self.parent, bg="#e3e3e3", fg="#202020", text=str(score), 
                                 font=("Calibri",155))
        self.score_label.place(relx=0.5,rely=0.2, anchor=CENTER)
        f = open('highscore.txt','r')
        highscore = 0
        for line in f:
            if highscore < int(line):
                highscore = int(line)
        f.close
        self.best_label = Label(self.parent, bg="#e3e3e3", fg="#202020", text=str(highscore),
                                font=("Calibri",75))
        self.best_label.place(relx=0.5,rely=0.4, anchor=CENTER)
        self.your_best_label = Label(self.parent, bg="#e3e3e3", fg="#202020", text='Your best',
                                     font=("Calibri",27))
        self.your_best_label.place(relx=0.5,rely=0.33,anchor=CENTER)

        self.mistake_label = Label(self.parent, bg="#e3e3e3", fg="#969696", text=self.message,
                                   font=("Calibri",32))
        self.mistake_label.place(relx=0.5,rely=0.60,anchor=CENTER)
        self.play_again_label = Label(self.parent, bg="#e3e3e3", fg="#969696", text='Tap to play again.',
                                      font=("Calibri",32))
        self.play_again_label.place(relx=0.5,rely=0.655,anchor=CENTER)

        image_sound = Image.open("./images/prescreen/sound1.png")
        image_sound = ImageTk.PhotoImage(image_sound)
        button_sound = Button(self.frame, image=image_sound, bg="#e3e3e3", fg="#e3e3e3",
                             relief=FLAT)
        button_sound.image = image_sound
        button_sound.place(x=40, y=791)

        image_highscore = Image.open("./images/prescreen/highscore1.png")
        image_highscore = ImageTk.PhotoImage(image_highscore)
        button_highscore = Button(self.frame, image=image_highscore, bg="#e3e3e3",
                                  fg="#e3e3e3", relief=FLAT)
        button_highscore.image = image_highscore
        button_highscore.place(x=246, y=791)

        self.parent.bind("<Return>",lambda event: Window(self.parent,self.frame))

        self.parent.bind("<R>", lambda event: Main(self.parent, self.frame))

        
