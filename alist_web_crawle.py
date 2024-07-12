from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

driver_path = r'F:\Tool\Chrome——drive\chromedriver.exe'  # 指定你的ChromeDriver路径

exist_url = []

def create_driver():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def collect_links(seed, depth):
    driver = create_driver()  # 创建新的WebDriver实例
    try:
        driver.get(seed)
        exist_url.append(seed)
        my_element_css = 'list-item.hope-stack.hope-c-dhzjXW.hope-c-PJLV.hope-c-PJLV-ikoJJtX-css'
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,TimeoutException)
        link_elements = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, my_element_css))
        )

        for link in link_elements:
            href = link.get_attribute('href')
            if  href not in exist_url:
                with open("ode6.txt", 'a', encoding='utf-8') as f:
                    f.write(href + '\n')
                if depth < 3:  
                    collect_links(href, depth + 1)
        driver.quit()
                    
        
    except Exception as e:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'hope-button.hope-c-ivMHWx.hope-c-ivMHWx-kcPQpq-variant-subtle.hope-c-ivMHWx-kWSPeQ-size-md.hope-c-ivMHWx-dvmlqS-cv.hope-c-PJLV.hope-c-PJLV-iikaotv-css'))
        )
        down_link = driver.find_elements(By.CLASS_NAME, 'hope-button.hope-c-ivMHWx.hope-c-ivMHWx-kcPQpq-variant-subtle.hope-c-ivMHWx-kWSPeQ-size-md.hope-c-ivMHWx-dvmlqS-cv.hope-c-PJLV.hope-c-PJLV-iikaotv-css')
        for each in down_link:
            down_href =  each.get_attribute('href')
            with open("xiaoliaoyou_link.txt", 'a', encoding='utf-8') as f:
                f.write(down_href+'\n')
        exist_url.append(seed)



def main():
    url_root = 'https://pan.t-satoru.top/ode5/Galgames/%E4%BB%8E%E5%85%B6%E4%BB%96%E7%AB%99%E6%90%AC%E8%BF%90%E7%9A%84%20%E5%AF%86%E7%A0%81%E6%9C%A8%E5%81%B6%20%E4%B8%8D%E6%8F%90%E4%BE%9B%E5%94%AE%E5%90%8E%E6%9C%8D%E5%8A%A1/9-nine' 
    collect_links(url_root, 0)

if __name__ == "__main__":
    main()
