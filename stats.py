from datetime import datetime

class Stats:
    def __init__(self, command: str, id: int):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()
        # self.print_stats()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print(f'\nid: {self.id}')
        print(f'command: {self.command}')
        print(f'response: {self.response}')
        print(f'start_time: {self.start_time}')
        print(f'end_time: {self.end_time}')
        print(f'duration: {self.duration}\n')

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        s = ''
        s +=  f'\nid: {self.id}'
        s += f'command: {self.command}'
        s += f'response: {self.response}'
        s += f'start_time: {self.start_time}'
        s += f'end_time: {self.end_time}'
        s += f'duration: {self.duration}\n'
        return s