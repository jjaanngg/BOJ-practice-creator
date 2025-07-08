#로그인 자동화

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time

#키 값 가져옴 from .venv
load_dotenv()
USERNAME = os.getenv("BOJ_ID")
PASSWORD = os.getenv("BOJ_PW")
print("USERNAME:", USERNAME)
print("PASSWORD:", PASSWORD)

def login_to_boj():
    options = webdriver.ChromeOptions() # 괄호를 붙여주어야 인스턴스가 생성됨
    #크롬 창을 전체 화면 크기로 연다.
    #시크릿 모드로 열고 싶을 때 options.add_argument("--incogito")
    #창 없이 백그라운드로 실행하고 싶을 때 options.add_argument("--headless")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    #BOJ 로그인 페이지 접속
    driver.get("https://www.acmicpc.net/login")
    time.sleep(1)

    driver.find_element(By.NAME, "login_user_id").send_keys(USERNAME)
    driver.find_element(By.NAME, "login_password").send_keys(PASSWORD)
    driver.find_element(By.ID, "submit_button").click()
    
    #CAPTCHA가 이미지 기반이기 때문에 코드 자체에서 인식하도록 하는 방식은 어렵기 때문에 input과 같은 수동적인 입력 방식으로 순차 처리한다.
    input("CAPTCHA가 있을 경우 수동으로 해결 후 Enter 키를 눌러주세요...")

    print("✅Login Completed✅")
    return driver