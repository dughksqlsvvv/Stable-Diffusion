"""General-purpose test script for image-to-image translation.

Once you have trained your model with train.py, you can use this script to test the model.
It will load a saved model from '--checkpoints_dir' and save the results to '--results_dir'.

It first creates model and dataset given the option. It will hard-code some parameters.
It then runs inference for '--num_test' images and save results to an HTML file.

Example (You need to train models first or download pre-trained models from our website):
    Test a CycleGAN model (both sides):
        python test.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan

    Test a CycleGAN model (one side only):
        python test.py --dataroot datasets/horse2zebra/testA --name horse2zebra_pretrained --model test --no_dropout

    The option '--model test' is used for generating CycleGAN results only for one side.
    This option will automatically set '--dataset_mode single', which only loads the images from one set.
    On the contrary, using '--model cycle_gan' requires loading and generating results in both directions,
    which is sometimes unnecessary. The results will be saved at ./results/.
    Use '--results_dir <directory_path_to_save_result>' to specify the results directory.

    Test a pix2pix model:
        python test.py --dataroot ./datasets/facades --name facades_pix2pix --model pix2pix --direction BtoA

See options/base_options.py and options/test_options.py for more test options.
See training and test tips at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/tips.md
See frequently asked questions at: https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix/blob/master/docs/qa.md
"""
import os
from options.test_options import TestOptions #테스트 옵션을 불러옵니다.
from data import create_dataset #데이터 셋 생성 함수
from models import create_model # 모델 생성 함수
from util.visualizer import save_images #이미지 저장 함수
from util import html #HTML 저장 및 페이지 관리 함수

try:
    import wandb  #wandb 라이브러리를 임포트, 사용 시 결과를 시각화 및 기록
except ImportError:
    print('Warning: wandb package cannot be found. The option "--use_wandb" will result in error.') #wandb 패키지가 없으면 경고 메시지 출력


if __name__ == '__main__': # 이 코드는 이 스크립트가 메인 프로그램으로 실행될 때만 실행됩니다.
    opt = TestOptions().parse()  # 테스트 옵션을 가져옵니다. 사용자가 설정한 파라미터를 읽어옵니다.
    # 테스트에서 하드 코딩된 파라미터 설정
    opt.num_threads = 0   # 테스트 코드에서는 멀티스레트를 지원하지 않으므로 0으로 설정합니다.
    opt.batch_size = 1    # 테스트에서는 배치 사이즈를 1오 설정합니다. 한 번에 하나의 이미지만 처리.
    opt.serial_batches = True  # 데이터 셔플을 비활성화합니다. (이미지를 랜덤하게 처리하지 않고 순차적으로 처리)
    opt.no_flip = True    # 이미지를 뒤집지 않습니다.(원본이미지 그대로 사용)
    opt.display_id = -1   # Visdom을 사용한 실시간 디스플레이를 비활성화합니다. 결과는 HTML 파일로 저장됩니다.
    dataset = create_dataset(opt)  # 데이터셋을 생성합니다. 'OPT' 옵션에 맞게 데이터셋을 준비.
    model = create_model(opt)      # 모델을 생성합니다. 'OPT.MODAL' 등의 설정을 기반으로 모델을 생성.
    model.setup(opt)               # 모델을 설정합니다. 네트워크를 로드하고, 스케줄러를 설정합니다.
    # 로그 설정
    if opt.use_wandb: #wandb 사용 여부 체크
        #wandb 프로젝트를 초기화하고 실험 이름과 설정을 기록합니다.
        wandb_run = wandb.init(project=opt.wandb_project_name, name=opt.name, config=opt) if not wandb.run else wandb.run
        wandb_run._label(repo='CycleGAN-and-pix2pix') # 실험을 wandb에 레이블링

    # 결과를 저장할 웹사이트 디렉토리 생성
    web_dir = os.path.join(opt.results_dir, opt.name, '{}_{}'.format(opt.phase, opt.epoch))  # 웹 디렉토리 경로 설정
    if opt.load_iter > 0:  # 'load_iter'가 0이 아니면, 해당 반복 번호를 경로에 추가
        web_dir = '{:s}_iter{:d}'.format(web_dir, opt.load_iter)
    print('creating web directory', web_dir) # 디렉토리가 생성됨을 출력
    webpage = html.HTML(web_dir, 'Experiment = %s, Phase = %s, Epoch = %s' % (opt.name, opt.phase, opt.epoch)) # HTML 웹 페이지 객체 생성
    # test with eval mode. This only affects layers like batchnorm and dropout.
    # For [pix2pix]: we use batchnorm and dropout in the original pix2pix. You can experiment it with and without eval() mode.
    # For [CycleGAN]: It should not affect CycleGAN as CycleGAN uses instancenorm without dropout.
    
    #평가 모드 설정
    if opt.eval:
        model.eval() #모델을 평가 모드로 설정 (배치 정규화 및 드롭아웃 레이어에 영향)
    
    #데이터셋에서 이미지를 하나씩 가져와서 처리
    for i, data in enumerate(dataset):
        if i >= opt.num_test:  # 'opt.num_test'만큼만 테스트 수행.
            break
        model.set_input(data)  # 데이터를 모델에 입력합니다.
        model.test()           # 모델에서 테스트를 수행합니다.
        visuals = model.get_current_visuals()  # 테스트 결과로부터 시각화된 이미지를 가져옵니다.
        img_path = model.get_image_paths()     # 처리된 이미지의 경로를 가져옵니다.
        if i % 5 == 0:  
            print('processing (%04d)-th image... %s' % (i, img_path)) # 5번째마다 진행 상황 출력
    
        # 결과 이미지를 HTML 파일에 저장
        save_images(webpage, visuals, img_path, aspect_ratio=opt.aspect_ratio, width=opt.display_winsize, use_wandb=opt.use_wandb)
    
    webpage.save()  # 웹 페이지에 저장된 이미지를 HTML 파일로 저장합니다.
