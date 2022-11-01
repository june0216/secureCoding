from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get("https://www.naver.com")  # 네이버 접속(크롬으로 접속) -> 아주 잠깐 뜬다.
#직접 글을 쓸 수도 있다.

finally:
    driver.quit()  # 브라우저를 닫고, 프로세스도 종료