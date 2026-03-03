from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# chrome_options.add_experimental_option("detach",True)
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service,options=options)

driver.get("https://uygulama.kulder.org/Giris")

user_name = driver.find_element(By.NAME,value="kullaniciAdi")
password = driver.find_element(By.NAME,value="sifre")
button = driver.find_element(By.XPATH,value='//*[@id="formKayit"]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[5]/button')

user_name.send_keys("98872013266")
password.send_keys("440442")
driver.execute_script("arguments[0].scrollIntoView(true);", button)
driver.execute_script("arguments[0].click();", button)

wait = WebDriverWait(driver, 20)
basvur = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Başvur")))
# basvur = driver.find_element(By.LINK_TEXT,value="Başvur")
driver.execute_script("arguments[0].scrollIntoView(true);", basvur)
driver.execute_script("arguments[0].click();", basvur)

basvur_success = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"btn-success")))
driver.execute_script("arguments[0].scrollIntoView(true);", basvur_success)
driver.execute_script("arguments[0].click();", basvur_success)

driver.save_screenshot("debug.png")

# time.sleep(6)
driver.close()







