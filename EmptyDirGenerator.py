import os 

for i in range(100):
    if not os.path.exists(str(i)):
        os.makedirs(str(i))
