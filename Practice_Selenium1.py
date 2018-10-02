from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time




driver = Chrome('C:/chromedriver/chromedriver.exe')
driver.get("http://www.google.com")
input_element = driver.find_element_by_name("q")
input_element.send_keys("python selenium")
input_element.submit()
#或者使用input_element = driver.find_element_by_name("q").send_keys("python\n")

#driver.back()是網頁返回鍵

RESULTS_LOCATOR = "//div/h3/a"

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

for item in page1_results:
    print(item.text)

time.sleep(2)
driver.quit()

elements = driver.find_elements_by_xpath('//div/h3/a')
#elements = driver.find_elements_by_css_selector('div.rc h3.r > a:nth-child(1)')使用css去尋找
for element in elements:
    print(element.text)
    print(element.get_attribute('href'))

