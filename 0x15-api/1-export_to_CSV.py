#!/usr/bin/python3
"""create a csv file and store the data inside"""
import csv
import requests
import sys
if __name__ == '__main__':
    """only run code when ran as main"""
    userId = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'
    """
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
            """
    user = requests.get("{}/users/{}".format(url, userId)).json()
    todos = requests.get("{}/todos".format(url)).json()
    for todo in todos:
        if todo.get('userId') == userId:
            # data = ["firstname", "second name", "thirdname"]
            data = ["{}".format(userId), "{}".format(user.get('username')),
                    "{}".format(todo.get('completed')),
                    "{}".format(todo.get('title'))]
            with open('{}.csv'.format(userId), 'a+') as f:
                writer = csv.writer(f, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(data)
