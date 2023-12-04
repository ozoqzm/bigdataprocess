f = open("data.txt", "r")
new = open("output9_4.txt", "w")

sum = 0
count = 0

for line in f:
    sum += float(line)
    count += 1
new.write("합계=" +str(sum)+ "\n")
new.write("평균=" +str(sum / count)+ "\n")
f.close()
new.close()