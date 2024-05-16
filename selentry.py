# from selenium import webdriver

# # Path to the WebDriver executable
# DRIVER_PATH = r'\Users\Kaya Evis\Downloads\chromedriver-win64'

# capabilities = webdriver.ChromeOptions()
# capabilities.binary_location = DRIVER_PATH
# # Create a new instance of the Chrome driver
# driver = webdriver.Chrome(options=capabilities)

# # Open the webpage
# driver.get("https://www.staples.com/mounts/directory_mounts?pn=1")

# # Wait for the dynamic content to load (you may need to adjust the wait time)
# driver.implicitly_wait(10)

# # Find and print the product titles and prices
# products = driver.find_elements_by_class_name("standard-tile__standard_tile_container")
# for product in products:
#     title = product.find_element_by_class_name("standard-tile__title").text.strip()
#     price = product.find_element_by_class_name("standard-tile__ada_hidden").text.strip()
#     print("Item:", title)
#     print("Price:", price)

# # Close the browser
# driver.quit()


from selenium import webdriver


# link to the chrome webdriver. Make sure to get the version that matcheds your Google Chrome version
# https://googlechromelabs.github.io/chrome-for-testing/

# Place Chrome driver in C:\Program Files (x86) or C:\Program Files

PATH = "C:\Program Files (x86)\chromedriver-win64 (1).zip\chromedriver-win64\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
cService = webdriver.ChromeService(executable_path = PATH)
driver = webdriver.Chrome(service=cService)


driver.get("https://www.staples.com/mounts/directory_mounts?")

# This prevents the browser from closing immediately.
while(True):
    pass


# brightdata - https://brightdata.com/