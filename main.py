from auth import login_to_boj
from navigator import fill_practice_form, go_to_group_and_create_practice
from problem import get_all_matching_problems, sample_problems, get_recent_problem_ids
from mongo import make_db, save_set
from set_manager import (
    get_next_set_number,
    get_set_composition,
    generate_title,
    calc_practice_period
)

driver = login_to_boj()
group_url = "https://www.acmicpc.net/group/23524"

# 한번에 한 세트만 만들어지게 하려고 반복문에서 제외함
db = make_db()      # DB 연결
recent_problem_ids = get_recent_problem_ids(db)
set_number = get_next_set_number(db)
tiers = get_set_composition(set_number)
# 3세트 자동 생성
for tier in tiers:
    tier_min, tier_max = {
        "Bronze": (1, 5),
        "Silver": (6, 10),
        "Gold": (11, 15),
        "Platinum": (16, 20)
    }[tier]
    count = 2 if tier == "Platinum" else 8

    all = get_all_matching_problems(tier_min, tier_max, exclude_ids=recent_problem_ids)
    sampled = sample_problems(all, k=count)

    contest_title = generate_title(set_number, tier)
    contest_start, contest_end = calc_practice_period(set_number, tier)

    form_data = {
        "contest_title": contest_title,
        "contest_start": contest_start,
        "contest_end": contest_end,
        "problem_id": [p["problemId"] for p in sampled]
    }
    go_to_group_and_create_practice(driver, group_url)
    fill_practice_form(driver, form_data)
    save_set(db,form_data, set_number) # DB에 저장

driver.quit()