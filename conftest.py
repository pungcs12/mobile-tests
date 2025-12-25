import pytest
from appium import webdriver

@pytest.fixture(scope="session")
def driver():
    caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "app": "/workspace/app.apk"
    }

    driver = webdriver.Remote(
        "http://host.docker.internal:4723",
        caps
    )

    yield driver
    driver.quit()
