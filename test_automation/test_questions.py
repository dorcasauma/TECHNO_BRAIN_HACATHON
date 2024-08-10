import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_question_one(driver):
    driver.get('https://www.tumacredo.com/#/homepage/welcome')

    driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()

    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('dorcasauma')

    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('angeldrc')

    driver.find_element(By.ID, 'login-btn').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be('https://www.tumacredo.com/#/home/dashboard'))

    assert driver.current_url == "https://www.tumacredo.com/#/home/dashboard", "Login failed"


def test_question_four(driver):
    driver.get('https://google.com')

    search_box = driver.find_element(By.NAME, 'q')

    search_box.send_keys('Test Automation')

    search_box.submit()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'search')))

    results = driver.find_elements(By.XPATH, "//div[@id='search']//div[@class='g']")
    assert len(results) > 0, "No search results found"

    time.sleep(5)

def test_question_five(appium_webdriver):

    # Wait for the WhatsApp main activity to load
    wait = WebDriverWait(appium_webdriver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'com.whatsapp:id/conversations_row_contact_name')))

    assert appium_webdriver.current_activity == '.Main', "WhatsApp did not launch successfully"

    time.sleep(5)

