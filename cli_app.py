import argparse
import requests
import json

# Define the endpoint for your Flask server
BASE_URL = 'http://127.0.0.1:5000'

# These methods format the arguments and make the appropriate requests to the server
def getAllStudents():
    response = requests.get(f'{BASE_URL}/students')
    if response.status_code == 200:
        students = response.json()
        for student in students:
            print(student)
    else:
        print(f'Error fetching students: {response.status_code} - {response.text}')

def addStudent(args):
    data = {
        'first_name': args.first_name,
        'last_name': args.last_name,
        'email': args.email,
        'enrollment_date': args.enrollment_date
    }
    response = requests.post(f'{BASE_URL}/students', json=data)
    if response.status_code == 200:
        print('Student added successfully.')
    else:
        print(f'Error adding student: {response.status_code} - {response.text}')

def updateStudentEmail(args):
    data = {'email': args.new_email}
    response = requests.put(f'{BASE_URL}/students/{args.student_id}', json=data)
    if response.status_code == 200:
        print('Email updated successfully.')
    else:
        print(f'Error updating email: {response.status_code} - {response.text}')

def deleteStudent(args):
    response = requests.delete(f'{BASE_URL}/students/{args.student_id}')
    if response.status_code == 200:
        print('Student deleted successfully.')
    else:
        print(f'Error deleting student: {response.status_code} - {response.text}')

if __name__ == "__main__":
    # Argument parsing logic for the CLI input
    parser = argparse.ArgumentParser(description='CRUD operations for students.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Subparser for the getAllStudents command
    parser_get_all = subparsers.add_parser('getall', help='Get all students')

    # Subparser for the addStudent command
    parser_add = subparsers.add_parser('add', help='Add a new student')
    parser_add.add_argument('--first_name', required=True, help='First name of the student')
    parser_add.add_argument('--last_name', required=True, help='Last name of the student')
    parser_add.add_argument('--email', required=True, help='Email of the student')
    parser_add.add_argument('--enrollment_date', required=True, help='Enrollment date of the student (YYYY-MM-DD)')

    # Subparser for the updateStudentEmail command
    parser_update = subparsers.add_parser('update', help='Update a student email')
    parser_update.add_argument('--student_id', type=int, required=True, help='ID of the student')
    parser_update.add_argument('--new_email', required=True, help='New email for the student')

    # Subparser for the deleteStudent command
    parser_delete = subparsers.add_parser('delete', help='Delete a student')
    parser_delete.add_argument('--student_id', type=int, required=True, help='ID of the student to delete')

    args = parser.parse_args()

    if args.command == 'getall':
        getAllStudents()
    elif args.command == 'add':
        addStudent(args)
    elif args.command == 'update':
        updateStudentEmail(args)
    elif args.command == 'delete':
        deleteStudent(args)
    else:
        parser.print_help()