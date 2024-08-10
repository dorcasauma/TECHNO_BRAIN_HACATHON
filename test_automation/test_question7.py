from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_add_to_cart(driver):
    driver.get("https://www.jumia.co.ke/")

    search_box = driver.find_element(By.NAME, 'q')

    search_box.send_keys('laptop')

    add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(),'Add to Cart')]")

    search_box.submit()