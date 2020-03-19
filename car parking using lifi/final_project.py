import cv2

cap = cv2.VideoCapture("park.mp4")
n_rows = 3
n_images_per_row = 3

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    height, width, ch = frame.shape

    roi_height = int(height / n_rows)
    roi_width = int(width / n_images_per_row)

    images = []

    for x in range(0, n_rows):
        for y in range(0,n_images_per_row):
            tmp_image=frame[x*roi_height:(x+1)*roi_height, y*roi_width:(y+1)*roi_width]
            images.append(tmp_image)

    # Display the resulting sub-frame
    for x in range(0, n_rows):
        for y in range(0, n_images_per_row):
            ret, cut = cv2.imshow(str(x*n_images_per_row+y+1), images[x*n_images_per_row+y])
            cv2.moveWindow(str(x*n_images_per_row+y+1), 100+(y*roi_width), 50+(x*roi_height))
            camera = cv2.VideoCapture(cut)
            car_cascade = cv2.CascadeClassifier('cars.xml')
            print('ok')
            # Get frames per second from video file. Syntax depends on OpenCV version: 
            (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
            if int(major_ver)  < 3 :
                fps = camera.get(cv2.cv.CV_CAP_PROP_FPS)
            else :
                fps = camera.get(cv2.CAP_PROP_FPS)
                fps=25
            #:if
            intTimeToNextFrame=int(1000.0/fps)-12 # '-12' estimation of time for processing
            while True:
                (grabbed,frame) = camera.read()
                grayvideo = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cars = car_cascade.detectMultiScale(grayvideo, 1.1, 1)
                print('ok2')
            for (x,y,w,h) in cars:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),1)
                cv2.imshow("video",frame)
            if cv2.waitKey(intTimeToNextFrame)== ord('q'):
                break
            camera.release()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()