file = open("SSLSecrets.log", "r") 
f = file.read().split("\n")

for i in f:
    if "CLIENT_RANDOM" in i: print(i)
