import glob

images = glob.glob("*.png")

with open("name.txt", 'w') as file:
    for img in images:
        file.write(img)
        file.write("\n")
