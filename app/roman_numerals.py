def parse(self):
  # roman_numerals = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'XI': 11, 'XIV': 14, 'XIX': 19, 'XX': 20, 'XXXIV': 34, 'XLI': 41, 'L': 50, 'XCIX': 99, 'C': 100, 'CCCXXXIII': 333, 'DLV': 555, 'CDXLIX': 449, "MCMLXXII": 1972}

  ROMAN_NUMERALS = {
      'M': 1000,
      'D': 500,
      'C': 100,
      'L': 50,
      'X': 10,
      'V': 5,
      'I': 1
  }

  total = 0
  prev = 0
  for i in range(len(self)):
    curr = ROMAN_NUMERALS[self[i]]
    if curr > prev:
      total += curr - 2 * prev
    else:
      total += curr
    prev = curr
  return total
# print(parse('IX'))








  # number = len(self)
  # counter = 0

  # for i in range(number):
  #   if i == number - 1 or roman_numerals[number[i]] >= roman_numerals[number[i + 1]]:
  #     counter += roman_numerals[number[i]]
  #   else:
  #     counter -= roman_numerals[number[i]]
  #   return counter



  # return roman_numerals.get(self)











#  def parse(self):
#   if self == 'I':
#     return 1
#   elif self == 'III':
#     return 3
#   elif self == 'IV':
#     return 4
#   elif self == 'V':
#     return 5
#   elif self == 'VI':
#     return 6
#   elif self == 'VII':
#     return 7
#   elif self == 'VIII':
#     return 8


