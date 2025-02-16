import pytest
from page_objects.search_page import SearchPage
from utilities.test_data import TestData

class TestSearchFlights:
    
    @pytest.mark.ui
    def test_search_one_way_flight(self, driver, logger):
        """Test one-way flight search functionality"""
        search_page = SearchPage(driver)
        test_data = TestData.get_flight_search_params()
        
        logger.info("Starting one-way flight search test")
        
        search_page.select_one_way_trip()
        search_page.enter_origin(test_data["origin"])
        search_page.enter_destination(test_data["destination"])
        search_page.enter_departure_date(test_data["departure_date"])
        search_page.click_search()
        
        assert search_page.are_search_results_displayed()
        assert search_page.get_search_results_count() > 0
        logger.info("One-way flight search test completed successfully")

    @pytest.mark.ui
    def test_search_round_trip_flight(self, driver, logger):
        """Test round-trip flight search functionality"""
        search_page = SearchPage(driver)
        test_data = TestData.get_flight_search_params()
        
        logger.info("Starting round-trip flight search test")
        
        search_page.select_round_trip()
        search_page.enter_origin(test_data["origin"])
        search_page.enter_destination(test_data["destination"])
        search_page.enter_dates(test_data["departure_date"], 
                              test_data["return_date"])
        search_page.set_passenger_count(test_data["passengers"])
        search_page.click_search()
        
        assert search_page.are_search_results_displayed()
        assert search_page.get_search_results_count() > 0
        logger.info("Round-trip flight search test completed successfully")

    @pytest.mark.ui
    def test_invalid_search_criteria(self, driver, logger):
        """Test search validation for invalid criteria"""
        search_page = SearchPage(driver)
        
        logger.info("Starting invalid search criteria test")
        
        search_page.enter_origin("XXX")  # Invalid airport code
        search_page.enter_destination("YYY")  # Invalid airport code
        search_page.click_search()
        
        assert search_page.is_error_message_displayed()
        logger.info("Invalid search criteria test completed successfully")

    @pytest.mark.ui
    def test_search_filters(self, driver, logger):
        """Test search results filtering"""
        search_page = SearchPage(driver)
        test_data = TestData.get_flight_search_params()
        
        logger.info("Starting search filters test")
        
        search_page.enter_origin(test_data["origin"])
        search_page.enter_destination(test_data["destination"])
        search_page.enter_departure_date(test_data["departure_date"])
        search_page.click_search()
        
        initial_results = search_page.get_search_results_count()
        search_page.apply_price_filter(max_price=500)
        filtered_results = search_page.get_search_results_count()
        
        assert filtered_results <= initial_results
        logger.info("Search filters test completed successfully")
