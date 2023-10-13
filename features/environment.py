# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chromium.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.options import Log
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.chromium.options import ChromiumOptions

@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    firefoxservice = Service(log_path="./tmp/geckodriver.log")
    context.browser = Firefox(service=firefoxservice)

    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


@fixture
def browser_chrome_headless(context):
    chromeoption = ChromiumOptions()
    chromeoption.add_argument('--headless=new')
    chromeoption.add_argument('--window-size=1300,700')
    chromeoption.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")

    # chromeoption.binary_location = ChromeDriverManager().install()
    context.browser = Chrome(options=chromeoption, service=Service(ChromeDriverManager().install())) #Chrome(options=chromeoption)

    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

#def before_all(context):
#    use_fixture(browser_firefox, context)
#    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.

def before_feature(context, feature):
    # Typically for testing with js
    if 'browser' in feature.tags:
        use_fixture(browser_firefox, context)
    if 'browser_headless' in feature.tags:
        use_fixture(browser_chrome_headless, context)