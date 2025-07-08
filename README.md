1단계 (기본 기능 구축)
problems.py: solved.ac API 연동, 문제 필터링 및 샘플링
db.py: MongoDB 연결 및 저장 테스트
config.py: 상수, .env 변수 불러오기

2단계 (자동화 로직)
auth.py: 로그인 처리 및 CAPTCHA 예외 핸들링
navigator.py: 연습 생성, 세트 업로드 자동화
main.py: 전체 스케줄 관리 및 로직 통합

3단계 (보안 & 예외처리, 로깅, 테스트)
.env, 예외처리, 유닛테스트, logging 추가

| `tier` 숫자 | 티어 이름    | 의미        |
| --------- | -------- | ----------       |
| 1\~5      | Bronze   | 가장 쉬운 문제들  |
| 6\~10     | Silver   | 기초적 알고리즘   |
| 11\~15    | Gold     | 중급 문제         |
| 16\~20    | Platinum | 상위권 알고리즘   |
| 21\~25    | Diamond  | 고난도 문제       |
| 26\~30    | Ruby     | 최상위 고수용 문제|