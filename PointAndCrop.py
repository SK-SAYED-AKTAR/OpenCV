import cv2
import numpy as np

pt1 = []
width, height = 240, 400
output = []
def draw_circle(event, x, y, flag, param):
    global pt1
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, (0, 0, 255), cv2.FILLED)
        pt1.append([x, y])
        cv2.imshow("Card", img)

        if len(pt1) == 4:
            pt1 = np.float32(pt1)
            cut_image()

def cut_image():
    global output
    pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    print("Point2:",pt2)
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    output = cv2.warpPerspective(img, matrix, (width, height))
    cv2.imshow("New Card", output)

img = cv2.imread("images/card.jpg")
cv2.imshow("Card", img)

while True:
    try:
        cv2.setMouseCallback("Card", draw_circle)
        if cv2.waitKey(0) == 27:
            print(pt1)
            cv2.destroyAllWindows()
            break
    except:
        break

print("Before output:", output)
output[:] = (255, 0, 0)
print("After output:", output)
cv2.imshow("Blue Card", output)
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

print(output.shape)
