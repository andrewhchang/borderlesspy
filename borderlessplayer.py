import gi
import pafy
import vlc
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class BorderlessWindow(Gtk.Window):
	global VIDURL

	def __init__(self):
		Gtk.Window.__init__(self, title="Borderless Player")
		self.set_size_request(300,50)

		urlBox = Gtk.Box(spacing = 0)

		self.entry = Gtk.Entry()
		self.entry.set_text("Please enter URL")
		self.entry.connect("activate", self.parseUrl)
		urlBox.pack_start(self.entry, True, True, 0)

		self.add(urlBox)
		urlButton = Gtk.Button.new_with_label("Go")
		urlBox.pack_start(urlButton, True, True, 0)


	def parseUrl(self, entry):
		"""
		#VIDURL = entry.get_text()
		VIDURL = "https://www.youtube.com/watch?v=Pv_5VTrHyqY"
		videoWindow = pafy.new(VIDURL)
		best = videoWindow.getbestaudio()
		playurl = best.VIDURL
		newvlc = vlc.MediaPlayer(playurl)
		player.play()
		while True:pass
		"""
		url = entry.get_text()                                                                                        
		myvideo = pafy.new(url)                                                                                                                       
		bestvid = myvideo.getbestvideo()                                                                                                                 
		bestVidUrl = bestvid.url                                                                                                                          
		player = vlc.MediaPlayer(bestVidUrl)                                                                                                           
		player.play()
		while True:pass

class VideoWindow(Gtk.Window):
	mystring = "String"

win = BorderlessWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()