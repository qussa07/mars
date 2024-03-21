import requests
import json

from requests import post

print(requests.get(f'http://127.0.0.1:5000/api/jobs').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/1').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/12321312').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/asdasdasdas').json())


"""print(post('http://127.0.0.1:5000/api/jobs', json={}).json())

print(post('http://127.0.0.1:5000/api/jobs',
           json={'job': 'Заголовок'}).json())"""

print(post('http://127.0.0.1:5000/api/jobs',
           json={'job': 'Заголовок',
                 'team_leader': 1,
                 'collaborators': 'Текст новости',
                 'work_size': 1,
                 'is_finished': False}).json())

'''print(requests.get(f'http://127.0.0.1:5000/api/jobs/1').json())
print(requests.delete('http://127.0.0.1:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(requests.delete('http://localhost:5000/api/jobs/1').json())
print(requests.get(f'http://127.0.0.1:5000/api/jobs/1').json())'''

print(requests.put('http://localhost:5000/api/jobs/1'))
