from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
import creds
PRODUCT_URL = "https://store.nvidia.com/en-us/geforce/store/?page=1&limit=9&locale=en-us&gpu=RTX%204090&category=GPU,DESKTOP"


options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options.add_argument('user-agent={0}'.format(user_agent))
driver = uc.Chrome()
driver.get(PRODUCT_URL)

out_of_stock_selector = "div.buy.cta-preorder.mobile-top.link-btn-disabled"

SMTP_HOST: str = "smtp.gmail.com"
SMTP_PORT: int = 587

smtp_obj = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(creds.gmail_username, creds.gmail_pw)


try:
    out_of_stock_div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, out_of_stock_selector)))
    smtp_obj.sendmail("jmwebb.dev@gmail.com", "jmwebb.personal@gmail.com",
                      "Subject: [Sniper 4090]: No 4090s in stock.\n Sorry :( will try again tomorrow")
    print("Found out-of-stock indicator element.")
except NoSuchElementException:
    smtp_obj.sendmail("jmwebb.dev@gmail.com", "jmwebb.personal@gmail.com",
                      "Subject: [Sniper 4090]: 4090 in stock!!.\n Check here: https://store.nvidia.com/en-us/geforce/store/?page=1&limit=9&locale=en-us&gpu=RTX%204090&category=GPU,DESKTOP")
    print("Unable to find out-of-stock indicator.")
finally:
    smtp_obj.quit()
