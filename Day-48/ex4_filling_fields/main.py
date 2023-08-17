from selenium import webdriver

# download chrome driver: https://chromedriver.chromium.org/downloads
chrome_driver_path = "path to your chrome driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Antonio")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Dias")
email = driver.find_element_by_name("email")
email.send_keys("antonio@email.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()
