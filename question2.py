"""
 * Name: Nolan
 * Student ID: 1113543
 * Date of Submission: 11/28/2024
 *
 * Program to manage a task scheduler using a max heap.
 * Features:
 * 1. Insert tasks with a specific priority.
 * 2. Retrieve the task with the highest priority.
 * 3. Display all pending tasks in descending priority order.
"""

import heapq

class TaskScheduler:
    def __init__(self):
        self.priority_heap = []  # Max heap (negative priority for max heap simulation)

    def insert_task(self, task, priority_level):
        # Push a task into the heap with negative priority (to simulate max heap behavior)
        heapq.heappush(self.priority_heap, (-priority_level, task))

    def fetch_highest_priority_task(self):
        if not self.priority_heap:
            return None
        # Pop and return the task with the highest priority
        _, task = heapq.heappop(self.priority_heap)
        return task

    def list_pending_tasks(self):
        # Return all tasks sorted by descending priority without modifying the heap
        return [(task, -priority) for priority, task in sorted(self.priority_heap, key=lambda x: -x[0])]

# Input processing
num_operations = int(input("Enter the number of operations: "))
task_manager = TaskScheduler()
results = []

for _ in range(num_operations):
    command = input().strip().split()
    if command[0] == "ADD":
        task = command[1]
        priority = int(command[2])
        task_manager.insert_task(task, priority)
    elif command[0] == "GET":
        highest_task = task_manager.fetch_highest_priority_task()
        if highest_task:
            results.append(highest_task)
        else:
            results.append("No tasks available.")

# Output results for "GET" commands
for task in results:
    print(task)

# Display the pending tasks
pending_tasks = task_manager.list_pending_tasks()
print("Remaining tasks:", pending_tasks)
