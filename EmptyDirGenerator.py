import os 

for i in range(5):
    if not os.path.exists(str(i)):
        os.makedirs(str(i))
