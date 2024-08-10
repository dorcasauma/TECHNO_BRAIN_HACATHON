import pytest
from appium import webdriver as appium_webdriver
from selenium import webdriver


@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def appium_webdriver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',  # Update to your device's version
        'deviceName': 'Android Emulator',
        'appPackage': 'com.whatsapp',
        'appActivity': 'com.whatsapp.Main',
        'automationName': 'UiAutomator2'
    }
    driver = appium_webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver