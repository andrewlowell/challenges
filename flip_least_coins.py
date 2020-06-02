# Coin flip

# def flip_least_coins(arr):
#   current_correct = arr[0]
#   first_count = 0
#   second_count = 0
#   for item in arr:
#     if item == current_correct:
#       second_count += 1
#     else:
#       first_count += 1
#     current_correct = 1 - current_correct

#   print(arr)
#   print(first_count, second_count)
#   return min(first_count, second_count)

def best_flip_least_coins(arr):
  correct = arr[0]
  count = 0
  for item in arr:
    if item == correct:
      count += 1
    correct = 1 - correct

  return min(count, len(arr) - count)

tests = [
  [0],
  [0, 1],
  [1, 1, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 1],
  [1,1,0,1,0,1,0],
  [0,0,1,1,1,0,1,0,1,1],
  [1,0,1,0,0,1,0,1],
  [0,0,1,0,1,1,0,1],
  [0,1,1,1,1,0,0,1],
  [1,0,1,1,1,1,0,1],
  [0,1,0,1,0,0,1,0],
  [0,1,1,0,0,0,1,1],
  [0,0,1,1,0,1,1,1],
  [0,1,1,1,0,1,1,1]
]
for test in tests:
  print(best_flip_least_coins(test))
