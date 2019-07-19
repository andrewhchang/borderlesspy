import sys
from gi.repository import Gtk

def __init__(self):
	Gtk.Window.__init__(title="Borderless Player")
	self.urlEntry = Gtk.Entry(max=0)
	urlEntry.show()

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()