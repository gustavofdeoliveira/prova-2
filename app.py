# importando as biblioteca
from ultralytics import YOLO
import cv2

video = cv2.VideoCapture(0)
model = YOLO('best.pt')
  

frame_width = int(video.get(3))
frame_height = int(video.get(4))
   
size = (frame_width, frame_height)
   
result = cv2.VideoWriter('video.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)
    
while(True):
    ret, frame = video.read()
  
    if ret == True: 
        result_frame = model.predict(frame, conf=0.6)
        result.write(result_frame[0].plot())
        cv2.imshow('Frame', result_frame[0].plot())
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
  
    # Break the loop
    else:
        break
  
video.release()
result.release()
    
# Closes all the frames
cv2.destroyAllWindows()
   
print("The video was successfully saved")