__author__ = 'Peng'



class Task_Instance():
    is_active = False
    name = ''

    def __init__(self, name=''):
        self.name = name

    def active(self):
        self.is_active = True
        print(self.name,'is active')

    def inactive(self):
        self.is_active = False
        print(self.name,'is inactive')




