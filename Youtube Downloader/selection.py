from pytube import YouTube

def selection(link):
  tags = []
  try:
    yt = YouTube(link)
  except:
    return 1
  options = input("Do you want audio or video? (audio/ video) ")
  if options.lower() == "video" or options.lower() == "v":
    for i in yt.streams.filter(progressive=True):
      info = str(i).lstrip("<Stream: itag=")
      info = info[:4]
      info = info.strip('"')
      tags.append(info)
    itag = tags[-1]
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    print("done! If you are using replit, please wait time depending on video length for the repl.it server to process the video!")
    return 0
    
  elif options.lower() == "audio" or options.lower() == "a":
    for i in yt.streams.filter(only_audio=True):
      info = str(i).lstrip("<Stream: itag=")
      info = info[:4]
      info = info.strip('"')
      tags.append(info)
    itag = tags[-1]
    stream = yt.streams.get_by_itag(itag)
    stream.download()
    print("done!")
    return 0
    
  else: 
    print("I don't understand...\n")
    selection(link)
