from django.db.models import fields
from .models import *
from rest_framework import serializers
import requests

def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def get_guitarra():
    response = generate_request('http://localhost:8000/api/guitarra/')
    if response:
       return response

def get_bajo():
    response = generate_request('http://localhost:8000/api/bajo/')
    if response:
       return response

def get_piano():
    response = generate_request('http://localhost:8000/api/piano/')
    if response:
       return response

def get_percusion():
    response = generate_request('http://localhost:8000/api/percusion/')
    if response:
       return response

def get_amplificador():
    response = generate_request('http://localhost:8000/api/amplificador/')
    if response:
       return response

def get_accesorio():
    response = generate_request('http://localhost:8000/api/accesorio/')
    if response:
       return response

def post_guitarra():
    response = generate_request('http://localhost:8000/api/accesorio/')
    if response:
       return response
 