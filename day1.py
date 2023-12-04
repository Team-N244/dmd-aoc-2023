import re


def solve(filename, part2=False):
  value_map = {
      "one": 1,
      "two": 2,
      "three": 3,
      "four": 4,
      "five": 5,
      "six": 6,
      "seven": 7,
      "eight": 8,
      "nine": 9
  }
  valid_digits = [r'\d']
  if part2:
    valid_digits.extend(value_map.keys())
  digit_match = '|'.join(valid_digits)
  
  c_vals = []
  with open(filename, 'r') as file:
    for line in file:
      matches = re.findall(r'(?=(' + digit_match + '))', line)
      # print(matches)
      first = str(
          value_map[matches[0]]) if matches[0].isdigit() is False else str(
              matches[0])
      last = str(
          value_map[matches[-1]]) if matches[-1].isdigit() is False else str(
              matches[-1])
      # print(matches[0] + ' | ' + matches[-1])

      # print(len(matches))
      c_vals.append(int(''.join([first, last])))

  # print(c_vals)
  print(sum(c_vals))
