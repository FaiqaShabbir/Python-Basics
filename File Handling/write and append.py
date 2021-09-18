import os

file = open("C:/Users/faiqa/OneDrive/Desktop/Python/write.txt", 'w')
file.write("Hello Faiqa!")
file.write("\nHello Faiqa again!")
file.close()

if os.path.exists("C:/Users/faiqa/OneDrive/Desktop/Python/defile.txt"):
    os.remove("C:/Users/faiqa/OneDrive/Desktop/Python/defile.txt")
else:
    print("You Dumb Ass!")
