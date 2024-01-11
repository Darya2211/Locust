from locust import HttpUser, task, between


class FacebankUser(HttpUser):

    wait_time = between(1, 5)
    host = 'https://demo.facebank.store/'

    @task
    def get_man_page(self):
        self.client.get('')

    @task(2)
    def get_event_page(self):
        self.client.get('events')