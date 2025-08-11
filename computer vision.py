import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

while True:
    ret, frame = kamera.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    contours, _= cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h, = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "Merah Terdeteksi", (x, y-10), cv2.
            FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            
    cv2.imshow("Deteksi warna merah", frame)
    cv2.imshow("masking", mask)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
kamera.release()
cv2.destroyAllWindows()
                    