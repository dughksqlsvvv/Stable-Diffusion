#제대로 된 저장및 이미지생성

#운영체제 관력 기능 사용을 위한 모듈
import os #디렉토리와 파일 경로 등 운영체제 관련 작업을 위한 표준 모듈
import csv
import os.path #파일과 디렉토리 경로 관련 기능을 위한 모듈
import shutil #파일 및 디렉토리 복사, 이동 등 고급 파일 작업을 위한 모듈
import json  #JSON파일을 읽고 쓰기 위한 모듈
# os 모듈에서 path 객체만 따로 가져오기
from os import path #파일 및 경로 관련 함수 사용을 위해 추가로 import
# Selenium webDriver를 사용해 웹 브라우저 자동화
from selenium import webdriver # 브라우저를 제어하기 위한 webDriver 객체 제공
from selenium.webdriver.common.by import By #HTML 요소를 찾기 위한 다양한 선택자 제공(e.g., ID,XPATH,CSS_SELECTOR)
from selenium.webdriver.support.ui import WebDriverWait# 특정 조건이 충족될 때까지 대기하기 위한 클래스
from selenium.webdriver.support import expected_conditions as EC # Selenium에서 제공하는 대기 조건 모음
from selenium.webdriver.chrome.options import Options # chrome 브라우저의 옵션 설정을 위한 클라스
from selenium.common.exceptions import TimeoutException #Selenium 작업 중 발생할 수 있는 타임아웃 예외 처리
#시간 관련 작업을 위한 표준 모듈
import time #대기 시간 설정이나 현재 시간 관련 기능을 사용하기 위한 모듈
#Selenium의 동작 체인을 사용해 복잡한 마우스 및 키보드 동작 수행
from selenium.webdriver.common.action_chains import ActionChains #드래그 앤 드롭, 마우스 오버 들 복작합 동작을 위한 클래스
# 데이터 분석과 CSV 파일 작업을 위한 pandas 라이브러리
import pandas as pd #데이터프레임 작업 및 CSV 파일 읽기/쓰기를 위한 강력한 라이브러리
from pywinauto import Application
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import TimeoutException,WebDriverException
from PIL import Image
# CSV 파일 경로(파일 이름과 디렉토리를 지정)
csv_file_path = r'C:\\Users\\bin\\Documents\\카카오톡 받은 파일\\new_map_floorplan_ids.csv'

# Chrome 드라이버 초기화 및 다운로드 경로 설정
download_path = "C:\\Users\\bin\\Desktop\\NEW_MapFloorPlanId" #파일 다운로드를 저장할 디렉토리 경로
chrome_options = Options()  #chrome 옵션 객체 생성
chrome_options.add_experimental_option("prefs", {  # 브라우저 설정에 다운로드 경로 지정
    "download.default_directory": download_path,   # 기본 다운로드 경로 설정
})
driver = webdriver.Chrome(options=chrome_options)  # chrome webDriver 객체 초기화

# 특정 URL롤 이동(로그인 페이지)
driver.get("https://planner.archisketch.com/?mapId=5f439e034030fe5cc5d09276&flip=0")
#이메일 입력 필드가 로드될 때까지 대기
username_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, 'email'))
)
#비밀번호 입력 필드가 로드될 때까지 대기
password_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)
#이메일 입력 필드에 사용자 이메일 입력
username_input.send_keys("dughksqlsvvv@naver.com")
#비밀번호 입력 필드에 사용자 비밀번호 입력
password_input.send_keys("zannman123@")
#로그인 버튼이 클릭 가능할 때까지 대기
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'sign-in-comfirm-btn')]"))
)
#로그인 버튼 클릭
print("로그인을 시도합니다.")
#로그인 버튼 클릭하여 로그인 시도
login_button.click()
# 3초 대기 (페이지 로드 및 안정성을 위해 사용)
time.sleep(3)
#로그인 후 특정 페이지로 이동
driver.get(f"https://planner.archisketch.com/?mapId=5f439e034030fe5cc5d09276&flip=0")

