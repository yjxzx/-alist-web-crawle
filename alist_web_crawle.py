from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')

driver_path = r'F:\Tool\Chrome——drive\chromedriver.exe' 

exist_url = []

def create_driver():
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def collect_links(seed, depth):
    driver = create_driver() 
    try:
        driver.get(seed)
        exist_url.append(seed)
        my_element_css = 'your_elements/修改元素'
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
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'your_elements/修改元素'))
        )
        down_link = driver.find_elements(By.CLASS_NAME, 'your_elements/修改元素')
        for each in down_link:
            down_href =  each.get_attribute('href')
            with open("xiaoliaoyou_link.txt", 'a', encoding='utf-8') as f:
                f.write(down_href+'\n')
        exist_url.append(seed)



def main():
    url_root = '你的url/your_url' 
    collect_links(url_root, 0)

if __name__ == "__main__":
    main()
