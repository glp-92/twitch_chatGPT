'''
Created on 13 jun. 2022

@author: Guille
@comment: gpt API integrated on python
'''


import json
from urllib import request


class gpt():


    def __init__(self, data):
        self.endpoint = data['gpt']['endpoint']
        self.headers = [
            ['Content-Type', 'application/json'],
            ['Authorization', data['gpt']['token']]
        ]


    def send_request(self, prompt, limit = 150):
        req = request.Request(self.endpoint, method="POST")
        for header in self.headers:
            req.add_header(header[0], header[1])
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": f"user", "content": f"{prompt}. Intenta limitar la respuesta a {limit} caracteres."}] 
        }
        payload = json.dumps(payload)
        payload = payload.encode()
        r = request.urlopen(req, data = payload)
        content = json.loads((r.read()).decode('utf-8'))
        return (content["choices"][0]["message"]["content"]).replace("\n", " ")