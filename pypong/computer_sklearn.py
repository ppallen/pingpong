import random
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 8cb9e44 (fifth)

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD


=======
from collision import *
from paddle import Paddle
from ball import Ball
>>>>>>> ad3ce87 (second)
=======


from collision import *
from paddle import Paddle
from ball import Ball
>>>>>>> a17531b (third)
=======


>>>>>>> 8cb9e44 (fifth)
class Computer:

    def __init__(self):
        # features: y position of paddle center, y position of ball center
        training_data = [[50, 150], [400, 200], [100, 110], [210, 190]]

        # 0 = move up, 1 = move down
        target_values = [1, 0, 1, 0]
<<<<<<< HEAD

        self.model = LogisticRegression()
        self.model.fit(preprocessing.normalize(training_data), target_values)
=======
        self.time=1
        self.data=[]
        self.data_value=[]        
        self.test=[]
        self.test_value=[]
        self.train=[]
        self.train_value=[]
    

        self.model = LogisticRegression()
        self.model.fit( preprocessing.normalize(training_data), target_values)
>>>>>>> 8cb9e44 (fifth)

        # prediction function used for linear regression
        print('f(paddle_center, ball_center) = {} + {} * paddle_center + {} * ball_center'.format(
            round(self.model.intercept_[0], 4),
            round(self.model.coef_[0][0], 4),
            round(self.model.coef_[0][1], 4)
        ))

        # uncomment to visualize the input and prediction data
        self._visualize_data_relationship()

    def move(self, paddle, ball):
        paddle_center = paddle.y + paddle.height / 2
        ball_center = ball.position[1] + ball.height / 2
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
        

        
        
>>>>>>> ad3ce87 (second)
=======
>>>>>>> a17531b (third)
=======
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing #特徵縮放
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import numpy as np
class Computer:

    def __init__(self):
        #Logistic邏輯斯迴歸
        # features: y position of paddle center, y position of ball center
        #以第一筆資料來看,板子中心50及球中心150,所以在球150的狀況之下板子要往上移動(1)
        training_data = [[50, 150], [400, 200], [100, 110], [210, 190]]
        
        # 1 = move up, 0 = move down
        target_values = [1, 0, 1, 0 ]

        #建立模型
        self.model = LogisticRegression()
        #訓練
        self.model.fit(preprocessing.normalize(training_data), target_values)
        

        print('Logistic訓練集: ',self.model.score(preprocessing.normalize(training_data),target_values))
        # prediction function used for linear regression
        #print('f(paddle_center, ball_center) = {} + {} * paddle_center + {} * ball_center'.format(
       #     round(self.model.intercept_[0], 4),
       #     round(self.model.coef_[0][0], 4),
       #     round(self.model.coef_[0][1], 4)
       # ))
        
        


        # uncomment to visualize the input and prediction data
        self._visualize_data_relationship(0)


        #LinearSVC
        self.model = svm.LinearSVC(C=100)
        self.model.fit (preprocessing.normalize(training_data), target_values)
        print('LinearSVC訓練集: ',self.model.score(preprocessing.normalize(training_data),target_values))
        self._visualize_data_relationship(1)
        
        
        
        
    def move(self, paddle, ball):
        paddle_center = paddle.y + paddle.height / 2
        ball_center = ball.position[1] + ball.height / 2

>>>>>>> d173cd7 (fourth)
        prediction = self.model.predict(preprocessing.normalize([[paddle_center, ball_center]]))
=======

        prediction = self.model.predict(([[paddle_center, ball_center]]))
>>>>>>> 8cb9e44 (fifth)
        print('input: [{}, {}], prediction: {}'.format(paddle_center, ball_center, prediction))

        if prediction == 0:
            paddle.move_up()

        if prediction == 1:
            paddle.move_down()

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
    
>>>>>>> ad3ce87 (second)
=======
>>>>>>> a17531b (third)
=======
>>>>>>> 8cb9e44 (fifth)
    def _visualize_data_relationship(self):
        random_inputs = []
        predictions = []

        for _ in range(0, 1000):
            y_paddle = random.randint(1, 300)
            y_ball = random.randint(1, 300)
<<<<<<< HEAD
=======
    def _visualize_data_relationship(self,x):
        random_inputs = []
        predictions = []

        for _ in range(0, 3000):#隨機3000筆資料
            y_paddle = random.randint(1, 500)
            y_ball = random.randint(1,500)
>>>>>>> d173cd7 (fourth)
=======
>>>>>>> 8cb9e44 (fifth)
            random_inputs.append([y_paddle, y_ball])

            predictions.append(self.model.predict([[y_paddle, y_ball]]))

