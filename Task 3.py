sum_result = []
for n in range(200, 301):
    result = []
    i = 1
    while i < n:
        if n % i == 0:
            divider = n / i
            result.append(divider)
        else:
            i += 1
    sum_result.append(sum(result))
for i in range(0, 101):
    for j in range(0, 101):
        if sum_result[i] == 200 + j and sum_result[i] == 200 + i:
            print(f"{200 +i} - {200 +j}")

