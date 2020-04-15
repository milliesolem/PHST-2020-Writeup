#PHST 2020 Writeup

![alt text](https://raw.githubusercontent.com/williamsolem/PHST-2020-Writeup/master/PHST%202020%20Writetup/phst_logo.png "phst_logo.png")

##Skjærtordag

![alt text](https://raw.githubusercontent.com/williamsolem/PHST-2020-Writeup/master/PHST%202020%20Writetup/1%20-%20Skj%C3%A6rtorsdag/skjrtorsdag.png "skjrtorsdag.png")

I denne oppgaven blir vi gitt et bilde `skjrtorsdag.png`, som det blir sakt inneholder noe muffens. Mulig det er lurt å starte med å sjekke EXIF-metadataen til filen, til dette finnes det et par verktøy man kan bruke, men jeg går med [ExifTool](https://exiftool.org/), som gjør en grei jobb:

```
$ exiftool skjrtorsdag.png
ExifTool Version Number         : 11.79
File Name                       : skjrtorsdag.png
Directory                       : .
File Size                       : 3.2 MB
File Modification Date/Time     : 2020:04:09 12:00:08+02:00
File Access Date/Time           : 2020:04:14 20:23:31+02:00
File Creation Date/Time         : 2020:04:14 20:23:31+02:00
File Permissions                : rw-rw-rw-
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1920
Image Height                    : 1080
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : CUFG{Qrer_snatre_zrt_nyqev!!}
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Image Size                      : 1920x1080
Megapixels                      : 2.1
```

Her får vi mye data, men noe som ser interessant ut er `Image Description`; Her får vi noe som ser ut som flagget (`CUFG{Qrer_snatre_zrt_nyqev!!}`), men med litt feil bokstaver. Det ser ut som det er brukt et Caesar chiffer, også kjent som et ROT13 chiffer. Det finnes mange resurser på nett som lar oss dekryptere et slikt chiffer, men jeg valgte å gå med [Cryptii](https://cryptii.com/pipes/rot13-decoder). Plugger vi inn chifferteksten får vi `PHST{Dere_fanger_meg_aldri!!}`, som er flagget.

Det er også relativt enkelt å gjøre dette med penn og papir, man bare forskyver alle bokstavene i teksten med 13 bokstaver i alfabetet, slik at "a" blir "n", "b" blir "o", "c" blir "p", osv. Kommer man til slutten av alfabetet går man bare til starten av alfabetet og fortsetter å telle. Samme metode fungerer også for dekryptering.

##Langfredag

![alt text](https://raw.githubusercontent.com/williamsolem/PHST-2020-Writeup/master/PHST%202020%20Writetup/2%20-%20Langfredag/paskeegg_langfredag.png "paskeegg_langfredag.png")

I denne oppgaven blir vi gitt et bilde `paskeegg_langfredag.png`, og det blir sagt at det finnes noe av interesse i blidet. Og det ser det ut som det gjør; blidet viser et bord med diverse verktøy, skruer, en kartong med påskeegg, og et ark med visse farger og teksten "Resistor Color Code". Om vi tar to og to sammen er det helt klart en korrelasjon mellom fargene på eggene og "Resistor Color Code". Det virker som det er brukt farger til å representere tall ved bruk av resistorfargekoder. Her er en tabell som viser hvilke farger og tall som hører sammen.

![alt text](https://raw.githubusercontent.com/williamsolem/PHST-2020-Writeup/master/PHST%202020%20Writetup/2%20-%20Langfredag/resistor_color_codes.png "resistor_color_codes.png")

Noterer vi ned  fargene på eggene får vi:

```
brun-brun-rød svart-grønn-rød svart-grønn-rød brun-brun-grønn brun-svart-lilla svart-grønn-brun
brun-svart-gul svart-grønn-rød brun-brun-gul svart-grønn-brun brun-brun-svart svart-oransje-oransje
```

Gjør vi så disse til deres ekvivalente tall får vi:


```
112 052 052 115 107 051
104 052 114 051 110 033
```

Dette ligner på ASCII-koder. Og riktig nok, omgjør vi tallene til deres ekvivalente ASCII-tegn får vi `p44sk3h4r3n!`, flagget er altså `PHST{p44sk3h4r3n!}`.


##Påskeaften

Her blir vi gitt nettaddressen `1F423.com`. Domenet er registrert, men leder ikke til noen server. Istedet får vi se om det er noe data i resource records til domenet. Personlig valtge jeg å gjøre dette igjennom [UltraTools](https://www.ultratools.com/tools/dnsLookup), men det er godt mulig i gjøre dette med `nslookup`-kommandoen og diverse andre verktøy, men som jeg lærte på den harde måten etter mye prøving og feiling er det lett å overse visse ting når man gjør det manuelt.

Resultatet blir:

| | |
| --- | --- |
| A     | No record found |
| TXT      | "These aren't the droids you're looking for"|
| LOC | 60 47 34.900 N 11 6 3.600 E 0m 0m 0m 0m |
| SOA | No record found |
| NS | No record found |
| SRV | No record found |
| SPF | No record found |
| CNAME | No record found |
| MX | No record found |
| AAAA | No record found |

Her får vi interessant informasjon, spesiellt de tallene, som ser ut til å være koordinater. Skriver vi `60°47'34.900" N 11°6'3.600" E` inn i en søkemotor ser vi at koordinatene peker direkte på Vikingskipet på Hamar. Flagget blir altså `PHST{Vikingskipet}`.


##Første påskedag

I denne oppgaven blir vi gitt en PCAP-fil `mistenklig.pcap`. En PCAP-fil er et opptak av nettverkstrafikk på et netverk, og kan leses ved bruk av et verktøy som [Wireshark](https://www.wireshark.org/). Vi blir fortalt at en aktør har fått fotfeste på en datamaskin på nettverket og bruker denne datamaskinen til å hente ut informasjon. Vår oppgave er altså da å finne ut hvilke informasjon aktøren har fått tak i. Hovedsakelig er vi ute etter titellen på et dokument.

Når man først åpner PCAP-filen kan den virke litt skummel; det er mange pakker som går til og fra, og en stor del av det er kryptert med TLS/SSL. Jeg fant at den enkleste måten å ta fatt på denne oppgaven er å filtrere ut pakker vi enten ikke kan lese siden de er kryptert, eller vi ganske enkelt ikke er interessert i. Nesten helt på toppen av Wireshark-vinduet ser man en tekstlinje som vi kan skrive i, her kan vi legge til filter. Vi starter med å filtere ut all kryptert TCP-kommunikasjon ved å skrive inn `!tcp.port==443`, her sier vi at så lenge kommuniskasjonen ikke er TCP igjennom port 443, så vises kommunikasjonen.

Allerede ser vi at det er noe muffens, det ser ut til at det er en TCP-kommunikasjon som går igjennom port 31337, som er selvfølgelig et av de magiske hacker-tallene, det virker som aktøren bruker. Hvis vi så høyre-klikker på en av disse pakkene og så klikker "Follow -> TCP Stream" får vi opp et nytt vindu med mye tekst:

```
CLIENT_HANDSHAKE_TRAFFIC_SECRET 048cdb34b84a4c2757aeba15ec563947de5162b95145f2a8b8097ca30f592193 0ffe2688f783ce31014d44000a9dcf3b3eba59efd32fdece13ad6e7f26abc099
SERVER_HANDSHAKE_TRAFFIC_SECRET 048cdb34b84a4c2757aeba15ec563947de5162b95145f2a8b8097ca30f592193 8c84053453390b462624a2f515d633e831025fb7af6bd8d8e3642c091c3d5841

... (Her er det hundrevis av linjer, så jeg kutter litt ned, du finner hele greia i SSLSecrets.log)

SERVER_TRAFFIC_SECRET_0 bbf51b72932a7141668bbea1c09bc0d21fef2602e6131752ae1b4be438602ac2 939b4214dec997b336d90bdd10e9d4f8ba47498bfc4e1f7ba89bf8631dd3bc22
EXPORTER_SECRET bbf51b72932a7141668bbea1c09bc0d21fef2602e6131752ae1b4be438602ac2 aaefecdde25a3fecffee11d2bde3e4c5f19a3792fefb6d2ec328a25d90a17860
```

Eureka! Her har vi all informasjonen vi trenger for å dekryptere TLS/SSL-kommuniskasjonen. Vi er egentlig bare interresert i de linjene som starter med `CLIENT_RANDOM`, I og med at de inneholder privat-nøklene til kommunikasjonen. Ved hjelp av litt python kan vi filtrere ut det vi ikke trenger:

```py
file = open("SSLSecrets.log", "r") 
f = file.read().split("\n")

for i in f:
    if "CLIENT_RANDOM" in i: print(i)
```


Nå bare kopierer vi det vi får ut av scriptet og limer det inn i en ny fil kalt `SSLKey.log`. Så, går vi over til Wireshark, og så klikker vi "Preferences -> Protocols -> TLS", under "(Pre)-Master-Secret log filename" trykker vi "Browse...", velger `SSLKey.log`, og trykker "OK". Etter dette skal noe av TLS-kommunikasjonen være dekryptert. Vi kan filtere slik at vi bare ser dekryptert kommunikasjon ved å skrive `http` inn i filter-feltet.

Her ser vi mye rart, mest ting og tang fra yr.no, men en ting som vekker oppmerksomhet, i og med at vi er ute etter et dokument, er en GET-request til en PDF:

```
GET /c?i=4fbb91ddd9d93eb946000000&tp=https%3A%2F%2Fwww.yr.no%2Fplace%2FNorway%2FInnlandet%2FHamar%2FVikingskipet%2Fforecast.pdf&ps=&co=15x6&ct=6&el=a&sr=&p=https%3A%2F%2Fwww.yr.no%2Fsted%2FNorge%2FInnlandet%2FHamar%2FVikingskipet%2F&c=desktop&t=article&s=&_r=1586301393748 HTTP/1.1
Host: p.lp4.io
Connection: keep-alive
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.163 Chrome/80.0.3987.163 Safari/537.36
Sec-Fetch-Dest: image
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: no-cors
Referer: https://www.yr.no/place/Norway/Innlandet/Hamar/Vikingskipet/
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9

HTTP/1.1 204 No Content
Date: Tue, 07 Apr 2020 23:16:33 GMT
Server: Apache/2.4.29 (Ubuntu)
```

Om vi dekoder delen med url-en med PDF-filen får vi `https://www.yr.no/place/Norway/Innlandet/Hamar/Vikingskipet/forecast.pdf`, om vi så åpner denne PDF-en ser vi at tittelen er `Weather forecast for Vikingskipet`, og siden flagget er breskrevet som `PHST{Tittel i dokument}` så blir flagget da `PHST{Weather forecast for Vikingskipet}`


##Andre påskedag

![alt text](https://img.url.here "paskekylligbetjenter.png")

Så kom vi til la grande finale til hele CTF-en, i denne oppgaven blir vi gitt tre filer: `merkelig.py`, `underfundig`, og `paskekylligbetjenter.png`. Python-scriptet virker til å være en slags interpreter til et esoterisk kodesrpåk som bruker påske-emojier som kommandoer, `underfundig` virker til å være et program skrevet i dette kode-språket, og `paskekylligbetjenter.png` er et bilde av påskekyllinger rundt en datamaskin som prøver å løse gåten.

Om vi kjører python-scriptet med `underfundig` som argument blir vi bedt om passord, og om vi ikke gir riktig passord, får vi en feilmeldig. Ved litt lesing av python-scriptet ser vi at `🐇` (emoji av kanin) blir brukt som en goto/jump-kommando, som tester om verdien som stack-pekeren pekert til ikke er 0, og om den ikke er det, håpper programmet til en annen del av programmet. Om vi nå ser på koden til `underfundig` ser vi at den har en sekvens med mange håpp, altså sjekker programmet passordet tegn-for-tegn, og når den kommer over et tegn som er feil, håpper den til feilmeldingen.

Utifra dette kan man lage et program som måler hvor "riktig" et passord er, og kan utifra det konstruere passordet. Her er et python-script som illustrerer dette:

```py
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
```

Scriptet tar koden til den orginale, men setter kommando-kjøringen i en `while True` løkke som kjører fram til  `break` blir kallt. Input til interpretern blir også byttet ut men en variabel `password` som kontinuerlig justeres. Koden har kommentarer slik at det er mulig å følge algoritmen. Kjører vi dette scriptet finner vi raskt ut at passordet ergo flagget er `PHST{Mitt navn er Gwyn. Pen Gwyn.}`.

For de som ikke vet, så var Pen Gwyn en agent for Sydpolar Sikkerhetstjenste SPST i PSTs julekalender i fjord. 

##Rebus
```
Your quest is now over
We hope it was fun
The journey must come to an end
Maybe you've won?

print("https://www.phst.no/" + alfa + bravo + charlie + delta + echo + ".html")
```

Igjennom hele denne CTF-en har vi fått rebus-ord ved å løse hver oppgave. Rebus-ordene er som følger (i rekkefølge av dagen de ble låst opp på);
```
bravo = "19de0b5a1eeef635c2b4fec6e7c7"
{delta: "03074978df7930e256789cb87ea67358"}
echo: "a3f6ce4eb662e4797a39b"
$charlie = "664150457e1f2ccc3399"
String alfa = "0c405bdf5899c3db8ba0d1909f9"
```

Setter vi disse sammen og slenger på en `.html` får vi `0c405bdf5899c3db8ba0d1909f919de0b5a1eeef635c2b4fec6e7c7664150457e1f2ccc339903074978df7930e256789cb87ea67358a3f6ce4eb662e4797a39b.html`. Går vi inn på denne siden blir vi gratulert får å ha løst alle oppgavene og kommet i mål, flagget er `PHST{Du klarte SHAbussen, veldig bra jobba!}`

##Tanker

Alt i alt synes jeg dette var en gøy, utfordrende, og ikke minst lærerik CTF. Denne CTF-en satte mine ferdigheter på prøve i områder jeg ellers ikke er så god i (f.eks. nettverksanalyse), jeg fikk godt utbytte av å jobbe med disse oppgavene. PST skuffer aldri med oppgaver som er både tankevekkende og underholdene. Gleder meg veldig til neste mysterium de kommer med.
