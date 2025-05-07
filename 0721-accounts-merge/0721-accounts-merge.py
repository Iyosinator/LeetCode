class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(acc[1], email)

        unions = collections.defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in unions.items()]
