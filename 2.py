def is_strobogrammatic(num):
  strobogrammatic_pairs = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

  for i in range(len(num) // 2):
    if num[i] not in strobogrammatic_pairs or strobogrammatic_pairs[num[i]] != num[-i - 1]:
      return False

  return True


def main():
  num = "69"

  is_strobogrammatic = is_strobogrammatic(num)
  print(is_strobogrammatic)


if __name__ == "__main__":
  main()
