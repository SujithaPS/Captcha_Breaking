
from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
from tensorflowpath import *
import numpy as np
import imutils
import cv2
import pickle
import pyperclip
import os

CAPTCHA_IMAGE_FOLDER = "input_image"
captcha_image_files = list(paths.list_images(CAPTCHA_IMAGE_FOLDER))
captcha_image_files = np.random.choice(captcha_image_files, size=(1,))
for image_file in captcha_image_files:
  raw_data = open(image_file, 'rb').read()
  captcha_text = solver.solve_captcha(raw_data)
  pyperclip.copy(captcha_text)
  print('Captcha Text: ' + captcha_text)
  exit()
