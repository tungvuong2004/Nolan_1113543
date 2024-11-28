"""
 * Name: Nolan
 * Student ID: 1113543
 * Date of Submission: 11/28/2024
 *
 * Program to schedule jobs with deadlines using a Max Priority Queue.
 * Features:
 * 1. Prioritize jobs with higher profit.
 * 2. Respect deadlines to maximize overall profit.
"""

def job_scheduling(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda x: x[0], reverse=True)

    # Determine the maximum deadline among all jobs
    max_deadline = max(job[1] for job in jobs)

    # Array to track scheduled jobs
    schedule = [None] * max_deadline

    total_profit = 0

    for profit, deadline in jobs:
        # Try to schedule the job at the latest available slot before its deadline
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if schedule[slot] is None:
                schedule[slot] = profit
                total_profit += profit
                break

    # Filter out None values to get the list of scheduled jobs and sort by profit
    scheduled_jobs = sorted([job for job in schedule if job is not None], reverse=True)

    return total_profit, scheduled_jobs

# Input handling
num_jobs = int(input("Enter the number of jobs: "))
job_list = []

for _ in range(num_jobs):
    profit, deadline = map(int, input().split())
    job_list.append((profit, deadline))

# Perform job scheduling
max_profit, scheduled_jobs = job_scheduling(job_list)

# Output results
print("Maximum Profit:", max_profit)
print("Scheduled Jobs:", scheduled_jobs)
