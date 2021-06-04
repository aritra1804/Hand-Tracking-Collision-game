import pymunk 
import cv2
import numpy as np
import mediapipe as mp
mp_hands = mp.solutions.hands

# define the space for handling physics
space = pymunk.Space()
space.gravity = 0, -500

# define balls as dynamic bodies for physics engine
balls_radius = 12
balls = [(300 + np.random.uniform(-30, 30), 400 + 50*i + 0.5*i**2) for i in range(50)]
balls_body = [pymunk.Body(100.0,1666, body_type=pymunk.Body.DYNAMIC) for b in balls]
for i, ball in enumerate(balls_body): 
    balls_body[i].position = balls[i]
    shape = pymunk.Circle(balls_body[i], balls_radius)
    space.add(balls_body[i], shape)
