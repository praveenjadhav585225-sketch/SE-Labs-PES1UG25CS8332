
from hypothesis import given, strategies as st

from attendance_eligibility_parser import (
    normalize_srn,
    attendance_from_ratio,
    attendance_from_register
)


# Test 1: SRN normalization should not crash
@given(st.text() | st.none())
def test_normalize_srn_no_crash(s):
    try:
        normalize_srn(s)
    except Exception as e:
        assert False, f"normalize_srn crashed with input {s!r}: {e}"


# Test 2: Attendance ratio should not crash
@given(st.text() | st.none())
def test_attendance_from_ratio_no_crash(s):
    try:
        attendance_from_ratio(s)
    except Exception as e:
        assert False, f"attendance_from_ratio crashed with input {s!r}: {e}"


# Test 3: Attendance register should not crash
@given(st.text() | st.none())
def test_attendance_from_register_no_crash(s):
    try:
        attendance_from_register(s)
    except Exception as e:
        assert False, f"attendance_from_register crashed with input {s!r}: {e}"
