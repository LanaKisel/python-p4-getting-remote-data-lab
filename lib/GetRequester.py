import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response=requests.get(self.url)
        return response.content

    def load_json(self):
        body_responses_list =[]
        body_responses= json.loads(self.get_response_body())
        for body_response in body_responses:
            body_responses_list.append(body_response)
        return body_responses_list
