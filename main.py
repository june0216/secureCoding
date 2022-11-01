from flask import Flask, request , render_template# flask내에 Flask가 있는데 (flask.Flask 사용)

app = Flask(__name__) # 클래스이다.
#__name__으로 기본적으로 매핑이 되어있다.
#/hello라고 해도 된다. 하지만 그냥 플라스크에서 처음에 저렇게 하라고 함
#app이라는 변수에 담으라고 한다.(가장 많이 쓰는 변수명)
#대부분의 프로그램들이 하나의 exe에 다 있는 것이 (모든 기능)이 있는 것이 아니라 서버마다 기능을 부여한다.
#예를 들어 인증서버, 관리자 서버, 음식점 관리자 서버 등으로 각각 서버마다 각각의 역할들이 다르다.
#이 서버들을 app으로 부르는 것이다. (기능이 있어서)


@app.route("/") #이것은 루트로 왔을 때 (naver.com/)일 때, /는 가장 홈화면이라고 생각할 수 있다. #여기서 com까지는 회사명이고 뒤에는 경로명이 있다. (경로마다 라우트해준다)
def home():
    return "<p>Hello, World!</p>"#/로 들어오는 것들을 이것을 출력함

@app.route("/111")
def page_111():
    #return "<h1>111</h1>" # 큰 글씨로 나올 것이다.
    return render_template('home.html')


#http://127.0.0.1/login?id=admin&pw=1234
@app.route("/login", methods=['GET'])#GET 또는 POST (전송 방식 선택) -> 디폴트는 GET이다.
def login_get():
    id = request.args.get('id') #request와 requests는 다르다. request(클래스)는 플라스크에서 사용(args=주소줄에서 받아온다)
    pw = request.args.get('pw')

    if id == 'admin' and pw == '1234': #지금은 하드코딩되어있지만 나중에 db를 추가하면 유동적일 수 있다.
        return
    else:
        return "Login fail"
    return render_template('login.html', var1=id)
#로그인으로 GET으로 받겠다. 아규먼트가 주소줄에 표시된다.


@app.route("/login", methods=['POST'])#GET 또는 POST (전송 방식 선택) -> 디폴트는 GET이다.
def login_post():
    id = request.form.get('id') #request와 requests는 다르다. request(클래스)는 플라스크에서 사용
    pw = request.form.get('pw')

    if id == 'admin' and pw == '1234': #지금은 하드코딩되어있지만 나중에 db를 추가하면 유동적일 수 있다.
        return 'Login sucess'
    else:
        return "Login fail"
    return "login"

@app.route("/login", methods=['POST', 'GET'])#GET 또는 POST (전송 방식 선택) -> 디폴트는 GET이다.
def login_getpost():
    q = {
        "name":"홍길동",
        "age":"20"
    }
    if request.method == 'GET':
        id = request.args.get('id')  # request와 requests는 다르다. request(클래스)는 플라스크에서 사용(args=주소줄에서 받아온다)
        pw = request.args.get('pw')
    else:
        id = request.form.get('id') #request와 requests는 다르다. request(클래스)는 플라스크에서 사용
        pw = request.form.get('pw')

    if id == 'admin' and pw == '1234': #지금은 하드코딩되어있지만 나중에 db를 추가하면 유동적일 수 있다.
        return render_template('login.html', var1=q) # 여러 개를 하나의 변수에 집어넣고 한다.
    else:
        return "Login fail"
    return "login"


#함수명은 다 달라야 한다. -> 하나의 파이썬이므로
#라우터도 똑같은 경로 불가능

#이제 프로그램을 돌리는 것이다.
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # 이 앱을 실행해라
#지금은 /로 들어오는 것만 처리, 나머지는 처리를 하지 못한다.

#디버그 모드를 ON으로 하면 문법적으로 오류가 없으면 알아서 재구동해준다.
#app.run() -> app.run(debug=TRUE)
#배포하면 이것을 지워주어야 한다.-> 해킹당할 수 있음

####
#포트 번호 5000인데 80으로 하면 기본값이다. "port=80"열기

#host='0.0.0.0' -> 지금 로컬 아이피로 전환되어 사용한다. -> 외부에서 접속 가능하다.

####
