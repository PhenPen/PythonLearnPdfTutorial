from urllib import request

count = 0
with request.urlopen("http://data.pr4e.org/cover3.jpg") as urlFile:
    with open("cover.jpg", mode="wb") as img:
        while True :
            data =  urlFile.read(10000)
            img.write(data)
            count = count + len(data)
            print(len(data),count)
            if len(data) < 1 : break
        

        