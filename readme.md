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
  print("EXCEPTION - {} - {}".format(type(e),e))
```

If you just want a quick AAAA record, use the convenience method:
```
import dnsOverHttps
try:
  aaaaRecord = dnsOverHttps.GoogleDNSQuery.getAAAARecordFor("google.com")
  print(aaaaRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e))
```

If you want more control, create an instance of `GoogleDNSQuery` with the domain name and record type (`a` or `aaaa`) in the constructor, and call `query()` method. This will return a list of `DNSRecord` objects you can iterate through in case there's more than 1 of that record type.

```
query = "google.com"
gd = dnsOverHttps.GoogleDNSQuery(query,"a")

try:
    dnsresponse = gd.query() # List of DNSResponse objects
    for i in dnsresponse: # iterate through them
        print("Record type is {} and record data is {}".format(i.recordType, i.recordData)) # 
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))
```


**Example**  
See and run `example.py`

**Limitations**  
Only A and AAAA records supported at the moment - more to come!