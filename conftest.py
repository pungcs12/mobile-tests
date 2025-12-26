import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="session")
def driver():
    app_path = os.path.abspath("app.apk")  # or tests/app.apk if needed

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app = app_path

    driver = webdriver.Remote(
        "http://192.168.1.112:4723",
        options=options
    )

    yield driver
    driver.quit()
