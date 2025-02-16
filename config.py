# Environment URLs
DEV_URL = "https://dev.travelbooking.com"
STAGING_URL = "https://staging.travelbooking.com"
PROD_URL = "https://travelbooking.com"

# API URLs
DEV_API_URL = "https://api.dev.travelbooking.com"
STAGING_API_URL = "https://api.staging.travelbooking.com"
PROD_API_URL = "https://api.travelbooking.com"

# Test Data
TEST_USER = {
    "email": "test@example.com",
    "password": "Test123!"
}

# Timeouts
EXPLICIT_WAIT = 10
IMPLICIT_WAIT = 5

# Browser Settings
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--headless"
]

# API Endpoints
ENDPOINTS = {
    "search_flights": "/api/v1/flights/search",
    "book_flight": "/api/v1/bookings",
    "get_booking": "/api/v1/bookings/{booking_id}"
}
