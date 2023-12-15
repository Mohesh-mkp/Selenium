
# <span style="color:purple;"> **Selenium Basic Concepts**

* ### Initializing Webdrivers
* ### Types of Locators
    - Locators with description
    - Relative Xpath Axes
* ### Navigation of windows
* ### Waits
    - Implicit Wait
    - Explicit Wait  
* ### Mouse Actions
    - Clicking
    - Doule Clicking
    - Right Click
    - Mouse Hover
    - Drag and Drop
* ### Handling Alers, Frames and windows
    - Handling Alerts
    - Handling Frames
    - Handling Windows   
* ### Scrolling Page
    - Scroll to Bottom of the Page
    - Scroll to Specific Element
    - Scroll by Pixels
    - Scroll to Top of the Page
* ### Save Screenshot
* ### Headless Browsing
* ### Logging and Report
* ### Page Object Model (POM)

## <span style="color:teal;">**Initializing Webdrivers**   
To open the URL or automate the test cases, we need to have web drivers for different browsers. Selenium can access the web driver in order to work with browsers.  


```Python
from selenium import  webdriver
driver = webdriver.Chrome('C:\Mohesh\Drivers\chromedriver.exe')
```

We can have multiple browser access and each browser has individual drivers. For example, chrome has chromedriver while Mozilla Firefox operates with Geckodriver. Similarly, other browsers also have their drivers supported by selenium.  

## <span style="color:teal;">**Types of Locators**
To fetch the location of an element, selenium uses different strategies. 

   * ID
   * Name
   * Link Text
   * Partial Link Text
   * Xpath
   * Tag Name
   * CSS Selector
   * Class Name


### [Explanation of locators](https://www.selenium.dev/documentation/webdriver/elements/locators/)

### **Locators with description**

| Locator             | Description                                                                                                             |
|---------------------|-------------------------------------------------------------------------------------------------------------------------|
| `class name`        | Locates elements whose class name contains the search value (compound class names are not permitted)                   |
| `css selector`      | Locates elements matching a CSS selector                                                                                |
| `id`                | Locates elements whose ID attribute matches the search value                                                           |
| `name`              | Locates elements whose NAME attribute matches the search value                                                         |
| `link text`         | Locates anchor elements whose visible text matches the search value                                                     |
| `partial link text` | Locates anchor elements whose visible text contains the search value. If multiple elements are matching, only the first one will be selected. |
| `tag name`          | Locates elements whose tag name matches the search value                                                                |
| `xpath`             | Locates elements matching an XPath expression     |


### **Relative Xpath Axes**

| AxisName                | Result                                                                                                 |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| `ancestor`              | Selects all ancestors (parent, grandparent, etc.) of the current node                                 |
| `ancestor-or-self`      | Selects all ancestors (parent, grandparent, etc.) of the current node and the current node itself      |
| `attribute`             | Selects all attributes of the current node                                                              |
| `child`                 | Selects all children of the current node                                                                |
| `descendant`            | Selects all descendants (children, grandchildren, etc.) of the current node                            |
| `descendant-or-self`    | Selects all descendants (children, grandchildren, etc.) of the current node and the current node itself|
| `following`             | Selects everything in the document after the closing tag of the current node                           |
| `following-sibling`     | Selects all siblings after the current node                                                            |
| `namespace`             | Selects all namespace nodes of the current node                                                        |
| `parent`                | Selects the parent of the current node                                                                 |
| `preceding`             | Selects all nodes that appear before the current node in the document, except ancestors, attribute nodes, and namespace nodes |
| `preceding-sibling`     | Selects all siblings before the current node                                                           |
| `self`                  | Selects the current node           |


## <span style="color:teal;">**Navigation of windows**

This section states the browser functionalities.   

| Actions    | Description                          
|-------------------------------------------|-----------------------------------------------------------------------|
| `driver.get(url)`                         | Accesses the specified URL using the driver.                           |
| `driver.back()`                           | Navigates back to the previous URL.                                    |
| `driver.forward()`                        | Navigates forward to the next URL.                                     |
| `driver.refresh()`                        | Refreshes the current browser page.                                    |
| `current_url = driver.current_url`        | Stores the present URL where the browser is located in the variable `current_url`. |
| `page_title = driver.title`               | Stores the title of the current URL page where the browser is located in the variable `page_title`. |
| `driver.execute_script("location.reload();")` | Executes a JavaScript command to reload the browser, another method to refresh. |

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


