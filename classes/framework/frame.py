from time import sleep
from random import randrange
from selenium.webdriver.common.keys import Keys
import datetime
import time
import pyautogui

class frame:
  # This class manages the interfacing between the program
  # and the website interface so that the code for the rest
  # of the program is more readable and easier to write.
  # This class has two levels:
  #
  # Level 1 functions will utilize try-catch because they
  # deal with direct selenium functions
  #
  # Level 2 functions manage level 1 functions and no longer
  # need to incorperate try-catch blocks
  parent = 0    # Keep track of the parent
  maxPass = 3   # How many times an error can happen before we decide failure
  errSleep = 30 # How long we should wait between failures
  start_time = time.process_time()

  def __init__(self, Parent):
    self.parent = Parent

  def action(self, act, msg="Action"):
    numPass = 0
    passed = False
    rtn = False
    i = 0
    while not passed:
      passed = act()
      rtn = passed
      sleep(1)
      numPass += 1
      if numPass > self.maxPass:
          self.log(msg + " Failed " + str(i) + " Times. Skipping Action...")
          passed = True
      i += 1
    return rtn
    sleep(1)

  def log(self, msg):
    f = open("data/logs/log-" + "app-" + self.parent.name + ".txt", "a")
    f.write(str(datetime.datetime.now().strftime('%H:%M')) + " // " + self.parent.name + " says: " + msg + "\n")
    f.close()

    # Level 1 Commands:

  def btn_click(self, path):
    try:
      self.parent.main.webMgr.driver.find_element_by_xpath(path).click()
      return True
    except:
      return False

  def xpath_typ(self, path, input):
    try:
      # Sends keys to an input xpath, return true if worked
      ipt = self.parent.main.webMgr.driver.find_element_by_xpath(path)
      ipt.clear()
      ipt.send_keys(input, Keys.TAB)
      return True
    except:
      return False

  def is_displayed(self, path):
    try:
      # Check if xpath exists for user, then return true if exists
      if self.parent.main.webMgr.driver.find_element_by_xpath(path).is_displayed():
        return True
      else:
        return False
    except:
      return False

  # Level 2 Commands:
  def clk(self, path, inputName):
    self.action(lambda: self.btn_click(path), inputName)
  def typ(self, path, _input, inputName):
    self.action(lambda: self.xpath_typ(path, _input), inputName)
  def dys(self, path, inputName):
    return self.action(lambda: self.is_displayed(path))
  def count_elm(self, path):
    return len(self.parent.main.webMgr.driver.find_elements_by_class_name(path))

  def typ_slow(self, path, input, error = "An Input"):
    array = list(input)
    for char in array:
      self.action(lambda: self.xpath_typ(path, char), char + ' Key in ' + error)
      sleepTime = randrange(2,10)
      sleep(sleepTime / 10)

  def scroll(self, clicks):
    pyautogui.scroll(clicks)

  def mouse_clk(self, posX, posY):
    pyautogui.moveTo(posX, posY, duration = 1)
    pyautogui.click()

  def keyboard_type(self, _input):
    array = list(_input)
    for char in array:
      self.press_key(char)

  def press_key(self, key):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)