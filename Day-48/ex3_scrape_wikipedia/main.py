from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# download chrome driver: https://chromedriver.chromium.org/downloads
chrome_driver_path = "path to your chrome driver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)
# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)