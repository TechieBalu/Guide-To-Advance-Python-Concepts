import requests

data = {
    'value1': 'abc',
    'value2': 123
}

response = requests.post('http://localhost:5000/process_data', json=data)
