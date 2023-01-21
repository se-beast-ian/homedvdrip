### imports 
import os 
import sys
import shutil


### Gather DVD info 
os.system("lsdvd -c -Oy > ./lsdvdout.py")
os.system("lsdvd -s > ./subtitles.txt")

try:
    from lsdvdout import lsdvd
except:
    sys.exit('lsdvd probably not installed')


subtitles = open(r"./subtitles.txt", "r")
print(subtitles.read())
print("Anything above 10 will ignore subtitles")

# Ask user which subtitle to burn in
subtitle = input("Which subtitle you want?: ")

# Create placeholder for series
dvdname = lsdvd["title"]
try:
    os.makedirs(dvdname)
except:
    print('Path Exists, clearing up')
    shutil.rmtree(dvdname)
    os.makedirs(dvdname)

for n in range(2, len(lsdvd["track"])):
    if (int(subtitle) >= 10):
        handbrakecmd = "HandBrakeCLI -i /mnt/dvd/ -t " + str(n) + " -f av_mp4 -o " + str(dvdname) + "/" + str(n) + ".mp4" + " -e x264 -r 25 -a 1 -E ffaac"
    else:
        handbrakecmd = "HandBrakeCLI -i /mnt/dvd/ -t " + str(n) + " -f av_mp4 -o " + str(dvdname) + "/" + str(n) + ".mp4" + " -e x264 -r 25 -a 1 -E ffaac -s " + str(subtitle) + " --subtitle-burned " + str(subtitle)

    print(handbrakecmd)
    os.system(handbrakecmd)
    rep = n - 1


# Report what was done
print('Ripped Titles: ', rep)

# Cleanup - 'atta boy' 
# remove lsdvdout.py 
os.remove('lsdvdout.py')
os.remove('subtitles.txt')
try: 
    shutil.rmtree('__pycache__')
except: 
    print('Cleanup Done')