<<<<<<< HEAD
<<<<<<< HEAD
=======
        #print("預測~~~",predictions)        

>>>>>>> 8cb9e44 (fifth)
        df = pd.DataFrame(random_inputs, columns=['y_center_paddle', 'y_center_ball'])
        df['action'] = predictions

        ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='blue')
        df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=100, color='magenta',
                                   ax=ax1)

        plt.legend(labels=['Move UP', 'Move DOWN'])

<<<<<<< HEAD
        plt.title('Relationship between Y position of paddle center and Y position of ball center', size=24)
        plt.xlabel('Y position of paddle center', size=18)
        plt.ylabel('Y position of ball center', size=18)

        plt.show()
=======
       

        
        #Logistic計算準確率
        #print(self.model.predict(random_inputs))
        if x==0:
            df = pd.DataFrame(random_inputs, columns=['y_center_paddle', 'y_center_ball'])
            df['action'] = predictions

            ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=50, color='blue')
            df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=50, color='magenta',
                                       ax=ax1)
            
            plt.legend(labels=['Move UP', 'Move DOWN'])

            plt.title('Logistic', size=24)
            plt.xlabel('Y position of paddle center', size=18)
            plt.ylabel('Y position of ball center', size=18)
           # plt.tight_layout()
            plt.show()
            print('Logistic測試集: ',self.model.score(preprocessing.normalize(random_inputs),predictions))
            error = 0
            for i,v in enumerate(self.model.predict(random_inputs)):
                if v != predictions[i]:
                    error += 1
            #print("Logistic準確率為: "+str((1-error)*100) +"%")
            
        
        #LinearSVC計算準確率
        if x == 1:
            #df = pd.DataFrame(random_inputs, columns=['y_center_paddle', 'y_center_ball'])
            #df['action'] = predictions

            #ax1 = df[df['action'] == 0].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=50, color='blue')
            #df[df['action'] == 1].plot(kind='scatter', x='y_center_paddle', y='y_center_ball', s=50, color='magenta',
           #                            ax=ax1)
            
            #plt.legend(labels=['Move UP', 'Move DOWN'])

           # plt.title('LinearSVC', size=24)
           # plt.xlabel('Y position of paddle center', size=18)
           # plt.ylabel('Y position of ball center', size=18)
           #plt.tight_layout()
        
            plt.scatter(preprocessing.normalize(random_inputs)[:,0], preprocessing.normalize(random_inputs)[:,1], c=predictions, s=30, cmap=plt.cm.Paired)  # 散點圖，根據 y值設定不同顏色
            ax = plt.gca()  # 移動座標軸
            xlim = ax.get_xlim()  # 獲得Axes的 x座標範圍
            ylim = ax.get_ylim()  # 獲得Axes的 y座標範圍
            xx = np.linspace(xlim[0], xlim[1], 30)  # 建立等差數列，從 start 到 stop，共 num 個
            yy = np.linspace(ylim[0], ylim[1], 30)  #
            YY, XX = np.meshgrid(yy, xx)  # 生成網格點座標矩陣 XUPT
            xy = np.vstack([XX.ravel(), YY.ravel()]).T  # 將網格矩陣展平後重構為陣列
            Z = self.model.decision_function(xy).reshape(XX.shape)
            ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
            linestyles=['--', '-', '--'])  # 繪製決策邊界和分隔
            #ax.scatter(self.model.support_vectors_[:, 0], self.model.support_vectors_[:, 1], s=100,
            #linewidth=1, facecolors='none', edgecolors='k')  # 繪製 支援向量
            plt.title("Classification by LinearSVM (youcans, XUPT)")
            plt.show()
            print('LinearSVC準確度：{:.4f}'.format(self.model.score(preprocessing.normalize(random_inputs),predictions)))  # 對訓練集的分類準確度
            #print('LinearSVC測試集: ',self.model.score(preprocessing.normalize(random_inputs),predictions))
            # 使用訓練資料預測分類
            predicted = self.model.predict(random_inputs)
        
            # 計算準確率
            #print( "LinearSVC準確率為:"+str(self.model.score(random_inputs, predictions)*100) +"%")
        
       
        
       
        
>>>>>>> d173cd7 (fourth)
=======
        plt.title('Random data,Relationship between Y position of paddle center and Y position of ball center', size=20)
        plt.xlabel('Y position of paddle center', size=18)
        plt.ylabel('Y position of ball center', size=18)

        plt.show()
>>>>>>> 8cb9e44 (fifth)
