from locators.main_page_locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):

    def open_base_url(self):
        self.go_to(self.base_url)

    def click_on_profile_button(self):
        self.wait_for_element_to_be_visible(MainPageLocators.PROFILE_BUTTON)
        self.click_on_element(*MainPageLocators.PROFILE_BUTTON)
 
    def get_login_to_account_button_text(self):
        return self.driver.find_element(*MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON).text
    
    def get_ingredients_details_text(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENTS_DETAILS).text

    def get_counter_of_fluorescent_bun(self):
        return self.driver.find_element(*MainPageLocators.COUNTER_OF_FLUORESCENT_BUN).get_attribute('innerText')

    def get_order_id_title_text(self):
        return self.driver.find_element(*MainPageLocators.ORDER_ID_TITLE).text
