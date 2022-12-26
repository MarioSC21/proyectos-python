from pytube import YouTube

link = input("Introduce el Link : ")
yt = YouTube(link)
#stream = yt.streams.filter(progressive=True)
stream = yt.streams.get_highest_resolution()

print("Iniciando descarga")
stream.download()
print("Descarga finalizada")