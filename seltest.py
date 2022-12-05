from selenium import webdriver
from selenium.webdriver.common.by import By
from ctypes import *
import time

# 1. Открыть браузер и развернуть на весь экран.
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(5)

# 2. Зайти на yandex.ru.
driver.get("https://market.yandex.ru/")
time.sleep(500)

# 3. В разделе маркет выбрать Сотовые телефоны.
openCatalog = driver.find_element(By.ID,"find_element_by_id").click()

# 4. Зайти в расширенный поиск.
# 5. Задать параметр поиска до 20000 рублей и Диагональ экрана от 3 дюймов.
# 6. Выбрать не менее 5 любых производителей, среди популярных.
# 7. Нажать кнопку Подобрать.
# 8. Проверить, что элементов на странице 10.
# 9. Запомнить первый элемент в списке.
# 10. Изменить Сортировку на другую (популярность или новизна).
# 11. Найти и нажать по имени запомненного объекта.
# 12. Вывести цифровое значение его оценки.
# 13. Закрыть браузер.