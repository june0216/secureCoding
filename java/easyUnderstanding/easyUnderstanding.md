## 50. 시각적으로 오해의 소지가 있는 식별자가 리터럴 사용에 주의하라(DCL50-J)

[case 1]

```java
int stem; // Position near the front of the boat
/* ... */
int stern; // Position near the back of the boat
```

- 이유 : stem과 stern에서 “m” 과 “rn”이 같아보일 수 있는 여지가 있다. 그래서 같은 변수라고 오해할 수 있기 때문이다.

⇒ 이러한 오해의 소지가 없게 확실히 구분할 수 있게 다른 변수명을 사용하는 방법을 이용해야 한다. 

---

[case 2]

```java
public class Visual {
public static void main(String[] args) {
		System.out.println(11111 + 1111l);
	}
}
```

- 이유 : 1과 l이 구분이 되지 않아서 “l”이지만 1로 오해할 수 있다.

⇒ 소문자 l을 대문자로 변경하여 확실히 구분해주는 것이 좋다. 

---

[case 3]

```java
int[] array = new int[3];
void exampleFunction() {
		array[0] = 2719;
		array[1] = 4435;
		array[2] = 0042;
		// ...
}
```

- 이유: “0042”부분에서 앞에 00을 붙이는 것은 십진수의 표현이 아니라 8진수로 해석되어 십진수 ‘42’이의 값이 아닌 전혀 다른 값이 들어가게 된다.

## 51. 가변형 메서드의 모호한 오버로딩을 삼가하라 (DCL57-J)

[case 1]

```java
class Varargs {
	private static void displayBooleans(boolean... bool) {
		System.out.print("Number of arguments: " + bool.length + ", Contents: ");
		for (boolean b : bool)
			System.out.print("[" + b + "]");
}

private static void displayBooleans(boolean bool1, boolean bool2) {
		System.out.println("Overloaded method invoked");
	}
public static void main(String[] args) {
		displayBooleans(true, false);
	}
}
```

*여기서 가변형 메서드 = 가변 인자이다. boolean … bool부분에서 “…”부분이 가변 인자를 사용하는 것이라고 의미하는 것이며 매개변수로 1개 이상이 들어온다는 것이다. 

- 이유 : **`displayBooleans`** 같은 이름의 함수가 오버로딩되어 있으며 하나의 메소드는 가변인자를 쓰기 때문에  main()에서 어떠한 메소드를 호출하는지 명확하게 알기 어렵기 때문이다.

*참고로 런타임을 해야 어떤 함수가 실행되는지 알 수 있는데 여기서는 2번째 함수가 우선순위가 높기 때문에 2번 함수가 실행되는 것을 알 수 있다. 

⇒ 해결 = 이렇게 애매한 부분이 있다면 메소드 이름을 분리하는 것이 좋다. 

## 52. 인밴드 오류 지표를 삼가하라(ERR52-J)

[case 1]

```java
static final int MAX = 21;
static final int MAX_READ = MAX-1;
static final char TERMINATOR ='\\';
int read;
char [] chBuff = new char [MAX];
BufferedReader buffRdr;
// Set up buffRdr
read = buffRdr.read(chBuff,0, MAX_READ);
chBuff[read] = TERMINATOR;
```

- 이유 : 코드를 작성한 의도는 버퍼에 있는 값들을 다 읽은 후 마지막 부분에 “\\”을 넣기 위해 “chBuff[read] = TERMINATOR” 부분이 있다. 하지만 read()함수의 경우에 EOF(end of file)을 만나면 -1을 리턴하는 특징이 있다. 그렇기 때문에 끝까지 읽었다면 마지막 인덱스에 TERMINATOR이 들어가는 것이 아니라 chBuff[-1]에 들어가게 되는 것으로 잘못된 코드이다.

⇒ read()반환값이 -1인지 확인하는 조건을 넣으면 된다. 

## 53. 조건식에서 대입문을 실행하지마라 (EXP51-J)

[case 1]

```java
public void f(boolean a, boolean b) {
	if (a = b) {
		/* ... */
	}
}
```

- 이유 : 컴파일은 되지만 의도적으로 대입 후 비교를 하기 위해서 작성한 것인지, 비교만 하려고 한 것인지 애매하기 때문에 잘못된 코드이다. 참고로, 대입 후 비교를 한다면 a에 b의 값이 대입되고 true인지 false인지 확인하기 때문에 결과는 b의 값에 달려있게 된다.

⇒ 해결 : 대입과 비교를 나누는 방식으로 확실하게 나타내는 것이 좋다. 

---

[case 2]

```java
public void f(boolean a, boolean b, boolean flag){
	while( (a = b) && flag){
	/* ..*/
   }
}
```

