#Пример 1: Автоматизация с Python (используя Selenium для работы с браузером)
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настроить драйвер (например, для Chrome)
driver = webdriver.Chrome()

# Открыть веб-сайт
driver.get("https://example.com")

# Найти элемент по ID и выполнить действие
search_box = driver.find_element(By.ID, "search")
search_box.send_keys("Python")

# Закрыть браузер
driver.quit()
