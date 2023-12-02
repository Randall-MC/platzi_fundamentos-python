counter = 0
counter_break = 0
counter_continue = 0

while counter < 10:
    counter += 1
    print(counter)

while counter_break < 10:
    if counter_break == 5:
        break
    counter_break += 1
    print(counter_break)

while counter_continue < 10:
    counter_continue += 1
    if counter_continue == 5:
        continue
    print(counter_continue)