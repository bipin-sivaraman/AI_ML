#!/usr/bin/env python3

"""
CSC500-1: CT3 (Part 2) - Program to create a 24-hour clock with alarm

"""

# Create an array to hold 24 hours
valid_hours = [f"{hours}:00" for hours in range(24)]

current_time = int(input('Enter the current time (in 24-hour format): '))
if current_time < 24:
    set_alarm = int(input('Set the alarm after (in hours): '))

    # Calculate the time remaining for the alarm
    alarm = (current_time + set_alarm) % 24

    print(f"Alarm set for {valid_hours[alarm]} hours")
else:
    print("Invalid time entered")