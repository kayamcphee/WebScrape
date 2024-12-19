from selenium import webdriver
from selenium.webdriver.common.by import By

# link to the chrome webdriver. Make sure to get the version that matcheds your Google Chrome version
# https://googlechromelabs.github.io/chrome-for-testing/

# Place Chrome driver in C:\Program Files (x86) or C:\Program Files

PATH = "C:\Program Files\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
cService = webdriver.ChromeService(executable_path = PATH)
driver = webdriver.Chrome(service=cService)


driver.get("https://www.staples.com/mounts/directory_mounts?")

products = driver.find_elements(By.CLASS_NAME  ,"SearchResults-UX2__searchGridColumn")

for product in products:
    title = product.find_element(By.CLASS_NAME, "standard-tile__title")
    price = product.find_element(By.CLASS_NAME, "standard-tile__ada_hidden")
    print("Item:", title)
    print("Price:", price)
# This prevents the browser from closing immediately.
while(True):
    pass
# brightdata - https://brightdata.com/