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
		self.entry.connect("activate", self.parseUrl)
		urlBox.pack_start(self.entry, True, True, 0)

		self.add(urlBox)
		urlButton = Gtk.Button.new_with_label("Go")
		urlBox.pack_start(urlButton, True, True, 0)


	def parseUrl(self, entry):
		url = entry.get_text()
		print(url)

win = BorderlessWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
win2 = BorderlessWindow()
win2.connect("destroy", Gtk.main_quit)
win2.show_all()
Gtk.main()