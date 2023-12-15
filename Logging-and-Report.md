 # <span style="color:teal;">**Logging and Report**
**1. Pytest with pytest-html :** We need to install the pytest report format in our system by giving this below command line in command prompt.
```
pip install pytest pytest-html
```
```python

import pytest
from selenium import webdriver

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
    yield driver
    driver.quit()

def test_example(setup_teardown):
    setup_teardown.get("https://www.example.com")
    assert setup_teardown.title == "Example Domain"

```
```
Run your script using the below command:

pytest test_script.py --html=report.html
```
Here, **'test_script.py'** is the python file and **'report.html'** is the report.

**2. unittest with HtmlTestRunner :** We need to install the pytest report format in our system by giving this below command line in command prompt.

```
pip install html-testRunner
```
```python
import unittest
from selenium import webdriver
import HtmlTestRunner

class TestExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

    def test_example(self):
        self.driver.get("https://www.example.com")
        self.assertEqual(self.driver.title, "Example Domain")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))

```
```
Run your script by using the below command:

python test_script.py
```
**3. Allure Framework :** We need to install the pytest report format in our system by giving this below command line in command prompt.
```
pip install allure-pytest
```
```python

import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import allure

@pytest.fixture
def setup_teardown():
    driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')
    yield driver
    driver.quit()

@allure.feature("Example Feature")
@allure.story("Example Story")
@allure.title("Test Example")
def test_example(setup_teardown):
    setup_teardown.get("https://www.example.com")
    with allure.step("Verify the title"):
        assert setup_teardown.title == "Example Domain"
    allure.attach(setup_teardown.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

```

```
# Run the script using below command line to generate report:

pytest test_script.py --alluredir=./allure-results


# Run your script using below code in terminal

allure serve ./allure-results
```
**4. Extent Reports :** We need to install the pytest report format in our system by giving this below command line in command prompt.
```
pip install extentreports
```
```python

import unittest
from selenium import webdriver
from extentreports import Report

class TestExample(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe')

    def test_example(self):
        self.driver.get("https://www.example.com")
        self.assertEqual(self.driver.title, "Example Domain")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    with Report('report.html', 'My Test Report') as report:
        unittest.main(testRunner=report)

```
```
Run your script using below code in terminal:

python test_script.py
```
