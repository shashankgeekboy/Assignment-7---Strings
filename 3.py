def add_strings(num1, num2):
  carry = 0
  result = ""

  i = len(num1) - 1
  j = len(num2) - 1

  while i >= 0 or j >= 0:
    digit1 = int(num1[i]) if i >= 0 else 0
    digit2 = int(num2[j]) if j >= 0 else 0

    sum_digit = digit1 + digit2 + carry
    carry = sum_digit // 10
    result = str(sum_digit % 10) + result

    i -= 1
    j -= 1

  if carry:
    result = str(carry) + result

  return result


def main():
  num1 = "11"
  num2 = "123"

  sum_string = add_strings(num1, num2)
  print(sum_string)


if __name__ == "__main__":
  main()
