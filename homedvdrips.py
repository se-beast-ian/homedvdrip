### imports 
import os 
#import subprocess
import sys
import shutil


### Gather DVD info 
os.system("lsdvd -c -Oy > ./lsdvdout.py")

try:
    from lsdvdout import lsdvd
except:
    sys.exit('lsdvd probably not installed')


# Create placeholder for series
dvdname = lsdvd["title"]
try:
    os.makedirs(dvdname)
except:
    print('Path Exists, clearing up')
    shutil.rmtree(dvdname)
    os.makedirs(dvdname)

for n in range(2, len(lsdvd["track"])):
    handbrakecmd = "HandBrakeCLI -i /mnt/dvd/ -t " + str(n) + " -f av_mp4 -o " + str(dvdname) + "/" + str(n) + ".mp4" + " -e x264 -r 25 -a 1 -E ffaac -s 2 --subtitle-burned 2"
    print(handbrakecmd)
    os.system(handbrakecmd)
    rep = n - 1


# Report what was done
print('Ripped Titles: ', rep)

# Cleanup - 'atta boy' 
# remove lsdvdout.py 
os.remove('lsdvdout.py')
try: 
    shutil.rmtree('__pycache__')
except: 
    print('Cleanup Done')