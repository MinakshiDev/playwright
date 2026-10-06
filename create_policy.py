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


def add_policy_area(page):
    page.goto(f"{WEBSITE_URL}policy_bank/policy-folder/")

    # Click Add button (XPath – last resort)
    page.locator(
        'xpath=//*[@id="main"]/div/div[5]/div[1]/div[2]/div[2]/a[1]'
    ).click()
    page.wait_for_timeout(2000)


    page.locator("#id_name").fill("testing")
    print("✅ Name Entered")
    page.wait_for_timeout(3000)

    page.locator("#id_description").fill("It is automated.")
    print("✅ Description Entered")
    page.wait_for_timeout(3000)

    save_button = page.locator("#main > div > div.policy_bank > form > div.form__cta.hidden-xs > button")
    save_button.wait_for(state="visible")
    save_button.scroll_into_view_if_needed()
    save_button.click()
    page.wait_for_timeout(3000)

def create_policy(page):
    page.goto(f"{WEBSITE_URL}policy_bank/policy-folder/")


    folder_list_container = page.locator("#main > div > div.policy-bank > div.space-above > div > div > div > "
    "div.div.flex.policy-bank-card-header.height--40 > div.block__dropdown > i")
    folder_list_container.click()
    page.wait_for_timeout(2000)
    page.locator("#dropdown-1 > li:nth-child(1) > a").click()
    page.wait_for_timeout(2000)

    page.locator("#main > div > div.policy_bank > form > div.form__inputs-group > ""div.flex.gap-20 > div.vertical-center > div > a").click()
    page.wait_for_timeout(2000)

    input_name = page.locator("#id_form-0-name")
    input_name.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Policy1")
    page.wait_for_timeout(2000)

    save_button = page.locator("#main-form-of-page > div.form__cta.hidden-xs > button")
    save_button.scroll_into_view_if_needed()
    save_button.click()
    page.wait_for_timeout(2000)

    page.locator("#main > div > div.policy_bank > form > div.folder-list-card.flex.gap-20.align-items-stretch > div.card.no-margin > div > a").click()
    page.wait_for_timeout(2000)

    name_input = page.locator("#id_name")
    name_input.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Policy")
    page.wait_for_timeout(2000)
    print("✅ Name Entered")

    area_dropdown = page.locator("#id_areas_field_main")
    area_dropdown.click()
    page.wait_for_timeout(2000)
    area_dropdown.locator("li").nth(1).click()
    page.wait_for_timeout(2000)
    print("✅ Areas selected")

    area_dropdown = page.locator("#id_status_field_main")
    area_dropdown.click()
    page.wait_for_timeout(2000)
    area_dropdown.locator("li").nth(2).click()
    page.wait_for_timeout(2000)
    print("✅ Areas selected")

    description = page.locator("#main > div > div.policy_bank > div > form > div.form__inputs-group > label:nth-child(2) > div > div > div > div > div.note-editing-area > div.note-editable")
    description.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Policy is created.")
    page.wait_for_timeout(2000)
    print("✅ Description selected")

    good_example = page.locator("#main > div > div.policy_bank > div > form > div.form__inputs-group > label:nth-child(3) > div > div > div > div > div.note-editing-area > div.note-editable")
    good_example.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Test is done.")
    page.wait_for_timeout(2000)
    print("✅ Good_Example selected")

    bad_example = page.locator(" #main > div > div.policy_bank > div > form > div.form__inputs-group > label:nth-child(4) > div > div > div > div > div.note-editing-area > div.note-editable")
    bad_example.click()
    page.wait_for_timeout(2000)
    page.keyboard.type("Test is due.")
    page.wait_for_timeout(2000)
    print("✅ Bad_Example selected")


    save_button = page.locator("#main > div > div.policy_bank > div > form > div.form__cta.hidden-xs > button")
    save_button.wait_for(state="visible")
    save_button.scroll_into_view_if_needed()
    save_button.click()
    page.wait_for_timeout(3000)
   
    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    page = browser.new_page(no_viewport=True) 
    login(page)
    #add_policy_area(page)
    create_policy(page)


    page.wait_for_timeout(5000)
    browser.close()

