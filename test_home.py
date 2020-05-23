# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestHome():
  def setup_method(self, method):
    self.driver = webdriver.Firefox(executable_path='D:\\Documentos\\Esp_Ing_Software\\Pruebas_Softw\\Selenium\\path\\geckodriver')
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_home(self):
    # Test name: home
    # Step # | name | target | value
    # 1 | open | /home | 
    self.driver.get("http://localhost:4200/home")
    # 2 | setWindowSize | 1040x754 | 
    self.driver.set_window_size(1040, 754)
    # 3 | click | id=name | 
    self.driver.find_element(By.ID, "name").click()
    # 4 | type | id=name | carolina
    self.driver.find_element(By.ID, "name").send_keys("carolina")
    # 5 | type | id=apellido | camacho
    self.driver.find_element(By.ID, "apellido").send_keys("camacho")
    # 6 | click | id=cedula | 
    self.driver.find_element(By.ID, "cedula").click()
    # 7 | type | id=cedula | 1245699
    self.driver.find_element(By.ID, "cedula").send_keys("1245699")
    # 8 | type | id=edad | 81
    self.driver.find_element(By.ID, "edad").send_keys("81")
    # 9 | click | id=paisOrigenSelect | 
    self.driver.find_element(By.ID, "paisOrigenSelect").click()
    # 10 | select | id=paisOrigenSelect | label=Colombia
    dropdown = self.driver.find_element(By.ID, "paisOrigenSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
    # 11 | click | css=#paisOrigenSelect > option:nth-child(47) | 
    self.driver.find_element(By.CSS_SELECTOR, "#paisOrigenSelect > option:nth-child(47)").click()
    # 12 | click | id=aeroOrigenSelect | 
    self.driver.find_element(By.ID, "aeroOrigenSelect").click()
    # 13 | select | id=aeroOrigenSelect | label=Cali - CLO - Alfonso Bonilla Aragon International Airport
    dropdown = self.driver.find_element(By.ID, "aeroOrigenSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Cali - CLO - Alfonso Bonilla Aragon International Airport']").click()
    # 14 | click | css=#aeroOrigenSelect > option:nth-child(13) | 
    self.driver.find_element(By.CSS_SELECTOR, "#aeroOrigenSelect > option:nth-child(13)").click()
    # sscroll down
    self.driver.execute_script("window.scrollTo(0,500)") 
    # 15 | click | id=paisDestinoSelect | 
    self.driver.find_element(By.ID, "paisDestinoSelect").click()
    # 16 | select | id=paisDestinoSelect | label=Colombia
    dropdown = self.driver.find_element(By.ID, "paisDestinoSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
    # 17 | click | css=#paisDestinoSelect > option:nth-child(47) | 
    self.driver.find_element(By.CSS_SELECTOR, "#paisDestinoSelect > option:nth-child(47)").click()
    # 18 | click | id=aeroDestinoSelect | 
    self.driver.find_element(By.ID, "aeroDestinoSelect").click()
    # 19 | select | id=aeroDestinoSelect | label=Medellin - EOH - Enrique Olaya Herrera Airport
    dropdown = self.driver.find_element(By.ID, "aeroDestinoSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Medellin - EOH - Enrique Olaya Herrera Airport']").click()
    # 20 | click | css=#aeroDestinoSelect > option:nth-child(40) | 
    self.driver.find_element(By.CSS_SELECTOR, "#aeroDestinoSelect > option:nth-child(40)").click()
    # 21 | click | id=aeroDestinoSelect | 
    self.driver.find_element(By.ID, "aeroDestinoSelect").click()
    # 22 | mouseDownAt | id=formControlRange | 322.6499938964844,12.183349609375
    element = self.driver.find_element(By.ID, "formControlRange")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 23 | mouseMoveAt | id=formControlRange | 322.6499938964844,12.183349609375
    element = self.driver.find_element(By.ID, "formControlRange")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 24 | mouseUpAt | id=formControlRange | 322.6499938964844,12.183349609375
    element = self.driver.find_element(By.ID, "formControlRange")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 25 | type | id=formControlRange | 352
    self.driver.find_element(By.ID, "formControlRange").send_keys("352")
    # 26 | click | id=formControlRange | 
    self.driver.find_element(By.ID, "formControlRange").click()
    # 27 | type | id=formControlRange | 393
    self.driver.find_element(By.ID, "formControlRange").send_keys("393")
    # 28 | click | id=formControlRange | 
    self.driver.find_element(By.ID, "formControlRange").click()
    # 29 | type | id=formControlRange | 460
    self.driver.find_element(By.ID, "formControlRange").send_keys("460")
    # 30 | click | id=formControlRange | 
    self.driver.find_element(By.ID, "formControlRange").click()
    # 31 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 32 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
