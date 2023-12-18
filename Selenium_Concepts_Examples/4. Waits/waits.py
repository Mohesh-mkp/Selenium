from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.greythr.com")

driver.maximize_window()


## inbuilt time of python
# time.sleep(15)

## Implicit wait of Selenium
'''driver.implicitly_wait(10)
demo_frme_pop = driver.find_element(By.CLASS_NAME, 'om-canvas-content')'''


## Explicit way of wait in selenium
driverWait = WebDriverWait(driver, 15)

demo_frame_close_btn = driverWait.until(EC.element_to_be_clickable((By.CLASS_NAME,'om-global-close-button')))

demo_frame_close_btn.click()

driver.close()

