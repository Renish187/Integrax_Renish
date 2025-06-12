class Train:
    def __init__(slf,trainNo):
        slf.trainNo = trainNo
    def book(slf,fro,to):
        print(f"Ticket is booked in train no : {slf.trainNo} from{fro} to {to}")
    def getStatus(slf):
        print(f"Train no:{slf.trainNo} is running on time.")
    def getFare(slf,fro,to):
        print(f"Ticket fare is :",randint(220,700))

a=Train(12345)
a.book(" kanpur","delhi")
a.getStatus()
a.getFare("kanpur","delhi")