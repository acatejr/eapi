from locust import HttpLocust, TaskSet

def raingages(l):
    l.client.get("/graphql?query={%0A%20 raingages {%0A%20%20%20 code%0A%20%20%20 name%0A%20%20%20 latitude%0A%20%20%20 longitude%0A%20 }%0A}&operationName=null")

class GraphQlBehavior(TaskSet):
    tasks = {raingages: 1}

class WebsiteUser(HttpLocust):
    task_set = GraphQlBehavior
    min_wait = 5000
    max_wait = 9000
