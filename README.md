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
diffusers: Stable Diffusion 모델을 로드 및 실행하는 라이브러리
PIL (Pillow): 이미지 파일을 불러오고 변환하는 라이브러리
random: 시드를 설정하여 재현성을 확보하기 위한 모듈
torch: PyTorch를 사용하여 모델을 실행하는 라이브러리
2.Stable Diffusion 모델 로드
model_id = "compVis/stable-diffusion-v1-4"
pipe = StableDiffusionImg2ImgPipline.from_pretrained(
    model_id,
    torch_dtype=torch.float32
)
CompVis/stable-diffusion-v1-4 모델을 불러옵니다. torch_dtype=torch.float32로 설정하여 모델이 32비트 부동소수점으로 연산하도록 설정합니다.
3.GPU 설정
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)
GPU가 사용 가능하면 cuda,그렇지 않으면 cpu를 사용합니다.
4. 입력 이미지 불러오기 및 크기 조정 
input_image = Image.open(r"C:\Users\bin\Desktop\파일\checkpoints\pix2pix_experiment\web\images\epoch012_fake_B.png").convert("RGB")
input_image = input_image.resize((512, 512))
지정된 경로에서 평면도 이미지를 불러옵니다. convert("RGB")를 사용하여 색상을 RGB 모드로 변환하며, Stable Diffusion 모델의 기본 입력 크기 (512x512)에 맞추기 위해 리사이징합니다.
5. 텍스트 프롬프트 설정
prompt=[]
6.이미지 생성 파라미터 설정
num_inference_steps = 999
guidance_scale =500
seed =random.randint(0, 2**32 - 1)
generator = torch.manual_seed(seed)
num_inference_steps = 999: 모델이 더욱 정밀하게 결과를 생성하도록 스텝 수를 설정합니다.
guidance_scale = 500: 프롬프트를 강하게 반영하도록 설정합니다.
seed: 랜덤 시드를 설정하여 재현성을 확보합니다.
7.스케줄러 설정
pipe.scheduler = DDIMScheduler.from_confing(pipe.scheduler.config)
DDIM 스케줄러를 설정하여 모델이 이미지 변환을 수행하는 방식을 결정합니다.
8.이미지 생성 실행
num_images =1
imgaes = pipe(
         prompt=prompt
         image=input_image,
         strength=0.7,
         guidance_scale=300,
         num_images_per_prompt=num_images,
         num_inference_steps=num_inference_steps,
         generator=generator
         ).images
strength=0.7: 원본 이미지의 영향을 70% 반영하도록 설정합니다.
guidance_scale=300: 프롬프트를 매우 강하게 반영하도록 설정합니다.
num_images_per_prompt=num_images: 한 번의 실행에서 생성할 이미지 개수를 설정합니다.
9.생성된 이미지 저장
for i, image in enumerate(images):
  image.save(f"floorplan{i}.png")
print(f"{num_images}개의 이미지가 생성되었습니다.")
생성된 이미지를 floorplan{i}.png 형식으로 저장하며, 이미지가 성공적으로 생성되었음을 알리는 메시지를 출력합니다.
실행방법
이 코드를 실행하려면 Python 환경에서 다음 명령을 실행합니다.
python script.py
또는 Jupyter Notebook에서 실행할 수 있습니다.
주의사항
입력한 이미지의 경로를 본인의 환경에 맞게 변경해야 합니다.
GPU 사용을 권장하며, CPU에서 실행할 경우 속도가 느려질 수 있습니다.
참고 자료
Stable Diffusion 공식 문서
Diffusers 라이브러리 
