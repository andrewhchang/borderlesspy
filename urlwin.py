import gi
import pafy
import ctypes
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
from borderlessplayer import BorderlessPlayer

class UrlWindow(Gtk.Window):
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
		xlib = ctypes.cdll.LoadLibrary("libX11.so")
		xlib.XInitThreads()

		url = entry.get_text() #retrieve url from entry box                                                                                       
		myvideo = pafy.new(url) #create new pafy video url                                                                                                                      
		
		
		#alter pafy url to play vid at best quality
		bestvid = myvideo.getbest()                                                                                                                 
		bestVidUrl = bestvid.url

		#create new vlc instance with content = pafy url                                                                                                                         
		#myPlayer = BorderlessPlayer()
		player = BorderlessPlayer().media_player_new(bestVidUrl)
		#self.destroy()
		player.video_set_key_input(True)                                                                                             
		GLib.idle_add(player.play())
		print(player.get_role())
		while True:pass
