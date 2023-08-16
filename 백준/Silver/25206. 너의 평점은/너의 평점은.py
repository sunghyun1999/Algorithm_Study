rating_dict = {"A+": 4.5, "A0": 4.0,
               "B+": 3.5, "B0": 3.0,
               "C+": 2.5, "C0": 2.0,
               "D+": 1.5, "D0": 1.0,
               "F": 0.0}

sum_value = 0
credit_sum = 0
for _ in range(20):
  input_data = input().split()
  if input_data[2] == "P":
    continue
  sum_value += float(input_data[1]) * rating_dict[input_data[2]]
  credit_sum += float(input_data[1])

print(round(sum_value/credit_sum, 6))