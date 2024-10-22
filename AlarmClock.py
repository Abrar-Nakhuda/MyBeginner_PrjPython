#AlarmClock
import time # we'll be updating the time every second
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "AlarmClockSound.mps"

if __name__ == "__main__":
    alarm_time = input("enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)

