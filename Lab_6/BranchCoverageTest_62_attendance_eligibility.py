
import pytest

from attendance_eligibility import (
    attendance_percent,
    exam_eligibility,
    attendance_warning
)


# 1. Attendance percentage: input validation
def test_total_classes_zero():
    with pytest.raises(ValueError):
        attendance_percent(0, 0, 0)


def test_negative_attended():
    with pytest.raises(ValueError):
        attendance_percent(-1, 40, 0)


def test_attended_exceeds_total():
    with pytest.raises(ValueError):
        attendance_percent(41, 40, 0)


# 2. Attendance percentage: medical leave conditions
def test_medical_leave_more_than_five():
    assert attendance_percent(20, 40, 8) == 62


def test_medical_leave_five_or_less():
    assert attendance_percent(20, 40, 5) == 62


# 3. Attendance percentage: credited attendance condition
def test_credited_attendance_exceeds_total():
    assert attendance_percent(38, 40, 5) == 100


def test_credited_attendance_does_not_exceed_total():
    assert attendance_percent(20, 40, 0) == 50


# 4. Exam eligibility conditions
def test_fees_not_paid():
    assert exam_eligibility(90, True, False) == "fees pending"


def test_fees_paid_and_attendance_above_75():
    assert exam_eligibility(80, False, True) == "eligible"


def test_attendance_below_75_with_condonation():
    assert exam_eligibility(70, True, True) == "eligible"


def test_attendance_below_75_without_condonation():
    assert exam_eligibility(70, False, True) == "condonation required"


def test_attendance_below_65():
    assert exam_eligibility(60, False, True) == "detained"


# 5. Attendance warning conditions
def test_attendance_at_least_85():
    assert attendance_warning(85, 2) is None


def test_attendance_below_75_more_than_four_weeks():
    assert attendance_warning(70, 5) == "critical"


def test_attendance_below_75_four_or_fewer_weeks():
    assert attendance_warning(70, 4) == "final notice"


def test_attendance_between_75_and_84():
    assert attendance_warning(80, 2) == "reminder"
