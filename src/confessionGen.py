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
		draw = ImageDraw.Draw(overlay)
		font = ImageFont.truetype(self.FONT, 55)
		width, height = bg_img.size
		# Checking if there's a confesser
		if '-' in confession and confession[-3:] != '...':
			## writing the confesser's name at the bottom
			confesser = confession[confession.rfind('-'):]
			confesser = textwrap.wrap(confesser, width=30)
			text = confession[:confession.rfind('-')]
			padding = 865
			for line in confesser:
				w, h = font.getsize(line)
				draw.text(((width - w) / 2, padding), line, font=font, fill="white")
				padding += self.pad
		else:
			text = confession
		# Wrapping the confession into a paragraph		
		para = textwrap.wrap(text, width=55)
		## Writing the confession
		for line in para:
			w, h = font.getsize(line)
			draw.text(((width - w) / 2, ((height - 180 - h) / 2) - (40 * len(para))), line, font=font, fill="white")
			height += h + self.pad