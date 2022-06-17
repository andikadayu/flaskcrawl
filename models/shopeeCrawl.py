from selenium import webdriver
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
import time


class shopeeCrawl:
    driver = uc
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    interval = 3

    def __init__(self, url):
        self.url = url

    def get_shopee(self):
        try:
            option = webdriver.ChromeOptions()
            option.add_argument("--headless")
            self.driver = uc.Chrome(options=option)
            self.driver.get('https://shopee.co.id/'+self.url)
            time.sleep(self.interval)
            self.driver.execute_script('window.scrollTo(0, 1500);')
            time.sleep(self.interval)

            html = BeautifulSoup(self.driver.page_source, 'html.parser')

            # get title
            title = self.driver.title

            return {'title': title}

        except NoSuchElementException as e:
            return e.msg
        except TimeoutException as e:
            return e.msg
