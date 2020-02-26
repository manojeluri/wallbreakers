from collections import Counter
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map = Counter()
        for d in cpdomains:
            times, domains = d.split()
            domains = domains.split('.')
            for i in range(len(domains)):
                domain = '.'.join(domains[i:])
                map[domain] += int(times)
        return ["{} {}".format(v,k) for k,v in map.items()]