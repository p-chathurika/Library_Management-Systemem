from educationaldvdmodel import EducationalDVD

def print_info(dvd):
    print(f"dvd NO: {dvd.dvd_number}, Title: {dvd.title},  Subject: {dvd.subject}, Rental Price: {dvd.rental_price}, Available Copies:{dvd.copies}")

class EducationalDVDFunction:
    
    def __init__(self):
        self.list_of_dvd = []
        self.__initial_data()

    def __initial_data(self):
        a_dvd1 = EducationalDVD(dvd_number="10", title="Birth of the Solar System",  subject="Astronomy", rental_price=2.50, copies=10)
        a_dvd2 = EducationalDVD(dvd_number="11", title="Pythagoras Theorem",  subject="Math", rental_price=1.00, copies=50)
        a_dvd3 = EducationalDVD(dvd_number="12", title="Humen resorces",  subject="Science", rental_price=2.50, copies=30)
        self.list_of_dvd.append(a_dvd1)
        self.list_of_dvd.append(a_dvd2)
        self.list_of_dvd.append(a_dvd3)

    def add(self):
        __dv = input("Enter dvd_number:").strip().upper()
        __title = input("title:").strip().upper()
    
        __subject = input("Subject:")
        __rental_price = float(input("rental_price:"))
        __copies = int(input("copies:"))

        a_dvd = EducationalDVD(dvd_number=__dv, title=__title,  subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_dvd.append(a_dvd)
        print(f"EducationalDVD added {a_dvd.dvd_number}-{a_dvd.title}")

    def remove(self):
        __dv = input("Enter dvd_number:")
        matched_data = list(x for x in self.list_of_dvd if x.dvd_number == __dv)
        for x in matched_data:
            self.list_of_dvd.remove(x)
            print("Item Removed.")

    def lend(self):
        __dv = input("Enter dvd_number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_dvd if x.dvd_number == __dv)
        for x in matched_data:
            x.copies -= __copies
            print("EducationalDVD Lent")

    def receive(self):
        __dV = input("Enter dvd_number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_dvd if x.dvd_number == __dV)
        for x in matched_data:
            x.copies += __copies
            print(f"EducationalDVD Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_dvd:
            print_info(dvd=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_dvd if x.copies > 0)
        for x in matched_data:
            print_info(dvd=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_dvd if x.copies == 0)
        for x in matched_data:
            print_info(dvd=x)

