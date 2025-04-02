
import random as r

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, trainNo, fromDest, toDest):
        print(f"Ticket is booked in train number {trainNo} from {fromDest} to {toDest}")

    def getStatus(self, trainNo):
        print(f"{trainNo} is running on time")

    def getFare(self, trainNo, fromDest, toDest):
        print(f"Ticket fair of train number {trainNo} from {fromDest} to {toDest} is {r.randint(1, 555)}")



t = Train(12345)
t.book(12345, "Rampur", "Delhi")
t.getStatus(12345)
t.getFare(12345, "Rampur", "Dehi")