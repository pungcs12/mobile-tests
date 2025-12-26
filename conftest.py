import pytest
from appium import webdriver
import os

app_path = os.path.join(os.getcwd(), "ApiDemos-debug.apk")

@pytest.fixture(scope="session")
def driver():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "emulator-5554",
        "app": app_path
    }

    driver = webdriver.Remote(
        "http://host.docker.internal:4723",
        # "http://127.0.0.1:4723",
        caps
    )

    yield driver
    driver.quit()
