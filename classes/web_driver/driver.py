from selenium.webdriver import ActionChains, FirefoxProfile
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class mgr_web_driver():
  main = 0
  driver = 0
  def __init__(self, Parent):
    self.main = Parent

  def start_driver(self, website):
    self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    self.driver.get(website)