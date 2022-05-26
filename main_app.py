from selenium import webdriver
import time
# chromedriver.exe path
PATH = "C:\Program Files (x86)\chromedriver.exe"
# Sporcle path
sporcle_url = "https://www.sporcle.com/"

# Initialise webdriver object
driver = webdriver.Chrome(PATH)

# Open url in browser
driver.get(sporcle_url)

# Enter iframe
f = driver.find_element_by_id("sp_message_iframe_576254")
print("found frame")
driver.switch_to.frame(f)
time.sleep(1)
elements = driver.find_elements_by_tag_name("button")

for el in elements:
    print(el.text)
time.sleep(1)

elements[-1].click()
