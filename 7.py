def backspace_compare(s, t):
  i = j = 0
  count_backspaces_s = 0
  count_backspaces_t = 0

  while i < len(s) or j < len(t):
    while i < len(s) and s[i] == '#':
      count_backspaces_s += 1
      i += 1

    while j < len(t) and t[j] == '#':
      count_backspaces_t += 1
      j += 1

    if i == len(s) or j == len(t):
      break

    if s[i] != t[j]:
      return False

    i += 1
    j += 1

  return count_backspaces_s == count_backspaces_t


def main():
  s = "ab#c"
  t = "ad#c"

  is_equal = backspace_compare(s, t)
  print(is_equal)


if __name__ == "__main__":
  main()
