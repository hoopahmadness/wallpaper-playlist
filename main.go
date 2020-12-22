package main

import ()

func main() {
	//set global config, hardcode for now
	conf := Config{
		wallpaperDirectory: "/home/steve/Dropbox/Backgrounds/",
		recordsDirectory:   "/home/steve/.wallpaper-playlist/",
		historyFile:        "/home/steve/.config/variety/history.txt",
	}

	//command line flag (?) to favorite or unfavorite current paper by checking variety's history, loading the master list, updating, and saving it to disk, then exit

	//goroutine to refresh playlists on start (save to disk) and every XX days
	//goroutine to change paper on start and again every 10 hours

	//unsorted comments
	//load previous data (playlists? and master list)
	//check dropbox for new papers, initialize them
	//SKIP FOR NOW - - - - read history, see what I've skipped, update statuses, wipe history
	//main playlist:
	//	all new papers
	//	15 favorite papers under 5 plays
	//	10 favorite papers not seen in 3 months
	//	 5 papers (fave or not) not seen in 9 months

	//wait forever, let routines do their thing

}

//function that finds the PID of a running instance of this program, and sends commands to its input
//https://serverfault.com/questions/178457/can-i-send-some-text-to-the-stdin-of-an-active-process-running-in-a-screen-sessi
