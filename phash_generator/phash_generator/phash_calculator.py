import cv2
from PIL import Image
import imagehash
import os


def calculate_phash(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp')):
        img = Image.open(file_path)
        return str(imagehash.phash(img))

    elif file_path.lower().endswith(('.mp4', '.mov', '.avi', '.mkv', '.webm')):
        cap = cv2.VideoCapture(file_path)
        success, frame = cap.read()
        cap.release()
        if not success:
            raise Exception('Could not read frame from video')

        # Convert the frame (which is a Numpy array) to an image format for hashing
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        return str(imagehash.phash(img))

    else:
        raise ValueError('Unsupported file type. Only Images and Videos are supported.')

