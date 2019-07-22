import gi
from urlwin import UrlWindow
from navwin import NavWindow
from gi.repository import Gtk, GLib
gi.require_version('Gtk', '3.0')


win = UrlWindow()
nav = NavWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
nav.show_all()
Gtk.main()