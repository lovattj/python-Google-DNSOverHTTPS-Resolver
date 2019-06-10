import dnsOverHttps

query = "cloudflare.com"

print("*** Demonstration of creating a new query object and getting all A records for the domain ***")
gd = dnsOverHttps.GoogleDNSQuery(query,"a")

try:
    dnsresponse = gd.query()
    for i in dnsresponse:
        print(i)
except Exception as e:
    print("EXCEPTION: {} - {}".format(type(e), e))


print("\n*** Demonstration of convenience method to just get an IPv4 A address for a domain ***")

try:
    a = dnsOverHttps.GoogleDNSQuery.getARecordFor(query)
    print(a)
except Exception as e:
    print(type(e))

print("\n*** Demonstration of convenience method to just get an IPv6 AAAA address for a domain ***")

try:
    a = dnsOverHttps.GoogleDNSQuery.getAAAARecordFor(query)
    print(a)
except Exception as e:
    print(type(e))