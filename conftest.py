import os
import logging
from pyvirtualdisplay import Display
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as Options_ff
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def mylogger(*msg):
    lm = " ".join([str(i) for i in msg])
    logging.info(lm)
    return True

BASE_DIR = ""

OS_TYPE = os.name
if OS_TYPE == "posix":
#    global TIMELABEL
    mylogger("We are in LINUX - posix")
    BASE_DIR = "/app"
#    logging.getLogger().addHandler(
#        logging.FileHandler(filename=os.environ.get('PTH', '/logs/') + TIMELABEL+ '/efind_test_log.log', mode='w+'))
if OS_TYPE == "nt":
    mylogger("We are in Windows - nt")
    BASE_DIR = "C:\\work\\tmp"

if BASE_DIR == "":
    print ("OS doesn't defined")
    #mylogger("OS doesn't defined")
    exit(1)

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    marker = request.node.get_closest_marker("browser")

    if marker and marker.args[0] == "mobile":
        btype = "mobile"
    elif marker and marker.args[0] == "tablet":
        btype = "tablet"
    else:
        btype = "desktop"

    if OS_TYPE == "posix":
        if btype == "desktop":
            display = Display(visible=0, size=(1920, 1200))
        elif btype == "mobile":
            display = Display(visible=0, size=(500, 700))
        elif btype == "tablet":
            display = Display(visible=0, size=(800, 700))
        display.start()
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        mylogger("start chrome browser for test:", btype)

        options = Options()
        options.add_argument("--start-maximized")
        if btype == "desktop":
            options.add_argument("window-size=1400,1200")
        elif btype == "mobile":
            options.add_argument("window-size=300,800")
        elif btype == "tablet":
            options.add_argument("window-size=800,800")

        options.add_experimental_option('prefs', {'download.default_directory': f"{BASE_DIR}/browser_downloads",
                                                  "download.prompt_for_download": False,
                                                  "download.directory_upgrade": True, "safebrowsing.enabled": True})
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-dev-shm-usage')

        if OS_TYPE == "nt":
            service = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=service, options=options)
        else:
            mylogger("We are in Linux")
            service = Service(executable_path=r'/usr/bin/chromedriver')
            browser = webdriver.Chrome(service=service, options=options)
            time.sleep(5)
    elif browser_name == "firefox":
        mylogger("start firefox browser for test:", btype)
        options = Options_ff()
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_capability("moz:firefoxOptions", {"log": {"level": "trace"}})
        options.log.level = "trace"
        if OS_TYPE == "posix":
            options.set_preference("browser.download.dir", f"{BASE_DIR}/browser_downloads")
        if OS_TYPE == "nt":
            options.set_preference("browser.download.dir", f"{BASE_DIR}\\browser_downloads")
        options.set_preference("general.useragent.override", "eFind.ru selenium bot")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "application/x-gzip;application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;application/vnd.ms-excel;text/csv;")

        browser = webdriver.Firefox(options=options)
        if btype == "desktop":
            browser.maximize_window()
        elif btype == "mobile":
            browser.set_window_size(400, 880)
        elif btype == "tablet":
            browser.set_window_size(800, 880)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    mylogger("quit browser..")
    if OS_TYPE == "posix":
        display.stop()
    browser.quit()

