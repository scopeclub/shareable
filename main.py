from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.page_load_strategy = 'eager'
#options.add_argument("--headless=new")
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
service = ChromeService("./chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service,options=options)

driver.get("https://toffeeshare.com/")
time.sleep(2)
upload=driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys("D:\ch.premchand\work\qr_code\ECE2020-24_32.xlsx")
driver.maximize_window()
time.sleep(10)