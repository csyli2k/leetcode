def minimumTotal(self, triangle: List[List[int]]) -> int:
    n=len(triangle[-1])
    dp=[0] *(n+1)
    for i in range(n-1,-1,-1):
        curr= triangle[i]
        for j in range(len(curr)):
            dp[j]= curr[j]+ min(dp[j],dp[j+1])
    return dp[0]
        