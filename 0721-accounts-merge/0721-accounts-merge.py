class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        p = [i for i in range(n)]
        r = [0] * n
        def find_ult_par(node):
            if  node == p[node]:
                return node
            p[node] = find_ult_par(p[node])
            return p[node]
        def union(u, v):
            u = find_ult_par(u)
            v = find_ult_par(v)
            if u == v:
                return
            if r[u] < r[v] :
                p[u] = v
            elif r[v] < r[u]:
                p[v]  = u
            else:
                p[v] = u
                r[u] += 1 
        email_to_account = {}
        for i in range(n):
            for j in range(1, len(accounts[i])):
                mail = accounts[i][j]
                if mail in email_to_account:
                    union(i, email_to_account[mail])
                else:
                    email_to_account[mail] = i
        mergeMail = {}            
        for mail, node in email_to_account.items():
            parent = find_ult_par(node)
            if parent not in mergeMail:
                mergeMail[parent] = []

            mergeMail[parent].append(mail)

        ans = []
        for node, mails in mergeMail.items():
            mails.sort()
            name = accounts[node][0]
            temp = [name] + mails
            ans.append(temp)

        return ans