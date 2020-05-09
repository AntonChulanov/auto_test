from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import pytest
import time
import math


def test_num1(browser,language):
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    time.sleep(10)
    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    button_find = button.get_attribute("data-loading-text")
    assert button_find is not None , "Нет кнопки" 
