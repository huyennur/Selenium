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

class TestUntitled():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_untitled(self):
    self.driver.get("https://www.facebook.com/")
    self.driver.set_window_size(780, 647)
    self.driver.find_element(By.ID, "email").send_keys("0986307401")
    self.driver.find_element(By.ID, "u_0_c_+/").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".\\_4-u5").text == "Đăng nhập Facebook\\\\nMật khẩu bạn đã nhập không chính xác. Quên mật khẩu?\\\\nĐăng nhập\\\\nQuên mật khẩu?"
  
