
EMAIL = "miemailregistradoenholded@proveedor.com"
PASSWORD ="mi jaca galopa y corta el viento"
CHROMEDRIVERPATH = "/usr/bin/chromedriver"
HOLDEDURL = "https://app.holded.com/tp/xxxxxxxxxxxxxxxxxx"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import sys, datetime, time, random
action= sys.argv[1]

if action!="in" and action!="out":
    print("O in o out, garrulo de schrodinger")
    exit(1)


class HoldedDriver:

  def __init__(self):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    self.driver = webdriver.Chrome(CHROMEDRIVERPATH, chrome_options=chrome_options)
    self.wait = WebDriverWait(self.driver, 10)
    self.driver.get(HOLDEDURL)
    email = self.driver.find_element_by_id("tpemail")
    password = self.driver.find_element_by_id("tppassword")
    form = self.driver.find_element_by_id("tp_signin")
    email.send_keys(EMAIL)
    password.send_keys(PASSWORD)
    form.submit()

  def clock(self,action):
    self.driver.get("https://app.holded.com/tp/dashboard")
    self.wait.until(lambda x: self.driver.find_element_by_class_name("btnclock"+action) )
    clock = self.driver.find_element_by_class_name("btnclock"+action)
    clock.click()

  def check_im_on_holiday(self):
    today = datetime.date.today()
    self.driver.get("https://app.holded.com/tp/timeoff")
    self.wait.until(lambda x: self.driver.find_element_by_class_name("hcalendar-day") )
    days = [str(el.text) for el in self.driver.find_elements_by_css_selector("div[data-monthnum='{}'] .hcalendar-day[data-timeoffid]".format(today.month-1))]
    return today.day in days


holded = HoldedDriver()
if not holded.check_im_on_holiday():
    # Para no fichar siempre a la misma hora, esperamos entre 0 y 10 minutos
    r = int(random.random() * 600.0 )
    print(r)
    time.sleep(r)
    holded.clock(action)
