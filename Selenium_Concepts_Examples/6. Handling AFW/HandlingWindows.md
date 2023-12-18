
# <span style="color:teal;">**Handling Windows**

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