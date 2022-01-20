import numpy as np
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
import pygame
>>>>>>> ad3ce87 (second)
=======
import pygame
import random
>>>>>>> a17531b (third)
=======

>>>>>>> d173cd7 (fourth)
=======
import pandas as pd
import random
import pygame
import matplotlib.pyplot as plt
>>>>>>> 8cb9e44 (fifth)
from computer_sklearn import Computer
from background import Background
from ball import Ball
from ball_gui import BallGui
from collision import *
from paddle import Paddle
from paddle_gui import PaddleGui
<<<<<<< HEAD
=======
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import svm
>>>>>>> 8cb9e44 (fifth)


class Game:

<<<<<<< HEAD
    #遊戲開始,設置玩家或電腦
    def __init__(self, paddle1computer=None, paddle2computer=None):
        self.paddle1computer = paddle1computer
        self.paddle2computer = paddle2computer
<<<<<<< HEAD
<<<<<<< HEAD

        self._setup()
        self._game_loop()
<<<<<<< HEAD
=======

        self._setup()
        self._game_loop()
>>>>>>> d173cd7 (fourth)

    #設置遊戲的介面包括板子,球,背景
=======
    def __init__(self, paddle1computer=None, paddle2computer=None):
        self.paddle1computer = paddle1computer
        self.paddle2computer = paddle2computer
        self._setup()
        self._game_loop()

>>>>>>> 8cb9e44 (fifth)
    def _setup(self):
        pygame.init()
        pygame.display.set_caption("pypong")

        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.timer = 0

        self.background = Background()

        self.paddle1 = Paddle()
        self.paddle2 = Paddle(760, 'player2.png')
        self.ball = Ball()

        self.paddle1_gui = PaddleGui(self.paddle1)
        self.paddle2_gui = PaddleGui(self.paddle2, 700)
        self.ball_gui = BallGui(self.ball)
<<<<<<< HEAD

        self.game_over = False
        self.running = True

    #推測哪個玩家為輸
    def _game_loop(self):
        while self.running:
            self.clock.tick(60)
<<<<<<< HEAD
=======
    #設置遊戲的介面包括板子,球,背景
    def _setup(self):
=======
        self._setup()
        self._game_loop()

    #設置遊戲的介面包括板子,球,背景
    def _setup(self):
>>>>>>> a17531b (third)
        pygame.init()#初始化
        pygame.display.set_caption("pypong")#視窗標題
        self.x = 10000
        self.screen = pygame.display.set_mode((800, 600))#視窗大小
        self.clock = pygame.time.Clock()
        self.timer = 0

        self.background = Background()#設定背景

        self.paddle1 = Paddle() #1P
        self.paddle2 = Paddle(760, 'player2.png')#2P
<<<<<<< HEAD
        self.ball = Ball(0)#設定球大小和初始速度
=======
        self.ball = Ball(0,True)#設定球大小和初始速度
>>>>>>> a17531b (third)

        self.paddle1_gui = PaddleGui(self.paddle1)#1P之Y點的座標位置標示圖
        self.paddle2_gui = PaddleGui(self.paddle2, 700)#2P之Y點的座標位置標示圖
        self.ball_gui = BallGui(self.ball)#球的圖片
        self.game_over = False#檢測輸家或贏家
        self.running = True

    
    def _game_loop(self):
        while self.running:#開打
            self.clock.tick(30)#幀數
<<<<<<< HEAD
>>>>>>> ad3ce87 (second)
=======
>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)
=======
        self.game_over = False
        self.running = True

    def _game_loop(self):
        while self.running:
            self.clock.tick(60)
>>>>>>> 8cb9e44 (fifth)
            self.timer += self.clock.get_time()

            self.screen.fill((0, 0, 0))

            self._handle_input()
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> ad3ce87 (second)
=======
>>>>>>> a17531b (third)
=======

>>>>>>> d173cd7 (fourth)
=======

>>>>>>> 8cb9e44 (fifth)
            if not self.game_over:
                self._update_state()
                self._draw_objects()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
            #推測哪個玩家生命已為0
