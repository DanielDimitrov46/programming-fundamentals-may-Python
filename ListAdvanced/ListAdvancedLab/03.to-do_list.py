notes = [0]*10
task = input().split('-')
while "End" not in task:
    priority = int(task[0])-1
    note = task[1]
    notes.pop(priority)
    notes.insert(priority,note)
    task = input().split('-')
result = [element for element in notes if element!=0]
print(result)