import gi
from urlwin import UrlWindow
from gi.repository import Gtk, GLib
gi.require_version('Gtk', '3.0')


win = UrlWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()