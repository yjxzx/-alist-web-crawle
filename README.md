# alist-web crawler

基于 Selenium 对 alist 下载链接的爬取。

## 代码文件
代码在 `alist_web_crawle.py` 中。

## 运行要求

### 1. 下载以下库文件

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
```
### 2. 载与 Chrome 版本匹配的 Selenium

### 3. 确保修改 driver_path 为你的 ChromeDriver 路径：

```python
driver_path = r'F:\Tool\Chrome——drive\chromedriver.exe'
```

### 4. change your elements/修改你想要的元素

### 5. 保存下载链接
最后的下载链接保存在当前运行 alist_web_crawle.py 的目录下。ode6.txt 记录所有链接。


## English

# alist Web Crawler

A web crawler for downloading links from alist using Selenium.

## Code File

The code is in `alist_web_crawle.py`.

## Requirements

### 1. Install the following libraries

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
```
### 2. Install Selenium that matches your Chrome version

### 3. Make sure to modify driver_path to your ChromeDriver path:
```python
driver_path = r'F:\Tool\Chrome——drive\chromedriver.exe'
```

### 4. change your elements/修改你想要的元素

### 5. Save download links  
Finally, the downloaded links will be saved in the current directory where alist_web_crawle.py is run. code6.txt records all links.



