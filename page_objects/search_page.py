from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    # Locators
    ORIGIN_INPUT = (By.ID, "origin")
    DESTINATION_INPUT = (By.ID, "destination")
    DEPARTURE_DATE_INPUT = (By.ID, "departure-date")
    RETURN_DATE_INPUT = (By.ID, "return-date")
    SEARCH_BUTTON = (By.ID, "search-flights")
    ONE_WAY_RADIO = (By.ID, "one-way")
    ROUND_TRIP_RADIO = (By.ID, "round-trip")
    PASSENGER_COUNT = (By.ID, "passenger-count")
    SEARCH_RESULTS = (By.CLASS_NAME, "search-results")
    FLIGHT_ITEMS = (By.CLASS_NAME, "flight-item")
    PRICE_FILTER = (By.ID, "price-filter")
    ERROR_MESSAGE = (By.CLASS_NAME, "search-error")
    
    def enter_origin(self, origin):
        """Enter origin airport"""
        self.enter_text(self.ORIGIN_INPUT, origin)
    
    def enter_destination(self, destination):
        """Enter destination airport"""
        self.enter_text(self.DESTINATION_INPUT, destination)
    
    def enter_dates(self, departure_date, return_date=None):
        """Enter flight dates"""
        self.enter_text(self.DEPARTURE_DATE_INPUT, departure_date)
        if return_date:
            self.enter_text(self.RETURN_DATE_INPUT, return_date)
    
    def enter_departure_date(self, departure_date):
        """Enter departure date only"""
        self.enter_text(self.DEPARTURE_DATE_INPUT, departure_date)
    
    def select_one_way_trip(self):
        """Select one-way trip option"""
        self.click_element(self.ONE_WAY_RADIO)
    
    def select_round_trip(self):
        """Select round trip option"""
        self.click_element(self.ROUND_TRIP_RADIO)
    
    def set_passenger_count(self, count):
        """Set number of passengers"""
        self.enter_text(self.PASSENGER_COUNT, str(count))
    
    def click_search(self):
        """Click search button"""
        self.click_element(self.SEARCH_BUTTON)
    
    def are_search_results_displayed(self):
        """Check if search results are displayed"""
        try:
            return self.find_element(self.SEARCH_RESULTS).is_displayed()
        except:
            return False
    
    def get_search_results_count(self):
        """Get number of search results"""
        results = self.driver.find_elements(*self.FLIGHT_ITEMS)
        return len(results)
    
    def select_first_available_flight(self):
        """Select the first available flight from results"""
        flights = self.driver.find_elements(*self.FLIGHT_ITEMS)
        if flights:
            flights[0].click()
    
    def apply_price_filter(self, max_price):
        """Apply price filter to search results"""
        price_filter = self.find_element(self.PRICE_FILTER)
        self.driver.execute_script(
            f"arguments[0].value = {max_price};", price_filter
        )
        price_filter.click()
    
    def is_error_message_displayed(self):
        """Check if error message is displayed"""
        try:
            return self.find_element(self.ERROR_MESSAGE).is_displayed()
        except:
            return False
