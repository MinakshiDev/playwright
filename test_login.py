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

def create_post(page):
    page.goto(WEBSITE_URL)
    flow_input = page.locator("#main > div > div.news > div.card.news__add-new > div > form > label > div")
    flow_input.click()
    page.wait_for_timeout(1000)
    page.keyboard.type("Hello! This post is created")

    page.keyboard.press("Enter")

    page.wait_for_selector("text=Hello! This post is created")

def edit_post(page):
    page.goto(WEBSITE_URL)
    first_news_item = page.locator("div#news-posts > :first-child")
    dropdown_container = first_news_item.locator(".block__dropdown")
    three_dot_menu = dropdown_container.locator("i")
    three_dot_menu.click()
    
    page.wait_for_timeout(3000)

    edit_option = dropdown_container.locator("ul > :first-child")
    edit_option.click()
    page.wait_for_timeout(3000)

    editable_div = first_news_item.locator(".create-news-form").locator(".textarea-mask")
    editable_div.click()
    page.wait_for_timeout(3000)
    editable_div.clear()

    page.keyboard.type("Updated the post!")
    page.wait_for_timeout(3000)
    page.keyboard.press("Enter")

    expect(first_news_item).to_contain_text("Updated the post!")
    print("Assertion passed: Text found!")

def get_first_news_card_id(page):

    page.wait_for_selector("div#news-posts > div")
    first_news_card = page.locator("div#news-posts > div").first
    card_id = first_news_card.get_attribute("id")

    print("First news card ID:", card_id)

    return card_id

def pin_post(page):

    first_news_item = page.locator("div#news-posts > :first-child")
    dropdown_container = first_news_item.locator(".block__dropdown")

    dropdown_container.locator("i").click()
    dropdown_container.locator("ul").wait_for(state="visible")

    pin_option = dropdown_container.locator("ul > li").nth(1)
    pin_option.click()

def verify_card_pinned_by_id(page, card_id):

    card = page.locator(f"#{card_id}")
    
    expect(card).to_have_class(re.compile("pinned"))
    
    print(f"✅ Card with ID {card_id} is pinned")



with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    login(page)
    #edit_post(page)
    get_first_news_card_id(page)
    pin_post(page)
    first_card_id = get_first_news_card_id(page)
    verify_card_pinned_by_id(page, first_card_id)

    page.wait_for_timeout(5000)
