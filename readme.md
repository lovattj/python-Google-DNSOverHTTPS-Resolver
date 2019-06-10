## DNS over HTTPS resolver for Python using Google DNS

**Requirements**  
Python 3.4+  
Requests library (https://2.python-requests.org/en/master/)

**How to use**  
If you just want a quick A record, use the convenience method:  
```
import dnsOverHttps
try:
  aRecord = dnsOverHttps.GoogleDNSQuery.getARecordFor("google.com")
  print(aRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e)
```

If you just want a quick AAAA record, use the convenience method:
```
import dnsOverHttps
try:
  aaaaRecord = dnsOverHttps.GoogleDNSQuery.getAAAARecordFor("google.com")
  print(aaaaRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e)
```
**Example**  
See and run `example.py`
