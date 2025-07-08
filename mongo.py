# aha 파트
# ※ Pymongo 
# - MongoDB를 Python으로 사용하기 위해 사용하는 라이브러리
import pymongo
from set_manager import get_next_set_number

# ※ main.py 실행 시, DB생성
# - MongoClient() : (옵션 포함)인스턴스 생성 -> MongoDB와 연결
# - get_database() : 사용할 DB를 지정 & 연결
def make_db():
    client = pymongo.MongoClient("mongodb://ynhea:0000@localhost:27017/")
    db_name = "testdb"
    db = client.get_database(db_name)
    return db

# ※ Collection 생성
def save_set(db, form_data, set_number):
    db.test_collection.insert_one({
        "set_number":   set_number,
        "title":        form_data["contest_title"],
        "problem_ids":  form_data["problem_id"],
        "start_date":   form_data["contest_start"],
        "end_date":     form_data["contest_end"]
    })