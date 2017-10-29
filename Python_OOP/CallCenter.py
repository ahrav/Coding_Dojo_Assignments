class call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print "ID: {}".format(self.unique_id)
        print "Name: {}".format(self.caller_name)
        print "Phone number: {}".format(self.caller_phone_number)
        print "Time of call: {}".format(self.time_of_call)
        print "Reason for call: {}".format(self.reason_for_call)

call1 = call(2, 'bob', 1, 2, 'sad')

class call_center(call):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def add(self):
        self.calls.append(call.caller_name)
        self.queue_size = len(self.calls)
        return self

    def remove(self):
        self.calls.pop(0)
        return self

c = call_center()
c.add()
print c.calls
