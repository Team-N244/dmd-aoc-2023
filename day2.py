import re


def solve(filename, part_two=False):
  red_max = 12
  green_max = 13
  blue_max = 14
  sum = 0

  # find the sum of the IDs of all the possible games
  with open(filename, 'r') as file:
    for game in file:
      game_red_max = 0
      game_green_max = 0
      game_blue_max = 0
      game_power = 1

      # print(re.match(r'Game (\d+): ((\d+) (\w+)[,;]?\s?)+', line))
      id = re.match(r'Game (\d+).*', game).group(1)
      sets = re.split(';', game)
      # print(sets)
      valid_game = False
      for set in sets:
        red_total = 0
        green_total = 0
        blue_total = 0

        color_counts = re.findall(r'(\d+) (\w+)', set)
        # print(color_counts)
        for count, color in color_counts:
          if color == 'red':
            red_total += int(count)
          elif color == 'green':
            green_total += int(count)
          elif color == 'blue':
            blue_total += int(count)

        # print('(' + id + ') | ', red_total, ' red | ', green_total, ' green',
        #       '\n', blue_total, ' blue | ')

        if (red_total >= game_red_max):
          game_red_max = red_total
        if (green_total >= game_green_max):
          game_green_max = green_total
        if (blue_total >= game_blue_max):
          game_blue_max = blue_total

        if (not part_two):
          if (red_total <= red_max and blue_total <= blue_max
              and green_total <= green_max):
            valid_game = True
            # print('Game ' + id + ' valid')
          else:
            valid_game = False
            # print('Game ' + id + ' invalid')
            break

      if (part_two):
        game_power = game_red_max * game_green_max * game_blue_max

        # print('(' + id + ') | ', game_red_max, ' game red | ', game_green_max,
        #       ' game green | ', game_blue_max, ' game blue', '\n')
        # print('(' + id + ') | ', ' game power ', game_power, '\n')
        sum += game_power
      else:
        if valid_game:
          sum += int(id)
          # print('current sum: ', id_sum, '\n')
        # print('-----------------------------------------------------')

  print('sum: ', sum, '\n==========================\n')
