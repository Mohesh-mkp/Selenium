
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
driver.maximize_window()

location = 'https://www.instagram.com/'

# Refresh window by selenium method
driver.refresh()

time.sleep(4)

# Refresh by Javascript 
driver.execute_script('location.reload();')

time.sleep(5)



driver.quit()
