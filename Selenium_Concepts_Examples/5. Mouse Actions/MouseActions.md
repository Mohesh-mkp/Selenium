


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
