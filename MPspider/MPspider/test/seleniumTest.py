import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

if __name__ == '__main__':
    # m = driverDemo()
    # m.start_request()

    driver = webdriver.Chrome()
    driver.get("http://weixin.sogou.com/")
    # assert "Python" in driver.title
    # elem = driver.find_element_by_name("query")
    print(driver.page_source)
    elem = driver.find_element_by_xpath('//*[@id="query"]')
    elem.clear()
    elem.send_keys("GQ实验室")
    elem.send_keys(Keys.RETURN)
    url = driver.current_url
    r = requests.get(url).status_code
    print(r)




