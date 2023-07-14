def can_be_shifted(s, goal):
  if s == goal:
    return True

  seen = set()
  queue = [s]

  while queue:
    string = queue.pop(0)
    for i in range(len(string)):
      new_string = string[i:] + string[:i]
      if new_string == goal:
        return True
      elif new_string not in seen:
        seen.add(new_string)
        queue.append(new_string)

  return False


def main():
  s = "abcde"
  goal = "cdeab"

  can_be_shifted = can_be_shifted(s, goal)
  print(can_be_shifted)


if __name__ == "__main__":
  main()