>>>>>>> ad3ce87 (second)
=======
            #推測哪個玩家生命已為0
>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)
=======
>>>>>>> 8cb9e44 (fifth)
            if self.paddle1.lives == 0:
                self._game_over('Player 2')

            if self.paddle2.lives == 0:
                self._game_over('Player 1')

            # refresh display
            pygame.display.flip()

<<<<<<< HEAD

    def _handle_input(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        for event in pygame.event.get():
=======
        for event in pygame.event.get():#處理輸入案件的事件
>>>>>>> ad3ce87 (second)
=======
        for event in pygame.event.get():#處理輸入案件的事件
>>>>>>> a17531b (third)
=======
        for event in pygame.event.get():
>>>>>>> d173cd7 (fourth)
=======
    def _handle_input(self):
        for event in pygame.event.get():
>>>>>>> 8cb9e44 (fifth)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

                if event.key == pygame.K_r:
                    self._setup()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d173cd7 (fourth)
#玩家的指令1P:W,S 2P:UP,DOWN
=======
>>>>>>> 8cb9e44 (fifth)
        if pygame.key.get_pressed()[pygame.K_w]:
            self.paddle1.move_up()

        if pygame.key.get_pressed()[pygame.K_s]:
            self.paddle1.move_down()

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.paddle2.move_up()

        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.paddle2.move_down()

<<<<<<< HEAD
<<<<<<< HEAD
=======
        if collision(self.paddle1, self.ball):
            arr1=[-1,0,1]
            self.x=10
            self.ball = Ball(30)
            self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, arr1[random.randint(0,2)]]))
        if collision(self.paddle2, self.ball):
            arr2=[-1,0,1]
            self.x=10      
            self.ball = Ball(30)
            self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, arr2[random.randint(0,2)]])) 
=======
#自動打
        #if collision(self.paddle1, self.ball):
        #    arr1=[-1,0,1]
        #    self.x=10
        #    self.ball = Ball(30)
        #    self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
        #    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, arr1[random.randint(0,2)]]))
        #if collision(self.paddle2, self.ball):
        #    arr2=[-1,0,1]
        #    self.x=10      
        #    self.ball = Ball(30)
        #    self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
        #    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, arr2[random.randint(0,2)]])) 
>>>>>>> a17531b (third)
        #玩家的指令1P:W,S,v,b,n 2P:UP,DOWN,1,2,3
        if pygame.key.get_pressed()[pygame.K_w]:
            self.paddle1.move_up()
        if pygame.key.get_pressed()[pygame.K_s]:
            self.paddle1.move_down()
        if pygame.key.get_pressed()[pygame.K_v]:

            if collision(self.paddle1, self.ball):
<<<<<<< HEAD
                self.x=10
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, -10]))
=======
                if self.ball.c:
                    self.x=10
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, -10]))
>>>>>>> a17531b (third)
            self.ball_gui = BallGui(self.ball)#球的圖片    
            
        if pygame.key.get_pressed()[pygame.K_b]:
            if collision(self.paddle1, self.ball):
<<<<<<< HEAD
                self.x=10
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, 0]))
=======
                if self.ball.c:
                    self.x=10
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, 0]))
>>>>>>> a17531b (third)
            self.ball_gui = BallGui(self.ball)#球的圖片
            
        if pygame.key.get_pressed()[pygame.K_n]:     
            if collision(self.paddle1, self.ball):
<<<<<<< HEAD
                self.x=10
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, 10]))
=======
                if self.ball.c:
                    self.x=10
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, 10]))
>>>>>>> a17531b (third)
            self.ball_gui = BallGui(self.ball)#球的圖片



        if pygame.key.get_pressed()[pygame.K_UP]:
            self.paddle1.move_up()
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.paddle1.move_down()
        if pygame.key.get_pressed()[pygame.K_KP1]:
            
            if collision(self.paddle2, self.ball):
