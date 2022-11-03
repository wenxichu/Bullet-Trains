import inquirer
from boarding import Passenger, system, date_today
from bullet_train import Japanese, French, Chinese, Korean, Italian

print("\n      ==== Metro City Train Station ====")
print("\x1B[3m" + "Take a ride on the fastest trains in the world!" + "\x1B[0m\n")
print(date_today() + "\n")


class MainMenu:
    def __init__(self):
        while True:
            home_screen()


def add_ticket(queue, train_type):
    print("Enter a passenger's ticket information in the fields below.\n")

    ticket = [
        inquirer.Text("country", message="Country"),
        inquirer.Text("name", message="Name"),
        inquirer.Text("seat_num", message="Seat No"),
        inquirer.Text("departure", message="Departure"),
        inquirer.Text("arrival", message="Arrival"),
        inquirer.Text("cost", message="Price"), ]

    answers = inquirer.prompt(ticket)
    new_person = Passenger(answers["country"], answers["name"], answers["seat_num"], answers["departure"],
                           answers["arrival"], answers["cost"])

    queue.add_passenger(new_person)
    train_type.add_entry(answers["name"])
    print("\nA ticket has been added to the registry.\n")


def show_depart(train_type):
    t = train_type.table
    d = train_type.times
    depart_menu = [
        inquirer.List("options",
                      message="Select One",
                      choices=["Check Status", "Go Back"],
                      carousel=False), ]

    choice = inquirer.prompt(depart_menu)["options"]
    train_type.change_status(t, d)

    if choice == "Check Status":
        train_type.get_status()
    elif choice == "Go Back":
        return


def show_status(train_type):
    status_menu = [
        inquirer.List("options",
                      message="Select One",
                      choices=["Remove Inactive", "Delete All", "Go Back"],
                      carousel=False), ]

    choice = inquirer.prompt(status_menu)["options"]

    if choice == "Remove Inactive":
        for p in train_type.table:
            if p[2] != "Active":
                train_type.table.remove(p)
    elif choice == "Delete All":
        train_type.table.clear()
    elif choice == "Go Back":
        return


def register_menu(queue, train_type):
    ticket_menu = [
        inquirer.List("options",
                      message="Select One",
                      choices=["Add Entry", "Remove First", "Delete All", "Go Back"],
                      carousel=False
                      ),
    ]

    choice = inquirer.prompt(ticket_menu)["options"]

    try:
        if choice == "Add Entry":
            add_ticket(queue, train_type)
        elif choice == "Remove First":
            queue.remove_passenger()
            train_type.table[0][2] = "Canceled"
        elif choice == "Delete All":
            queue.delete_all()
            for t in range(len(train_type.table)):
                train_type.table[t][2] = "Canceled"
        elif choice == "Go Back":
            return
    except IndexError:
        print("The train queue is empty! Try something else.\n")
        return


def train_gui(train_name, train_type):
    print(f"The local time is {train_type.get_time()}.\n")
    while True:
        main_menu = [
            inquirer.List("actions",
                          message="What do you want to do?",
                          choices=["Set Departure Time", "View Ticket Status", "Ticket Registration", "Go Back"],
                          carousel=False), ]

        action = inquirer.prompt(main_menu)["actions"]
        queue = system(train_name)

        if action == "Set Departure Time":
            try:
                train_type.set_departure()
                show_depart(train_type)
            except ValueError:
                print("Error: Time should be in 0:00 AM/PM format.\n")
        elif action == "View Ticket Status":
            train_type.get_status()
            show_status(train_type)
        elif action == "Ticket Registration":
            queue.print_record()
            register_menu(queue, train_type)
        elif action == "Go Back":
            break


def home_screen():
    bullet_trains = [
        inquirer.List("train",
                      message="Which train are you going to look at?",
                      choices=["L0 Series Maglev", "TGV POS", "Shanghai Maglev", "HEMU-430X", "Frecciarossa 1000",
                               "Exit Menu"], carousel=False), ]

    answer = inquirer.prompt(bullet_trains)["train"]

    if answer == "L0 Series Maglev":
        print(f"L0 Series Maglev"
              f"\nSpeed: 374 mph"
              f"\nCountry: Japan\n")
        japan = Japanese()
        train_gui(answer, japan)
    elif answer == "TGV POS":
        print(f"TGV POS"
              f"\nSpeed: 357 mph"
              f"\nCountry: France\n")
        france = French()
        train_gui(answer, france)
    elif answer == "Shanghai Maglev":
        print(f"Shanghai Maglev"
              f"\nSpeed: 268 mph"
              f"\nCountry: China\n")
        china = Chinese()
        train_gui(answer, china)
    elif answer == "HEMU-430X":
        print(f"HEMU-430X"
              f"\nSpeed: 262 mph"
              f"\nCountry: South Korea\n")
        korea = Korean()
        train_gui(answer, korea)
    elif answer == "Frecciarossa 1000":
        print(f"Frecciarossa 1000"
              f"\nSpeed: 245 mph"
              f"\nCountry: Italy\n")
        italy = Italian()
        train_gui(answer, italy)
    elif answer == "Exit Menu":
        exit()


MainMenu()
