digits = 1 + int(input("Enter precision: "))
denom = float(3)
pi_total = float(1)
for i in range(1,digits):
	digits -= 1
	pi_total = pi_total - (1.0 / denom ) + (1.0 / (denom + 2))
	denom += 4
pi_total = pi_total * 4
print(str(pi_total))
