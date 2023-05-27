from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import undetected_chromedriver as uc
ua = UserAgent()

PRODUCT_URL = "https://store.nvidia.com/en-us/geforce/store/?page=1&limit=9&locale=en-us&gpu=RTX%204090&category=GPU,DESKTOP"


options = Options()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
options.add_argument('user-agent={0}'.format(user_agent))
driver = uc.Chrome()

driver.get(PRODUCT_URL)
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

# nav_to_product_page_btn_selector = "#nv-button-4fb922d15e"

# nav_to_product_page_btn = driver.find_element(
#     By.CSS_SELECTOR, nav_to_product_page_btn_selector)

# nav_to_product_page_btn.click()