<<<<<<< HEAD
                self.x=10      
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, -10]))   
=======
                if self.ball.c:
                    self.x=10      
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, -10]))   
>>>>>>> a17531b (third)
            self.ball_gui = BallGui(self.ball)#球的圖片
           
           
            
        if pygame.key.get_pressed()[pygame.K_KP2]:
            if collision(self.paddle2, self.ball):
<<<<<<< HEAD
                self.x=10      
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, 0]))
=======
                if self.ball.c:
                    self.x=10      
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, 0]))
>>>>>>> a17531b (third)
            self.ball_gui = BallGui(self.ball)#球的圖片
            
        if pygame.key.get_pressed()[pygame.K_KP3]:
            if collision(self.paddle2, self.ball):
<<<<<<< HEAD
                self.x=10      
                self.ball = Ball(30)
                self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, 10]))
            self.ball_gui = BallGui(self.ball)#球的圖片
>>>>>>> ad3ce87 (second)
=======
                if self.ball.c:
                    self.x=10      
                    self.ball = Ball(30,False)
                    self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
                    self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, 10]))
            self.ball_gui = BallGui(self.ball)#球的圖片
>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)
=======
>>>>>>> 8cb9e44 (fifth)
        # let computer move the paddles if activated
        if self.paddle1computer is not None:
            self.paddle1computer.move(self.paddle1, self.ball)

        if self.paddle2computer is not None:
            self.paddle2computer.move(self.paddle2, self.ball)
<<<<<<< HEAD

    #更新碰撞檢測,碰到上下邊界時座標為負,計算玩家的生命數量,加快球的速度
    def _update_state(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> d173cd7 (fourth)
        if collision_screen_left(self.ball):
            self.paddle1.lives -= 1
            self.ball.reset()
            self.background.flash()

        if collision_screen_right(self.ball):
            self.paddle2.lives -= 1
            self.ball.reset()
=======
    def _update_state(self):
        if collision_screen_left(self.ball):
            #print("P1的資料為:",self.paddle1computer.data)
            #print("P1的資料量為:",len( self.paddle1computer.data))
            #print("P2的資料為",self.paddle2computer.data)
            #print("P2的資料量為:",len(self.paddle1computer.data))

            self.paddle1computer.train_value.clear()
            self.paddle1computer.test_value.clear()
            self.paddle2computer.train_value.clear()
            self.paddle2computer.test_value.clear()
            
            self.Train_1P()
            self.Train_2P()
            
            self.Data_picture("Logistic")
            self.Data_picture("LinearSVC")
            
            self.paddle1.lives -= 1
            self.ball.reset()
            self.paddle1computer.data.clear()
            self.paddle2computer.data.clear()
            self.background.flash()
        if collision_screen_right(self.ball):
            
            #print("P1的資料為:",self.paddle1computer.data)
            #print("P1的資料量為:",len( self.paddle1computer.data))
            #print("P2的資料為",self.paddle2computer.data)

            self.paddle1computer.train_value.clear()
            self.paddle1computer.test_value.clear()
            self.paddle2computer.train_value.clear()
            self.paddle2computer.test_value.clear()
                
            self.Train_1P()
            self.Train_2P()
            self.Data_picture("Logistic")
            self.Data_picture("LinearSVC")
            
            self.paddle2.lives -= 1
            self.ball.reset()
            self.paddle1computer.data.clear()
            self.paddle2computer.data.clear()
>>>>>>> 8cb9e44 (fifth)
            self.background.flash()

        if collision_screen_top(self.ball) or collision_screen_bottom(self.ball):
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, -1]))
<<<<<<< HEAD

<<<<<<< HEAD
=======
        
=======
>>>>>>> a17531b (third)
        #檢測球到達左邊界時,1P生命-1
        if collision_screen_left(self.ball):
            self.paddle1.lives -= 1
            self.paddle1.position = [self.paddle1.x,pygame.display.get_surface().get_height()/2]
            self.x=10000
<<<<<<< HEAD
            self.ball = Ball(0)
            #1P發球
=======
            self.ball = Ball(0,True)
