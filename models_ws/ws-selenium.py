from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.google.com/maps")

driver.quit()