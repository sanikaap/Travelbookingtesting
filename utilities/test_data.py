import json
import os
from datetime import datetime, timedelta

class TestData:
    @staticmethod
    def get_flight_search_params():
        """Get test data for flight search"""
        return {
            "origin": "NYC",
            "destination": "LAX",
            "departure_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "return_date": (datetime.now() + timedelta(days=37)).strftime("%Y-%m-%d"),
            "passengers": 1
        }
    
    @staticmethod
    def get_booking_data():
        """Get test data for booking creation"""
        return {
            "flight_id": "FL123",
            "passenger": {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com"
            },
            "payment": {
                "card_number": "4111111111111111",
                "expiry_date": "12/25",
                "cvv": "123"
            }
        }
    
    @staticmethod
    def get_flight_booking_data():
        """Get test data for UI booking flow"""
        return {
            "origin": "NYC",
            "destination": "LAX",
            "departure_date": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d"),
            "return_date": (datetime.now() + timedelta(days=37)).strftime("%Y-%m-%d"),
            "passenger_first_name": "John",
            "passenger_last_name": "Doe",
            "passenger_email": "john.doe@example.com",
            "card_number": "4111111111111111",
            "expiry_date": "12/25",
            "cvv": "123"
        }
