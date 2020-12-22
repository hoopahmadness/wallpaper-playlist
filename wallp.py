import os
from re import findall
from random import randrange
import shutil

maxLimit = 10
seedNum = 3
penalty = 8


#load previous data
#load from active papers, update statuses (in case I delete/add some)
#load from archive papers, add new papers to active roster and folder
#read history, see what I've skipped, update statuses, wipe history
#seed random papers from the archive
#remove the stuff

#write new data, close

class paper:
	def __init__(self, name):
		self.name = name
		self.status = True
		self.deleted = False
		self.played = 0
		
	def play(self, num =1):
		self.played +=num
		if self.played >=maxLimit:
			self.status=False
	
	def remove(self):
		self.played = 0
		#delete from active roster
		try:
			os.remove('/home/steve/Pictures/Backgrounds/{}'.format(self.name))
			print('removal {}'.format(self.name))
		except OSError:
			x=5
	def delete(self):
		#deleted from archive!
		self.remove()
		self.deleted = True
		#...is this complete?
	
	def add(self):
		#adds to active roster
		shutil.copy2('/home/steve/Dropbox/Backgrounds/{}'.format(self.name), '/home/steve/Pictures/Backgrounds/')
		print('added {}'.format(self.name))

##time class here
class time:
	def __init__(self, hours, mins):
		self.time = hours*60 + mins
	def differ(self, hours, mins):
		newtime = hours*60 + mins
		x = newtime - self.time
		self.time = newtime
		while x<0:
			x+=(12*60)
		if x <=3:
			return True
		else:
			return False
			
		
#load previous data
f = open('/home/steve/Documents/wallpaperInfo.txt', 'r')
ARC = {}
lottery = []
for line in f:
	line = line.split(',')

	(name, status, plays) = line
	plays = int(plays)
	ARC[name] = paper(name)
	ARC[name].play(plays)
	if 'alse' in status:##lol quirks
		ARC[name].status = False
		lottery.append(name)
		try:
			ARC[name].remove()
		except OSError: #This will happen if the file is already not there~
			x=5
		except:
			print("Weird, tried to remove this false paper, but couldn't!")
	
f.close()
#load from active papers, update statuses (in case I delete/add some)
activeList = os.listdir('/home/steve/Pictures/Backgrounds/')
for name in activeList:#if a picture was added to the folder, this will
# go ahead and add it to our database
	if name not in ARC.keys():
		#ARC[name] = paper(name) #because this will mess things up
		print('You tried to add {}, you should copy that into the Dropbox folder...'.format(name))
		
for name in ARC.keys(): #if a picture was deleted from the folder, this
# will go ahead and invalidate our database instance
	if name not in activeList:
		ARC[name].status = False

#load from archive papers, add new papers to active roster and folder
archiveList = os.listdir('/home/steve/Dropbox/Backgrounds/')
for name in archiveList:
	if name not in ARC.keys(): #New pictures in the folder are added to the database and added to
	#the active folder
		ARC[name] = paper(name)
		ARC[name].add()
	elif not ARC[name].status: #if they already exist, but are false, they are given to the lottery
		lottery.append(name)
		
for name in ARC.keys(): #if a picture was deleted from the folder, this
# will delete this from our database
	if name not in archiveList:
		ARC[name].delete()
		print('{} was not in the archives and is therefore being wiped from history'.format(name))

#read history, see what I've skipped, update statuses, wipe history?
f =open('/home/steve/.config/wallch/History.conf', 'r')
allText = f.read()
f.close()

f = open('/home/steve/.config/wallch/History.conf', 'w')
f.write('')
		
		
#name, time, type
snippets = findall('path=.+/(.+)\n\d.+time=(\d\d):(\d\d)\n\d.+type=(\d)', allText)
i=0
#print(snippets)
try:
	while int(snippets[i][3])!=1:
		i+=1
	name = snippets[i][0]
	math = time(int(snippets[i][1]), int(snippets[i][2]))
	ARC[name].play() #each item in the history gets a play
	for item in snippets[i+1:]:
		(newname, hours, mins, kind) = item
		(hours, mins, kind) = (int(hours), int(mins), int(kind))
		if kind ==1:
			if math.differ(hours, mins):
				ARC[name].play(penalty)
				print('{} is penalized.'.format(name))
			name = newname
			#ARC[name].play() ##Why did I do this? I play the next one, too? oh well
except:
	print('Error trying to read your "snippet"')
#random seeding
for i in range(seedNum):
	try:
		x = randrange(len(lottery))
		ARC[lottery[x]].status=True
	except:
		x=4
		
#commit changes
for name in ARC.keys():
	papel = ARC[name]
	if papel.status and name not in activeList:
		papel.add()
	if not papel.status and name in activeList:
		papel.remove()
		
#write new data, close
f = open('/home/steve/Documents/wallpaperInfo.txt', 'w')
for name in ARC.keys():
	if name in archiveList:
		papel = ARC[name]
		myStr = '{}, {}, {}\n'.format(papel.name, papel.status, papel.played)
		f.write(myStr)
f.close()