
## <span style="color:teal;">**Initializing Webdrivers**   
To open the URL or automate the test cases, we need to have web drivers for different browsers. Selenium can access the web driver in order to work with browsers.  


```Python
from selenium import  webdriver
driver = webdriver.Chrome('C:\Mohesh\Drivers\chromedriver.exe')
```

We can have multiple browser access and each browser has individual drivers. For example, chrome has chromedriver while Mozilla Firefox operates with Geckodriver. Similarly, other browsers also have their drivers supported by selenium.  
