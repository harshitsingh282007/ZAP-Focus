import time
import random
import sys

QUOTES = [
    "Small steps every day lead to big results.",
    "You don’t have to be perfect — just consistent.",
    "Focus on progress, not perfection.",
    "You’re doing better than you think.",
    "Take a deep breath. You’ve got this!",
    "ADHD is your superpower when channeled right!",
    "Done is better than perfect.",
    "Celebrate every tiny win!",
    "Even one page of progress is still a chapter finished.",
    "Be proud of every minute you stayed focused!"
]

tasks = []

def show_menu():
    print("\n========== ZAP-Focus! ==========")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Start Pomodoro Focus Session (25 + 5)")
    print("5. Exit")
    print("================================")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"title": task, "done": False})
    print(f"✅ Task '{task}' added!")

def view_tasks():
    if not tasks:
        print("📭 No tasks added yet.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks):
        status = "✅ Done" if task["done"] else "❌ Not Done"
        print(f"{i + 1}. {task['title']} - {status}")

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"🎉 Task '{tasks[index]['title']}' marked as done!")
        else:
            print("❗ Invalid task number.")
    except:
        print("⚠️ Please enter a valid number.")

def countdown_timer(minutes, label):
    total_seconds = int(minutes * 60)
    print(f"\n🔔 {label} Timer: {minutes} minute(s). Stay on task!\n")
    while total_seconds > 0:
        mins = total_seconds // 60
        secs = total_seconds % 60
        time_str = f"{label} Time Left: {mins:02d}:{secs:02d}"
        print(time_str)
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    print(f"{label} Time Left: 00:00 ✅")

def focus_session():
    print("\n🎯 Starting ZAP-Focus Session (25 min Focus + 5 min Break)")
    print("💬 " + random.choice(QUOTES))

    countdown_timer(25, "Focus")

    print("\n📢 Focus session over! Time for a short 5-minute break.")
    print("💬 " + random.choice(QUOTES))

    countdown_timer(5, "Break")

    print("\n✅ Break finished. Well done!")
    print("💪 " + random.choice(QUOTES))

def main():
    print("\n⚡ Welcome to ZAP-Focus! Your terminal-based productivity partner.\n")
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            focus_session()
        elif choice == '5':
            print("\n👋 Exiting ZAP-Focus.")
            print("🌟 Remember: Progress is built one focus session at a time. Keep going. 🌟")
            print("🔁 Come back anytime you want to reset, refocus, and move forward.\n")
            print("💡 ZAP-Focus powered by your commitment. Stay sharp!\n")
            break
        else:
            print("❗ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == '__main__':
    main()
