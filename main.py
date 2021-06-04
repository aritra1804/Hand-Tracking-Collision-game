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
    
fingers_radius = 20
fingers = [pymunk.Body(10, 1666, body_type=pymunk.Body.KINEMATIC) for i in range(21)]
for i, finger in enumerate(fingers):
    finger_shape = pymunk.Circle(fingers[i], fingers_radius)
    space.add(fingers[i], finger_shape)
    
for hand_landmarks in results.multi_hand_landmarks:
  for i, finger in enumerate(fingers):
    x = int(hand_landmarks.landmark[i].x * image.shape[1])
    y = image.shape[0]-int(hand_landmarks.landmark[i].y * image.shape[0])
    fingers[i].position = x, y
