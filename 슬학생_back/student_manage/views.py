from django.shortcuts import render



# 해당 반의 전체 출석 목록 조회
def attendance_list(request, class_id, date):
    pass


# 출석 상세 보기 / 출석 상태 변경
def attendance_detail(request, student_id, date):
    pass


# 출석 상태 변경 요청 제출
def attendance_change(request, student_id, date):
    pass


# 해당 학생의 태도 목록 조회
def note_list(request, student_id):
    pass


# 학생 태도 상세 보기
def note_detail(request, student_id, note_id):
    pass