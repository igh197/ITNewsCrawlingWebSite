from random import random

from bs4 import BeautifulSoup
from selenium import webdriver

# 셀레니움에 다양한 옵션을 적용시키기 위한 패키지
from selenium.webdriver.chrome.options import Options

# 크롬 드라이버 매니저를 실행시키기 위해 설치해주는 패키지
from selenium.webdriver.chrome.service import Service
# 자동으로 크롬 드라이브를 최신으로 유지해주는 패키지
from webdriver_manager.chrome import ChromeDriverManager
# 클래스, 아이디, css_selector를 이용하고자 할때
from selenium.webdriver.common.by import By
# 키보드 입력
from selenium.webdriver.common.keys import Keys

import time
from app import db
from models.models import News


def crawling():
    user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    options_ = Options()
    options_.add_argument(f"User-Agent={user}")
    options_.add_experimental_option("detach", True)
    options_.add_experimental_option("excludeSwitches", ["enable-logging"])
    # 드라이버 설치 및 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options_)

    # url 설정 및 접속
    url = "https://news.naver.com/breakingnews/section/105/283"
    driver.get(url)
    time.sleep(0.5)
    title_list = []
    content_list = []
    copyright_list = []
    for i in range(35):
        title = driver.find_elements(By.CLASS_NAME, 'sa_text_title')[i].text
        content = driver.find_elements(By.CLASS_NAME, 'sa_text_lede')[i].text
        copyright = driver.find_elements(By.CLASS_NAME, 'sa_text_press')[i].text
        news = News(title, content, copyright)
        db.session.add(news)
        db.session.commit()

