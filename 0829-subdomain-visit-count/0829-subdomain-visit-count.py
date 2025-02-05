class Solution:
    def subdomainVisits(self, cpdomains):
        counter = collections.Counter()
        for cpdomain in cpdomains:
            count, *domains = cpdomain.replace(" ",".").split(".")
            for i in range(len(domains)):
                counter[".".join(domains[i:])] += int(count)
        return [" ".join((str(v), k)) for k, v in counter.items()]
'''
           
           '900 google.mail.com"
           "50 yahoo.com"
           "1 intel.mail.com" 
           "5 wiki.org"

           mail.com - 900 + 1 = 901
           .com - 900 + 50 + 1 = 951
           .org - 5 = 5

           "901 mail.com",
           "951 .com",
           "5 wiki.org"
'''