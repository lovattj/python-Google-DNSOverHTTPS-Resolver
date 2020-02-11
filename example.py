import dnsOverHttps

print("*** Demonstration of creating a new query object and getting all A records for the domain ***")
query = "bbc.co.uk"
gd = dnsOverHttps.GoogleDNSQuery(query,"a")

try:
    dnsresponse = gd.query() # List of DNSResponse objects
    for i in dnsresponse: # iterate through them
        print("Record type is {} and record data is {}".format(i.recordType, i.recordData)) # 
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))


print("\n*** Demonstration of convenience method to just get an IPv4 A address for a domain ***")

try:
  aRecord = dnsOverHttps.GoogleDNSQuery.getARecordFor("bbc.co.uk")
  print(aRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e))

print("\n*** Demonstration of convenience method to just get an IPv6 AAAA address for a domain ***")

try:
  aaaaRecord = dnsOverHttps.GoogleDNSQuery.getAAAARecordFor("bbc.co.uk")
  print(aaaaRecord) # IP Address here!
except Exception as e:
  print("EXCEPTION - {} - {}".format(type(e),e))