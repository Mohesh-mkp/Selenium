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


## Few explicit wait expected conditions

- element_to_be_clickabel
- visibility_of_element_located
- title_contains
- text_to_be_present_in_element
- invisibility_of_element_located
- element_to_be_selected_
- alert_is_present
- number_of_windows_to_be
- frame_to_be_available_and_switch_to_it


## Difference between Implicit wait and Explicit wait

| Differences           | **Implicit Wait**                                      | **Explicit Wait**                                      |
| ---------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| **Declaration**        | Set once at the beginning of the script using `driver.implicitly_wait(time_in_seconds)`. | Defined using `WebDriverWait` in combination with expected conditions. |
| **Scope**              | Applies globally to all elements throughout the entire script. | Applies to specific elements or conditions, allowing more fine-grained control. |
| **Wait Condition**    | Waits for a specified amount of time (in seconds) for the element to be present in the DOM before throwing `NoSuchElementException`. It does not wait for the element to become visible or clickable. | Explicit wait waits for a certain condition to occur before proceeding further in the code. Conditions include `element_to_be_clickable`, `visibility_of_element_located`, etc. |
| **Usage**              | Useful for handling general synchronization issues and reducing the likelihood of `NoSuchElementException` errors. | Useful for waiting for specific elements or conditions that might take longer to appear, become clickable, or meet other criteria. |
| **Summary**            | Implicit wait is a general wait applied globally and is useful for handling synchronization issues throughout the script. | Explicit wait is a more targeted approach, allowing you to wait for specific conditions on specific elements. This provides more control over synchronization and can be more efficient in certain scenarios. |
