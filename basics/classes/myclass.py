class MyRouter(object):
    "This is a class that describes the characteristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios

    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The serial numberr of: ", self.serialno)
        print("The IOS version is: ", self.ios)
        print("The model and date combined: ", self.model + manuf_date)

router1 = MyRouter("R1", "2600", "123456", "12.4")
router1.print_router("2018-10-10")

router2 = MyRouter("R2", "7200", "123456", "12.3")
router2.print_router("2018-10-10")

setattr(router2, "ios", "12.4")
router2.print_router("2018-10-10")

router2.ios = "12.3"
router2.print_router("2018-10-10")

print(hasattr(router2, "ios"))

delattr(router2, "ios")

print(isinstance(router2, MyRouter))

class MyNewRouter(MyRouter):
    def __init__(self, routername, model, serialno, ios, portsno):
        MyRouter.__init__(self, routername, model, serialno, ios)
        self.portsno = portsno

    def print_new_router(self, string):
        print(string + self.model)

new_router1 = MyNewRouter("newr1", "1800", "111111", "12.2", "10")
print(new_router1.portsno)

print(new_router1.model)
print(new_router1.ios)

new_router1.print_router("asdfassdf")

print(issubclass(MyNewRouter, MyRouter))

