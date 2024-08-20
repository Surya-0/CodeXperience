from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        visit = set()
        for email in emails:
            local_name,domain_name = email.split('@')
            local_name = ''.join(local_name.split('.'))
            local_name = local_name.split('+')[0]
            res = local_name + "@" + domain_name
            visit.add(res)

        return len(visit)

