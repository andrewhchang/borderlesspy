import gi
from gi.repository import Gtk, GLib
gi.require_version('Gtk', '3.0')

class NavWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Video Control")
		self.playback_button = Gtk.Button()
		self.stop_button = Gtk.Button()

		self.play_image = Gtk.Image.new_from_icon_name("gtk-media-play", Gtk.IconSize.MENU)
		self.pause_image = Gtk.Image.new_from_icon_name("gtk-media-pause", Gtk.IconSize.MENU)
		self.stop_image = Gtk.Image.new_from_icon_name("gtk-media-stop", Gtk.IconSize.MENU)

		def toggle_player_playback(self, widget, data=None):
			if self.is_player_active == False and self.player_paused == False:
				self.player.play()
				self.playback_button.set_image(self.pause_image)
				self.is_player_active == True

			elif self.is_player_active == True and self.player_paused == True:
				self.player.play()
				self.playback_button.set_image(self.pause_image)
				self.player_paused == False

			elif self.is_player_active == True and self.player_paused == False:
				self.player.pause()
				self.playback_button.set_image(self.play_image)
				self.player_paused == True

			else:
				pass

			self.playback_button.set_image(self.play_image)
			self.stop_button.set_image(self.stop_image)
			
			self.playback_button.connect("clicked", self.toggle_player_playback)
			self.stop_button.connect("clicked", self.stop_player)
			self.draw_area.connect("realize",self._realized)
			
			self.hbox = Gtk.Box(spacing=6)
			self.hbox.pack_start(self.playback_button, True, True, 0)
			self.hbox.pack_start(self.stop_button, True, True, 0)
			
			self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
			self.add(self.vbox)
			self.vbox.pack_start(self.draw_area, True, True, 0)
			self.vbox.pack_start(self.draw_area, False, False, 0)

			self.show_all()

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
				self.vbox.pack_start(self.draw_area, False, False, 0)

				self.show_all()