# assignment title
print "\n----------Assignment: Call Center----------\n"

# create class: "Call"
class Call(object):
	# this method to run every time a new call is instantiated
	def __init__(self, unique_id, name, phone_num, time, reason):
		self.id = unique_id
		self.name = name
		self.phone_num = phone_num
		self.time = time
		self.reason = reason

	# displays call info
	def displayCall(self):
		print "ID: {}".format(self.id)
		print "Name: {}".format(self.name)
		print "Phone number: {}".format(self.phone_num)
		print "Time called: {}".format(self.time)
		print "Reason for calling: {}".format(self.reason)
		return self

# create instances of Call class
caller1 = Call(242, "Devin", "650-242-1311", "5:30", "no reason")
caller2 = Call(243, "Darren", "650-353-3511", "6:30", "for a reason")

# create CallCenter class
class CallCenter(object):
	def __init__(self):
		# create empty list
		self.call_list = []
		self.queue_size = 0
		print "\n-----Call List-----"

	# adds new call to list
	def addCall(self, new_call):
		# if new calls are in a list iterate through the list and append to 'call_list' and increase queue
		if type(new_call) == list:
			for call in range(0, len(new_call)):
				self.call_list.append(new_call[call])
				self.queue_size += 1
		# if new calls aren't in a list append to 'call_list' and increase queue
		else:
			self.call_list.append(new_call)
			self.queue_size += 1
		return self

	# removes first call from 'call_list' and updates
	def remCall(self):
		del self.call_list[0]
		print "\n\n-----Updated Call List-----"
		self.queue_size -= 1
		return self

	# displays call list
	def display(self):
		call_count = 0
		for new_call in self.call_list:
			call_count += 1
			print "\nCall: #{}\nName: {}\nPhone number: {}\n".format(call_count, new_call.name, new_call.phone_num)
		print "Queue Size: {}".format(self.queue_size)
		
# create instance of class: "CallCenter"
call_center1 = CallCenter()

# gives each instance some instructions through CallCenter's methods
call_center1.addCall([caller1, caller2]).display()
call_center1.remCall().display()

# end separator
print ""