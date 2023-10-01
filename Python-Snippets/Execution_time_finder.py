import time
start_time = time.time()
for i in range(20):
  if i % 2 == 0:
    print(i, end = " ") 
end_time = time.time()
time_taken = end_time - start_time
print("\nTime: ", time_taken)