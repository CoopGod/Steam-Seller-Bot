# Steam Seller Bot
# -----------------------------------------------
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.remote_connection import LOGGER
import logging
from time import sleep

# Gather user info:
selection = int(input("How many cards do you want to sell?: "))


# Load page and begin loop to sell all cards
class SteamBot:
    def __init__(self):
        # chromeDriver to open site:
        self.driver = webdriver.Chrome()
        self.driver.get("https://steamcommunity.com/login/home/")

        # wait until user has opened the inventory
        print("Please Enter your information and Navigate to the Steam Inventory page.")
        WebDriverWait(self.driver, 60).until(expected_conditions.title_contains("Inventory"))

        # main loop
        self.sell_card(False) # run once to check terms box
        count = 1
        while count < selection:
            self.sell_card(True)
            count += 1

        # end credits
        print(f"You sold {selection} cards!")
        print("Made by CoopGod --> github.com/coopgod")
        sleep(8)

    # Loop To sell cards
    def sell_card(self, item_box_checked):
        sleep(2)
        # Steam catagory header
        self.driver.find_element_by_xpath('//*[@id="inventory_link_753"]/span[3]').click()
        # Advanced Options Menu Button
        self.driver.find_element_by_xpath('//*[@id="filter_tag_show"]/span').click()
        sleep(1)
        # Advanced Options Menu
        self.driver.find_element_by_xpath("//*[@id='tag_filter_753_0_misc_marketable']") \
            .click()
        self.driver.find_element_by_xpath("//input[@id='tag_filter_753_0_item_class_item_class_2']") \
            .click()
        # Select first card
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[9]/div[2]/div[1]/div[1]/div[1]/div[3]/div/a") \
            .click()
        sleep(2)
        # Copy starting price
        startingPrice = self.driver.find_elements_by_xpath('//*[@id="iteminfo1_item_market_actions"]/div/div[2]')[0].text
        # Get starting value
        priceRawArray = startingPrice.split(' ')
        priceToSell = priceRawArray[3].split('V')[0]
        print(f"Selling for ${priceToSell}")
        sleep(0.5)
        # Sell Cards button
        self.driver.find_element_by_xpath('//*[@id="iteminfo1_item_market_actions"]/a/span[2]') \
            .click()
        sleep(2)
        # Type in starting price
        self.driver.find_element_by_xpath("//*[@id='market_sell_buyercurrency_input']") \
            .send_keys(priceToSell)
        sleep(2)
        # Click terms checkbox
        if not item_box_checked:
            self.driver.find_element_by_xpath('//*[@id="market_sell_dialog_accept_ssa"]').click()
            sleep(2)
        # Click sell button
        self.driver.find_element_by_xpath("//*[@id='market_sell_dialog_accept']/span") \
            .click()
        sleep(2)
        # Click accept
        self.driver.find_element_by_xpath("//*[@id='market_sell_dialog_ok']/span") \
            .click()


SteamBot()
