# taeho_repository ![HitCount](http://hits.dwyl.com/KHU-Face-ID/taeho_repository.svg)

## 1. image_capture
카메라에 얼굴이 n프레임이상 인식되면 n프레임마다 캡쳐하여 저장한다.(이미지가 저장될때 확인용 글씨는 저장되지 않는다.)

* 얼굴을 인식하지 못했을 경우

![png](https://github.com/KHU-Face-ID/taeho_repository/blob/master/image/capture/20-03-26_23-53-06.png?raw=true)

* 얼굴을 인식했을 경우(캡쳐함)

![png](https://github.com/KHU-Face-ID/taeho_repository/blob/master/image/capture/20-03-26_23-51-26.png?raw=true)

## 2. face_recognition(https://github.com/ageitgey/face_recognition)
얼굴이 나온 이미지를 label별로 각각 폴더에 저장하면 여러장의 사진을 인식해 학습하여 얼굴인식이 가능하다. >> 여러장으로 학습시키니 확실히 성능이 늘었다.

* 결과 이미지

![png](https://github.com/KHU-Face-ID/taeho_repository/blob/master/image/face_recognition/result.png?raw=true)

## 3. Use smart phone camera
ip webcam을 통해 스마트폰 카메라를 쓰니 화질이 아주 좋고 부드러워짐. 하지만 face_recognition을 돌리니 어차피 노트북에서 모델이 돌아가는 딜레이가 있어서 때문에 그전과 비슷하게 끊긴다. >> 가벼운 모델을 쓰거나 좋은 서버가 필요할 듯 하다.
