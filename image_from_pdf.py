from pdf2image import convert_from_path

path = "~/revenue.pdf"
images = convert_from_path(path)

p = 0

for i in images:
	if p == 6:
		i.save("out.jpg","JPEG")
		break
	p += 1
