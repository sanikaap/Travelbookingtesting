from locust import HttpUser, task, between
from utilities.test_data import TestData

class TravelBookingUser(HttpUser):
    wait_time = between(1, 5)
    
    def on_start(self):
        """Setup data needed for tests"""
        self.search_params = TestData.get_flight_search_params()
        self.booking_data = TestData.get_booking_data()
    
    @task(3)
    def search_flights(self):
        """Simulate flight search"""
        self.client.get("/api/v1/flights/search", 
                       params=self.search_params)
    
    @task(1)
    def create_booking(self):
        """Simulate booking creation"""
        self.client.post("/api/v1/bookings",
                        json=self.booking_data)
    
    @task(2)
    def view_booking(self):
        """Simulate viewing booking details"""
        # Using a static booking ID for simulation
        self.client.get("/api/v1/bookings/BOOK123")
