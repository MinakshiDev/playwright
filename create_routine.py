from playwright.sync_api import sync_playwright, expect
import re
import os
from dotenv import load_dotenv

load_dotenv()

WEBSITE_URL = os.getenv("PROJECT_URL", "https://example.com/")
USERNAME = os.getenv("PROJECT_USERNAME")
PASSWORD = os.getenv("PROJECT_PASSWORD")

USERNAME_SELECTOR = "input[name='auth-username']"  
PASSWORD_SELECTOR = "input[name='auth-password']"
LOGIN_BUTTON_SELECTOR = "button[type='button']"  

def login(page):
    page.goto(WEBSITE_URL)

    page.wait_for_timeout(1000)
    page.fill(USERNAME_SELECTOR, USERNAME)
    page.wait_for_timeout(1000)
    page.fill(PASSWORD_SELECTOR, PASSWORD)

    page.wait_for_timeout(1000)
    page.click(LOGIN_BUTTON_SELECTOR)
    page.wait_for_timeout(5000)

def create_routine(page):
    page.goto(f"{WEBSITE_URL}client-planning/routines/create/?next=%2Fclient-planning%2Froutines%2F")
    page.wait_for_timeout(2000)

    name_input = page.locator("#id_name")
    name_input.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("testing!")
    page.wait_for_timeout(2000)
    print("✅ Name Entered")

    add_image = page.locator("#routine-form > div.form__inputs-group > div.wci-image-selector.card > div.wci-image-selector__empty-state.wci-image-selector__state-visible > a")
    add_image.click()
    page.wait_for_timeout(2000)
    choose_image = page.locator("#routine-form > div.form__inputs-group > div.wci-image-selector.card > div.modal.wci-image-selector__modal.open > div > div > div:nth-child(10) > img")
    choose_image.click()
    page.wait_for_timeout(2000)
    print("✅ Image selected")

    keyword_dropdown = page.locator("#id_keyword_field_main")
    keyword_dropdown.click()
    page.wait_for_timeout(2000)
    keyword_dropdown.locator("li").nth(4).click()
    page.wait_for_timeout(2000)
    print("✅ Keyword selected")

    weekdays_dropdown = page.locator("#id_weekdays_field_main")
    weekdays_dropdown.click()
    page.wait_for_timeout(2000)
    weekdays_dropdown.locator("li").nth(2).click()
    page.wait_for_timeout(2000)
    print("✅ Weekdays selected")

    client_dropdown = page.locator("#id_clients_field_main")
    client_dropdown.click()
    page.wait_for_timeout(2000)
    client_dropdown.locator("li").nth(3).click()
    page.wait_for_timeout(2000)
    print("✅ Clients selected")

    area_dropdown = page.locator("#id_areas_field_main")
    area_dropdown.click()
    page.wait_for_timeout(2000)
    area_dropdown.locator("li").nth(1).click()
    page.wait_for_timeout(2000)
    print("✅ Areas selected")

    step_input_1 = page.locator("#id_steps-0-description")
    step_input_1.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Clean a table")
    page.wait_for_timeout(2000)
    
    step_input_2 = page.locator("#id_steps-1-description")
    step_input_2.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Mop floor")
    page.wait_for_timeout(2000)
    
    step_input_3 = page.locator("#id_steps-2-description")
    step_input_3.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Dispose trash")
    page.wait_for_timeout(2000)

    save_button = page.locator("#routine-form > div.form__cta.hidden-xs > button")
    save_button.click()

    print("✅ Routine created successfully")



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    page = browser.new_page(no_viewport=True) 
    login(page)
    create_routine(page)


    page.wait_for_timeout(5000)
    browser.close()


