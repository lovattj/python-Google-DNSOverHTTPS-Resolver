## DNS over HTTPS resolver for Python using Google DNS

**Requirements**  
Requests library (https://2.python-requests.org/en/master/)

**How to use**  
If you just want a quick A record:  
```
import dnsOverHttps
try:
  aRecord = dnsOverHttps.GoogleDNSQuery.getARecordFor("google.com")
  print(a)
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e)
```

**Example**  
See and run `example.py`
