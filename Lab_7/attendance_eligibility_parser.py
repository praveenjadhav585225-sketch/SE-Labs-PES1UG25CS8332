
def normalize_srn(srn):
    """
    Trims, removes spaces and upper-cases an SRN.
    Returns None for invalid input.
    """
    if not isinstance(srn, str):
        return None

    srn = srn.strip().replace(' ', '').upper()

    if not srn:
        return None

    return srn


def attendance_from_ratio(text):
    """
    Converts ATTENDED/HELD into a whole-number percentage.
    Returns None for invalid input.
    """
    if not isinstance(text, str):
        return None

    try:
        parts = text.strip().split('/')

        if len(parts) != 2:
            return None

        attended = int(parts[0].strip())
        held = int(parts[1].strip())

        if attended < 0 or held <= 0:
            return None

        if attended > held:
            return None

        return attended * 100 // held

    except (ValueError, TypeError):
        return None


def attendance_from_register(marks):
    """
    Calculates attendance percentage from P/A marks.
    Returns None for invalid input.
    """
    if not isinstance(marks, str):
        return None

    marks = marks.strip().upper()

    if not marks:
        return None

    if any(mark not in ('P', 'A') for mark in marks):
        return None

    return marks.count('P') * 100 // len(marks)


def main():
    print("==== Running normalize_srn ====")
    value = input("Enter an SRN (e.g. pes1ug23cs001): ")
    print("Normalized SRN:", normalize_srn(value))

    print("\n==== Running attendance_from_ratio ====")
    value = input("Enter classes attended and held as ATTENDED/HELD (e.g. 30/40): ")
    print("Attendance percent:", attendance_from_ratio(value))

    print("\n==== Running attendance_from_register ====")
    value = input("Enter the register as P/A marks (e.g. PPAPP): ")
    print("Attendance percent:", attendance_from_register(value))


if __name__ == "__main__":
    main()