## <span style="color:teal;">**Mouse Actions** 

In Selenium, mouse actions refer to the interaction with a web page's elements using the mouse. Selenium provides a **ActionChains** class to perform various mouse and keyboard actions. Common mouse actions include:

* **Clicking :** Simulating a mouse click on a web element.
```python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://example.com")

element = driver.find_element_by_id("exampleElement")

# Perform a click action
ActionChains(driver).click(element).perform()

# Close the browser
driver.quit()

```

* **Doule Clicking :** Simulating a double click on a web element.
```python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://example.com")

element = driver.find_element_by_id("exampleElement")

# Perform a double click action
ActionChains(driver).double_click(element).perform()

# Close the browser
driver.quit()

```

* **Right Click :** Simulating a right-click on a web element.

```python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://example.com")

# Locate the element to right-click
element = driver.find_element_by_id("exampleElement")

# Create an ActionChains object
actions = ActionChains(driver)

# Perform a right-click on the element
actions.context_click(element).perform()

# Example: Select an option from the context menu
# Assuming the context menu has an option with the text "Open Link in New Tab"
open_in_new_tab_option = driver.find_element_by_xpath("//div[contains(text(), 'Open Link in New Tab')]")

# Perform a click on the "Open Link in New Tab" option
actions.click(open_in_new_tab_option).perform()

# Close the browser
driver.quit()

```

* **Mouse Hover :** Moving the mouse cursor to a specific web element.

```python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://example.com")

element = driver.find_element_by_id("exampleElement")

# Move the mouse to the element
ActionChains(driver).move_to_element(element).perform()

# Close the browser
driver.quit()

```

* **Drag and Drop :** Dragging an element from one location and dropping it onto another.

```python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://example.com")

source_element = driver.find_element_by_id("sourceElement")
target_element = driver.find_element_by_id("targetElement")

# Perform a drag-and-drop action
ActionChains(driver).drag_and_drop(source_element, target_element).perform()

# Close the browser
driver.quit()

```

## <span style="color:teal;">**Handling Alers, Frames and windows** 

- ### <span style="color:grey;">**Handling Alers**
    Handling alerts is a common scenario in web automation where a web page displays a pop-up dialog box that requires user interaction. Selenium provides methods to deal with these alerts.    

    There are three types of alerts: simple alerts, confirmation alerts, and prompt alerts.   

* Simple Alert : 
A simple alert is one that displays only a message and an OK button.

```python

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Triggering a simple alert
driver.execute_script("alert('This is a simple alert');")

# Wait for the alert to appear (use WebDriverWait if necessary)
time.sleep(2)

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

# Close the browser
driver.quit()

```

* confirmation alerts : 
A confirmation alert has an OK button and a Cancel button. You can choose to accept or dismiss the alert based on your requirements.

```python

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Triggering a confirmation alert
driver.execute_script("confirm('Do you want to proceed?');")

# Wait for the alert to appear (use WebDriverWait if necessary)
time.sleep(2)

# Switch to the alert and accept it
alert = driver.switch_to.alert
alert.accept()

# Or dismiss the alert
# alert.dismiss()

# Close the browser
driver.quit()

```

* Prompt alerts :
A prompt alert is similar to a confirmation alert but includes a text input field. You can enter text and choose to accept or dismiss the alert.

```python
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Triggering a prompt alert
driver.execute_script("prompt('Please enter your name:');")

# Wait for the alert to appear (use WebDriverWait if necessary)
time.sleep(2)

# Switch to the alert, enter text, and accept it
alert = driver.switch_to.alert
alert.send_keys("John Doe")
alert.accept()

# Or dismiss the alert
# alert.dismiss()

# Close the browser
driver.quit()

```

**Switching to the Alert :** Use Alert(driver) to switch to the currently active alert.

**Getting Alert Text :** Use **'alert.text'** to retrieve the text content of the alert.

**Entering Text (for Prompt Alerts) :** If the alert is a prompt, you can use **'alert.send_keys("text")'** to enter text into the input field.

**Accepting or Dismissing the Alert :**  
- **Use alert.accept()** to accept the alert (click OK or Yes).   
- **Use alert.dismiss()** to dismiss the alert (click Cancel or No).

```
Note: 

You can also use conditional statements to handle different scenarios depending on the content or type of the alert. Additionally, consider using WebDriverWait for better synchronization when dealing with alerts in real-world scenarios.

```

