# Вариант 5

def is_palindrome(n: int) -> bool:
	digits: str = str(n)
	length = len(digits)
	for i in range(0, length // 2):
		if digits[i] != digits[-(i + 1)]:
			return False

	return True


for i in range(10, 101):
	if is_palindrome(i) and is_palindrome(i ** 3):
		print(f'Палиндром: {i}. {i}^3 = {i ** 3} — тоже палиндром.')
