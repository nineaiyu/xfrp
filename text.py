#!/usr/bin/env python
# -*- coding:utf-8 -*-
# project : xfrp
# filename : text
# author : ly_13
# date : 2022/9/2

import requests
import base64

client_id = 'fWzuaVXD1oBswLXimATGdMoEQwhnwFU0hUtvQsse'
client_secret = 'FVydhrPnhcXoT3tuEaqqiDXgOHBT72fDuPK0YvnwDMD7bAg9lOlSRQlGGaYrRPzPO1Jp3ks9DSTsVVz0tarrsjjJYfbo0kCBMmf5yePAMblaevtQlXGmGVFvjbwIhDqj'

credential = f"{client_id}:{client_secret}"

b_token = base64.b64encode(credential.encode("utf-8"))

print(b_token, b_token.decode())


def get_access_token():
    data = {
        'grant_type': 'client_credentials'
    }
    headers = {
        'Authorization': f'Basic {b_token.decode()}'
    }
    req = requests.post('http://127.0.0.1:8000/o/token/', data=data, headers=headers)
    print(req.json())


def remove_token(token):
    data = {
        'token': token,
        'client_id': client_id,
        'client_secret': client_secret
    }

    req = requests.post('http://127.0.0.1:8000/o/revoke_token/', data=data)
    print(req.content, req.status_code)


def test_token(token):

    headers = {
        'Authorization': f'Bearer  {token}'
    }
    req = requests.get('http://localhost:8000/users/',  headers=headers)
    print(req.content, req.status_code)

test_token('P8uaDFf9xwqKeIqdFaR3b7BRdp6kjE')