- 이유 : 먼저 a에 b를 대입하고 그 결과 값을 flag와 비교한다. 즉, b가 true이면서 flag가 true일 경우를 의미하게 된다. 하지만 의도한 것은 그런 것이 아니라 a와 b가 같은 경우와 flag가 true일 경우이기 때문에 잘못된 코드이다.

## 54 if, for, while 문의 몸체에 중괄호를 사용하라 (EXP52-J)

[case 1]

```java
int login;
if (invalid_login())
	login = 0;
else
	login = 1;
```

- 이유 : 다음과 같이 if문에 걸린 문장이 1개일 경우에는 중괄호를 생략해도 되지만 가급적이면 중괄호를 쓰는 것이 좋다.

---

[case 2]

```java
int login;
if (invalid_login())
	login = 0;
else
// Debug line added below
	System.out.println("Login is valid\n");
// The next line is always executed
	login = 1;
```

- 이유 : else에 걸린 문장이 2개인데 중괄호를 묶지 않았기 때문이다. 그래서 login = 1의 경우 else조건일 때 실행되는 것이 아니라 의도와 다르게 항상 실행될 것이다.

---

[case 3]

```java
int privileges;
if (invalid_login())
	if (allow_guests())
		privileges = GUEST;
else
	privileges = ADMINISTRATOR;
```

- 이유 : 의도한 것은 `**if (invalid_login())**`에 대한 else 문으로 **`privileges = ADMINISTRATOR;`** 을 적었지만 else문은 들여쓰기와 상관없이 가장 가까운 if를 따르기 때문에 안쪽 if문에 대한 else문이 되어 의도와 다르게 되었기 때문에 잘못된 코드이다.

---

[case 4] 

```java
int privileges;
if (invalid_login())
	if (allow_guests())
		privileges = GUEST;
	else
		privileges = ADMINISTRATOR
```

- 이유 : 이 부분은 의도대로 동작하는 것(else가 안쪽 if문을 따른다)은 맞지만 더 명확하게 하기 위해서는 중괄호가 필요하다.

## 55. if, for, while 조건식 직후에 세미콜론을 입력하지 마라 (MSC51-J)

[case 1]

```java
if(a == b); {
}
```

- 이유 : 조건식 직후에 세미콜론을 쓰면 안된다. if조건을 알아보고 이에 대해 어떠한 실행문이 나와서 실행을 해야 하는데 조건만 비교하고 아무 실행없이 끝나므로 잘못된 코드이다.

## 56. case 레이블에 연계된 모든 문장은 break문으로 마무리하라 (MSC52-J)

[case 1]

```java
int card = 11;
switch (card) {
/* ... */
		case 11:
			System.out.println("Jack");
		case 12:
			System.out.println("Queen");
			break;
		case 13:
			System.out.println("King");
			break;
		default:
			System.out.println("Invalid Card");
			break;
}
```

- 이유: 여기서는 case 11일때 하나의 문장만 실행하도록 의도하고 했지만 break문이 없어서 case12의 문장도 실행하게 된다. 그렇기 때문에 잘못된 코드이다. 참고로, switch 문은 애매하다.
    - 만약 if(c == 11 || c == 12 || c == 13)의 경우를 노리고 break문을 안쓰는 경우가 있을 수 있다.
    - 하지만 타인이 봤을 때 오타로 보일 가능성이 있으므로 애매한 부분이다.
    - 따라서 이러한 애매한 부분을 없애기 위해 case문 하나당 break가 꼭 있는 경우에만 사용하는 것이 좋다.
    

## 57. 반복문 카운터의 부주의한 순환을 피하라 (MSC54-J)

[case 1]

```java
for (i = 1; i != 10; i += 2) {
// ...
}
```

- 이유 : 여기서 반복문의 종료 조건은 i가 10일 때인데 i의 증가 추세를 보면 1, 3, 5, 7, 9, 11 ..로 증가하기 때문에i가 10이 될 수 없는 상황이므로 무한루프가 된다는 점에서 잘못된 코드이다.

---

[case 2]

```java
for (i = 1; i != 10; i += 5) {
// ...
}
```

- 이유 : 반복문의 종료조건은 i 가 10일 때이지만 i는 1, 6, 11, 16, 21….로 증가하므로 종료조건을 만나지 못해 무한 루프에 빠지게 된다.

---

[case 3]

```java
for (i = 1; i <= Integer.MAX_VALUE; i++) {
// ...
}
```

