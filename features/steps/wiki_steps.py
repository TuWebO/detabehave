# -- FILE: features/steps/wiki_steps.py
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

@when(u'I search by "{lat}" and "{long}" coords using wiki nearby API')
def step_impl(context, lat, long):
     nearby_url = 'https://en.wikipedia.org/wiki/Special:Nearby?#/coord/' + lat + ',' + long
     context.browser.get(nearby_url)
     delay = 5 # seconds
     try:
         context.myElem = WebDriverWait(context.browser, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mw-nearby-pages > div > div.mw-vue-page-list.mw-vue-nearby__pagelist')))
         assert context.myElem is not None
     except TimeoutException:
         assert False


@then(u'I should see "{search_term}" in the wiki nearby results page')
def step_impl(context, search_term):

    card_titles = context.myElem.find_elements(By.CLASS_NAME, "cdx-card__text__title")
    card_titles_text = ''
    for e in card_titles:
        card_titles_text += e.text + ' '
    
    assert search_term in card_titles_text