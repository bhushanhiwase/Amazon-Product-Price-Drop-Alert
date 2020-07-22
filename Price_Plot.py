from matplotlib import pyplot as plt

y = []
x = []

with open("price_logs.csv", "r") as file:
    for i in file:                                      # To read all the lines in the file
        data1 = file.read()
        k1 = data1.split("\n")

        for item in k1:
            data2 = item.split(",")
            if len(data2) == 4:
                x.append(data2[0])
                y.append(float(data2[2]))

plt.xlabel("Date")
plt.ylabel("Price")

plt.bar(x, y)

plt.show()

