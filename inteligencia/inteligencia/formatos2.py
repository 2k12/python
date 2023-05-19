import cv2


def cargarvideo():
    # Cargar el video
    video = cv2.VideoCapture('./pictures/ia.mp4')
    
    while video.isOpened():
        ret, frame = video.read()
    
        # Realiza operaciones en cada fotograma
    
        cv2.imshow('Video', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    video.release()
    cv2.destroyAllWindows()

