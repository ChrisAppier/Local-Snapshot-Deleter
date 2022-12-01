#This script finds Time Machine local snapshots and deletes them

from subprocess import call, check_output as co
from sys import exit

#Listing the snapshots and saving them into a list
snapshots = co("tmutil listlocalsnapshots /",shell=1).decode().split()[4::]

#Deleting the snapshots
for i in snapshots:
    call("tmutil deletelocalsnapshots "+i[22:-6],shell=1)

exit()
