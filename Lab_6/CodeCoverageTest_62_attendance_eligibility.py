
from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)


# Attendance percentage tests
def test_plain_percent():
    assert attendance_percent(30, 40, 0) == 75


def test_zero_total_classes():
    try:
        attendance_percent(0, 0, 0)
        assert False
    except ValueError:
        assert True


def test_negative_attendance():
    try:
        attendance_percent(-1, 40, 0)
        assert False
    except ValueError:
        assert True


def test_attendance_exceeds_total():
    try:
        attendance_percent(45, 40, 0)
        assert False
    except ValueError:
        assert True


def test_medical_leave_capped():
    assert attendance_percent(20, 40, 10) == 62


def test_credited_attendance_capped():
    assert attendance_percent(38, 40, 5) == 100


# Exam eligibility tests
def test_eligible():
    assert exam_eligibility(80, False, True) == "eligible"


def test_fees_pending():
    assert exam_eligibility(90, True, False) == "fees pending"


def test_condonation_eligible():
    assert exam_eligibility(70, True, True) == "eligible"


def test_condonation_required():
    assert exam_eligibility(70, False, True) == "condonation required"


def test_detained():
    assert exam_eligibility(60, False, True) == "detained"


# Attendance warning tests
def test_no_warning():
    assert attendance_warning(90, 2) is None


def test_critical_warning():
    assert attendance_warning(70, 5) == "critical"


def test_final_notice():
    assert attendance_warning(70, 3) == "final notice"


def test_reminder():
    assert attendance_warning(80, 2) == "reminder"