- ### <span style="color:grey;">**Handling Frames**

    Handling frames (or iframes) in Selenium involves switching the WebDriver's focus to the desired frame before interacting with the elements inside it. Here's an example demonstrating how to handle frames using Python and Selenium:
```python

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Switching to a frame by index (0-based)
driver.switch_to.frame(0)

# Alternatively, you can switch to a frame by name or ID
# driver.switch_to.frame("frameName")  # By name
# driver.switch_to.frame("frameId")    # By ID

# Perform actions inside the frame
frame_element = driver.find_element(By.XPATH, "//div[@class='example-frame']")
frame_text = frame_element.text
print("Text inside the frame:", frame_text)

# Switching back to the default content (main page)
driver.switch_to.default_content()

# Perform actions outside the frame
main_page_element = driver.find_element(By.XPATH, "//div[@class='example-main']")
main_page_text = main_page_element.text
print("Text on the main page:", main_page_text)

# Close the browser
driver.quit()

```
- **Switching to a Frame :** 
Use **driver.switch_to.frame()** and specify the frame's index, name, or ID.

- **Performing Actions Inside the Frame :**
 After switching to the frame, you can find and interact with elements as you normally would.

- **Switching Back to the Default Content :**
After performing actions inside the frame, use **driver.switch_to.default_content()** to switch back to the main page.
```
Note:

It's important to note that switching to a frame is necessary before interacting with elements inside that frame. If you attempt to interact with elements inside a frame without switching to it first, Selenium will not find those elements.

You may also encounter scenarios where frames are nested (frames within frames). In such cases, you may need to switch to the parent frame or use a combination of "switch_to.parent_frame()" to navigate up the frame hierarchy.

Remember to handle frames carefully, considering the structure of the HTML document you are working with, and adjust your script accordingly.

```

- ### <span style="color:grey;">**Handling Windows**

    Handling multiple browser windows in Selenium involves switching the WebDriver's focus between different windows.

```python

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Get the current window handle (main window)
main_window_handle = driver.window_handles[0]

# Open a new window with JavaScript (or any method)
driver.execute_script("window.open('', '_blank');")

# Switch to the new window
new_window_handle = driver.window_handles[1]
driver.switch_to.window(new_window_handle)

# Perform actions in the new window
driver.get("https://www.example2.com")
new_window_title = driver.title
print("Title of the new window:", new_window_title)

# Close the new window
driver.close()

# Switch back to the main window
driver.switch_to.window(main_window_handle)

# Perform actions in the main window
main_window_title = driver.title
print("Title of the main window:", main_window_title)

# Close the browser
driver.quit()

```

```
Note:

When handling multiple windows, be aware of the following considerations:

Each window has a unique window handle, and you use these handles to switch between them.
Make sure to close windows appropriately to avoid leaving open windows after the test completes.

Ensure that your script adapts to the specific scenarios you encounter, as window handling can vary depending on the web application's behavior.
```

## <span style="color:teal;">**Scrolling Page**
In Selenium, you can scroll a web page using JavaScript.

- ### <span style="color:grey;">**Scroll to Bottom of the Page**

```python

from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Close the browser
driver.quit()

```
**Note :**  This script uses '**execute_script**' to run a JavaScript command that scrolls the page to its bottom. Adjust the **'scrollTo'** parameters as needed.


- ### <span style="color:grey;">**Scroll to Specific Element**

```python

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Find the target element
element = driver.find_element(By.ID, "targetElement")

# Scroll to the target element
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Close the browser
driver.quit()

```
**Note :** This script scrolls the page to bring a specific element into view using the **'scrollIntoView'** JavaScript function.

- ### <span style="color:grey;">**Scroll by Pixels**

```python

from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Scroll down by 500 pixels
driver.execute_script("window.scrollBy(0, 500);")

# Scroll up by 200 pixels
driver.execute_script("window.scrollBy(0, -200);")

# Close the browser
driver.quit()

```

**Note :** Here, **'scrollBy'** is used to scroll the page by a specified number of pixels. Positive values scroll down, and negative values scroll up.

- ### <span style="color:grey;">**Scroll to Top of the Page**

```python

from selenium import webdriver

driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
driver.get("https://www.example.com")

# Scroll to the top of the page
driver.execute_script("window.scrollTo(0, 0);")

# Close the browser
driver.quit()

```

**Note :** This script scrolls the page to the top using **'window.scrollTo(0, 0)'**.


## <span style="color:teal;">**Save Screenshot**
In Selenium, you can capture screenshots of the browser window using the save_screenshot method.  
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