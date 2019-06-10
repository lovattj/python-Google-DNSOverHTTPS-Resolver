import dnsOverHttps

print("*** Demonstration of creating a new query object and getting all A records for the domain ***")
query = "google.com"
gd = dnsOverHttps.GoogleDNSQuery(query,"a")

try:
    dnsresponse = gd.query()
    for i in dnsresponse:
        print(i)
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))


print("\n*** Demonstration of convenience method to just get an IPv4 A address for a domain ***")

import dnsOverHttps
try:
  aRecord = dnsOverHttps.GoogleDNSQuery.getARecordFor("google.com")
  print(aRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e))

print("\n*** Demonstration of convenience method to just get an IPv6 AAAA address for a domain ***")

import dnsOverHttps
try:
  aaaaRecord = dnsOverHttps.GoogleDNSQuery.getAAAARecordFor("google.com")
  print(aaaaRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e))