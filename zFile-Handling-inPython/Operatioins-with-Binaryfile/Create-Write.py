file = open("document.bin","wb")
sentence = bytearray("This is good".encode("ascii"))
file.write(sentence)
file.close()