- 이유 : for문의 순서를 보면 i= 1을 대입하고
    
    `i <= Integer.MAX_VALUE`의 조건을 비교한 후 for 문 안에 문장을 실행한 후  `i++`을 실행한다. 그렇기 때문에 위와 같은 상황은 int형의 max값에 도달한 후 i++을 실행하여 i++에서 int i의 오버플로우가 발생한다. 오버플로우 발생 후 다시 조건을 비교할 때 오버플로우 발생 이후 들어간 값이기 때문에 max값보다 작은 값이 들어가게 되어 무한루프에 빠지게 되므로 잘못된 코드이다. 
    

---

[case 4]

```java
for (i = 0; i <= Integer.MAX_VALUE - 1; i += 2) {
// ...
}
```

- 이유 : i는 0, 2, 4,…로 증가하므로 Max에 도달했을 때
    
     `i <= Integer.MAX_VALUE - 1` 이 조건을 만족하게 되므로 for문 안의 문장들을 수행한 후 i가 2를 증가하게 되는데 이때, 오버플로우가 발생하게 되어 종료조건에 만족하지 못하게 된다. 이렇게 무한 루프로 빠져서 종료하지 못하기 때문에 잘못된 코드이다. 
    

⇒ 해결 : 증감 숫자와 조건에 있는 “-2”와 같은 숫자가 일치해야 한다. 

## 58. 연산의 우선순위를 위해 괄호를 사용하라 (EXP53-J)

[case 1]

```java
public static final int MASK = 1337;
public static final int OFFSET = -1337;

public static int computeCode(int x) {
		return x & MASK + OFFSET;
}
```

- 이유 : 산술 연산자가 먼저인지 비트 연산자가 먼저인지 헷갈릴 수 있기 때문에 괄호로 정확하게 어떤 것이 먼저 실행되는지 표현하는 것이 좋다.

---

[case 2]

```java
public class PrintValue {
public static void main(String[] args) {
	String s = null;
	// Prints "1"
	System.out.println("value=" + s == null ? 0 : 1);
	}
}
```

- 이유 : 의도한 것은 s의 값이 null이면 0이고 null이 아니면 1을 반환하도록 한 것이다. 하지만 실제로는 ("value=" + s)이것이 먼저 실행되고 ("value=" + s)의 값이 null인지 아닌지 확인하게 되므로 잘못된 코드이다.

## 60. 실수 연산을 위해서는 정수를 실수로 변환하라 (NUM50-J)

[case 1]

```java
short a = 533;
int b = 6789;
long c = 4664382371590123456L;

float d = a / 7; // d is 76.0 (truncated)
double e = b / 30; // e is 226.0 (truncated)
double f = c * 2; // f is -9.1179793305293046E18
// because of integer overflow
```

- 이유 : 실수 변환을 하지 않아 정확한 값을 얻지 못하기 때문이다.
    - `float d = a / 7;` , `double e = b / 30;`의 경우 7과 30이 각각 이 정수이므로 나눗셈 이후 반올림한 값이 되어 정확한 값을 얻지 못했다.  그래서 7과 30을 실수타입으로 변환 후 나눗셈을 하면 더 정확한 값을 얻을 수 있다.
    - long c는 Long타입이 가지고 있는 max값을 저장하고 있다. 그렇기 때문에  c *2에서 버퍼오버플로우가 발생하게 된다. 여기서 c를 double로 변환해준다면 오버플로우가 발생되지 않을 수 있다.

---

[case 2]

```java
int a = 60070;
int b = 57750;
double value = Math.ceil(a/b);
```

- 이유 : ceil() 함수는 소수점이 있을 때 올림하는 함수이다. 하지만 a와 b는 모두 정수이고 결과도 정수로 나오기 때문에 소수점이 없게 된다. 따라서  정확한 값이 나오지 않는다는 문제가 있다.  한 쪽을 실수로 변환시켜 소수점이 나오게 한다면 정확한 값을 얻을 수 있다.

## 62.가독성 있고 일관된 주석을 사용하라 (MSC55-J)

[case 1]

```java
// */ /* Comment, not syntax error */
f = g/**//h; /* Equivalent to f = g / h; */
/*//*/ l(); /* Equivalent to l(); */
m = n//**/o
+ p; /* Equivalent to m = n + p; */
a = b //*divisor:*/c
+ d; /* Equivalent to a = b + d; */
```

- 이유 : 한 줄 주석인 //와 여러 줄 주석인 */의 방식이 혼합되어있어서 통으로 주석인지 아닌지 헷갈릴 수 있다. 따라서 이는 잘못된 코드이며 한 줄 주석만 사용하는 것이 바람직하다.
    - `m = n + p;` 이 의도한 것이지만 한 줄 주석과 섞여있어서 다른 문장 처럼 보여 헷갈릴 여지가 있다.
    - `a = b + d;` 을 의도한 것이지만 한 줄 주석과 여러 줄 주석이 섞여서 다른 문장으로 헷갈릴 여지가 있다.

