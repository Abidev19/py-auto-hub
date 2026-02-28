from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://uygulama.kulder.org/Giris")

user_name = driver.find_element(By.NAME,value="kullaniciAdi")
password = driver.find_element(By.NAME,value="sifre")
button = driver.find_element(By.XPATH,value='//*[@id="formKayit"]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div[5]/button')

user_name.send_keys("98872013266")
password.send_keys("440442")
button.click()

wait = WebDriverWait(driver, 10)
basvur = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Başvur")))
# basvur = driver.find_element(By.LINK_TEXT,value="Başvur")
basvur.click()

basvur_success = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"btn-success")))
basvur_success.click()

# time.sleep(6)
driver.close()
