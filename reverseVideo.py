import cv2

def play_video(vid, fps, fnumber, width, height):
   
    frame_index = fnumber-1
    codec = cv2.VideoWriter_fourcc(*"XVID")
    output = cv2.VideoWriter("sayed_reverse_video.avi", codec, fps, (width, height))
    
    while vid.isOpened():
        
        # SET THE FRAME POSITON AT THE END
        vid.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = vid.read()
        
        if ret == True:
            cv2.imshow("Playing Video", frame)
            output.write(frame)
        else:
            break
        
        if cv2.waitKey(25) == ord("q"):
            break
        
        
        # FINALLY DECREASE THE FRAME INDEX
        frame_index = frame_index-1
        
        
    output.release()
    vid.release()
    cv2.destroyAllWindows()
        

if __name__ == "__main__":
    vid = cv2.VideoCapture("cartoon.mp4")  # ENTER THE VIDEO PATH HERE
    
    fps = vid.get(cv2.CAP_PROP_FPS)
    fnumber = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    # Play the video
    play_video(vid, fps, int(fnumber), int(width), int(height))