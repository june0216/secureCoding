#다른 소스코드 ->
#다른 서버이다. 하나는 웹서버이고 post요청 보내는 서버이다.
#커맨드 창 2개로 2개의 서버를 돌리자
#python test_post.py -> 테스트해보기
import requests

q = {
    'id':"admin", # 딕셔너리임
    'pw':"1234"
}
r = requests.post("http://127.0.0.0/login", data=q)
#r = requests.get("http://127.0.0.0/login", params=q)
print(r.text)