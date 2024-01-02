import requests


def  MKCallUrl ():
    print ("inside MKCallUrl")
    # api-endpoint
    URL = "http://maps.googleapis.com/maps/api/geocode/json"

    # location given here
    location = "delhi technological university"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address': location}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    # extracting latitude, longitude and formatted address
    # of the first matching location
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    formatted_address = data['results'][0]['formatted_address']

    # printing the output
    return

#localhost
def MKUrlTest2():
    # ..\Apps\Python\Python36>python -m http.server

    print ("inside test 2")
    #URL = "http://www.yahoo.com"
    URL = "http://localhost:8000"
    #PARAMS =
    r = requests.get(url=URL)
    exitCode = r.status_code
    print (exitCode)
    #data = r.json()
    #print (r.json())
    return


# -------------------------- post test
def MKTestPost():
    # importing the requests library
    import requests

    # defining the api-endpoint
    API_ENDPOINT = "http://pastebin.com/api/api_post.php"

    # your API key here
    API_KEY = "06918e479c7b2c3f34f4eaa46beae1e1"

    # your source code here
    source_code = ''' 
    print("Hello, world!") 
    a = 1 
    b = 2 
    print(a + b) 
    '''

    # data to be sent to api
    data = {'api_dev_key': API_KEY,
            'api_option': 'paste',
            'api_paste_code': source_code,
            'api_paste_format': 'python'}

    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text
    pastebin_url = r.text
    print("The pastebin URL is:%s" % pastebin_url)
    return



# -------- test both get & post
def MKTestUrl2 ():
    print ("\n---TESTING GET")
    #simple get
    responseGet = requests.get(url='http://google.com')
    statusCodeGet = responseGet.status_code
    print ("status code=", statusCodeGet)

    # get with params
    payload = {"value": "hello"}
    responseGet = requests.get(url='http://google.com', params=payload)
    statusCodeGet = responseGet.status_code
    print ("status code=", statusCodeGet)

    # get with json
    r = requests.get('https://api.spotify.com/v1/search?type=artist&q=snoop')
    from pprint import pprint
    pprint(r.json())


    # POST some form-encoded data:
    print ("\n--- TESTING POST")
    post_data = {'username': 'joeb', 'password': 'foobar', 'salary': 123}
    responsePost = requests.post(url='http://httpbin.org/post', data=post_data)
    statusCodePost = responsePost.status_code
    print ("status code=", statusCodePost)
    return


# -------- main
print ("hello")
MKTestUrl2()

