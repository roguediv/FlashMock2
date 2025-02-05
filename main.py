# External Libraries
from selenium.webdriver import ActionChains, FirefoxProfile
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from threading import Thread
from multiprocessing import Pool
import os
import pyautogui
import keyboard

# Local Libraries
from random import randrange
from time import sleep

# User Code
from classes.web_driver.driver import *
from classes.pages.square import *

class main():
  webMgr = 0
  squ = 0
  def __init__(self):
    self.webMgr = mgr_web_driver(self)
    self.squ = square(self)

main()