class Subject:

    def __init__(self):
        self._observers = []

    def attach(self,observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self,observer):
        self._observers.remove(observer)

    def notify(self,modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self,name = ""):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data = value
        self.notify()

class HexViewer:
    def update(self, subject):
        print('HexViewer: Subject {} has data 0x{:x}'.format(subject.name, subject.data))

class OctalViewer:
    def update(self, subject):
        print('OctalViewer: Subject' + str(subject.name) + 'has data ' + str(oct(subject.data)))

class DecimalViewer:
    def update(self, subject):
        print('DecimalViewer: Subject % s has data % d' % (subject.name, subject.data))

if __name__ == "__main__":

    obj1 = Data("Data1")
    obj2 = Data("Data2")

    view1 = HexViewer()
    view2 = OctalViewer()
    view3 = DecimalViewer()

    obj1.attach(view1)
    obj1.attach(view2)
    obj1.attach(view3)

    obj2.attach(view1)
    obj2.attach(view2)
    obj2.attach(view3)

    obj1.data = 10
    obj2.data = 20