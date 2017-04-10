#!/usr/bin/env python
import itertools
import re

numcourses = int(re.findall('Number of courses: ([0-9]*)', raw_input())[0], 10)
numhours = int(re.findall('Number of hours remaining: ([0-9]*)', raw_input())[0], 10)
#print numcourses, numhours

costfunctions = []
for _ in range(numcourses):
    tmp = raw_input()
    tmp2 = tmp[tmp.find(': ')+2:].split(' ')
    #print tmp2
    costfunctions.append([int(i, 10) for i in tmp2])

#print costfunctions

def grade_schedule(schedule):
    grade = 0
    for (course, hours) in enumerate(schedule):
        if hours >= len(costfunctions[course]):
            hours = len(costfunctions[course])
        if hours > 0:
                grade += costfunctions[course][hours-1]
    return grade

'''
def bruteforce(numcourses, numhours):
    tmp = [list(range(numhours+1)) for _ in range(numcourses)]
    bestgrade = 0
    bestschedules = []
    for schedule in itertools.product(*tmp):
        if sum(schedule) == numhours:
            grade = grade_schedule(schedule)
            if grade > bestgrade:
                bestgrade = grade
                bestschedules = [schedule]
            elif grade == bestgrade:
                bestschedules.append(schedule)
    return (bestgrade, bestschedules)

def bruteforce_main():
    bestgrade, bestschedules = bruteforce(numcourses, numhours)
    #print bestgrade
    for schedule in bestschedules:
        print ' '.join(map(str, schedule))

#bruteforce_main()
'''

def memofix(f): 
    memo = dict() 
    # memoizing kwargs is left as an exercise to the reader 
    def inner(*args): 
            if not memo.has_key(args): 
                memo[args] = f(inner, *args) 
            return memo[args] 
    inner.__name__ = "memoized_" + f.__name__ 
    return inner 

@memofix
def dynprog(rec, hours, schedule):
    if hours == 0:
        #print 'base0'
        return schedule
    if sum(schedule) == numhours:
        #print 'base1'
        return schedule

    #print hours, schedule

    bestschedule = schedule
    bestgrade = grade_schedule(bestschedule)
    
    for course in range(numcourses):
        improvement = list(schedule)
        improvement[course] += 1
        tmp = rec(hours-1, tuple(improvement))
        #print tmp, grade_schedule(tmp), sum(tmp)
        grade = grade_schedule(tmp)
        #print improvement, grade, course
        if grade >= bestgrade:
            bestschedule = tmp
            bestgrade = grade_schedule(bestschedule)
    return bestschedule
        
def dynprog_main():
    schedule = dynprog(numhours, tuple(0 for _ in range(numcourses)))
    print ' '.join(map(str, schedule))

dynprog_main()
