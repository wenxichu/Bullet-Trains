import time
from abc import ABC, abstractmethod
from datetime import datetime, date


class Passenger:
    def __init__(self, country, name, seat_num, departure, arrival, cost):
        self.country = country
        self.name = name
        self.seat_num = seat_num
        self.departure = departure
        self.arrival = arrival
        self.cost = cost
        self.next = None

    def show_info(self):
        print(f"Name: {self.name}   Seat No: {self.seat_num}   From: {self.departure}   To: {self.arrival}  "
              f" Price: {self.cost} {self.currency()}")
        return " "

    def currency(self):
        if self.country == "Japan":
            return "YEN"
        elif self.country == "France" or self.country == "Italy":
            return "EUR"
        elif self.country == "China":
            return "RMB"
        elif self.country == "South Korea":
            return "WON"
        else:
            return "USD"


def date_today():
    today = date.today()
    date1 = today.strftime("%m/%d/%Y")
    message = "Today's date is {}".format(date1)
    return message


class BulletTrain(ABC):
    # Local Time
    @abstractmethod
    def get_time(self):
        local_time = time.localtime()
        clock = time.strftime("%H:%M:%S", local_time)
        print(f"The local time is: {clock}")

    # Passenger Status
    @staticmethod
    def change_status(records, depart_time):
        for t in records:
            arrive_time = datetime.strptime(t[1], "%I:%M %p")
            if arrive_time > depart_time:
                t[2] = "Missed"
            else:
                t[2] = "Active"

    # Departure Time
    @abstractmethod
    def set_departure(self):
        question = input("Set the departure time (e.g. 12:00 AM): ")
        departure_time = datetime.strptime(question, "%I:%M %p").time()
        return departure_time


class Bookings:
    def __init__(self, ticket):
        new_ticket = ticket
        self.records = [ticket]
        self.first_person = new_ticket
        self.last_person = new_ticket
        self.length = 1

    def empty_train(self):
        if not self.records:
            return True
        else:
            return False

    def print_record(self):
        pointer = self.first_person
        while pointer is not None:
            pointer.show_info()
            pointer = pointer.next

    def add_passenger(self, ticket):
        self.records.append(ticket)
        new_passenger = ticket
        if self.first_person is None:
            self.first_person = new_passenger
            self.last_person = new_passenger
        else:
            self.last_person.next = new_passenger
            self.last_person = new_passenger
        self.length += 1

    def remove_passenger(self):
        if self.empty_train():
            return "This passenger is not in the registry."
        pointer = self.first_person
        self.records.pop(0)
        if self.length == 1:
            self.first_person = None
            self.last_person = None
        else:
            self.first_person = self.first_person.next
            pointer.next = None
        self.length -= 1
        return pointer

    def latest_entry(self):
        if self.empty_train():
            print("There are no passengers on the train.")
        else:
            newest = self.records[self.length-1]
            newest.show_info()

    def delete_all(self):
        while self.records:
            self.remove_passenger()
        self.length = 0


def system(train):
    if train == "L0 Series Maglev":
        return j_entries
    if train == "TGV POS":
        return f_entries
    if train == "Shanghai Maglev":
        return c_entries
    if train == "HEMU-430X":
        return k_entries
    if train == "Frecciarossa 1000":
        return i_entries


japan_queue = Passenger("Japan", "Hanako", "A-1", "Tokyo", "Osaka", 120)
j_entries = Bookings(japan_queue)

france_queue = Passenger("France", "Marie", "B-2", "Paris", "Reims", 80)
f_entries = Bookings(france_queue)

china_queue = Passenger("China", "Wenxi", "C-3", "Shanghai", "Hangzhou", 90)
c_entries = Bookings(china_queue)

korea_queue = Passenger("South Korea", "Daewon", "D-4", "Chongju", "Seoul", 110)
k_entries = Bookings(korea_queue)

italy_queue = Passenger("Italy", "Lorenzo", "E-5", "Florence", "Rome", 100)
i_entries = Bookings(italy_queue)
