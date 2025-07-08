#문제 수집 및 샘플링

import requests
import random
import time  # 요청 사이에 약간의 텀을 주기 위해 사용

# 기존의 문제 가져오기
def get_recent_problem_ids(db):
    docs = db.test_collection.find({}, {"problem_ids": 1})
    problem_ids = set()
    for doc in docs:
        problem_ids.update(doc.get("problem_ids", []))
    return problem_ids

def get_all_matching_problems(tier_min, tier_max, max_solved=10000, max_pages=20, exclude_ids=None):
    #10000문제 이하, 10000명 이하가 푼 문제 수가 20페이지 이하일 것이다 예상
    #50(한번에 가져올 수 있는 문제 수) x 20(예상 최대 페이지 수) = 1000
    collected = []
    page = 1
    size = 50
    exclude_ids = exclude_ids or set() # 기존 문제를 집합으로 가져옴

    while True:
        query = f"tier:{tier_min}..{tier_max} solved:<{max_solved}"
        url = "https://solved.ac/api/v3/search/problem"
        #search/problem 문제 풀이 관련 API 호출

        params = {
            "query": query,
            "page": page,
            "size": size
        }

        response = requests.get(url, params=params)
        #정수 200으로 확인하는 이유는 서버가 상태 코드를 포함한 응답
        #으로 보내는데 요청이 성공적으로 처리되었을 때 반환되는 값이 200이다.
        if response.status_code != 200:
            print("API 호출 실패:", response.status_code)
            break

        #데이터를 json 형식으로 파싱
        data = response.json()
        
        #items 키는 실제 문제들의 리스트를 가지고 있음
        items = data.get("items", [])

        # 중복 문제 필터링
        new_items = [item for item in items if item["problemId"] not in exclude_ids]
        
        #문제들을 리스트에 저장
        collected.extend(new_items)

        # 마지막 페이지까지 왔다면 중단
        if page * size >= data["count"]:
            break

        page += 1
        if page > max_pages:  # API 부하 방지를 위한 안전장치
            break
        time.sleep(0.2)  # 속도 제한 방지용 딜레이

    return collected

def sample_problems(problems, k=8):
    return random.sample(problems, k=min(k, len(problems)))