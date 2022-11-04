N = int(input())
price_sack = [[0]*(N+1) for _ in range(3)]

for i in range(1, N+1):
    r, g, b = map(int, input().split())
    price_sack[0][i] = r + min(price_sack[1][i-1], price_sack[2][i-1])
    price_sack[1][i] = g + min(price_sack[0][i-1], price_sack[2][i-1])
    price_sack[2][i] = b + min(price_sack[0][i-1], price_sack[1][i-1])
    
print(min(price_sack[0][N], price_sack[1][N], price_sack[2][N]))    