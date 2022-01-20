import random
import pygame


<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def acc_factor(paddle, ball):
=======
def acc_factor(paddle, ball,x):
>>>>>>> ad3ce87 (second)
    ball_center = ball.position[1] + ball.height / 2
    paddle_center = paddle.y + paddle.height / 2

=======
def acc_factor(paddle, ball,x):
    ball_center = ball.position[1] + ball.height / 2
    paddle_center = paddle.y + paddle.height / 2

    #中心相減
>>>>>>> a17531b (third)
=======
def acc_factor(paddle, ball):
    ball_center = ball.position[1] + ball.height / 2
    paddle_center = paddle.y + paddle.height / 2

>>>>>>> d173cd7 (fourth)
    distance = ball_center - paddle_center

    if distance == 0:
        distance = random.randint(10, 100)
<<<<<<< HEAD
<<<<<<< HEAD

<<<<<<< HEAD
    return distance / 10
=======

    return distance / x
>>>>>>> ad3ce87 (second)
=======
    return distance / x
>>>>>>> a17531b (third)
=======

    return distance / 10
>>>>>>> d173cd7 (fourth)

=======
def acc_factor(paddle, ball):
    ball_center = ball.position[1] + ball.height / 2
    paddle_center = paddle.y + paddle.height / 2

    distance = ball_center - paddle_center

    if distance == 0:
        distance = random.randint(0, 100)
    else:
        distance = random.randint(-100, 100)
    return distance / 10
>>>>>>> 8cb9e44 (fifth)

def collision_screen_left(ball):
    return ball.position[0] <= 0


def collision_screen_right(ball):
    surface_width = pygame.display.get_surface().get_width()
    return ball.position[0] + ball.width >= surface_width


def collision_screen_top(ball):
    return ball.position[1] <= 0


def collision_screen_bottom(ball):
    surface_height = pygame.display.get_surface().get_height()
    return ball.position[1] + ball.height >= surface_height


def collision(paddle, ball):
    return aabb_collision(
        paddle.x,
        paddle.y,
        paddle.width,
        paddle.height,
        ball.position[0],
        ball.position[1],
        ball.width,
        ball.height
    )

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
def aabb_collision(a_x, a_y, a_width, a_height, b_x, b_y, b_width, b_height):
    collision_x = a_x + a_width >= b_x and b_x + b_width >= a_x
    collision_y = a_y + a_height >= b_y and b_y + b_height >= a_y

    return collision_x and collision_y
