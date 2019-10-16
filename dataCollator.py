import os

for conc in [0, 1, 10, 100, 1000]:
	for mem in [128, 256, 512, 1024, 2048]:
		fileName = "p{}out{}.data".format(mem, conc)

		f = open(fileName)
		f.readline()
		data = f.read()

		f.close()
		os.remove(fileName)

		f = open("p{}out{}full.data".format(mem, conc), "a")
		f.write(data)
		f.close()


