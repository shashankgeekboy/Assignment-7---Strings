def reverse_k_chars(s, k):
  reversed_string = ""
  i = 0
  while i < len(s):
    if i + k <= len(s):
      reversed_string += s[i:i + k][::-1]
      i += 2 * k
    else:
      reversed_string += s[i:][::-1]
      break

  return reversed_string


def main():
  s = "abcdefg"
  k = 2

  reversed_string = reverse_k_chars(s, k)
  print(reversed_string)


if __name__ == "__main__":
  main()
