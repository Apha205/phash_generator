from sqlite3.dbapi2 import Timestamp

import cv2 #loads the video
from PIL import Image #PIL turns images to frames
import numpy as np #Numpy is used for combining images(arrays)- Images are arrays
import imagehash #Gets the image phash
import os #used for video path

from PIL.Image import fromarray
from docutils.nodes import image
from imagehash import phash
from twisted.conch.scripts.tkconch import frame

#We are telling python that we are grabing 25 frames, each resized to 160px width and lay them into 5*5 grid
SPRITE_WIDTH = 160 #pixels
ROWS = 5
COLUMNS = 5
FRAME_COUNT = ROWS * COLUMNS #25 frames

#We need to get the video duration to be able to skip the intros and the outros(first and last 5%) which are often black
def get_video_duration(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Failed to open the video file: {video_path}")
    #frames per second
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    duration = frame_count / fps
    cap.release()
    return duration #in seconds

def extract_frames(video_path):
    duration = get_video_duration()
    cap = cv2.VideoCapture(video_path)

    offset = 0.05 * duration #offset means skipping 5% of the video
    step = (0.90 * duration) / FRAME_COUNT
    frames =[]
    for i in range(FRAME_COUNT):
        timestamp = offset + i * step
        cap.set(cv2.CAP.PROP_POS_MSEC, timestamp * 1000) #Milliseconds
        ret, frame = cap.read()
        if not ret:
         continue

# Convert and resize frames
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image,fromarray((frame).resize(SPRITE_WIDTH, SPRITE_WIDTH))
        frames.append(image)
    cap.release()
    return frames

#Combine all the 25 thumbnail frames to a single image(a sprite) that visually summarizes the whole video
#The sprite will be used as input to calculate the phash(We will generate the phash from this sprite)
def create_sprite(frames):
    sprite = Image.new('RGB', (SPRITE_WIDTH * 5, SPRITE_WIDTH * 5)) #Create a blank image(the sprite)
    for idx in enumerate(frames):    #enumerate(frames) lets us loop through each frame with its index(idx)
        row = idx // 5
        col = idx % 5
        sprite.paste(frame, col * SPRITE_WIDTH, row * SPRITE_WIDTH) #Paste the frames at the calculated position
        return sprite

def get_phash():
    video_phash = phash(sprite)
    return   video_phash