---

[case 2]

```java
/* Comment with end comment marker unintentionally omitted
security_critical_method();
/* Some other comment */
```

- 이유 : `/*`와 `*/`의 짝이 맞지 않아서 의도한 것인지 아닌지 헷갈리기 때문이다. → 한 줄 주석으로 통일하는 것이 좋다.

## 63. 과도한 코드와 값을 찾아 제거하라 (MSC56-J)

[case 1]

```java
public int func(boolean condition)
{
	int x = 0; 
	if(condition){
		x = foo();
		return x;
	}
	if(x != 0){
		//code
	}
	return x;
}
```

- 이유 : if (x ! = 0) 조건 부분에 해당하는 코드는 절대로 실행할 수 없는 환경이므로 잘못된 코드이다.
    - 먼저 int x = 0로 세팅이 되었고 if(condition) 이 실행되면 바로 함수를 빠져나간다. 하지만 if(condition)의 조건에 맞지 않는다면 아래의 문장이 실행될텐데 x가 처음에 0으로 세팅되었고 x가 변하는 부분은 if(condition)조건 실행문 안에 있다. x는 그대로 0이며 if문에 들어갈 수 없게 된다.  또한, if(condition)조건문을 통과하여 x를 변화시키는 실행문을 실행하게 된다고 하더라도 함수를 return하게 되므로 아래의 문장까지 실행하지 않고 끝나게 된다.

---

[case 2]

```java
public int string_loop(String str) {
	for (int i =0; i < str.length(); i++)
	{
		if(i == str.length())
		{
			//code
		}
	}
	return 0;
}
```

- 이유 : `if(i == str.length())` 이 조건은 절대로 만족할 수가 없는 조건이기 때문에 잘못된 코드이다. 왜냐하면 for문에 들어갈 조건에서 `i < str.length()`로 인해 `i == str.length()`이라면 애초에 for문자체에 들어올 수 없게 된다. 그리고  그 안에 있는  `if(i == str.length())` 이 부분도 실행할 수 없기 때문에 절대로 만족할 수 없는 코드이다.

---

[case 3]

```java
String s;
String t;
// ...
s.equals(t);
```

- 이유 : **`s.equals(t);`**이렇게 두 개의 문자열을 비교를 했으면 그 결과를 어떤 변수에 저장하거나 그 결과를 확인해야 하는데 결과를 확인하지 않았기 때문에 실행해도 쓸모 없는 코드가 되었다.

---

[case 4]

```java
int p1 = foo();
int p2 = bar();
if (baz()) {
	return p1;
} else {
	p2 = p1;
}
return p2;
```

- 이유 : `return p1`과 `return p2` 부분이 있는데 이 2개의 문장이 서로 값은 의미를 지닌다. 쓸모없는 문장이 되므로 잘못된 코드이다.
    - `else p2 = p1;` 부분으로 인해 p2에 p1값이 대입되므로 그 이후에 나오는 `return p2`는 결국 `return p1`이라는 의미이다.
    - 여기서 if - else도 무의미하고 p2도 무의미하다.

## 64. 논리적 완벽을 추구하라 (MSC57-J)

[case 1]

```java
if(a ==b) {
/* ... */
}
else if(a == c) {
/* ... */
}
```

- 이유 : `else`가 없기 때문에 두 개의 문장에 해당되지 않은 경우에 대해서 처리를 할 수 없기 때문에 잘못된 코드이다.

---

[case 2]

```java
switch(x) {
case 0: foo(); break;
case 1: bar(); break;
}
```

- 이유 : x가 0 혹은 1일 때의 처리는 있지만 둘 다 해당이 되지 않은 경우 default에 대한 코드가 없어서 아무런 처리가 없기 때문에 잘못된 코드이다.

---

[case 3]

```java
final static int ORIGIN_YEAR = 1980;
/* Number of days since January 1, 1980 */
public void convertDays(long days){
	int year = ORIGIN_YEAR;
/* ... */
	while(days> 365) {
		if(IsLeapYear(year)) {
				if(days> 366) {
						days-= 366;
						year +=1;}
		}else{
				days-= 365;
				year +=1;
		}
	}
}
```

- 이유 : if-else짝이 맞지 않는다.
    - `if(IsLeapYear(year))` 에 대응하는 else문장이 없어서 윤년이면서 366일 경우, if 조건 내에 있는 변수`(day)`를 변경하여 while문을 빠져나갈 수 있게 하는 부분을 실행하지 못하게 되어 while문을 종료하지 못하고 무한 루프가 발생한다.
