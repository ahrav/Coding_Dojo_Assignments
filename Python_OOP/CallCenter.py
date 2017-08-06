class call(object):
    def __init__(self, unique_id, caller_name, caller_phone_number, time_of_call, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone_number = caller_phone_number
        self.time_of_call = time_of_call
        self.reason_for_call = reason_for_call
    def display(self):
        print self.unique_id
        print self.caller_name
        print self.caller_phone_number
        print self.time_of_call
        print self.reason_for_call

class call_center(object):
    def __init__(self, calls, queue_size):
        self.calls =
