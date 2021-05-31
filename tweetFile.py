def writeFiles(fileLocation, text):
    f = open(fileLocation, 'w', encoding="utf-8")

    f.write(text)

    f.close()