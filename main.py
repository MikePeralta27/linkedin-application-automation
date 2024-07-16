from selenium import webdriver
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "peralta.michael27@gmail.com"
ACCOUNT_PASSWORD = "Mjavier27@*"
PHONE = "1234567890"


def abort_application():

    # click close button
    close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard button
    dismiss_button = driver.find_element(By.CSS_SELECTOR, value="[data-control-name='discard_application_confirm_btn']")
    dismiss_button.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=3921696513"
    "&f_AL=true&f_WT=2&geoId=103644278&keywords=Python%20developer%20entry%20level"
    "&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

# click sign in button
time.sleep(2)
signin_button = driver.find_element(by=By.CSS_SELECTOR,
                                    value="[data-tracking-control-name='public_jobs_nav-header-signin']")
signin_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
signin_btn = driver.find_element(by=By.CSS_SELECTOR, value="[type='submit']")
signin_btn.click()

input("Press Enter when you solve the captcha")

# Get all the jobs
jobs_list = driver.find_elements(By.CSS_SELECTOR, "ul.scaffold-layout__list-container li.ember-view")

# Applying to jobs
for job in jobs_list:
    print(f"Opening job list {job.text}")
    job.click()
    time.sleep(2)

    # Apply to job

    try:
        easy_apply_button = driver.find_element(by=By.ID, value=".jobs-s-apply button")
        easy_apply_button.click()

        # If application requires phone number and the filed is empty, then fill in the numbers
        # Find an <input> element where the id contains phoneNumber
        time.sleep(5)
        phone_field = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone_field == "":
            phone_field.send_keys(PHONE)

        # Check if submit button
        # Submit the application
        submit_btn = driver.find_element(by=By.CSS_SELECTOR, value='footer button')
        if submit_btn.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex Application, skipped.")
            continue
        else:
            # Click submit button
            print("Submitting job Application")
            submit_btn.click()

        time.sleep(2)
        # Click Close Button
        close_btn = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_btn.click()

    except NoSuchElementException:
        abort_application()
        print("No Application button, Skipped.")
        continue


time.sleep(5)
driver.quit()

