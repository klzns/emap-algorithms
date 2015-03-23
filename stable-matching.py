# Stable Matching - Gale-Shapley Algorithm

# Let the input be:

# Men
# Tom	Jen Nic Lis
# Mat	Nic Lis Jen
# Ken	Jen	Lis	Nic
men = {
	'Tom': ['Jen', 'Nic', 'Lis'],
	'Mat': ['Nic', 'Lis', 'Jen'],
	'Ken': ['Jen', 'Lis', 'Nic']
}

# Women
# Jen	Tom	Mat	Ken
# Lis	Ken Mat Tom
# Nic	Mat Ken Tom
women = {
	'Jen': ['Tom', 'Mat', 'Ken'],
	'Lis': ['Ken', 'Mat', 'Tom'],
	'Nic': ['Mat', 'Ken', 'Tom']
}

class Person:
	def __init__(self, name, preferences):
		self.name = name
		self.preferences = preferences

		self.engaged_to = None
		self.proposed_to = []

	def find_match_not_proposed(self):
		for woman in self.preferences:
			if not (woman in self.proposed_to):
				return woman
		return None

	def would_rather(self, a, b):
		if self.preferences.index(a) < self.preferences.index(b):
			return True
		else:
			return False

def stable_matching (men, women):
	# Initialize all men and women to free
	free_men_names = []

	men_dict = {}
	for name in men:
		free_men_names.append(name)
		man = Person(name, men[name])
		men_dict[name] = man

	women_dict = {}
	for name in women:
		woman = Person(name, women[name])
		women_dict[name] = woman

	free_man_name = free_men_names.pop()

	# While exists a free man m who still has a woman w to propose to
	while free_man_name:

		# Get highest ranked woman to whom m has not yet proposed
		man = men_dict[free_man_name]
		woman_name = man.find_match_not_proposed()		
		woman = women_dict[woman_name]
		
		# If w is free
		if woman.engaged_to is None:

			# (m, w) become engaged
			woman.engaged_to = free_man_name
			man.engaged_to = woman_name

		else: # some pair (m', w) already exists

			# If w prefers m to m'
			if woman.would_rather(free_man_name, woman.engaged_to):
				# (m, w) become engaged
				ex_man_name = woman.engaged_to
				woman.engaged_to = free_man_name
				man.engaged_to = woman_name

				# m' becomes free
				ex_man = men_dict[ex_man_name]
				ex_man.engaged_to = None
				free_men_names.append(ex_man_name)
			else:
				# m will propose to the next woman
				free_men_names.append(free_man_name)

		man.proposed_to.append(woman_name)

		if free_men_names:
			free_man_name = free_men_names.pop()
		else:
			free_man_name = None

	pairs = []
	for man in men_dict:
		pairs.append([man, men_dict[man].engaged_to])

	return pairs

def print_pair(pair):
	print pair[0] + ' is engaged to ' + pair[1]

if __name__ == '__main__':
	pairs = stable_matching(men, women)

	for pair in pairs:
		print_pair(pair)





