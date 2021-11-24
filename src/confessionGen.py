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
		bg_img = Image.open(self.IMAGE)
		width, height = bg_img.size
		## Generating as much confessions as confessions length
		for amount in range(self.quantity):
			cur_time = str(datetime.datetime.now().time())
			overlay = Image.new("RGBA", (width, height), "white")
			overlay.paste(bg_img, (0, 0))
			confession = self.confessions[amount]
			## Checking confession length (Split into 2 pages or not)
			if len(confession.split(" ")) > 70:
				confession = confession.split(" ")
				self.addConfession(" ".join(confession[:len(confession)//2]) + "...", overlay, bg_img)
				overlay.save(f"confession_{cur_time}.png")
				overlay = Image.new("RGBA", (width, height), "white")
				overlay.paste(bg_img, (0, 0))
				self.addConfession("..." + " ".join(confession[(len(confession)//2):]), overlay, bg_img)
				overlay.save(f"confession_{cur_time}(2).png")
			else:
				self.addConfession(confession, overlay, bg_img)
				overlay.save(f"confession_{cur_time}.png")
				

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