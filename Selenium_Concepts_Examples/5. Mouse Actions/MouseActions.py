from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()
driver.get("https://www.greythr.com")
driver.maximize_window()

driverWait = WebDriverWait(driver, 15)

demo_frame_close_btn = driverWait.until(EC.element_to_be_clickable((By.CLASS_NAME,'om-global-close-button')))
login_page_login_btn = driver.find_element(By.ID, 'header_login_btn')

actions = ActionChains(driver)

# Single Click Action
actions.click(demo_frame_close_btn).perform()

# Mouse Hover
actions.move_to_element(login_page_login_btn).perform()


driver.close()

