from selenium.webdriver.common.by import By
from .base_page import BasePage

class BookingPage(BasePage):
    # Locators
    FIRST_NAME_INPUT = (By.ID, "passenger-first-name")
    LAST_NAME_INPUT = (By.ID, "passenger-last-name")
    EMAIL_INPUT = (By.ID, "passenger-email")
    CARD_NUMBER_INPUT = (By.ID, "card-number")
    EXPIRY_DATE_INPUT = (By.ID, "expiry-date")
    CVV_INPUT = (By.ID, "cvv")
    COMPLETE_BOOKING_BTN = (By.ID, "complete-booking")
    BOOKING_REFERENCE = (By.CLASS_NAME, "booking-reference")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    def enter_passenger_details(self, first_name, last_name, email):
        """Enter passenger details in the booking form"""
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_INPUT, email)
    
    def enter_payment_details(self, card_number, expiry_date, cvv):
        """Enter payment details in the booking form"""
        self.enter_text(self.CARD_NUMBER_INPUT, card_number)
        self.enter_text(self.EXPIRY_DATE_INPUT, expiry_date)
        self.enter_text(self.CVV_INPUT, cvv)
    
    def complete_booking(self):
        """Complete the booking process and return booking reference"""
        self.click_element(self.COMPLETE_BOOKING_BTN)
        return self.get_text(self.BOOKING_REFERENCE)
    
    def is_error_displayed(self):
        """Check if error message is displayed"""
        try:
            return self.find_element(self.ERROR_MESSAGE).is_displayed()
        except:
            return False
    
    def get_error_message(self):
        """Get the error message text"""
        return self.get_text(self.ERROR_MESSAGE)
