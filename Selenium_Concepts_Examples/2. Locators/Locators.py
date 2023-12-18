
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.youtube.com')

my_wait = WebDriverWait(driver, 10)

yt_logo = driver.find_element(By.XPATH, "//div[@id='start']/descendant::a")
yt_logo.click()

cotent_list = driver.find_elements(By.XPATH, "//div[@id='scroll-container']/iron-selector/yt-chip-cloud-chip-renderer")
print(len(cotent_list))

time.sleep(5)

for count in range(len(cotent_list)):
    temp = cotent_list[count]
    if temp.text == 'Gaming':
        temp.click()
        time.sleep(2)
        #print(cotent_list[count])


driver.execute_script("window.scrollBy(0, 1500);")

time.sleep(5)

driver.quit()