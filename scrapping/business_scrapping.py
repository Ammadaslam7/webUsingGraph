from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

webdriver_path = r'C:\Program Files (x86)\chromedriver.exe'
s = Service(webdriver_path)
driver = webdriver.Chrome(service=s)
url = 'https://www.daraz.pk/home-decoration/'
driver.get(url)
product_elements = driver.find_elements(By.XPATH, '//div[@class="gridItem--Yd0sa"]')
for product_element in product_elements:
    # Extract product name
    product_name = product_element.find_element(By.XPATH, './/div[@class="title-wrapper--IaQ0m"]').text
    
    # Extract product price
    product_price = product_element.find_element(By.XPATH, './/span[@class="currency--GVKjl"]').text
    
    # Print or store the extracted information
    print("Product Name:", product_name)
    print("Product Price:", product_price)
    print("------------------------")

# Close the browser
driver.quit()

