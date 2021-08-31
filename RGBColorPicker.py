################################################ SAYED THE PROGRAMMER ###############################################

import cv2
import numpy as np

img = np.zeros((400, 612, 3), np.uint8)
cv2.namedWindow("Color Picker")
cv2.imshow("Color Picker", img)
r, g, b = 0, 0, 0


def fHandler(x):
    get_trackbar_value()


def create_trackbar():
    cv2.createTrackbar("R", "Color Picker", 0, 255, fHandler)
    cv2.createTrackbar("G", "Color Picker", 0, 255, fHandler)
    cv2.createTrackbar("B", "Color Picker", 0, 255, fHandler)


def get_trackbar_value():
    global r, g, b
    r = cv2.getTrackbarPos("R", "Color Picker")
    g = cv2.getTrackbarPos("G", "Color Picker")
    b = cv2.getTrackbarPos("B", "Color Picker")


if __name__ == "__main__":
    create_trackbar()
    while True:
        cv2.imshow("Color Picker", img)
        img[:] = [b, g, r]
        print("R:", r)
        print("G:", g)
        print("B:", b)
        if cv2.waitKey(1) == 27:
            cv2.destroyAllWindows()
            break
        else:
            pass
        print("------End of main-----")
