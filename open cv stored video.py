import cv2

vid = cv2.VideoCapture("D:/MOVIES/Enola_Holmes_2_2022_1080p_NF_WEBRip_1600MB_DD5_1_x264_GalaxyRG.mkv")
  
while(True):

    ret, frame = vid.read()

    cv2.imshow('frame', frame)
      
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
