# 2024GEP

## 따라하기

- #### 환경 설정

yolov5 git clone 해오기(https://github.com/ultralytics/yolov5)
```
!git clone https://github.com/ultralytics/yolov5
```

requirements.txt 다운받기
```
!pip install -r requrirements.txt
```

- #### 학습 방법

```
!python ./yolov5/train.py --img 416 --batch 8 --epochs 200 --data data.yaml --cfg ./yolov5/models/yolov5s.yaml --weights start_model.pt --name model_name
```
- `data.yaml` : 만든 데이터셋의 data.yaml 파일 경로
- `start_model.pt` : Pre-trained Model의 파일 경로
- `model_name` : 학습시키는 모델의 이름

- #### 객체 탐지 방법
```
!python ./yolov5/detect.py --source ./test --weights model.pt
```
- `./test` : 탐지하고자 하는 사진이나 영상의 파일 경로 혹은 사진이나 영상이 있는 폴더 경로
- `model.pt` : 탐지에 사용하는 모델

## 코드 설명

- #### `graph.ipynb`

그래프 그리는 코드   

`plot_r`는 하나의 그래프를 그릴 때 사용  
`plot_r` 위에 있는 함수는 여러개 출력 및 기타  
*아래는 신경 쓰지 마셈

- #### `Img_extraction.py`

영상에서 이미지를 특정 시간 간격으로 따오는 프로그램   

주석 보면 이해 갈거임

- #### `split_folder.py`

라벨이랑 사진이랑 모두 같이 있을 때, test, train, vaild로 특정 비율로 나누는 프로그램   

주석 보면 이해 갈거임

- #### `split_files.py`

test, train, vaild로 나눴을 때, img 파일이랑 label 파일 나누는 프로그램

- #### 기타 프로그램

걍 읽어보면(+ 파일이름) 이해 갈거임   

*data.yaml 파일 만드는 프로그램은 딱히 없음 걍 알아서 만드셈

## 부가 설명

- #### dataset, labels

labels는 데이터(이미지 + 라벨) 하나에 모아놓은거 dataset은 test, train, vaild로 나눈거 (모델 학습에 직접적으로 사용)

- #### 1234

1234 붙은건 전람회에 낸 모델에 사용한거  

class가 1, 2, 3, 4 만 있음   

- #### 123456789

class가 1, 2, 3, 4, 5, 6, 7, 8, 9 다 있음

- #### class

1. 0번 뒤집음
2. 1번 뒤집을 차례
3. 1번 뒤집음
4. 2번 뒤집을 차례
5. 2번 뒤집음
6. 3번 뒤집을 차례
7. 3번 뒤집음
8. 4번 뒤집을 차례
9. 4번 뒤집음 (= 끝)

- #### 제외한 데이터

exp02_c3_0055 이유 : 흔들림