time.sleep(3) #페이지 로드 또는 초기 상태를 안정화시키기 위해 3초 대기
driver.maximize_window()
# 추가적인 대기 시간
time.sleep(3)

#첫번째 요소가 클릭 가능할 때까지 대기(XPATH로 찾음)
element =WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]'))
        )
    #첫 번째 요소 클릭
element.click()
print("완료")
        #두 번째 요소가 클릭 가능할 때까지 대기 (XPATH로 찾음)
element = WebDriverWait(driver, 30).until(
EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/section/div[2]/div[2]/div[3]'))
        )       #두 번째 요소 클릭
element.click()
print("완료2")
    #세 번째 요소가 DOM에 존재할 때까지 대기 (XPATH로 찾음)
element = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section/div[2]/div[2]/div[3]'))
        )   #세 번째 요소 클릭
element.click()
print("완료3")
    #네 번째 요소가 DOM에 존재할 때까지 대기 (XPATH로 찾음)
element_ = WebDriverWait(driver, 30).until(
EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/section/section/div[2]/div[1]/div[2]'))
        )   #네 번째 요소 클릭
element_.click()
print("완료4") 

# JSON 파일을 읽어서 데이터를 로드
try:
    json_file_path = 'C:\\Users\\bin\\Desktop\\new_map_floorplan_ids.json'

    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # JSON 파일을 파이썬 객체로 로드
        print("JSON 데이터 로드 성공")
except Exception as e:
    print("JSON 파일 로드 실패", e)
    exit()
#DataFrame 생성
try:
    df = pd.DataFrame(data)
    print("DataFrame 생성 성공")
except Exception as e:
    print("DataFrame 생성 실패:", e)
    exit()

#'mapFloorplanId' 열이 존재하는지 확인
if 'mapFloorplanId' in df.columns:
    map_ids = list(set(df['mapFloorplanId']))  # 고유한 map IDs 추출
    print("map_ids:", map_ids)
else:
    print("'mapFloorplanId' 열이 데이터에 존재하지 않습니다.")
    exit()

# 출력 디렉터리 생성 (존재하지 않으면)
output_dir = "C:\\Users\\bin\\Desktop\\NEW_MapFloorPlanId"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)   # 디렉터리 생성
    print(f"디렉터리가 생성되었습니다: {output_dir}")

#각 mapFloorPlanId에 대해 이미지를 저장
try:
    for map_floorplan_id in map_ids:  # map IDs 반복
        new_file_path = os.path.join(output_dir, f"{map_floorplan_id}.png")  # 새 파일 경로 설정
        print(f"새로운 파일 경로: {new_file_path}")
        
        # mapFloorPlanId가 포함된 URL로 이동
        url = f"https://planner.archisketch.com/?mapId={map_floorplan_id}&flip=0"
        print(f"URL: {url}")
        
        # URL 접속
        driver.get(url)
        time.sleep(10)  # 패이지 로드 대기
        
        # 첫번째 클릭 시도
        print("첫 번째 클릭 시도...")
        element = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/section/section/div[2]/div[2]/div[3]'))
        )
        element.click()
        print("첫 번째 클릭 완료")

        # 두번째 클릭 시도
        print("두 번째 클릭 시도...")
        element = WebDriverWait(driver, 35).until(
            EC.presence_of_element_located((By.XPATH, '//section/section/div[2]/div[1]/div[2]'))
        )
        element.click()
        print("두 번째 클릭 완료")

        time.sleep(1)  # 작업 완료 대기
        
        # 캡쳐된 파일 이동
        shutil.move("C:\\Users\\bin\\Desktop\\NEW_MapFloorPlanId\\capture (1).png", new_file_path)
        print(f"파일 이동 완료: {new_file_path}")
        
        print("싸이클 완료, 10초 대기 중...")
        time.sleep(10)  # 다음 반복 전에 대기

except Exception as e:
    print(f"오류 발생: {e}")
    print("페이지 로딩 실패, 재시도 중...")

finally:
    driver.quit()  # WebDriver 종료