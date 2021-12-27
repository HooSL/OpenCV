import cv2
import numpy as np

#캠으로부터 데이터를 가져오기
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print('카메라로부터 정보를 얻을 수 없습니다.')
else :
    #프레임의 정보를 가져와 보기!

    #화면 크기를 말하는것! (width, height)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    print(frame_width,frame_height)

    out = cv2.VideoWriter('data/videos/output.avi', 
                     cv2.VideoWriter_fourcc('M', 'J','P','G'),
                     10,
                     (frame_width, frame_height))
    #캠으로부터 사진을 계속 입력 받아서 화면에도 표시하고 위의 out에 저장을 해주면 된다
    while True :
        ret, frame = cap.read()
        if ret == True :
            # 화면에도 표시하고
            cv2.imshow('Video', frame)
            # 파일에도 저장한다.
            out.write(frame)

            #유저가 esc를 누르면 촬영종료
            if cv2.waitKey(1) & 0xFF == 27:
                break
        else:
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

