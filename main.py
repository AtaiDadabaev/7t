from conftest import *
from page_objects.main_page import main_page
from page_objects.product_page import product_page
import time

def test_6(driver):
    time.sleep(2)
    main_page(driver).click(main_page.macbook)
    main_page(driver).click(product_page.fav_button)
    
def test_7(driver):
    time.sleep(2)
    main_page(driver).click(main_page.macbook)
    main_page(driver).click(product_page.button_cart)

def test_8(driver):
    time.sleep(2)
    main_page(driver).click(main_page.droptablet)
    main_page(driver).click(main_page.samsung)
    main_page(driver).click(product_page.button_cart)


def test_9(driver):
    time.sleep(2)
    main_page(driver).click(main_page.droptelephone)
    main_page(driver).click(main_page.iphone)
    main_page(driver).click(product_page.button_cart)


def test_10(driver):
    time.sleep(2)
    main_page(driver).click(main_page.macbook)
    product_page(driver).click(product_page.review)
    product_page(driver).write(product_page.input_name, "name")
    product_page(driver).write(product_page.input_review, "review review review review review review")
    product_page(driver).click(product_page.mark)
    product_page(driver).click(product_page.button_review)