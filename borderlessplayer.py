import vlc

class BorderlessPlayer(vlc.Instance):
	def __init__(self):
		self.vlc_instance = vlc.Instance()
