# https://github.com/yoga-0731/amazon-price-tracker-bot/

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.amazon.in/AGARO-Utensils-Stainless-Resistant-Cookware/dp/B09XTYCLDJ/ref=sr_1_6?crid=1AYIA3HNZ6HL2&keywords=kitchen+utensils&qid=1686540620&sprefix=kitchen+utensil%2Caps%2C421&sr=8-6")
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)

price_through_xpath = driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span[2]/span[2]')
print(price_through_xpath.text)

driver.quit()
