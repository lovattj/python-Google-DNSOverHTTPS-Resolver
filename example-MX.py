import dnsOverHttps

print("*** Demonstration of creating a new query object and getting all MX records for the domain ***")
query = "google.com"
gd = dnsOverHttps.GoogleDNSQuery(query,"mx")

try:
    dnsresponse = gd.query() # List of DNSResponse objects
    mxSorted = sorted(dnsresponse, key=lambda x: x.recordData[:2]) # Sort the MX records in order
    for i in mxSorted: # iterate through them
        print("Record type is {} and record data is {}".format(i.recordType, i.recordData)) # 
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))