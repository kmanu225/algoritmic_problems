fichier = open("p22_names.txt", "r")
names = []

for line in fichier.readlines():
    names += line.split(",")

fichier.close()

if __name__ == "__main__":
    names = [name[1:-1] for name in names]
    names.sort()
    print(names)
