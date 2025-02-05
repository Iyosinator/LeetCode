class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_count = {}

        for cpdomain in cpdomains:
            count, domain = cpdomain.split(' ')
            count = int(count)

            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                subdomain_count[subdomain] = subdomain_count.get(subdomain, 0) + count

        result = [f"{count} {domain}" for domain, count in subdomain_count.items()]

        return result
