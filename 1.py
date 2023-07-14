def is_isomorphic(s, t):
  mapping = {}
  seen = set()

  for i in range(len(s)):
    if s[i] not in mapping:
      if t[i] in seen:
        return False
      mapping[s[i]] = t[i]
      seen.add(t[i])
    elif mapping[s[i]] != t[i]:
      return False

  return True


def main():
  s = "egg"
  t = "add"

  is_isomorphic = is_isomorphic(s, t)
  print(is_isomorphic)


if __name__ == "__main__":
  main()
