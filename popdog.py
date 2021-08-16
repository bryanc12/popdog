from selenium import webdriver

username = "Bryan"
link = "https://popdog.click/"
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options, executable_path="./chromedriver.exe")
browser.get(link)
browser.implicitly_wait(10)
browser.find_element_by_id("nameTextField").send_keys(username)
browser.find_element_by_id("settingsClose").click()
dog = browser.find_element_by_id("myImage")
dogClicked = browser.find_element_by_id("myImageClick")
cookie = browser.find_element_by_id("cookie")

while True:
    cookieAvailability = cookie.get_attribute("style")
    if cookieAvailability[58:].strip() == "block;":
        cookie.click()
    dog.click()
    dogClicked.click()