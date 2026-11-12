from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)

try:
    # Open Konga
    driver.get("https://www.konga.com")

    # Verify the page loaded
    print("Page title:", driver.title)
    assert "Konga" in driver.title, "Konga homepage did not load"
    print("TEST PASSED: Konga homepage loaded")

finally:
    driver.quit()