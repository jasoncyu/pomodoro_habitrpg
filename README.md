pomodoro_habitrpg
=================

HabitRPG Pomodoro Integration

This is a python script to integrate the Pomodoro app of 
http://pomodoro.ugolandini.com/ with [HabitRPG](habitrpg.com).

When you start a pomodoro, a task with that name will be created
on HabitRPG. 

# Instructions
1. Install python requests module by running
    pip install requests
2. Put `putMeInPomodoro.applescript` into the "Start" field of
the Scripts tab in the Pomodoro app.
3. Put `add_habit.py` into `/Applications/Pomodoro.app/Contents/Resources`.

The first line of `add_habit.py` is the location of your Python distribution,
which you can find with `which python`. 
