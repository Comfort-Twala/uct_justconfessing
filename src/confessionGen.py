#### IMPORTS ####
from PIL import Image, ImageDraw, ImageFont
import textwrap, datetime

"""
ConfessionGenerator class responsible for creating full confession image.
"""
class ConfessionGenerator:
	## Constructor and initialisations
	def __init__(self, confessions = []):
		self.confessions = confessions
		self.FONT = "assets/KGSueEllenFrancisco.tff"
		self.IMAGE = "assets/uct_base.jpg"
		self.pad = 57 	## padding
		self.quantity = len(self.confessions)

	"""
	generate method produce final confessions
	"""	
	def generate(self):
		pass

	"""
	addConfession method to write confession onto the background image
	"""
	def addConfession(self, confession, overlay, bg_img):
		pass