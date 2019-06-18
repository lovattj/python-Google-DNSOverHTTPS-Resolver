import dnsOverHttps

print("*** Demonstration of creating a new query object and getting all TXT records for the domain ***")
query = "google.com"
gd = dnsOverHttps.GoogleDNSQuery(query,"txt")

try:
    dnsresponse = gd.query() # List of DNSResponse objects
    for i in dnsresponse: # iterate through them
        print("Record type is {} and record data is {}".format(i.recordType, i.recordData)) # 
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))