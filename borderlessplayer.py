import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class BorderlessWindow(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Borderless Player")
		self.set_size_request(300,50)

		urlBox = Gtk.Box(spacing = 0)

		self.entry = Gtk.Entry()
		self.entry.set_text("Please enter URL")
		gtk_signal_connect (self.entry, "activate", parseUrl)
		urlBox.pack_start(self.entry, True, True, 0)

		self.add(urlBox)
		urlButton = Gtk.Button.new_with_label("Go")
		urlBox.pack_start(urlButton, True, True, 0)


	def parseUrl(self, button, str):
		print(str)

win = BorderlessWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()