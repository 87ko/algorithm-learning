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
# ３の累乗である数nのおかかを、1にち3きれ食べるとしたら、何日分たべられるかな

def everydayOkaka(n):
	return everydayOkakaHelper(n/3, 0)

def everydayOkakaHelper(n, count):
	if n == 1: return count+1
	return everydayOkakaHelper(n/3, count+1)

print(everydayOkaka(3))


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
