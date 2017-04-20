#This library is based off of HTML parsing
#IT IS NOT AN OFFICIAL API

from pcxp import auth, parse

USERNAME = ''
PASSWORD = ''

session = auth.login(USERNAME, PASSWORD)

#Examples

#Student details
#profile = parse.profile(session)

#Tag usages: INFO_PRO, ASSIGN_GEN, ASSIGN_SCH, GRD_GEN, GRD_SCH
# assign_count = parse.assignment_details(session, 'INFO_PRO')
# recent_assign = parse.assignment_details(session, 'ASSIGN_GEN')
# grades = parse.assignment_details(session, 'ASSIGN_SCH')
#report = parse.assignment_details(session, 'GRD_GEN')
# schedule = parse.assignment_details(session, 'GRD_SCH')

#List Example
grades_list = parse.get_info(session, 'ASSIGN_GEN')
print(grades_list)
