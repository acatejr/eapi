from locust import HttpLocust, TaskSet

def raingages(l):
    l.client.get("/api/srer/v1.0/raingages")


class RestBehavior(TaskSet):
    tasks = {raingages: 1}

class WebsiteUser(HttpLocust):
    task_set = RestBehavior
    min_wait = 5000
    max_wait = 9000
