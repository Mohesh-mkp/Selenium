# <span style="color:teal;">**Save Screenshot**
In Selenium, you can capture screenshots of the browser window using the **'save_screenshot'** method.  
Here's an example in Python:

```python

from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Assigning direct path with name for screenshot
screen_path = 'path/to/image/to/store'

# Take a screenshot and save it to a file
driver.save_screenshot(screen_path)

# Close the browser
driver.quit()

```
