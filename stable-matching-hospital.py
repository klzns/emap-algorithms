# Stable Matching - Gale-Shapley Algorithm
# for the hospital problem

hospitals = {
	'Saint Paul Hospital': {
		'preferences': ['Jen', 'Nic', 'Lis', 'Tom'],
		'positions': 1,
	},
	'University Hospital': {
		'preferences': ['Nic', 'Lis', 'Tom', 'Jen'],
		'positions': 2,
	},
	'Grand Central Hospital': {
		'preferences': ['Jen', 'Tom', 'Lis', 'Nic'],
		'positions': 1
	}
}

students = {
	'Jen': ['Saint Paul Hospital', 'University Hospital', 'Grand Central Hospital'],
	'Lis': ['Grand Central Hospital', 'University Hospital', 'Saint Paul Hospital'],
	'Nic': ['University Hospital', 'Grand Central Hospital', 'Saint Paul Hospital'],
	'Tom': ['Grand Central Hospital', 'University Hospital', 'Saint Paul Hospital']
}


class Hospital:
	def __init__(self, name, positions, preferences):
		self.name = name
		self.preferences = preferences
		self.positions = positions
		self.open_positions = positions

		self.students_assigned = []
		self.proposed_to = []

	def find_match_not_proposed(self):
		for student in self.preferences:
			if not (student in self.proposed_to):
				return student
		return None

	def assign(self, student):
		self.students_assigned.append(student)
		self.open_positions = self.open_positions - 1

	def kick(self, student):
		self.students_assigned.remove(student)
		self.open_positions = self.open_positions + 1


class Student:
	def __init__(self, name, preferences):
		self.name = name
		self.preferences = preferences

		self.assigned_to = None

	def would_rather(self, a, b):
		if self.preferences.index(a) < self.preferences.index(b):
			return True
		else:
			return False


def stable_matching (hospitals, students):
	# Initialize all hospitals and studens free
	available_hospitals = []

	hospitals_dict = {}
	for name in hospitals:
		available_hospitals.append(name)
		positions = hospitals[name]['positions']
		preferences = hospitals[name]['preferences']
		hospital = Hospital(name, positions, preferences)
		hospitals_dict[name] = hospital

	students_dict = {}
	for name in students:
		student = Student(name, students[name])
		students_dict[name] = student

	available_hospital = available_hospitals.pop()

	# While exists a hospital whith an open position
	while available_hospital:

		# Get highest ranked student to whom h has not yet proposed
		hospital = hospitals_dict[available_hospital]
		student_name = hospital.find_match_not_proposed()		
		student = students_dict[student_name]
		
		# If s is free
		if student.assigned_to is None:

			# (h, s) become engaged
			student.assigned_to = available_hospital
			hospital.assign(student_name)

		else: # some pair (h', s) already exists

			# If s prefers h to h'
			if student.would_rather(available_hospital, student.assigned_to):
				# (h, s) become engaged
				former_hospital_name = student.assigned_to
				student.assigned_to = available_hospital
				hospital.assign(student_name)

				# h' lose student
				former_hospital = hospitals_dict[former_hospital_name]
				former_hospital.kick(student_name)
				available_hospitals.append(former_hospital_name)

		hospital.proposed_to.append(student_name)

		# If hospital still have an open position
		if hospital.open_positions > 0:
			available_hospitals.append(hospital.name)

		if available_hospitals:
			available_hospital = available_hospitals.pop()
		else:
			available_hospital = None

	pairs = []
	# Make pairs array
	for hospital in hospitals_dict:
		pairs.append([hospital, hospitals_dict[hospital].students_assigned])

	return pairs


def print_pair(pair):
	print pair[0] + ' students:'
	# Print in a nice english
	if len(pair[1]) > 1:
		last = pair[1][-1]
		rest = pair[1][0:(len(pair[1])-1)]
		print '- ' + (', '.join(rest)) + ' and '+ str(last) + '.'
	else:
		print '- ' + pair[1][0] + '.'


if __name__ == '__main__':
	pairs = stable_matching(hospitals, students)

	for pair in pairs:
		print_pair(pair)

		