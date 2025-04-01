import sys
import os
import cv2
import numpy as np

###########################################################
###########################################################

start_min = 4
start_sec = 42

finish_min = 4
finish_sec = 47

# tic =          # tic 초에 1 장 찍기
tic_frame = 15

video_num = 2
img_class = 4

###########################################################
###########################################################

start = start_min*60 + start_sec
finish = finish_min*60 + finish_sec

# 각자 영상 경로에 맞추어 수정
video_path = f"C:/2024GEP/videos/gogi_experiment_{video_num}.mp4"
img_path = f"C:/2024GEP/img/class_{img_class}"

try:
    video = cv2.VideoCapture(video_path)
    print('동영상 읽기 성공')
except:
    print('동영상 읽기 실패')

# fps = video.get(cv2.CAP_PROP_FPS)
fps = 30



def get_name(img_path):
    img = os.listdir(img_path)
    img_num = int(img[-1][-8:-4]) + 1
    name = (f"x{img_class}_exp{video_num : #03d}_{img_num : #05d}.jpg").replace(' ', '') # ex) exp01_c1_0002.jpg
    return name

def display_video(img):
    cv2.imshow('animation', img) # 동영상을 잘 읽어왔을때

    k = cv2.waitKey(33) # waitKey(33) : 한장의 사진을 0.033초 동안 띄움
    
    if k == 49: # 1을 눌렀을 때
        print('동영상 종료')
        video.release()
        cv2.destroyAllWindows()
        return 0
    return 1

start_frame = start * fps
finish_frame = finish * fps
# tic_frame = tic * fps

frame_count = 0

while True:
    ret, img = video.read() # 성공 여부(bool), 이미지
    frame_count += 1
    
    if not ret : # ret이 False일때 (파일에 문제가 있거나 동영상이 끝났을때)
        print('이미지 읽기 실패 또는 모두 읽음')
        video.release()
        cv2.destroyAllWindows() # 윈도우 실행창 종료
        break

    
    if start_frame <= frame_count and frame_count <=finish_frame:
        now_frame = frame_count - start_frame
        if now_frame % tic_frame == 0:
            name = get_name(img_path)
            cv2.imwrite(f"{img_path}/{name}", img)
    
    
    if finish_frame < frame_count:
        video.release()
        break
    
    # if display_video(img)==0:
    #     break