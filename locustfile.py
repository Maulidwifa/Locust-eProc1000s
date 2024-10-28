from locust import HttpUser, task, between
from login import LoginTask 
from listUserManagement import  *

class MyUser:
    wait_time = between(1, 3)

    @task
    def login(self):
        LoginTask(self).login(self)

    @task
    def listUser(self):
        ListUserManajement(self).listUser(self)
        
    