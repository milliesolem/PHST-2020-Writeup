import sys, os

digits = {"🎲": 0, "🍫": 1,  "🎮": 2, "🎧": 3, "🎨": 4, "🍬": 5}
base = len(digits)

def parse_num(code):
    num = 0
    for i,c in enumerate(code):
        num += digits[c] * base**i
    return num

def convert_num(n):
    res = ""
    

if len(sys.argv) < 2:
    print("Mangler programfil!")
    exit(1)

code = open(sys.argv[1], "rt", encoding="utf8").read()
pc = 0

stack = [0] * 256
sp = 0

jumpstack = []
checkstack = []
writestack = []

#passord er 34 tegn, dette kan vi se igjennom at koden sjekker lengden til passordet først. Å brekrefte dette blir latt som oppgave til leseren :)
password = [0]*34
oldlen=0
while True:
    jumpstack = []
    #array som følger hva jump-kommandoen tar inn
    checkstack = []
    writestack = []
    stack = [0] * 256
    pc=0
    sp=0
    while pc < len(code):
        op = code[pc]
        pc += 1
        if op == "🐰":
                stack[sp] = parse_num(code[pc:pc+4])
                writestack.append(stack[sp])
                sp += 1
                pc += 4
        elif op == "🐥":
            stack[sp] = stack[sp-1]
            sp += 1
        elif op == "🌱":
            sp -= 1
            stack[sp-1] += stack[sp]
            stack[sp-1] %= base**4
        elif op == "🌻":
            sp -= 1
            stack[sp-1] -= stack[sp]
            stack[sp-1] %= base**4
        elif op == "🐇":
            sp -= 1
            #hiver på verdien i stack
            checkstack.append(stack[sp])
            if stack[sp] != 0:
                pc += parse_num(code[pc:pc+4])
                jumpstack.append(code[pc:pc+4])
            else:
                pc += 4
        elif op == "🥚":
            sp -= 1
            stack[sp-1] ^= stack[sp]
        elif op == "🐤":
            sp -= 1
        elif op == "🐣":
            line = password
            for c in line:
                stack[sp] = c
                sp += 1
            stack[sp] = len(line)
            sp += 1
        elif op == "🌞":
        	#Vi vil gjerne at scriptet fortsetter å kjøre etter vi har prøvd et passord
            pass
    #Sjekker om vi har kommet noe lengre på å finne passordet og printer status
    if (len(checkstack)>oldlen):
        print(" ".join(str(x) for x in password))
        pass
    if(len(checkstack)==len(password)+1):
        break
    #Øker nåvøerende tegn med 1. Lengden på checkstack, som indikerer hvor mye av passordet vi vet, brukes som index til å finne hvilket tegn vi må finne.
    password[len(password)-len(checkstack)+1]=password[len(password)-len(checkstack)+1]+1
    #I tilfelle noe køddes til vil vi ikke gå utenfor  7-bits rekkevidde på tegn
    password[len(password)-len(checkstack)+1]=password[len(password)-len(checkstack)+1]%128
    oldlen=len(checkstack)
print("P"+"".join(chr(x) for x in password[1:]))
