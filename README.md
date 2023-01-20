# homedvdrip
Python script to help rip home-made DVDs. 

## Requirements
- lsdvd (https://linux.die.net/man/1/lsdvd)
- HandbrakeCli (https://handbrake.fr/)

The python script runs *lsdvd* and calls *HandbrakeCli* on each chapter (2..n-tracks). 
Currently set to 25fps (ripping old videos from a family archive).
