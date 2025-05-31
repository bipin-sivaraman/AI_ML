#!/usr/bin/env python3

'''
CSC500-1: CT7 - A program that describes a course's location, instructor, and meeting time.
'''

course_room = {'CSC101': 3004, 'CSC102': 4501, 'CSC103': 6755, 
               'NET110': 1244, 'COM241': 1411}

course_instructor = {'CSC101': 'Haynes', 'CSC102': 'Alvarado',
                     'CSC103': 'Rich', 'NET110': 'Burke', 'COM241': 'Lee'}

course_meeting_time = {'CSC101': '8:00 a.m.', 'CSC102': '9:00 a.m.',
                       'CSC103': '10:00 a.m.', 'NET110': '11:00 a.m.', 'COM241': '1:00 p.m.'}

class InvalidEntry(Exception):
    pass

def display_course_list():
    '''
    Display's the list of courses and collect user input.
    '''

    print("-"*45)
    print('Select a course number from the below list.\n')

    for course in course_room.keys():
        print(f' - {course}')

    user_selection = input('\nEnter course number: ').upper()

    return user_selection

def print_course_details(choice):
    '''
    Parses the respective dictionaries and return room number, instructor, and meeting time.
    '''

    room_number = course_room[choice]
    instructor = course_instructor[choice]
    meeting_time = course_meeting_time[choice]

    print(f'\nThe course {choice} will be held in Room {room_number}, taught by Professor {instructor}, and will meet at {meeting_time}\n')


if __name__ == "__main__":

    user_input = display_course_list()
    try:
        if user_input not in course_room.keys():
            raise InvalidEntry('Invalid course number')
        
        print_course_details(user_input)
    except InvalidEntry as error:
        print(f'Error: Course {user_input} is an {error}')