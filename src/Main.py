import confessionGen

"""
Main class that provides user interface and entrance to program
"""
class Main:
	def __init__(self):
		self.file = "input/confessions.txt"
		self.encoding = "utf-8"

	"""
	Program usage menu
	"""
	def usage(self):
		usage = """Usage:\nTo use program ensure that all your 
confessions are written in the confessions.txt
file in the input folder."""
		return usage

	"""
	Program Driver
	"""
	def main(self):
		print("\tCONFESSIONS GENERATOR")
		print("=====================================")
		print("    ***  Starting operation  ***")
		try:
			with open(self.file, encoding=self.encoding) as file:
				confessions = file.readlines()
		except FileNotFoundError:
			print("Error: Oops ... couldn't find that file\n")
			print(self.usage)
			confessions = []

		generator = confessionGen.ConfessionGenerator(confessions=confessions)
		generator.generate()

		print("DONE\n*** Check the output folder!")
		print("=====================================")
		print("\t@trof_talks_tech")


if __name__ == "__main__":
	Main().main()