from lecturecdmodel import LectureCD

def print_info(CD):
    print(f"Cd NO: {CD.cd_number}, Title: {CD.title},  Subject: {CD.subject}, Rental Price: {CD.rental_price}, Available Copies:{CD.copies}")

class LectureCDFunction:
    
    def __init__(self):
        self.list_of_CD = []
        self.__initial_data()

    def __initial_data(self):
        a_CD1 = LectureCD(cd_number="21", title="Basics of Western Music",  subject="Music", rental_price=1.50, copies=11)
        a_CD2 = LectureCD(cd_number="22", title="Japanese Language",  subject="Foreign Languages", rental_price=2.00, copies=3)
        a_CD3 = LectureCD(cd_number="55", title="biologyical resorces",  subject="Science", rental_price=3.50, copies=20)
        self.list_of_CD.append(a_CD1)
        self.list_of_CD.append(a_CD2)
        self.list_of_CD.append(a_CD3)

    def add(self):
        __cd = input("Enter cd_number:").strip().upper()
        __title = input("title:").strip().upper()
    
        __subject = input("Subject:")
        __rental_price = float(input("rental_price:"))
        __copies = int(input("copies:"))

        a_CD = LectureCD(cd_number=__cd, title=__title,  subject=__subject, rental_price=__rental_price, copies=__copies)
        self.list_of_CD.append(a_CD)
        print(f"lectureCD added {a_CD.cd_number}-{a_CD.title}")

    def remove(self):
        __cd = input("Enter cd_number:")
        matched_data = list(x for x in self.list_of_CD if x.cd_number == __cd)
        for x in matched_data:
            self.list_of_CD.remove(x)
            print("Item Removed.")

    def lend(self):
        __cd = input("Enter cd_number:")
        __copies = int(input("enter lend copies:"))
        matched_data = list(x for x in self.list_of_CD if x.cd_number == __cd)
        for x in matched_data:
            x.copies -= __copies
            print("lectureCD Lent")

    def receive(self):
        __cd = input("Enter cd_number:")
        __copies = int(input("enter receive copies:"))
        matched_data = list(x for x in self.list_of_CD if x.cd_number == __cd)
        for x in matched_data:
            x.copies += __copies
            print(f"lectureCD Received with {__copies} Copies")

    def display_all(self):
        for x in self.list_of_CD:
            print_info(CD=x)

    def display_available(self):
        matched_data = list(x for x in self.list_of_CD if x.copies > 0)
        for x in matched_data:
            print_info(CD=x)

    def display_unavailable(self):
        matched_data = list(x for x in self.list_of_CD if x.copies == 0)
        for x in matched_data:
            print_info(CD=x)
