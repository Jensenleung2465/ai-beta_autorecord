#import some application for the "bootloader"
from tqdm import tqdm
import time as t
import core
from rich import print
import os

#<systemvar>
dir = "/" # define the system defpath
sysversion = "v1.0.1.0.1" # define the system version
gtimestamp = core.gettime() # get the time from core.py
#</systemvar>

def boot() :
	#set up the bootloader tqdm code
	tqdm_bar = tqdm(total=100)
	tqdm_bar.set_description("setup BOIS...")
	print("getting time from your settings and core")
	t.sleep(1)
	#print time
	print(f"gtimestamp = {gtimestamp}")
	tqdm_bar.update(10)
	t.sleep(1)
	#write a log in boot.log by core.writelog()
	print("write a log to boot.log")
	core.writelog(f"{gtimestamp}_bootloader")
	print("done!")
	tqdm_bar.update(40)
	t.sleep(1)
	print("systemchecking...")
	tqdm_bar.update(40)
	t.sleep(0.5)
	tqdm_bar.update(10)
	t.sleep(0.2)
	print("bootloader done")
	if __name__ != "__main__" :
		return core.writelog("bootloader done")

#added if __app__ == "__main__" : in 2025/7/25 22:18.
if __name__ == "__main__" :
	boot()