# ZillowAPIExamples

Using your personal Zillow API Key, queries the API for a range of street numbers on provided street in provided city and state and returns all valid addresses with their current Zestimate.

Example Usage:
  python .\main.py [your_zws_id] 'Church Ave' 'Scotch Plains NJ' 2025 2050

Just meant to be an example of how to get API Result from Zillow and process information.  Obviously other data elements present, incl lat/lon coordinates, etc.

Left to the programmer to do more with this code and have fun with it

# Zillow API Notes
https://www.zillow.com/howto/api/APIOverview.htm

## Note
You are limited to 1000 API calls per day with the free unverified token
This code uses ranges, you can easily blow through your API Limit in a single run of this code

Look at the code, if you run a range of 1000 address, it will only return those with valid addresses/results, but it will have made 1000 API calls!
