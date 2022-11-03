import pytz
from tabulate import tabulate
from datetime import datetime
from boarding import BulletTrain


class Japanese(BulletTrain):
    table = [["Hanako", "01:00 PM", "Active"]]
    times = None

    def __init__(self):
        self.train = "L0 Series Maglev"
        self.status = "Active"
        self.arrival_time = datetime.now(pytz.timezone("Asia/Tokyo"))
        self.departure_time = 0

    def __str__(self):
        return "Japan"

    def add_entry(self, name):
        local_time = self.arrival_time.strftime("%I:%M %p")
        Japanese.table.append([name, local_time, self.status])

    @classmethod
    def del_entry(cls):
        Japanese.table.pop(0)

    def get_time(self):
        return self.arrival_time.strftime("%I:%M %p")

    @classmethod
    def get_status(cls):
        headers = ["Passenger Name", "Time of Arrival", "Ticket Status"]
        print(tabulate(Japanese.table, headers, tablefmt="github"))

    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        self.departure_time = datetime.strptime(question, "%I:%M %p")
        print(f"\nThe train will depart at {self.departure_time}.\n")
        Japanese.times = self.departure_time


class French(BulletTrain):
    table = [["Marie", "12:00 PM", "Active"]]
    times = None

    def __init__(self):
        self.train = "TGV POS"
        self.status = "Active"
        self.arrival_time = datetime.now(pytz.timezone("Europe/Paris"))
        self.departure_time = 0

    def __str__(self):
        return "France"

    def add_entry(self, name):
        local_time = self.arrival_time.strftime("%I:%M %p")
        French.table.append([name, local_time, self.status])

    @classmethod
    def del_entry(cls):
        French.table.pop(0)

    def get_time(self):
        return self.arrival_time.strftime("%I:%M %p")

    @classmethod
    def get_status(cls):
        headers = ["Passenger Name", "Time of Arrival", "Ticket Status"]
        print(tabulate(French.table, headers, tablefmt="github") + "\n")

    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        self.departure_time = datetime.strptime(question, "%I:%M %p")
        print(f"\nThe train will depart at {self.departure_time}.\n")
        French.times = self.departure_time


class Chinese(BulletTrain):
    table = [["Wenxi", "03:00 PM", "Active"]]
    times = None

    def __init__(self):
        self.train = "Shanghai Maglev"
        self.status = "Active"
        self.arrival_time = datetime.now(pytz.timezone("Asia/Shanghai"))
        self.departure_time = 0

    def __str__(self):
        return "China"

    def add_entry(self, name):
        local_time = self.arrival_time.strftime("%I:%M %p")
        Chinese.table.append([name, local_time, self.status])

    @classmethod
    def del_entry(cls):
        Chinese.table.pop(0)

    def get_time(self):
        return self.arrival_time.strftime("%I:%M %p")

    @classmethod
    def get_status(cls):
        headers = ["Passenger Name", "Time of Arrival", "Ticket Status"]
        print(tabulate(Chinese.table, headers, tablefmt="github") + "\n")

    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        self.departure_time = datetime.strptime(question, "%I:%M %p")
        print(f"\nThe train will depart at {self.departure_time}.\n")
        Chinese.times = self.departure_time


class Korean(BulletTrain):
    table = [["Daewon", "11:00 AM", "Active"]]
    times = None

    def __init__(self):
        self.train = "HEMU-430X"
        self.status = "Active"
        self.arrival_time = datetime.now(pytz.timezone("Asia/Seoul"))
        self.departure_time = 0

    def __str__(self):
        return "South Korea"

    def add_entry(self, name):
        local_time = self.arrival_time.strftime("%I:%M %p")
        Korean.table.append([name, local_time, self.status])

    @classmethod
    def del_entry(cls):
        Korean.table.pop(0)

    def get_time(self):
        return self.arrival_time.strftime("%I:%M %p")

    @classmethod
    def get_status(cls):
        headers = ["Passenger Name", "Time of Arrival", "Ticket Status"]
        print(tabulate(Korean.table, headers, tablefmt="github") + "\n")

    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        self.departure_time = datetime.strptime(question, "%I:%M %p")
        print(f"\nThe train will depart at {self.departure_time}.\n")
        Korean.times = self.departure_time


class Italian(BulletTrain):
    table = [["Lorenzo", "10:00 AM", "Active"]]
    times = None

    def __init__(self):
        self.train = "Frecciarossa 1000"
        self.status = "Active"
        self.arrival_time = datetime.now(pytz.timezone("Europe/Rome"))
        self.departure_time = 0

    def __str__(self):
        return "Italy"

    def add_entry(self, name):
        local_time = self.arrival_time.strftime("%I:%M %p")
        Italian.table.append([name, local_time, self.status])

    @classmethod
    def del_entry(cls):
        Italian.table.pop(0)

    def get_time(self):
        return self.arrival_time.strftime("%I:%M %p")

    @classmethod
    def get_status(cls):
        headers = ["Passenger Name", "Time of Arrival", "Ticket Status"]
        print(tabulate(Italian.table, headers, tablefmt="github") + "\n")

    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        self.departure_time = datetime.strptime(question, "%I:%M %p")
        print(f"\nThe train will depart at {self.departure_time}.\n")
        Italian.times = self.departure_time
