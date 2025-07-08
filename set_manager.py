#제목, 기간, 세트 번호 계산
from datetime import datetime, timedelta
import pymongo

# Mongo 사용해 set_number 받아옴
def get_next_set_number(db):
    # 현재까지 저장된 세트 중 가장 큰 set_number를 찾음
    latest_entry = db.test_collection.find_one(
        sort=[("set_number", pymongo.DESCENDING)]   # 내림차순 정렬
    )
    if latest_entry and "set_number" in latest_entry:
        return latest_entry["set_number"] + 1
    else:
        return 1  # 처음이면 1부터 시작

def get_set_composition(set_number: int) -> list:
    base = ["Bronze", "Silver", "Gold"]
    if set_number % 2 == 0:
        base.append("Platinum")
    return base

def generate_title(set_number: int, tier: str) -> str:
    emoji_map = {
        "Bronze": "🥉",
        "Silver": "🥈",
        "Gold": "🥇",
        "Platinum": "🏆"
    }
    tier_emoji = emoji_map[tier]
    return f"⚔️ Problem Random Defense {set_number} ({tier_emoji}{tier}{tier_emoji})"


def next_sunday(today=None):
    today = today or datetime.now()
    days = (6 - today.weekday()) % 7 + 1
    sunday = today + timedelta(days=days)
    return datetime(sunday.year, sunday.month, sunday.day)

def calc_practice_period(set_number: int, tier: str):
    start = next_sunday()
    if tier == "Platinum":
        end = start + timedelta(days=13)  # 2주
    else:
        end = start + timedelta(days=6)   # 1주
    return start.strftime("%Y-%m-%d 00:00"), end.strftime("%Y-%m-%d 23:59")