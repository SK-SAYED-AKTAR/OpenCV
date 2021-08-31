import cv2
import pyautogui as gui
import numpy as np

codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
framePerSec = 4.0
output = cv2.VideoWriter("record.avi", codec, framePerSec, gui.size())

while True:
    img = gui.screenshot()
    f = np.array(img)
    # f = cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
    output.write(f)
    if cv2.waitKey(1) == ord("q"):
        break

output.release()
cv2.destroyAllWindows()

# import pyautogui as p
# import cv2 as c
# import numpy as np
# #Create resolution
# rs = p.size()
# #filename in which we store recording
# fn = "output.avi"
# #Fix the frame rate
# fps = 60.0
# fourcc = c.VideoWriter_fourcc(*'XVID')
# output = c.VideoWriter(fn,fourcc,fps,rs)
# #create recording module
# c.namedWindow("LIve_Recording",c.WINDOW_NORMAL)
# #Resize the window
# c.resizeWindow("Live",(600,400))
# while True:
#     img = p.screenshot() #image
#     f = np.array(img) #convert image into array
#     f = c.cvtColor(f,c.COLOR_BGR2RGB)
#     output.write(f)
#     # c.imshow("screenshot", f)
#     if c.waitKey(1) == ord("q"):
#         break
# c.destroyAllWindows()
# output.release()