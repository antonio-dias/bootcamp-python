from selenium import webdriver

# download chrome driver: https://chromedriver.chromium.org/downloads
chrome_driver_path = "path to your chrome driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

driver.close()
driver.quit()
