markdown
#Stable Diffusion 이미지 변환 코드 문서
##개요
이 코드는 Stable Diffusion Img2Img 모델을 사용하여 기존의 평면도 이미지를 변환하는 스크립트입니다.
##환경 설정
이 코드를 실행하기 위해서는 다음과 같은 라이브러리가 필요합니다.
###필수 라이브러리 설치 
```bash
pip install torch diffusers pillow
1. 라이브러리 임포트
from diffusers import StableDiffusionImg2ImgPipeline, DDIMScheduler
from PIL import Image
import random
import torch

