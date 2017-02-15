# GoShort
Google URL Shortener API

# Installation

```bash
$ git clone https://github.com/nurfitriyanto/GoShort.git
```

```bash
$ cd GoShort
```

```bash
$ virtualenv -p pyton3 venv3
```

```bash
$ source venv3/bin/active
```

```bash
$ pip install -r requirements.txt
```

```bash
$ cp config.py.sample config.py
```

```bash
$ nano config.py
```

```bash
#! config.py

URL_API = 'https://www.googleapis.com/urlshortener/v1/url'
KEY_TOKEN = '' #insert your key token
```

```bash
$ python3 run.py
```

# Using

Open your browser

1. Generate your long url.  \n
Example : http://0.0.0.0:5000/longShortUrl?longUrl=https://github.com/nurfitriyanto/GoShort \n
Output : \n
```bash
{
  "id": "https://goo.gl/1wBMcE", 
  "kind": "urlshortener#url", 
  "longUrl": "https://github.com/nurfitriyanto/GoShort"
}
```

2. Generate your short url. \n
Example : http://0.0.0.0:5000/shortLongUrl?shortUrl=https://goo.gl/1wBMcE \n
Output : \n
```bash
{
  "id": "https://goo.gl/1wBMcE", 
  "kind": "urlshortener#url", 
  "longUrl": "https://github.com/nurfitriyanto/GoShort", 
  "status": "OK"
}
```

3. analytics. \n
Example : http://0.0.0.0:5000/analytics?shortUrl=https://goo.gl/1wBMcE \n
Output : \n
```bash
{
  "analytics": {
    "allTime": {
      "browsers": [
        {
          "count": "2", 
          "id": "Chrome"
        }
      ], 
      "countries": [
        {
          "count": "1", 
          "id": "ID"
        }
      ], 
      "longUrlClicks": "2", 
      "platforms": [
        {
          "count": "1", 
          "id": "Windows"
        }, 
        {
          "count": "1", 
          "id": "X11"
        }
      ], 
      "referrers": [
        {
          "count": "1", 
          "id": "unknown"
        }, 
        {
          "count": "1", 
          "id": "www.google.com"
        }
      ], 
      "shortUrlClicks": "2"
    }, 
    "day": {
      "browsers": [
        {
          "count": "2", 
          "id": "Chrome"
        }
      ], 
      "countries": [
        {
          "count": "1", 
          "id": "ID"
        }
      ], 
      "longUrlClicks": "2", 
      "platforms": [
        {
          "count": "1", 
          "id": "Windows"
        }, 
        {
          "count": "1", 
          "id": "X11"
        }
      ], 
      "referrers": [
        {
          "count": "1", 
          "id": "unknown"
        }, 
        {
          "count": "1", 
          "id": "www.google.com"
        }
      ], 
      "shortUrlClicks": "2"
    }, 
    "month": {
      "browsers": [
        {
          "count": "2", 
          "id": "Chrome"
        }
      ], 
      "countries": [
        {
          "count": "1", 
          "id": "ID"
        }
      ], 
      "longUrlClicks": "2", 
      "platforms": [
        {
          "count": "1", 
          "id": "Windows"
        }, 
        {
          "count": "1", 
          "id": "X11"
        }
      ], 
      "referrers": [
        {
          "count": "1", 
          "id": "unknown"
        }, 
        {
          "count": "1", 
          "id": "www.google.com"
        }
      ], 
      "shortUrlClicks": "2"
    }, 
    "twoHours": {
      "browsers": [
        {
          "count": "2", 
          "id": "Chrome"
        }
      ], 
      "countries": [
        {
          "count": "1", 
          "id": "ID"
        }
      ], 
      "longUrlClicks": "2", 
      "platforms": [
        {
          "count": "1", 
          "id": "Windows"
        }, 
        {
          "count": "1", 
          "id": "X11"
        }
      ], 
      "referrers": [
        {
          "count": "1", 
          "id": "unknown"
        }, 
        {
          "count": "1", 
          "id": "www.google.com"
        }
      ], 
      "shortUrlClicks": "2"
    }, 
    "week": {
      "browsers": [
        {
          "count": "2", 
          "id": "Chrome"
        }
      ], 
      "countries": [
        {
          "count": "1", 
          "id": "ID"
        }
      ], 
      "longUrlClicks": "2", 
      "platforms": [
        {
          "count": "1", 
          "id": "Windows"
        }, 
        {
          "count": "1", 
          "id": "X11"
        }
      ], 
      "referrers": [
        {
          "count": "1", 
          "id": "unknown"
        }, 
        {
          "count": "1", 
          "id": "www.google.com"
        }
      ], 
      "shortUrlClicks": "2"
    }
  }, 
  "created": "2017-02-15T08:07:41.027+00:00", 
  "id": "https://goo.gl/1wBMcE", 
  "kind": "urlshortener#url", 
  "longUrl": "https://github.com/nurfitriyanto/GoShort", 
  "status": "OK"
}
```
