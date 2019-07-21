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
		url = entry.get_text() #retrieve url from entry box                                                                                       
		myvideo = pafy.new(url) #create new pafy video url                                                                                                                      
		
		
		#alter pafy url to play vid at best quality
		bestvid = myvideo.getbest()                                                                                                                 
		bestVidUrl = bestvid.url

		#create new vlc instance with content = pafy url                                                                                                                         
		#myPlayer = BorderlessPlayer()
		player = BorderlessPlayer(bestVidUrl)
		player.set_fullscreen(False)                                                                                                     
		player.play()
		while True:pass

class BorderlessPlayer(vlc.MediaPlayer):
	def __init__(self):
		self.vlc_instance = vlc.MediaPlayer(
            "--no-video-deco " +
            "--no-embedded-video " +
            "--video-x=X  " + 
            "--video-y=Y  " 
		)

class NavWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Python-Vlc Media Player")

		self.playback_button = Gtk.Button()
        self.stop_button = Gtk.Button()
        self.play_image = Gtk.Image.new_from_icon_name(
                "gtk-media-play",
                Gtk.IconSize.MENU
            )
        self.pause_image = Gtk.Image.new_from_icon_name(
                "gtk-media-pause",
                Gtk.IconSize.MENU
            )
        self.stop_image = Gtk.Image.new_from_icon_name(
                "gtk-media-stop",
                Gtk.IconSize.MENU
            )

        def toggle_player_playback(self, widget, data=None):
	        if self.is_player_active == False and self.player_paused == False:
	            self.player.play()
	            self.playback_button.set_image(self.pause_image)
	            self.is_player_active = True

	        elif self.is_player_active == True and self.player_paused == True:
	            self.player.play()
	            self.playback_button.set_image(self.pause_image)
	            self.player_paused = False

	        elif self.is_player_active == True and self.player_paused == False:
	            self.player.pause()
	            self.playback_button.set_image(self.play_image)
	            self.player_paused = True
	        else:
	            pass

	        self.playback_button.set_image(self.play_image)
	        self.stop_button.set_image(self.stop_image)
	        self.playback_button.connect("clicked", self.toggle_player_playback)
	        self.stop_button.connect("clicked", self.stop_player)

        def stop_player(self, widget, data=None):
	        self.player.stop()
	        self.is_player_active = False
	        self.playback_button.set_image(self.play_image)

		    self.draw_area.connect("realize",self._realized)
			self.hbox = Gtk.Box(spacing=6)
	        self.hbox.pack_start(self.playback_button, True, True, 0)
	        self.hbox.pack_start(self.stop_button, True, True, 0)

	        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	        self.add(self.vbox)
	        self.vbox.pack_start(self.draw_area, True, True, 0)
	        self.vbox.pack_start(self.hbox, False, False, 0)

	        self.show_all()

win = BorderlessWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()