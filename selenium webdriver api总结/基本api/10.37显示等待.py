#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Ie(executable_path = "e:\\IEDriverServer")
driver.get("http://www.sogou.com

")
input_box=driver.find_element_by_id("query")
wait = WebDriverWait(driver, 10, 0.2)
wait.until(EC.visibility_of(input_box))
input_box.send_keys(u"光荣之路")
wait.until(EC.element_to_be_clickable((By.ID ,"stb")))
button=driver.find_element_by_id("stb")
button.click()

time.sleep(3)

driver.close()
