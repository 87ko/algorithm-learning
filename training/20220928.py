# dm内 再帰とっくんっ！

# No.1 n日目のおかか
# にゃんこは1日目に1きれ、2日目に3きれ、3日目に6きれ、と、おかかを発見します
# n日目に発見するおかかの数はいくつ？

# 例えば
# n=1 のときは 1
# n=2 のときは 1+2 → f(2-1)+2
# n=3 のときは　1+2+3 → f(3-1)+3
# となるので、 f(n-1) + n を返してあげるとよい

def findOkaka(n):
	if n == 1: return 1
	return n + findOkaka(n-1)

print(findOkaka(4)) # 16



# No.2 おかかを3で割っていく
# ３の累乗である数nのおかか 何回3でわれるかな

def divide3Okaka(n):
	return divide3OkakaHelper(n/3, 0)

def divide3OkakaHelper(n, count):
	if n == 1: return count+1
	return divide3OkakaHelper(n/3, count+1)

print(divide3Okaka(3))


# No.3 n匹のお猫様が並ぶ方法の総数　

def patternOrder(n):
	if n == 1: return 1
	return n * patternOrder(n-1)

print(patternOrder(4))


# No.4 もらえるおかかが毎日2倍ずつ増えていきます。
# 1日目は1きれです。2日目は2きれです。n日目にもらえるおかかは何きれでしょうか？

def howmanyOkaka(n):
	if n == 1: return 1
	return 2 * howmanyOkaka(n-1)

print(howmanyOkaka(3))


# No.5 m と n　の最大公約数をもとめる
# (m, n) とおいて、 m % n = r を (n, r) とおく
# r = 0 のとき、 n　が公約数となる

def gcd(m,n):
	if(m%n == 0): return n
	return gcd(n, m%n)

print(gcd(15,12))
