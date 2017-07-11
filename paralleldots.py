import requests
BASE_URL = 'https://apis.paralleldots.com/'
API_KEY = 'uZ8VfRk6e3ER9TgjsHyipqa6H2jFgvCMbgZ39hFVd0U'
input = raw_input('Enter text:')
request_url = BASE_URL + 'sentiment?sentence1=%s&apikey=%s'%(input,API_KEY)
response= requests.get(request_url, verify=False).json()
print response
