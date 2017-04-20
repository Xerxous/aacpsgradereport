CLIP = 5

TARGET_ELEMENT = 'td'

DISCARD = ['\n', '\t', '\r', '\xc2\xa0']

LINK  = {
    'INFO_PRO': 'https://parentconnect.aacps.org/StudentInfoProfile.asp',
    'INFO_GEN': 'https://parentconnect.aacps.org/StudentInfoGeneral.asp',
    'ASSIGN_GEN': 'https://parentconnect.aacps.org/AssignmentsGeneral.asp',
    'ASSIGN_SCH': 'https://parentconnect.aacps.org/AssignmentsSchedule.asp',
    'GRD_GEN': 'https://parentconnect.aacps.org/GradesGeneral.asp',
    'GRD_SCH': 'https://parentconnect.aacps.org/GradesSchedule.asp'
}

CHUNKS = {
    'INFO_PRO': 2,
    'INFO_GEN': 31,
    'ASSIGN_GEN': 8,
    'ASSIGN_SCH': 5,
    'GRD_GEN': 6,
    'GRD_SCH': 4
}

DISPLACE = {
    'INFO_PRO': 0,
    'INFO_GEN': 0,
    'ASSIGN_GEN': 0,
    'ASSIGN_SCH': 0,
    'GRD_GEN': 0,
    'GRD_SCH': 1
}

TAGS = {
    'INFO_PRO': 0,
    'ASSIGN_GEN': 1,
    'ASSIGN_SCH': 2,
    'GRD_GEN': 3,
    'GRD_SCH': 4
}

LABELS = [
    ['course', 'assign_count'],
    ['course', 'period', 'assignment', 'type', 'score', 'due', 'remark', 'teacher'],
    ['course', 'title', 'grade', 'score' ,'teacher'],
    ['course', 'title', 'pcc', 'credits', 'grade', 'teacher'],
    ['course', 'title', 'period', 'teacher'],
    ['name', 'nickname', 'residence', 'phone', 'mailing', 'grade', 'mix','counselor', 'school', 'birthday']
]
