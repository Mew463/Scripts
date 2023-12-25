from pytube import YouTube
# Use this website instead: https://ssyoutube.com/en3/youtube-video-downloader
f = open(r"/Users/mingweiyeoh/Documents/GitHub/Scripts/Python/Youtube Downloader/Songs.text", "r")

for eachurl in f:
    YouTube(eachurl).streams.filter(only_audio=True, file_extension = ".mp4").first().download("/Users/mingweiyeoh/Downloads")
    name = YouTube(eachurl).title
    print("Successfully downloaded " + name)







