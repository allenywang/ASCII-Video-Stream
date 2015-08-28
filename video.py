
from PIL import Image
import os
import cv2
import numpy


def main():


    # Begin capturing video. You can modify what video source to use with VideoCapture's argument. It's currently set
    # to be your webcam.
    capture = cv2.VideoCapture(0)

    while True:
        # To quit this program press q.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Breaks down the video into frames
        ret, frame = capture.read()

        # Displays the current frame
        cv2.imwrite('test.jpg', frame)
        os.system('python img2txt/img2txt.py test.jpg')
        cv2.waitKey(10)

        # Converts image to grayscale.






if __name__ == "__main__":
    main()
