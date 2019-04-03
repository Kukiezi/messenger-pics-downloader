import os
import time
import json
# SELENIUM RELATED IMPORTS
from driver import initializeDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
# IMPORT FUNCTIONS
from downloader import downloadImages
from fb_login import login
from menu import menu_loader


def startDownloader():
    # CHECK IF LAUNCHING FROM FOLDER OR NOT
    for fname in os.listdir('.'):
        if fname == "config.json":
            current_dir = os.getcwd()
            break
    else:
        current_dir = f"{os.getcwd()}/messenger-pics-downloader"
    # INITIALIZING VARIABLES
    delay = 10
    print("Welcome to Messenger_Pics_Downloader")
    print("To change program settings go to config.json")
    with open(f"{current_dir}/config.json") as f:
        config = json.load(f)
    # START MENU
    data = menu_loader(config)

    try:
        # INITIALIZING DRIVER
        driver = initializeDriver(current_dir)

        # LOGGING TO FACEBOOK
        print("Logging in to Facebook.com...")
        driver.get('https://www.facebook.com/login/')
        login(driver, data["username"], data["password"])
        print("Logged in!")

        # STARTING IMAGE SRC DOWNLOADING
        print("Starting image source scrapping...")
        driver.get(data["messenger_path"])
        # sleep to make sure messenger window is fully ready and object is clickable
        time.sleep(3)
        # click first image in right menu
        driver.find_element_by_class_name("_3m31").click()
        # variables needed for scrapping
        break_rule = 0
        image_count = 1
        break_scrapping_counter = 1
        start_scrapping_from_counter = 1
        scrapping = True
        image_links = []
        # sleep to make sure first picture loads
        time.sleep(3)
        while scrapping:
            try:
                # small break between every scrap to make sure picture is ready
                time.sleep(0.5)
                if config["settings"]["start_scrapping_at_pic"] != 0:
                    while start_scrapping_from_counter < config["settings"]["start_scrapping_at_pic"]:
                        time.sleep(0.5)
                        driver.find_element_by_xpath(
                            '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/a').click()
                        print(
                            f"skipping {start_scrapping_from_counter} picture")
                        start_scrapping_from_counter += 1

                # if the video was displayed instead of image we throw TimeOutException and skip video
                WebDriverWait(driver, delay).until(EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/img')))
                # scrap src from img
                image_src = driver.find_element_by_xpath(
                    '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[1]/div[2]/div[1]/div/img').get_attribute("src")

                print(f"Getting image source: {image_count}")
                # adding src to list
                if image_src not in image_links:
                    image_links.append(image_src)
                    # UNCOMMENT IF YOU WANT ALL THE SOURCES TO BE SAVED IN images.txt FILE
                    # file = open(f"{current_dir}/images.txt", "a")
                    # file.write(image_src + "\n\n")
                    # file.close()
                else:
                    break_rule += 1
                # go to next image
                driver.find_element_by_xpath(
                    '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/a').click()
                # if src fails adding 10 times it means program is completed
                if break_rule == 10:
                    break
                # check if check_stop_every_pic was reached
                if config["settings"]["check_stop_every_pic"] == break_scrapping_counter:
                    while True:
                        scrapping_question = input(
                            f"Do You want to stop scrapping at {image_count} and start downloading? (y/n): ")
                        if scrapping_question == 'y':
                            scrapping = False
                            break
                        elif scrapping_question == 'n':
                            break_scrapping_counter = 0
                            break
                        else:
                            print("Only y/n are accepted!")

                image_count += 1
                break_scrapping_counter += 1

            except TimeoutException:
                # write to file that we skipped video at ceratin position
                file = open(f"{current_dir}/errors.txt", "a")
                file.write(
                    f"Error: Was not able to save file: {image_count}. It was not image file. \n\n")
                file.close()
                driver.find_element_by_xpath(
                    '//*[@id="facebook"]/body/div[5]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/a').click()
                image_count += 1

    # if we get driver error write it to file
    except WebDriverException as ex:
        file = open(f"{current_dir}/webdriver_error.txt", "w")
        file.write(
            f"{str(ex)}")
        file.close()
        print("Exception occured! Will download all images gathered until exception. Check webdriver_error.txt for more details.")

    # DOWNLOADING IMAGES
    print("Downloading images...")

    if not data["folder_name"]:
        data["folder_name"] = "images"

    os.makedirs(f"{current_dir}/{data['folder_name']}", exist_ok=True)
    img_name = 1
    for image in image_links:
        downloadImages(current_dir, data["folder_name"], img_name, image)
        print(f"Downloaded image: {img_name}")
        img_name += 1

    driver.quit()

    print(f"""
    Task Completed!
    Your images are in folder {data["folder_name"]}
    Have Fun!""")