>>>>>>> a17531b (third)
            self.ball.reset(First_Player = True,Second_Player = False)
            self.background.flash()
            
        #檢測球到達左邊界時,2P生命-1
        if collision_screen_right(self.ball):
            self.paddle2.lives -= 1
            self.paddle2.position = [self.paddle2.x,pygame.display.get_surface().get_height()/2]
            self.x=10000
<<<<<<< HEAD
            self.ball = Ball(0)
            #2P發球~
=======
            self.ball = Ball(0,True)
>>>>>>> a17531b (third)
            self.ball.reset(First_Player = False,Second_Player = True)
            self.background.flash()

        #檢測球到達上或下邊界時,向量y的方向*(-1)
        if collision_screen_top(self.ball) or collision_screen_bottom(self.ball):
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([1, -1]))

        #print("加速度為:",self.ball.acceleration)
<<<<<<< HEAD
>>>>>>> ad3ce87 (second)
=======
>>>>>>> d173cd7 (fourth)
        self.ball.position += self.ball.acceleration
        self.ball.acceleration_multiply(np.array([1 + self.timer / 100000000, 1]))

        if collision(self.paddle1, self.ball):
<<<<<<< HEAD
<<<<<<< HEAD
=======
            
>>>>>>> d173cd7 (fourth)
=======
        
        if len(self.paddle1computer.data)<1000 and len(self.paddle1computer.data)<1000:
            self.Data() 
        else:
            print("目前P1資料為",len(self.paddle1computer.data),"筆資料和P2有",len(self.paddle1computer.data),"筆資料")
        
        self.ball.position += self.ball.acceleration
        self.ball.acceleration_multiply(np.array([1 + self.timer / 100000000, 1]))
       


        if collision(self.paddle1, self.ball):
>>>>>>> 8cb9e44 (fifth)
            self.ball.accelerate(acc_factor(self.paddle1, self.ball))
            self.background.flash((0, 255, 0), 100)

        if collision(self.paddle2, self.ball):
<<<<<<< HEAD
            self.ball.accelerate(acc_factor(self.paddle2, self.ball))
            self.background.flash((0, 255, 0), 100)
<<<<<<< HEAD
=======
            self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
            #self.background.flash((0, 255, 0), 100)
=======

        self.ball.position += self.ball.acceleration
        self.ball.acceleration_multiply(np.array([1 + self.timer / 100000000, 1]))
        
        #self.random_collision()
        if collision(self.paddle1, self.ball):

            self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
           # self.background.flash((0, 255, 0), 100)

        
>>>>>>> a17531b (third)

        if collision(self.paddle2, self.ball):
            self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
            #self.background.flash((0, 255, 0), 100)
<<<<<<< HEAD
>>>>>>> ad3ce87 (second)
=======

>>>>>>> a17531b (third)
=======
>>>>>>> d173cd7 (fourth)

        self.background.update()
    
    #物件的圖片
