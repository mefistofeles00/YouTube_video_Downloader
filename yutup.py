from pytube import YouTube



link = input("\nlütfen indirmek istediğiniz youtube linkini (url) den kopyalayarak giriniz: ---->")

yt = YouTube(link)

#Bilgileri gösterelim
print("Başlık: ",yt.title)
print("Video izlenme: ",yt.views)
print("video uzunluğu: ",yt.length)
print("Rating of Video: ",yt.rating)


ys = yt.streams.get_highest_resolution()

#indirmeye başlasın artık

print(f"Downloading video: {yt.title} ")

ys.download()

print("Download Completed or video bitti!!!")


