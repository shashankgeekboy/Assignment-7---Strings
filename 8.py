def check_straight_line(coordinates):
  if len(coordinates) < 2:
    return False

  slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
  for i in range(2, len(coordinates)):
    if (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0]) != slope:
      return False

  return True


def main():
  coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

  is_straight_line = check_straight_line(coordinates)
  print(is_straight_line)


if __name__ == "__main__":
  main()
