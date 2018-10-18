import requests
import xmltodict
import sys

zillow_base_url = 'https://www.zillow.com/webservice/GetSearchResults.htm'

def print_usage():
  print('')
  print('Usage:')
  print('  zws-id        Zillow provided API ID')
  print('  street name   Street name, i.e. Main St')
  print('  city state    City & State, i.e. Scotch Plains NJ')
  print('  range start   Numeric range to start searching')
  print('  range end     Numeric range to end searching')
  print('')
  print('Example:')
  print("  python .\main.py [your_zws_id] 'Church Ave' 'Scotch Plains NJ' 2025 2050")
  print('')
  exit()


def get_zillow_result(zws_id, street_address, city_state):
  url = zillow_base_url
  querystring = {"zws-id":zws_id,"address":street_address,"citystatezip":city_state}

  response = requests.request("GET", url, params=querystring)
  # Uncomment to see full response from Zillow
  # print(response.text)  
  return xmltodict.parse(response.text)

def find_zestimates(range_start, range_end, street, city_state, zws_id):
  for street_number in range(range_start, range_end):
    zillow_result = get_zillow_result(zws_id, str(street_number) + '+' + street, city_state)
    
    if int(zillow_result['SearchResults:searchresults']['message']['code']) == 0:
      if (int(zillow_result['SearchResults:searchresults']['response']['results']['result']['address']['street'].split()[0]) == street_number):
        print('Address: {}  Zestimate: ${:,}'.format(
          str(zillow_result['SearchResults:searchresults']['response']['results']['result']['address']['street']),
          int(zillow_result['SearchResults:searchresults']['response']['results']['result']['zestimate']['amount']['#text'])))  
# main
if len(sys.argv) != 6:
  print_usage()

# ToDo: Validate received command line data
zws_id = sys.argv[1]
street = sys.argv[2].replace(' ','+')
city_state = sys.argv[3].replace(' ','+')
range_start = int(sys.argv[4])
range_end = int(sys.argv[5])

find_zestimates(range_start, range_end, street, city_state, zws_id)
