#연습 폼 자동 입력

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def go_to_group_and_create_practice(driver, group_url):
    driver.get(group_url)
    time.sleep(2)

    # "연습 만들기" 탭 클릭
    practice_tab = driver.find_element(By.LINK_TEXT, "연습 만들기")
    practice_tab.click()

    # 연습 폼이 완전히 뜰 때까지 기다림
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.NAME, "contest_title"))  # 또는 By.ID, "practice_title"
    )

def fill_practice_form(driver, form_data):
    try:
        # 1. 연습 제목 입력
        title_input = driver.find_element(By.NAME, "contest_title")
        title_input.clear()

        # 이모지 포함된 문자열 safely 입력
        emoji_title = form_data["contest_title"]
        driver.execute_script("""
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('change'));
        """, title_input, emoji_title)


        # 2. 시작 시간
        start_input = driver.find_element(By.NAME, "contest_start")
        start_input.clear()
        start_input.send_keys(form_data["contest_start"])  # yyyy-mm-dd hh:mm

        # 3. 종료 시간
        end_input = driver.find_element(By.NAME, "contest_end")
        end_input.clear()
        end_input.send_keys(form_data["contest_end"])

        # 4. 문제 입력
        for problem_id in form_data["problem_id"]:
            problem_input = driver.find_element(By.ID, "problem-search")  # ← 실제 ID로 수정
            problem_input.clear()
            problem_input.send_keys(str(problem_id))
            problem_input.send_keys(Keys.ENTER)
            time.sleep(0.2)  # 추가 버튼 누른 효과

        # 5. 프리즈 시간 (30분)
        freezing_input = driver.find_element(By.NAME, "contest_freeze")
        freezing_input.clear()
        freezing_input.send_keys("0")
        freezing_input.send_keys(Keys.TAB)

        # 6. 패널티 (20분)
        penalty_input = driver.find_element(By.NAME, "contest_penalty")
        penalty_input.clear()
        penalty_input.send_keys("0")
        penalty_input.send_keys(Keys.TAB)

        # 패널티 계산: 누적 (기본값 유지)
        # 제출하지 않은 참가자 숨기기
        #    → 라벨 텍스트 기반으로 클릭 처리 (예: "보여주지 않음" 선택)
        hide_option = driver.find_element(By.XPATH, '//label[contains(text(), "보여주지 않음")]')
        hide_option.click()


        # 9. "만들기" 버튼 클릭
        driver.find_element(By.ID, "save_button").click()

        print("✅ 연습 생성 완료")

    except NoSuchElementException as e:
        print("❌ 연습 폼 자동 입력 실패:", e)