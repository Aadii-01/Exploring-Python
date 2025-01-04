import requests
from datetime import datetime

my_lat = 87.854481
my_long = 34.589310
sunrset = "https://api.sunrise-sunset.org/json"

"""
ord = {
    "lat (float)": "Latitude in decimal degrees. Required.",
    "lng (float)": "Longitude in decimal degrees. Required.",
    "date (string)": "Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. If not present, date defaults to current date. Optional.",
    "callback (string)": "Callback function name for JSONP response. Optional.",
    "formatted (integer)": "0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and day_length will be expressed in seconds. Optional.",
    "tzid (string)": "A timezone identifier, like for example: UTC, Africa/Lagos, Asia/Hong_Kong, or Europe/Lisbon. The list of valid identifiers is available in this List of Supported Timezones. If provided, the times in the response will be referenced to the given Time Zone. Optional.",
}
"""

parameters={
    "lat" : my_lat,
    "lng" : my_long,
    "formatted" : 0,
}

response = requests.get(url= sunrset_url, params = parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
now = datetime.now()
print(now)