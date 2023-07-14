def reverse_words(s):
  words = s.split()
  reversed_words = []

  for word in words:
    reversed_word = ""
    for i in range(len(word) - 1, -1, -1):
      reversed_word += word[i]
    reversed_words.append(reversed_word)

  return " ".join(reversed_words)


def main():
  s = "Let's take LeetCode contest"

  reversed_string = reverse_words(s)
  print(reversed_string)


if __name__ == "__main__":
  main()
