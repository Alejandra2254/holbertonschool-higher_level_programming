# 0x11. Python - Network #1
General 
## How to fetch internet resources with the Python package urllib
The simplest way to use urllib.request is as follows:
```
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
html = response.read()
```
To store it in a temporary location
```
import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass
```
## How to decode urllib body response
```
 with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()
        print('Body response:$')
        print('   - type: {}'.format(type(body)))
        print('   - content: {}'.format(body))
        print('   - utf8 content: {}'.format(body.decode('utf-8')))
```
## How to use the Python package requests #requestsiswaysimplerthanurllib
```
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"type":"User"...'
>>> r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```
## How to make HTTP GET request
* If you do not pass the data argument, urllib uses a GET request. One way in which GET and POST requests differ is that POST requests often have “side-effects”: they change the state of the system in some way 
```
>>> import urllib.request
>>> import urllib.parse
>>> data = {}
>>> data['name'] = 'Somebody Here'
>>> data['location'] = 'Northampton'
>>> data['language'] = 'Python'
>>> url_values = urllib.parse.urlencode(data)
>>> print(url_values)  # The order may differ from below.  
name=Somebody+Here&language=Python&location=Northampton
>>> url = 'http://www.example.com/example.cgi'
>>> full_url = url + '?' + url_values
>>> data = urllib.request.urlopen(full_url)
```
## How to make HTTP POST/PUT/etc. request
* Sometimes you want to send data to a URL. With HTTP, this is often done using what’s known as a POST request.
```
import urllib.parse
import urllib.request

url = 'http://www.someserver.com/cgi-bin/register.cgi'
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values)
data = data.encode('ascii') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
```
## How to fetch JSON resources
## How to manipulate data from an external service