total = 0
#s = raw_input("Enter the string \n")
l = list(s)

for i in range(len(l)):
    if l[i] == 'a' or l[i] == 'e' or l[i] == 'i' or l[i] == 'o' or l[i] == 'u':
        total += 1

print ("Number of vowels: %d" % total)
