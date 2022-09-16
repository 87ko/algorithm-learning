from dataclasses import replace
import math

# cmd + E で実行

# 3-3
# N(>=2) 個の相異なる整数a0-aN-1
# 2番目に小さい値を求めるO(N）のアルゴリズム
def findSecondMinimum(arr):
	min_first = math.inf
	min_second = math.inf

	for i in range(len(arr)):
		if arr[i] < min_first:
			min_second = min_first
			min_first = arr[i]
		elif arr[i] < min_second:
			min_second = arr[i]

	return min_second

# arr = [4,3,10,8,1]
# print(findSecondMinimum(arr))


# 3-4
# N個の整数 a0-aN-1
# 2個選んで差をとる。差の最大値を求める O(N)

def maxDiff(arr):
	minValue = math.inf
	maxValue = 0

	for i in range(len(arr)):
		if arr[i] < minValue:
			minValue = arr[i]
		if arr[i] > maxValue:
			maxValue = arr[i]

	return maxValue - minValue

# arr = [4,3,10,8,1]
# print(maxDiff(arr))


# 3-5
# Nこの正の整数 a0 - aN-a
# Nこの整数がすべて偶数ならば2でわった値に置き換える
# 何回の操作を行うことになるかアルゴリズムを設計する

def replace2divide(arr):
	ans = []
	for i in range(len(arr)):
		if arr[i]%2==0:
			ans.append(arr[i])
		else:
			return 0

	return len(arr)

# arr = [2,6,8,4,10]
# print(replace2divide(arr))

# 3-6
# 2つの正の数 K, N   0<=X,Y,Z<=K をみたす X+Y+X=N をみたす
# O(N^2)

def searchXYZ(K, N):
	# 0 <= X,Y,Z <= K の組
	count = 0
	print(f"X, Y, Z = ")
	for i in range(K, -1, -1):
		for j in range(K, -1, -1):
			z = N-i-j
			# 残りの数がKより大きかったらスキップ
			if z > K or z < 0: continue
			# 残りの数もKの範囲内だったらカウント
			print(f"[{i}, {j}, {N-i-j}]")
			count += 1

	return count

# print(searchXYZ(3,4))

# O(2^N)
def insertPlus(S):
	N = len(str(S))
	ans = 0
	# N桁の間（N-1）に+が入るか入らないか、を0or1で表す
	for i in range(0, 2**(N-1)):
		# bitをN-1桁で表示する..
		bit = ('0'*(N-1) + str(bin(i))[2:])[-(N-1):]
		print('bin(i)..',i, bit)
		tmp = 0 # 部分和
		for j in range(0, N-1):
			# 桁があがるときは *10 をする
			tmp *= 10
			# 桁jの数値を足す
			tmp += int(str(S)[j])
			# 1があれば + を挿入する
			if bit[j] == '1':
				print('tmp', tmp)
				ans += tmp
				# tmpを初期化する
				tmp = 0

		tmp *= 10 # 桁があがるときに *10
		tmp += int(str(S)[N-1]) # 最後桁を足す
		ans += int(tmp)

		print('tmp',tmp)
		tmp = 0

	return ans

print(insertPlus(123))
