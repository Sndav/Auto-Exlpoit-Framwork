import requests
import time


class T_CloudEye:

    def __init__(self, key, url_uniq, url_prefix):
        ''' eg. fas.poc.22d0d6.dnslog.info , url_uniq = 22d0d6 url_prefix=fas.poc'''
        self.key = key
        self.prefix = url_prefix
        self.uniq = url_uniq
        self.url = url_prefix + "." + url_uniq + ".dnslog.info"

    def getDnsRecord(self, delay=2):
        time.sleep(delay)
        # query = self.random + '.' + self.custom
        api_base = 'http://cloudeye.me/api/{key}/{domain}/DNSLog/'.format(
            key=self.key, domain=self.prefix)
        return requests.post(api_base).content

    def getHttpRecord(self, delay=2):
        time.sleep(delay)
        api_base = 'http://cloudeye.me/api/{key}/{domain}/ApacheLog/'.format(
            key=self.key, domain=self.prefix)
        return requests.post(api_base).content

    def verifyDNS(self, delay=2):
        return 'dnslog.info' in self.getDnsRecord(delay)

    def verifyHTTP(self, delay=2):
        return 'dnslog.info' in self.getHttpRecord(delay)

    def getFullUrl(self):
        return self.url

if __name__ == '__main__':
    pass
