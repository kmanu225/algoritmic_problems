from itertools import chain

from keyLogger import isSecured


chaine = "G=d:Dl:T=9NS1c$9qC%,^EdUVLnU-7"
sections = [chaine[i:i+6] for i in range(len(chaine)-5)]

print(sections)
print(isSecured('Dl:T=9'))