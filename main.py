#Import neccesary libraries
import yt_dlp
import os
from pydub import AudioSegment, effects
import glob

#IMPORTANT - UPDATE VARIABELE WITH PATH TO FFMPEG EXECUTABLE
AudioSegment.converter = "/opt/homebrew/bin/ffmpeg"

#Define variables
#Change this to where you prefer files to be exported to
workingdir = "./Documents"
os.chdir(workingdir)
location = os.getcwd()
print(location)
#Loudness that files will be normalized to
target_DBFS = -16

#Specify yt_dlp options
ydl_opts = {
    'format': 'm4a/bestaudio/best',
    'outtmpl': "",
    'sleep_interval_requests': 1,
    'sleep_interval': 1.5,
    'max_sleep_interval': 4,
    'ignoreerrors': True,
    #'cookiefile': '/Users/elliothodges/Documents/cookies.txt',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

#Define functions
def extractAudio(link):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(link)
    return True

def createSubFolder(name):
    if not os.path.exists(name):
         directory = os.mkdir("./"+str(name))
         return "./"+str(name)
    else:
        print("Directory already exists!")
        return False

def playlistDownload(id, link):

    path = createSubFolder(str(id))
    ydl_opts['outtmpl'] = os.path.join(path, '%(title)s.%(ext)s')
                                    
    os.chdir(path)
    extractAudio(str(link))
    return True

def normalizeAudio(input, output):
    audio = AudioSegment.from_mp3(input)
    dbChange = target_DBFS - audio.dBFS
    #normalized_audio = effects.normalize(audio)
    normalized_audio = audio.apply_gain(dbChange)
    normalized_audio.export(output, format=os.path.splitext(output)[1][1:], bitrate="128k")

def normalizeFiles(id):
    if not os.path.exists("normalized"):
        os.mkdir("normalized")
        for filename in os.listdir("./"+id):
            if filename.endswith(('.wav', '.mp3', '.flac')):  # Add or remove extensions as needed
                input_filepath = os.path.join(id, filename)
                output_filepath = os.path.join("normalized", filename)
                normalizeAudio(input_filepath, output_filepath)
                print(f"Normalized: {filename} -> {output_filepath}")
        return True
    else:
        print("Normalized folder already exists!")
        return False


#Run program
order_id = input("Please enter a name for the playlist: ")
playlist = input("Please enter a yt playlist link: ")


playlistDownload(order_id, playlist)
normalizeFiles(str(order_id))

