
"""
Longest Common Subsequence(LCS).

string1 = ABCDGH
string2 = AEDFHR


LCS(string1,string2) = ADH
Length of LCS = 3
"""

#Brute Force approach for finding LCS
def lcs_brute(a,b,i,j) -> int:
	if i==len(a) or j==len(b):
		return 0 
	

	if a[i]==b[j]:
		return 1+lcs_brute(a,b,i+1,j+1)

	return max(lcs_brute(a,b,i+1,j),lcs_brute(a,b,i,j+1))


#Optimised top down approach for finding LCS
def lcs_topdown(a,b,i,j,dp) -> int: 
	if i==len(a) or j==len(b):
		return 0

	if dp[i][j]!=-1:
		return dp[i][j]

	if a[i] == b[j]:
		return 1+lcs_topdown(a,b,i+1,j+1,dp)

	dp[i][j] = max(lcs_topdown(a,b,i+1,j,dp),lcs_topdown(a,b,i,j+1,dp))
	return dp[i][j]


#Optimised bottom up approach for finding LCS
def lcs_bottomup(a,b) -> int:
	m = len(a)
	n = len(b)

	dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

	for i in range(1,m+1):
		for j in range(1,n+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]

			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	return dp[m][n]  


# Function to print the LCS
def get_lcs(a,b) -> str:
	m = len(a)
	n = len(b)

	dp = [[0 for _ in range(n+1)]for _ in range(m+1)]

	for i in range(1,m+1):
		for j in range(1,n+1):
			if a[i-1] == b[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]

			else:
				dp[i][j] = max(dp[i-1][j],dp[i][j-1])
	
	i,j = m,n
	ans  = []
	while i>0 and j>0:
		if a[i-1]==b[j-1]:
			ans.insert(0,a[i-1])
			i-=1
			j-=1
		else:
			if dp[i][j-1]>dp[i-1][j]:
				j-=1
			else:
				i-=1

	return "".join(ans)


string1 = "ABCDGH"
string2 = "AEDFHR"

# lcs = lcs_brute(string1,string2,0,0) -> using brute force
# lcs = lcs_bottomup(string1,string2) -> using bottomup approach

dp = [[-1 for i in range(len(string2)+1)] for j in range(len(string1)+1)]
lcs_length = lcs_topdown(string1,string2,0,0,dp)
lcs = get_lcs(string1,string2)

print(lcs_length)
print(lcs)


