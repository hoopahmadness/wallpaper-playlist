package main

import (
	// "path/filepath"
	"time"
)

type Wallpaper struct { //add json tags to this
	name           string
	filepath       string
	dateAdded      time.Time
	dateLastPlayed time.Time
	playCount      int
	tags           []string
	playlists      []*Playlist
	skips          []time.Time
	favorite       bool
}

//creates a new wallpaper from a filepath
func newWallpaper(filepath string) *Wallpaper {
	//parse name from filepath
	//attempt to set dateAdded based on metadata, or perhaps to today
	//set date last played to dateAdded
	//favorite to true
	//everything else zero
	return &Wallpaper{}
}

//for internal use, change the playcount arbitrarily
func (w *Wallpaper) addPlays(plays int) {
	w.playCount += plays
}

func (w *Wallpaper) Play() {
	//some logic to set the desktop background
	//update dateLastPlayed to today
	w.addPlays(1)
}