=======

            self.ball.accelerate(acc_factor(self.paddle2, self.ball))
            self.background.flash((0, 255, 0), 100)

        self.background.update()
    def Data(self):
        paddle1_center =int( self.paddle1.y + self.paddle1.height / 2)
        paddle2_center =int( self.paddle2.y + self.paddle2.height / 2)
        ball_center =int( self.ball.position[1] + self.ball.height / 2)
        
        self.paddle1computer.data.append([paddle1_center,ball_center])
        self.paddle2computer.data.append([paddle2_center,ball_center])


    def Train_1P(self):
        
        for j in range(0,len(self.paddle1computer.data)):
            if j > int((len(self.paddle1computer.data))*0.2):
                self.paddle1computer.train.append(self.paddle1computer.data[random.randint(0,len(self.paddle1computer.data)-1)])
            else:
                self.paddle1computer.test.append(self.paddle1computer.data[random.randint(0,len(self.paddle1computer.data)-1)])
                
        #print("1P資料~~~~",self.paddle1computer.data) 
        #print("1P訓練~~~~",self.paddle1computer.train)
        #print("1P訓練長度~~~~",len(self.paddle1computer.train))
        #print("1P測試~~~~",self.paddle1computer.test)
        #print("1P測試長度~~~~",len(self.paddle1computer.test))
        
        
        
    def Train_2P(self):
        
        for j in range(0,len(self.paddle2computer.data)):
            if j > int((len(self.paddle2computer.data))*0.2):
                self.paddle2computer.train.append(self.paddle2computer.data[random.randint(0,len(self.paddle2computer.data)-1)])
            else:
                self.paddle2computer.test.append(self.paddle2computer.data[random.randint(0,len(self.paddle2computer.data)-1)])
                
        #print("2P資料~~~~",self.paddle2computer.data) 
        #print("2P訓練~~~~",self.paddle2computer.train)
        #print("2P訓練長度~~~~",len(self.paddle2computer.train))
        #print("2P測試~~~~",self.paddle2computer.test)
        #print("2P測試長度~~~~",len(self.paddle2computer.test))
        
        
    def Data_picture(self,choice):
        if choice == "Logistic":
            training_data = [[50, 150], [400, 200], [100, 110], [210, 190]]
            # 0 = move up, 1 = move down
            target_values = [1, 0, 1, 0]
            
            model = LogisticRegression()
            model.fit(preprocessing.normalize(training_data), target_values)

            #1P
            for i in range(0,len(self.paddle1computer.train)):
                self.paddle1computer.train_value.append(model.predict([self.paddle1computer.train[i]]))
                
            #print("Train~~~~",self.paddle1computer.train)
            #print("Value~~~~",self.paddle1computer.train_value)
            
            df = pd.DataFrame(self.paddle1computer.train, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle1computer.train_value


            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                       ax=ax1)
            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P1_Logistic_train', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
            

            
                        
            for i in range(0,len(self.paddle1computer.test)):
                self.paddle1computer.test_value.append(model.predict([self.paddle1computer.test[i]]))
                
            #print("Value~~~~",self.paddle1computer.train_value)
            
            df = pd.DataFrame(self.paddle1computer.test, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle1computer.test_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                       ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P1_Logistic_test', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
            
            print("Logistic,1P訓練集準確度:",model.score( self.paddle1computer.train,  self.paddle1computer.train_value))
            print("Logistic,1P測試集準確度:",model.score( self.paddle1computer.test,  self.paddle1computer.test_value))
            
                    
            #2P
            for i in range(0,len(self.paddle2computer.train)):
                self.paddle2computer.train_value.append(model.predict([self.paddle2computer.train[i]]))
                
            #print("Value~~~~",self.paddle1computer.train_value)
            
            df = pd.DataFrame(self.paddle2computer.train, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle2computer.train_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                       ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P2_Logistic_train', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
            
           
            
                        
            for i in range(0,len(self.paddle2computer.test)):
                self.paddle2computer.test_value.append(model.predict([self.paddle2computer.test[i]]))
                
            #print("Value~~~~",self.paddle1computer.train_value)
            
            df = pd.DataFrame(self.paddle2computer.test, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle2computer.test_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                       ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P2_Logistic_test', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
            
            
            print("Logistic,2P訓練集準確度",model.score( self.paddle2computer.train,  self.paddle2computer.train_value))
            print("Logistic,2P測試集準確度",model.score( self.paddle2computer.test,  self.paddle2computer.test_value))
           
            
        else:
            training_data = [[50, 150], [400, 200], [100, 110], [210, 190]]
            # 0 = move up, 1 = move down
            target_values = [1, 0, 1, 0]

            
            model = svm.SVC(kernel="linear",C=100)
            model.fit(preprocessing.normalize(training_data), target_values)

            self.paddle1computer.train_value.clear()
            self.paddle1computer.test_value.clear()
            self.paddle2computer.train_value.clear()
            self.paddle2computer.test_value.clear()
            
            #1P
            for i in range(0,len(self.paddle1computer.train)):
                self.paddle1computer.train_value.append(model.predict([self.paddle1computer.train[i]]))
                 
            #print("Value~~~~",self.paddle1computer.train_value)
            

            df = pd.DataFrame(self.paddle1computer.train, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle1computer.train_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                        ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P1_SVM_train', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
             

          
            
                         
            for i in range(0,len(self.paddle1computer.test)):
                self.paddle1computer.test_value.append(model.predict([self.paddle1computer.test[i]]))
                 
             #print("Value~~~~",self.paddle1computer.train_value)
             
            df = pd.DataFrame(self.paddle1computer.test, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle1computer.test_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                        ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P1_SVM_test', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
             
            print("SVM,1P訓練集準確度",model.score( self.paddle1computer.train,  self.paddle1computer.train_value))
            print("SVM,1P測試集準確度",model.score( self.paddle1computer.test,  self.paddle1computer.test_value))
            
                        
            #2P
            for i in range(0,len(self.paddle2computer.train)):
                self.paddle2computer.train_value.append(model.predict([self.paddle2computer.train[i]]))
                 
            #print("Value~~~~",self.paddle1computer.train_value)
             
            df = pd.DataFrame(self.paddle2computer.train, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle2computer.train_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                        ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P2_SVM_train', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
             
          
            
                         
            for i in range(0,len(self.paddle2computer.test)):
                self.paddle2computer.test_value.append(model.predict([self.paddle2computer.test[i]]))
                 
             #print("Value~~~~",self.paddle1computer.train_value)
             
            df = pd.DataFrame(self.paddle2computer.test, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = self.paddle2computer.test_value

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                        ax=ax1)

            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('P2_SVM_test', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
            plt.show()
             
            print("SVM,2P訓練集準確度",model.score( self.paddle2computer.train,  self.paddle1computer.train_value))
            print("SVM,2P測試集準確度",model.score( self.paddle2computer.test,  self.paddle1computer.test_value))

  
>>>>>>> 8cb9e44 (fifth)
    def _draw_objects(self):
        self.background.draw(self.screen)

        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)

        self.ball.draw(self.screen)

        self.paddle1_gui.draw(self.screen)
        self.paddle2_gui.draw(self.screen)
        self.ball_gui.draw(self.screen)

<<<<<<< HEAD
    #遊戲結束,判斷是否繼續
=======
>>>>>>> 8cb9e44 (fifth)
    def _game_over(self, winner):
        self.game_over = True

        surface_width = pygame.display.get_surface().get_width()
        surface_height = pygame.display.get_surface().get_height()

        font = pygame.font.Font('freesansbold.ttf', 18)

        text = font.render('GAME OVER', True, (255, 255, 255))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2 - 40))
        self.screen.blit(text, text_rect)

        text = font.render('WINNER: {}'.format(winner), True, (153, 255, 153))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2))
        self.screen.blit(text, text_rect)

        text = font.render('Press "r" to restart or "esc" to quit', True, (192, 192, 192))
        text_rect = text.get_rect(center=(surface_width / 2, surface_height / 2 + 40))
        self.screen.blit(text, text_rect)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
=======
#執行程式
>>>>>>> ad3ce87 (second)
=======
    def random_collision(self):
        if collision(self.paddle1, self.ball):
            arr1=[-1,0,1]
            self.x=10
            self.ball.accelerate(acc_factor(self.paddle1, self.ball,self.x))
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, arr1[random.randint(0,2)]]))
    
        if collision(self.paddle2, self.ball):
            arr2=[-1,0,1]
            self.x=10      
            self.ball.accelerate(acc_factor(self.paddle2, self.ball,self.x))
            self.ball.acceleration = np.multiply(self.ball.acceleration, np.array([-1, arr2[random.randint(0,2)]])) 


#執行程式

>>>>>>> a17531b (third)
=======

>>>>>>> d173cd7 (fourth)
if __name__ == '__main__':
=======

if __name__ == '__main__':
    a=1
>>>>>>> 8cb9e44 (fifth)
    # play against computer
    #game = Game(paddle2computer=Computer())

    # play against human
    #game = Game()

    # computer vs computer
<<<<<<< HEAD
    game = Game(paddle1computer=Computer(), paddle2computer=Computer())
=======
    game = Game(paddle1computer=Computer(), paddle2computer=Computer())
>>>>>>> 8cb9e44 (fifth)
