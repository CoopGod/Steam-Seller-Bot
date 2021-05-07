# path to sell at use current price of item
# SS AUTOBOT
# -----------------------------------------------
from selenium import webdriver
from time import sleep

# Gather user info:
steamUser = input("Steam Username: ")
steamPass = input("Steam Password: ")
selection = int(input("How many cards do you want to sell?: "))


# Load page and begin loop to sell all cards
class SteamBot:
    def __init__(self, user, password):
        # chromeDriver to open site:
        self.driver = webdriver.Chrome()
        self.driver.get("https://steamcommunity.com/login/home/")
        self.driver.implicitly_wait(15)
        # Login Page
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div["
                                          "1]/div/div/div/div/form/div[1]/input") \
            .send_keys(user)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div["
                                          "1]/div/div/div/div/form/div[2]/input") \
            .send_keys(password)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div/div[1]/div/div/div/div/div["
                                          "3]/div[1]/button/span") \
            .click()
        sleep(1)
        # Steam Guard
        steamAuth = input("Steam Guard Code: ")
        self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[3]/div[1]/div/input") \
            .send_keys(steamAuth)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/div[1]/div[1]/div[1]") \
            .click()
        # Main account page
        self.driver.find_element_by_xpath("//span[contains(text(),'Inventory')]") \
            .click()
        # Inventory page
        self.driver.find_element_by_xpath("//*[@id='inventory_link_753']/span[2]") \
            .click()
        sleep(5)

        self.sell_card(False)

        # Continue to sell cards
        count = 1
        while count < selection:
            self.sell_card(True)
            count += 1

        print(f"You sold {selection} cards!")
        sleep(8)

    # Loop To sell cards
    def sell_card(self, item_box_checked):
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[7]/div[2]/div[1]/div[2]/div/div[5]/div[4]/div["
                                          "3]/div[1]/span") \
            .click()
        sleep(2)
        # Advanced Options Menu
        self.driver.find_element_by_xpath("//*[@id='tag_filter_753_0_misc_marketable']") \
            .click()
        self.driver.find_element_by_xpath("//input[@id='tag_filter_753_0_item_class_item_class_2']") \
            .click()
        # Select first card
        self.driver.find_element_by_xpath("//body/div[1]/div[7]/div[2]/div[1]/div[2]/div[1]/div[5]/div["
                                          "9]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/a[1]") \
            .click()
        sleep(2)
        # Copy starting price
        startingPrice = self.driver.find_elements_by_xpath('//*[@id="iteminfo0_item_market_actions"]/div/div[2]')
        # Get starting value
        priceRaw = startingPrice[0].get_attribute('innerHTML')
        priceRawArray = priceRaw.split(' ')
        priceRawArray2 = priceRawArray[3].split('<br>')
        price = priceRawArray2[0]

        # Sell Cards button
        self.driver.find_element_by_xpath('//*[@id="iteminfo0_item_market_actions"]/a/span[2]') \
            .click()
        sleep(2)
        # Type in starting price
        self.driver.find_element_by_xpath("//*[@id='market_sell_buyercurrency_input']") \
            .send_keys(price)
        sleep(2)
        # Click terms checkbox
        if not item_box_checked:
            self.driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div[2]/div[4]/div[1]/div[3]/div/input") \
                .click()
            sleep(2)
        # Click sell button
        self.driver.find_element_by_xpath("//*[@id='market_sell_dialog_accept']/span") \
            .click()
        sleep(2)
        # Click accept
        self.driver.find_element_by_xpath("//*[@id='market_sell_dialog_ok']/span") \
            .click()


SteamBot(steamUser, steamPass)
