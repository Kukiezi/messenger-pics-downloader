from selenium import webdriver
import os


def initializeDriver(directory):
    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_argument("--headless")
    options.add_argument("--mute-audio")
    options.add_argument("--kiosk")
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(
        f"{directory}/chromedriver", options=options)
    return driver
