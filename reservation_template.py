import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options = Options()

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option('prefs', {
    'credentials_enable_service': False,
    'profile': {
        'password_manager_enabled': False
    }
})
s = Service('C:\\Windows\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

wait = WebDriverWait(driver, 30)

stealth(driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
)


#CLAIM RESERVATION

#change name, date, size, time
name = "NAME"

month = "MONTH (2 digit)"

day = "DAY (2 digit)"

size = "SIZE"

timeorig = "TIME (military)"

picktime = timeorig.replace(":","%3A")

url = "https://www.exploretock.com/" + name + "/search?date=2022-" + month + "-" + day + "&size=" + size + "&time=" + picktime

t = datetime.datetime.today()
#change time to reserve
#military time hour
acthour =  0 
future = datetime.datetime(t.year,t.month,t.day,acthour,0,1)
time.sleep((future-t).total_seconds())

driver.get(url)

time.sleep(0.5)

#change reservation name and time
resname = 'KEYWORD'
restime = 'TIME PM'
res = driver.find_element(By.XPATH, "//div[@class='SearchModalExperiences-item Consumer-reservation' and .//h2[contains(.,resname)]]//button[./span[contains(.,restime)]]")

res.click()


#OPTIONAL: CONFIRM RESERVATION


#login = driver.find_element(By.XPATH, "//*[@id='#maincontent']/div/div[1]/div/div/div/div/div[2]/div[3]/span/button")

#login.click()

#user = driver.find_element(By.ID, "email")

email = "EMAIL"

#user.send_keys(email)

#pas = driver.find_element(By.ID, "password")

password = "PASSWORD"

#pas.send_keys(password)

#pas.submit()

#time.sleep(4)

#final = driver.find_element(By.XPATH, "//button[./span[contains(.,'Complete reservation')]]")

#final.click()