import time
from selenium import webdriver

username = "Bryan"
cps = 10
delay = (1000/cps)/1000
link = "https://popdog.click/"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path="./chromedriver.exe")
browser.get(link)
print("Connecting to https://popdog.click...")
browser.implicitly_wait(10)
print("Looking for \"play\" button.")
browser.find_element_by_class_name("play").click()
print("Clicked on the \"play\" button.")
print("Looking for \"username\" field.")
browser.find_element_by_id("nameTextField").send_keys(username)
print("Done inserting username.")
print("Looking for \"close\" button")
browser.find_element_by_id("settingsClose").click()
print("Clicked on the \"close\" button.")
print("Fetching element to click on.")
dog = browser.find_element_by_id("myImage")
dogClicked = browser.find_element_by_id("myImageClick")
cookie = browser.find_element_by_id("cookie")
print("Done fetching all element required.\n\nLet's Go!")

while True:
    cookieAvailability = cookie.get_attribute("style")
    if cookieAvailability[58:].strip() == "block;":
        cookie.click()
    dog.click()
    dogClicked.click()
    time.sleep(delay)
