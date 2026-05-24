# YT-CD-BOT
Automatic tool for downloading and converting YT playlists into files reading for burning to CDs. 


This is a simple tool I wrote that's meant to run in your command line. It uses yt_dlp to scrape the YouTube playlist you enter and downloads and converts the playlist as mp3s. It then uses pydub to normalize all the mp3s to a default target loudness of -16 dBFS, similar to how streaming services normalize LUFS. This is great for burning to a CD, as all the songs will be perceived at roughly the same loudness and you won't have to keep adjusting the volume while listening to the CD.

## Setup
YT-CD-BOT requires both the `yt_dlp` and `pydub` libraries, as well as the `audioop` module if using Python 3.13+
```
pip install yt_dlp
pip install pydub
pip install audioop-lts
```
After downloading the python file, update the `AudioSegment.converter` on line 8 with the path to your ffmpeg executable. Also change the `workingdir` variable on line 12 with the path to where you want the files to be downloading to.

## Usage Instructions
1. Run the Python file in your terminal and enter a name for your playlist. This just determines the folder name where the files are saved.
2. Provide a valid YouTube playlist link (YT Music links also supported).
3. Wait until the process is finished. Once completed, you will be able to find the mp3 files as well as the normalized mp3 files in the folder you named.

## Potential Issues
YouTube is known to frequently throw 403 errors when using automated processes to download videos. You will most likely get a 403 after repeated use of this program. To circumvent this, you can try to pass a cookies.txt file in the `ydl_opts' arguments. I've also had luck in the past using VPNs to change IPs. If all else fails you'll have to wait until it works again.
