# README
The Ultimate Study Guide
## Introduction
Your performance on 61A Exam can be improved with practice and by spending additional effort to master the course material beyond just completing assignments.

Following the lectures and doing homeworks/discussions is definitely useful, but probably is not quite enough. Maybe that wasn't the case in your high school or community college.

Re-engineer and optimize the way you study. This improvement of study strategy was something discussed on office hours, small piazza posts, 1-to-1 conversations with TAs, brainstorm session with your study group.

## The Basics
1. Watch lecture / Read textbook / Go through slides
- Passive Learning: teacher-centered, whereby students recieve information from the instructor and internalize it (direct instruction and lecturing).
Passive learners may quietly absorb information received or the learning experience. They may not interact with others, share insights, or contribute to dialogue.
- Active Learning: student-centered, whereby students take an active or participatory role in the learing process.
- Socratic Method: students and instructors engage in cooperative argumentative dialogue.
2. Attending tutorials and discussions
3. Completing Homework / Labs / Projects

Take these three steps to gain a better understanding of the material and treat them as **the very basics** before starting an exam preparation. However, it is not to say that you have to earn full scores on everything or fully understand the lectures from the first watch. The point is that there are some extra steps apart from these three that you should take to absorb the material better. 

## Exam Preparation
1. Conceptual Understanding
2. Active Practice
    - Compile a list of every single worksheet you have seen in this class so far (discussion, homework, or resources page). Allocate about a week of time to complete all of them, X worksheets per day.
    - Grade yourself harshly
    - Close the gaps in conceptual understanding and compile a cheatsheet. 
        -  full of reflections about the problems/concepts you have found challenging
        - compress without losing the meaning
        - generalize takeways into rules and patterns
    - Go to cs61a.org/resources and complete at least 2-4 past exams, but ideally 5-7


## Git Branch
#### Abstraction Layers of Branches
##### Layer 0: Main Branch `main`
Tree root, stores basic files (README.md, .gitignore ...) that consist a repository.
- Merge from: `develop``

##### Layer 1: Develop Branch `develop`
Tree trunk, stores LOG.md (used to update study progress and later weekly learning materials).
- Merge into: `main`

##### Layer 2: Weekly Branches `week-##`
Most time working on these truly branches. Each weekly branch is totally independent from other weekly branches. Only the merging order in develop indicates their time-related order.
- branch from:  `develop`
- merge into: `develop`

##### Layer 3: Hotfix Branches `hotfix-##`
Small changes in weekly specific branches, probably happend later 
- metaphor: many leaves
- branch from: `week-##`
- merge into: `week-##`
- when to merge: everytime the fix is done
#### Workflow
0. Initialize an empty repository
1. Create branches: `develop` and `main`
2. Create `README.md`, `.gitignore`...  in `main`
3. Create `LOG.md` in `develop`
4. Branching `week-##`, making schedule in LOG.md, commiting on the weekly projects
5. Move to the next week branch after this week is done, repeat 4
6. Once occuring a problems, move back to previous week branches, Create `hotfix` branch, fix, and merge (vanish) into that week
7. After some time (maybe a week or two after that week), if one week is considered complete and no potential problems, merge into `develop`
8. After a lone time, merge `develop` into `main`
