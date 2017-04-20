# PCxp-service
Email service for automated grade report

# Parconn API - Python
A Hackjob to expose "read-only elements" of AACPS [ParentCONNECTxp](https://parentconnect.aacps.org/). Designed for notification services for active students.

Keep in mind that __this API is not official__ and it may become deprecated by small changes.

## Keep in mind...
If you intend to use this API for a notification service, keep in mind that:
* ParentCONNECTxp pushes the grades __about 30 minutes before 3:00AM(EST) and 6:00PM(EST)__. So the best times to make a request are 6:00AM(EST) and 6:00PM(EST).

* __AACPS may automatically block your IP address__ if you consistently make large number of requests. It may take a while to get unblocked, depending on the severity of your offense.

## How to use - parse.py
https://parentconnect.aacps.org/ __[insert page here]__

ex) https://parentconnect.aacps.org/StudentInfoProfile.asp

This API can read from four pages after auth:
* __StudentInfoProfile.asp__ - ID: `INFO_PRO`

  lists number of graded assignments from each class

* __StudentInfoGeneral.asp__ - ID: `INFO_GEN`

  displays your student information. This page is deviates from the other pages and need to be evoked by the `profile()` method.
* __AssignmentsGeneral.asp__ - ID: `ASSIGN_GEN`

  lists your graded assignments
* __AssignmentsSchedule.asp__ - ID: `ASSIGN_SCH`

  lists your grades for each class
* __GradesGeneral.asp__ - ID: `GRD_GEN`

  lists your report cards grades when available
* __GradesSchedule.asp__ - ID: `GRD_SCH`

  lists your year schedule

The API directly accesses these pages with GET requests and parses them into Python objects. Each page has their own ID shown above and object structure.

The `parconn.py` file demonstrates how each page should be accessed.

### IDs and Course objects
You only have to know two methods from the `parse.py` module: `profile(session)` and `assignment_details(session, ID)`. The latter can access 5 pages with the same method through IDs.

Use the `dir()` method to explore the attributes.

Every ID input returns an `Info` object with course names as attributes. A course name looks like this: `A13810`.
#### INFO_PRO (assignment count)

  Each course contains the following attributes:
  * `course` - course ID
  * `assign_count` - number of assignments graded this week

#### ASSIGN_GEN (assignment grade)

  Each course contains the following attributes:
  * `course` - course ID
  * `period` - class period
  * `assignment` - assignment name
  * `type` - type of assignment
  * `score` - assignment score
  * `due` - due date
  * `remark` - notes from the grader
  * `teacher` - name of the teacher

#### ASSIGN_SCH (class grade)

  Each course contains the following attributes:
  * `course` - course ID
  * `title` - class name
  * `grade` - class grade (A/B/C/...)
  * `score` - class score out of 100
  * `teacher` - name of the teacher

#### GRD_GEN (report card grade)

  Each course contains the following attributes:
  * `course` - course ID
  * `title` - class name
  * `pcc` - potential course credits
  * `credits` - credits earned
  * `grade` - final grade (A/B/C/...)
  * `teacher` - name of the teacher

#### GRD_SCH

  Each course contains the following attributes:
  * `course` - course ID
  * `title` - class name
  * `period` - class period
  * `teacher` - name of the teacher

## Raw List Query
If you just want a list without any object label wrappers, you can use the `get_info(session, ID)` method. It returns an list of lists, each pertaining to a class.
