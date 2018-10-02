from selenium import webdriver
import time
import sys

inputA = input('請輸入您要搜尋的資料：')
keyword = inputA
inputB = input('請輸入您要搜尋的總頁數：')
pages = int(inputB)

def googlesearchtool(pages,keyword):

    driver = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    driver.get('https://www.google.com.tw/#gws_rd=ssl')

    driver.find_element_by_name('q').send_keys(keyword)
    driver.find_element_by_name('q').submit()
    page =1
    for round in range(pages):
        elements = driver.find_elements_by_xpath('//div/h3/a')
        print('---------這是第', page, '頁資料------------------------')
        for element in elements:
            print(element.text)
            print(element.get_attribute('href'))
        # search_web=driver.current_url
        page+=1
        driver.find_element_by_class_name('pn').click()
    time.sleep(2)
    driver.quit()

if str(keyword) is not None:
    if pages<=0:
        print('輸入的值錯誤，無法搜尋')
        time.sleep(2)
        exit()
    else:
        googlesearchtool(pages,keyword)
else:
    print('未輸入任何所需搜尋資料，因此無法進行搜尋，程序即將進行關閉')
    time.sleep(2)
    exit()

input()#input()使程式可以暫時停在輸出畫面。













