keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
ja = "qwertasdfgzxcv"
mo = "yuiophjklbnm"

left, right = input().split()
target = input()

position = {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3),
            't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7),
            'o': (0, 8), 'p': (0, 9), 'a': (1, 0), 's': (1, 1),
            'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5),
            'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 'z': (2, 0),
            'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4),
            'n': (2, 5), 'm': (2, 6)}

result = 0
for alpha in target:
  if alpha in ja:
    a = position[left]
    b = position[alpha]
    result += abs(a[0]-b[0]) + abs(a[1]-b[1]) + 1
    left = alpha
  elif alpha in mo:
    a = position[right]
    b = position[alpha]
    result += abs(a[0]-b[0]) + abs(a[1]-b[1]) + 1
    right = alpha

print(result)