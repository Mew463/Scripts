from pytube import YouTube
# Use this website instead: https://ssyoutube.com/en3/youtube-video-downloader
f = open(r"C:\Users\mingw\Documents\Scripts\Python\Youtube Downloader\Songs.text", "r")

for eachurl in f:
    YouTube(eachurl).streams.filter(only_audio=True).first().download("c:/Users/mingw/Downloads")
    name = YouTube(eachurl).title
    print("Successfully downloaded " + name)







