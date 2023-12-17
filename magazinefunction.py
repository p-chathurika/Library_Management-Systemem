from magazinemodel import Magazine

def print_info(magazine):
    print(f"Magazine NO: {magazine.mag_number}, Title: {magazine.title}, print_type: {magazine.print_type}, Subject: {magazine.subject}, Rental Price: {magazine.rental_price}, Available Copies:{magazine.copies}")

class MagazineFunction:
    
    
    def __init__(self):
        self.list_of_magazine = []
        self.__initial_data()

    def __initial_data(self):
        a_magazine1 = Magazine(mag_number="1", title="History of Cricket", print_type="color", subject="Sports", rental_price=5.00, copies=7)
        a_magazine2 = Magazine(mag_number="2", title="Evolution of the Computer", print_type="black&white", subject="Technology", rental_price=3.00, copies=21)
        a_magazine3 = Magazine(mag_number="3", title="History of Music", print_type="white", subject="Science", rental_price=22.50, copies=13)
        self.list_of_magazine.append(a_magazine1)
        self.list_of_magazine.append(a_magazine2)
        self.list_of_magazine.append(a_magazine3)

    def add(self):
        __Mag = input("Enter mag_number:").strip().upper()
        __title = input("title:").strip().upper()
        __print_type = input("print_type:")
        __subject = input("Subject:")
        __rental_price = float(input("rental_price:"))
        __copies = int(input("copies:"))

        a_magazine = Magazine(mag_number=__Mag, title=__title, print_type=__print_type, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_magazine.append(a_magazine)
        print(f"Magazine added {a_magazine.mag_number}-{a_magazine.title}")

    def remove(self):
        __Mag = input("Enter mag_number:")
        matched_data = list(x for x in self.list_of_magazine if x.mag_number == __Mag)
        for x in matched_data:
            self.list_of_magazine.remove(x)
            print("Item Removed.")

    def lend(self):
        __Mag = input("Enter mag_number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_magazine if x.mag_number == __Mag)
        for x in matched_data:
            x.copies -= __copies
            print("Magazine Lent")

    def receive(self):
        __Mag = input("Enter mag_number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_magazine if x.mag_number == __Mag)
        for x in matched_data:
            x.copies += __copies
            print(f"Magazine Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_magazine:
            print_info(magazine=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_magazine if x.copies > 0)
        for x in matched_data:
            print_info(magazine=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_magazine if x.copies == 0)
        for x in matched_data:
            print_info(magazine=x)
