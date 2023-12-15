## <span style="color:teal;">**Waits**  
Selenium supports two types of wait.
*   Implicit wait
*   Explicit wait

**Implicit Wait :** The implicit wait instructs the WebDriver to wait for a certain amount of time before throwing an exception when attempting to locate an element. It is set once for the entire duration of the WebDriver object.   

```python
from selenium import webdriver

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

# Set an implicit wait for 10 seconds
driver.implicitly_wait(10)

# Navigate to a web page
driver.get("https://example.com")

# Find an element using implicit wait
element = driver.find_element_by_id("exampleElement")

# Perform some action on the element
element.click()

# Close the browser
driver.quit()

```


**Explicit Wait :** Explicit wait is more versatile as it allows you to specify conditions for waiting on a particular element or situation. It waits for a certain condition to occur before proceeding with the execution of the code.  

```python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

# Navigate to a web page
driver.get("https://example.com")

# Defining explicit wait with a variable
driver_wait = WebDriverWait(driver, 10)

# Explicitly wait for up to 10 seconds until the element is clickable
element = driver_wait.until(
    EC.element_to_be_clickable((By.ID, "exampleElement"))
)

# Perform some action on the element
element.click()

# Close the browser
driver.quit()

```


