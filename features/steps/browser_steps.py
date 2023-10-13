# -- FILE: features/steps/browser_steps.py
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

@given(u'I visit "{url}" with title "{H1_title}"')
def step_impl(context, url, H1_title):

    context.browser.get(url)
    delay = 3 # seconds
    try:
        context.myElem = WebDriverWait(context.browser, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'H1')))
    except TimeoutException:
        assert False

    assert H1_title in context.browser.title

@given(u'I visit "{url}"')
def step_impl(context, url):
    
    context.browser.get(url)
    assert url in context.browser.current_url