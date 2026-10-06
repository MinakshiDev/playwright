from playwright.sync_api import sync_playwright, expect
import time
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

def create_notes(page):
    page.goto(f"{WEBSITE_URL}notes/")
    notes_add_icon = page.locator("#main > div > div.notes > div.fixed-action-btn.direction-top > a > i")
    notes_add_icon.wait_for(state="visible")  
    notes_add_icon.click()
    page.wait_for_timeout(3000)

def add_note(page):
    add_button = page.locator("div.fixed-action-btn")
    add_button.wait_for(state="visible")
    add_button.hover()

    second_option = page.locator("div.fixed-action-btn ul > li").nth(1)
    second_option.wait_for(state="visible")
    second_option.click()

    print("✅ Clicked second hover option (Social dokumentation)")
    page.wait_for_timeout(5000)

def create_social_documentation(page):
    page.goto(f"{WEBSITE_URL}notes/create/lss/?back=/notes/")

    
    summary_input = page.locator("#id_summary")
    summary_input.click()
    page.wait_for_timeout(3000)
    page.keyboard.type("Automated summary for social documentation")
    page.wait_for_timeout(2000)


    details_input = page.locator("div.note-editable")
    details_input.click()
    details_input.fill("This is an automated detailed description.")
    page.wait_for_timeout(2000)

    enhet_input = page.locator("#create-note-form > div > div:nth-child(1) > div.pill-box > div > label:nth-child(1)")
    enhet_input.click()


    print("🔹 Selecting Client...")
    client_trigger = page.locator("#id_clients_field_main")
    client_trigger.click()
    page.wait_for_timeout(5000)
    client_trigger.locator("li").nth(2).click()
    print("✅ Client selected")


    keyword_trigger = page.locator("#id_minor_keyword_field_main")
    keyword_trigger.click()
    page.wait_for_timeout(3000)
    keyword_trigger.locator("li").nth(1).click()
    keyword_trigger.locator("li").nth(2).click()
    print("✅ Keyword selected")

    print("🔹 Saving note...")
    save_button = page.locator("input#_sign_button")
    save_button.click()

    # 7️⃣ Verify saved
    expect(page.locator("text=Utkast sparat")).to_be_visible()
    print("✅ Social documentation created successfully")

    
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    browser = p.chromium.launch(
        headless=False,
        args=["--start-maximized"]
    )

    page = browser.new_page(no_viewport=True) 
    login(page)
    create_notes(page)
    add_note(page)
    create_social_documentation(page)
    

    page.wait_for_timeout(5000)
    browser.close()











