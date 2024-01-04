#!/usr/bin/python3
"""script to get information about an employee using rest api"""
import requests
import sys
if __name__ == '__main__':
    """only run code when ran as main"""
    userId = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get("{}/{}".format(url, userId))
    name = response.json().get('name')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    notCompleted = 0
    completed = 0
    for todo in todos.json():
        if todo.get('userId') == userId:
            if todo.get('completed'):
                completed += 1
            else:
                notCompleted += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        name, completed, (completed + notCompleted))
    )
    for todo in todos.json():
        if todo.get('userId') == userId and \
                todo.get('completed'):
            print('\t {}'.format(todo.get('title')))
