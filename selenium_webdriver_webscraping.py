# https://github.com/yoga-0731/amazon-price-tracker-bot/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Preventing browser from closing
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create object
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.in/AGARO-Utensils-Stainless-Resistant-Cookware/dp/B09XTYCLDJ/ref=sr_1_6?crid=1AYIA3HNZ6HL2&keywords=kitchen+utensils&qid=1686540620&sprefix=kitchen+utensil%2Caps%2C421&sr=8-6")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

price_through_xpath = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
print(price_through_xpath.text)


# Challenge - 1: Getting Upcoming Events from python.org page
driver.get('https://www.python.org')

upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text.split('\n')
events = {upcoming_events[i]: upcoming_events[i+1] for i in range(0, len(upcoming_events), 2)}
print(events)

# Challenge - 2: Getting Wikipedia data
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
article_count = count[0].text
print(article_count)

# Clicking
count[0].click()
# (or)
count = driver.find_element(By.LINK_TEXT, str(article_count))
count.click()

# Typing/Searching and hitting Enter
search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys('Python')
search_bar.send_keys(Keys.ENTER)

driver.quit()
