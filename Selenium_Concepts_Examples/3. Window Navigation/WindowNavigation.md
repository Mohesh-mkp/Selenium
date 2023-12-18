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