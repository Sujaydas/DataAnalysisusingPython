import os
for filename in os.listdir("."):
	#if filename.startswith("@"):
	os.rename(filename, "chelsea" + filename[:])
