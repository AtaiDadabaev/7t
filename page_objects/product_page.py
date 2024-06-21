from page_objects.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class product_page(base_page):
    button_cart = (By.CSS_SELECTOR, "#button-cart")
    fav_button = (By.CSS_SELECTOR, "div.btn-group:nth-child(1) > button.btn.btn-default:nth-child(1)")

    review = (By.PARTIAL_LINK_TEXT, "Отзывов (")
    input_name = (By.CSS_SELECTOR, "#input-name")
    input_review = (By.CSS_SELECTOR, "#input-review")
    mark = (By.CSS_SELECTOR, "input:nth-child(5)")
    button_review = (By.CSS_SELECTOR, "#button-review")