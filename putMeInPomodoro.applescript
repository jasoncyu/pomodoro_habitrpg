set taskName to "$pomodoroName"
set addHabitScript to "/Applications/Pomodoro.app/Contents/Resources/add_habit.py "
set cmd to addHabitScript
set cmd to cmd & quoted form of taskName
do shell script cmd