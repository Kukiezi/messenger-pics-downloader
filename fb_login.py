def login(driver, login, password):
    driver.find_element_by_name('email').send_keys(login)
    driver.find_element_by_name('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()
    return driver
