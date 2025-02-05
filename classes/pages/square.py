from classes.framework.frame import *
from random import random
import json

from classes.invoice.invoice import *

class square():
  webPage = 'https://squareup.com/us/en'
  # Set variables for later use:
  main = 0              # Keep track of parent
  name = "Square"       # Platform we are using for charges
  mgr = 0               # Keep track of framework code
  info = 0              # Json data
  prevHook = 0          # Keep track of prev customer

  # Variables you may adjust:
  currentHook = 121     # Where to begin pulling customers
  maxHook = 150         # Where to end pulling customers
  dontCrg = ['0', '0']  # List of customer numbers we don't want to charge
  
  def __init__(self, Parent):
    self.main = Parent
    self.mgr = frame(self)
    # Run code to pull JSON data from the database. Redacted for purposes of having this code public. 
    with open() as json_file:
      self.info = json.loads(json_file.read()) # Where decrypted json data and merchant info are loaded from database
    self.signIn()

  def signIn(self):
    # Navigate to the merchant website and sign in
    self.main.webMgr.start_driver(self.webPage)
    self.mgr.clk('//*[@id="735gGmzBRZBLLrnQxBIs8O"]', 'Sign In')
    self.mgr.typ('//*[@id="email"]', self.info['login']['email'], 'Email Address')
    self.mgr.typ('//*[@id="password"]', self.info['login']['password'], 'Password')
    self.mgr.clk('//*[@id="sign-in-button"]', 'sign in')
    sleep(10)
    self.mgr.clk('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/button', 'Enter Info')
    sleep(10)
    while (self.currentHook != self.prevHook):
      # Cycle through all customers in the json data
      # Keep track of current place in charges
      self.prevHook = self.currentHook
      self.hook_loop(self.currentHook)
      if (str(self.currentHook + 1) in self.info['users']):
        self.currentHook += 1
      if (self.currentHook >= self.maxHook):
        self.prevHook = self.currentHook
      sleep(5)
  
  def hook_loop(self, i):
    # Manages interfacing with the website during charges
    print(i)
    if (self.info['users'][str(i)]['userID'] not in self.dontCrg):
      price = '9.95'
      self.mgr.mouse_clk(randrange(762, 1336), randrange(307, 335))
      self.mgr.keyboard_type(price)
      self.mgr.scroll(-10000)
      self.mgr.mouse_clk(randrange(762, 946), randrange(843, 874))
      self.mgr.keyboard_type(self.info['users'][str(i)]['cc'])
      self.mgr.scroll(-10000)
      self.mgr.mouse_clk(randrange(1154, 1336), randrange(844, 874))
      self.mgr.keyboard_type(self.info['users'][str(i)]['exp'])
      self.mgr.mouse_clk(randrange(765, 944), randrange(896, 926))
      self.mgr.keyboard_type(self.info['users'][str(i)]['cvv'])
      self.mgr.mouse_clk(randrange(1154, 1336), randrange(894, 925))
      self.mgr.keyboard_type(self.info['users'][str(i)]['zipcode'])
      self.mgr.mouse_clk(randrange(1814, 1878), randrange(92, 120))
      sleep(5)
      self.mgr.mouse_clk(randrange(900, 1000), randrange(423, 451))
      inv = invoice()
      
      inv.gen_ros('ROS_' + self.info['users'][str(i)]['userID'] + '_', self.info['users'][str(i)]['userID'], self.info['users'][str(i)]['email'], self.info['users'][str(i)]['fname'], self.info['users'][str(i)]['lname'], self.info['users'][str(i)]['address'], self.info['users'][str(i)]['city'], self.info['users'][str(i)]['state'], self.info['users'][str(i)]['zipcode'], price)