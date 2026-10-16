
"""Election system for voter registration and ballot management."""

import hashlib
import os
import secrets
from datetime import datetime

from defusedxml import ElementTree as safe_element_tree
from defusedxml.common import DefusedXmlException

ADMIN_PASSWORD = os.environ.get("ELECTION_ADMIN_PASSWORD")
POLLS_CLOSE_HOUR = 18

voters = {}
ballots = []
candidates = ["Alice", "Bob", "NOTA"]


def register_voter(voter_id, name, age):
    """Register a voter who meets the minimum age requirement."""
    if age < 18 or voter_id in voters:
        return False

    voters[voter_id] = {
        "name": name,
        "hash": hashlib.sha256(voter_id.encode()).hexdigest(),
        "voted": False,
    }
    return True


def is_officer(role):
    """Check whether a role belongs to an election officer."""
    return role == "election_officer"


def cast_vote(voter_id, candidate, when):
    """Record a valid vote if the voter is eligible."""
    if voter_id not in voters:
        return False

    if voters[voter_id]["voted"]:
        return False

    if candidate not in candidates:
        return False

    if when.hour >= POLLS_CLOSE_HOUR:
        return False

    ballots.append(candidate)
    voters[voter_id]["voted"] = True
    return True


def tally():
    """Return vote counts for each candidate."""
    counts = {}
    for candidate in ballots:
        counts[candidate] = counts.get(candidate, 0) + 1
    return counts


def winner():
    """Return the leading candidate, or None when there are no votes."""
    counts = tally()
    if not counts:
        return None
    return max(counts, key=counts.get)


def vote_percent(candidate):
    """Calculate the percentage of votes received by a candidate."""
    total_votes = len(ballots)
    if total_votes == 0:
        return 0.0
    return tally().get(candidate, 0) * 100 / total_votes


def turnout():
    """Calculate voter turnout as a percentage."""
    if not voters:
        return 0.0
    return len(ballots) / len(voters) * 100


def count_for(candidate, ballot_list=None):
    """Count votes for a candidate in a ballot list."""
    if ballot_list is None:
        ballot_list = ballots
    return sum(ballot == candidate for ballot in ballot_list)


def announce():
    """Return vote-count announcements for all candidates."""
    counts = tally()
    return [
        f"{candidate}: {counts.get(candidate, 0)}"
        for candidate in candidates
    ]


def receipt_number():
    """Generate a random six-digit receipt number."""
    return f"RCPT-{secrets.randbelow(900000) + 100000}"


def import_postal_ballots(xml_text):
    """Import valid postal ballots using a secure XML parser."""
    try:
        root = safe_element_tree.fromstring(xml_text)
    except (DefusedXmlException, ValueError, TypeError):
        return 0

    imported = 0
    for node in root.iter("ballot"):
        candidate = node.get("candidate")
        if candidate in candidates:
            ballots.append(candidate)
            imported += 1

    return imported


def main():
    """Run a demonstration of election system operations."""
    voters.clear()
    ballots.clear()

    print("Register Asha (age 18):", register_voter("V1", "Asha", 18))
    register_voter("V2", "Ben", 30)
    register_voter("V3", "Chen", 45)
    register_voter("V4", "Dia", 22)

    print("Is a plain 'voter' an election officer?", is_officer("voter"))
    print(
        "Ben votes Alice:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 10, 0)),
    )
    print(
        "Ben votes Alice again:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 11, 0)),
    )
    print(
        "Chen votes 'bob':",
        cast_vote("V3", "bob", datetime(2026, 11, 20, 12, 0)),
    )
    print(
        "Dia votes Bob at 18:30:",
        cast_vote("V4", "Bob", datetime(2026, 11, 20, 18, 30)),
    )

    postal_xml = (
        "<postal><ballot voter='V1' candidate='Bob'/></postal>"
    )
    print("Postal ballots imported:", import_postal_ballots(postal_xml))
    print("Tally:", tally())
    print("Winner:", winner())
    print("Alice %:", vote_percent("Alice"))
    print("Turnout %:", turnout())
    print("Announcements:", announce())
    print("Receipt:", receipt_number())


if __name__ == "__main__":
    main()
