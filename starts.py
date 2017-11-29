def stars(list):
	for i in range(len(list)):
		print '*'*list[i]

# stars([4, 6, 1, 3, 5, 7, 25])


def stars2(arr):
	for thing in arr:
		if type(thing) is int:
			print '*'*thing
		elif type(thing) is str:
			print thing[0].lower()*len(thing)

stars2([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])