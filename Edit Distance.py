class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        
        dp=[[-1 for _ in range(n)] for _ in range(m)]

        def dfs(p,q):
            if p>=m and q>=n:
                return 0
            if p>=m:
                return n-q
            if q>=n:
                return m-p
            if dp[p][q]!= -1:
                return dp[p][q]
            
            if word1[p]==word2[q]:
                dp[p][q]=dfs(p+1, q+1)
            else:
                dp[p][q]=1 + min(dfs(p+1,q), dfs(p,q+1), dfs(p+1,q+1))
            return dp[p][q]
        return dfs(0,0)