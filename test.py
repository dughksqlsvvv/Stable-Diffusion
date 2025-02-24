개요

이 코드는 PIL(Python lmaging library)의 Image및 ImageOps 모듈을 사용하여 이미지를 특정 크기로 리사이징하고, 크기가 맞지 않는 경우 검정색 배경을 추가하여 정해진 크기로 맞춥니다.

필요 라이브러리

PIL(Python lmaging library,Pillow 패키지에서 제공)

Image 및 ImageOps모듈

코드설명

import Image, ImageOps # 이미지 처리 라이브러리 PIL에서 Image 및 ImageOps 모듈을 임포트

PIL 라이브러리를 이용하여 이미지를 로드하고 조작할 수 있도록 합니다.

#원본 이미지 로드 (파일 경로를 자신의 이미지 경로에 맞게 수정)

image = Image.open()#PNG 파일 혹은 다른 형식의 이미지

Image.open()을 사용하여 지정된 경로에서 이미지를 불러옵니다.

파일 경로는 사용자의 환경에 맞게 변경해야 합니다.

#원본 이미지 크기

original_width, original_height = image.size #원본 이미지의 너비와 높이 저장

image.size를 사용하여 원본 이미지의 크기(너비,높이)를 가져옵니다.

#목표 크기 설정
target_width =512  #목표 이미지의 너비 (픽셀 단위)

target_height =256 #목표 이미지의 높이 (픽셀 단위) 

이미지 리사이징 후 저장할 목표 크기를 저장합니다.

#원본 이미지의 비율 계산
aspect_ratio = original_width / original_width #원본 이미지의 너비와 높이 비율 계산

#목표 크기에서 새로운 크기 계산 (비율 유지)
if target_width / target_height > aspect_ratio: #목표 크기의 너비와 높이 비율이 원본 비율보다 클 경우
  new_width = target_height * aspect_ration #새로운 너비 계산
  new_heiht = target_height # 새로운 높이는 목표 높이와 같음
else:
  new_width = target_width #새로운 너비는 목표 너비와 같음
  new_heighr = target_width / aspect_ratio #새로운 높이는 목표너비에 맞춰 비율에 맞게 계산

#이미지 리사이즈
resized_image = image.resize(int(new_heighr), int(new_height)), Image.Resampling.LANCZOS) #비율에 맞게 이미지를 리사이즈

image.resize()를 사용하여 새로운 크기로 이미지를 조정합니다.

#이미지 크기와 목표 크기가 일치하지 않으면 패딩 추가
#배경색 (검정색)을 추가하여 목표 크기로 맞추기
  new_image =Image.new("RGB",(target_width, target_height), (0,0,0)) #목표 크기만큼 새로운 검정 배경 이미지를 생성
새로운 검정색 (RGB(0,0,0))배경을 생성하여, 원본 이미지와 목표 크기가 일치하지 않을 경우 배경을 추가합니다.

new_image.paste(resized_image, ((target_width - int(new_width)) // 2,(target_height - int(new_height)) // 2))  # 리사이즈된 이미지를 가운데 배치
paste()를 사용하여 배경 중앙에 리사이즈된 이미지를 배치합니다.

#최종 이미지 저장(PNG 형식)
resized_image.save("",format="PNG") #결과 이미지를 PNG 형식으로 저장
save()를 사용하여 최종 이미지를 PNG파일로 저장합니다.
결론
이 코드는 특정 크기로 이미지를 리사이징하고, 부족한 부분을 검정색 배경으로 채우는 기능을 수행합니다. 다만 몇가지 수정이 필요하며, 이를 반영하면 정확한 결과를 얻을 수 있습니다.
