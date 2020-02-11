class BadStatusCodeResponseException(Exception):
    pass

class BadDNSResponseException(Exception):
    pass

class NoDNSResultsException(Exception):
    pass

class InvalidRecordTypeException(Exception):
    pass

class DNSRecord():
    recordType = ""
    recordData = ""

    def __init__(self, recordType, recordData):
        self.recordType = recordType
        self.recordData = recordData
    
    def __str__(self):
        return "Record type: {} - Record data: {}".format(self.recordType, self.recordData)

class GoogleDNSQuery():
    domain = ""
    recordType = ""
    cd = False 
    REQUEST_BASE_URI = "https://dns.google.com/resolve?"

    def __init__(self, domain, recordType):

        self.domain = domain
        self.recordType = recordType

    def query(self):
        if (not(self.recordType == "a" or self.recordType == "aaaa" or self.recordType == "mx" or self.recordType == "txt")):
            raise InvalidRecordTypeException("Record type requested was {} and this is not supported.".format(self.recordType))

        import requests
        builtQuery = "{}name={}&type={}".format(self.REQUEST_BASE_URI, self.domain, self.recordType)
        response = requests.get(builtQuery, timeout=5)

        if (response.status_code!=200):
            raise BadStatusCodeResponseException()
        parsedJsonResponse = response.json()
        if (parsedJsonResponse["Status"]!= 0):
            raise BadDNSResponseException
        if not "Answer" in parsedJsonResponse:
            raise NoDNSResultsException

        output = []
        for r in parsedJsonResponse["Answer"]:
            output.append(DNSRecord(r["type"],r["data"]))
        
        return output

    @staticmethod
    def getARecordFor(domain):
        gd = GoogleDNSQuery(domain,"a")
        r = gd.query()
        return r[0].recordData

    @staticmethod
    def getAAAARecordFor(domain):
        gd = GoogleDNSQuery(domain,"aaaa")
        r = gd.query()
        return r[0].recordData        