import math

def is_prime(n: int) -> bool:
	while(f ** 2 <= n):
		if n % f == 0:
			return False
		f += 2
	return True

if __name__ == '__main__':
	print(is_prime(13))
