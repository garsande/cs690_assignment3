"""Write exactly three pytest tests in this file.

TODO 1: Add one test derived from acceptance criterion AC-1.
TODO 2: Add one test derived from acceptance criterion AC-2.
TODO 3: Add one test derived from acceptance criterion AC-3.

Use only the public functions in ``reference``: reservation_disposition and
can_offer_to_waitlist. Do not edit the reference module. Call them with named
arguments, as in tests/test_reference_smoke.py.

Name each test so the acceptance criterion it checks is visible from the test
name or an adjacent comment, for example: def test_ac1_<what_it_checks>().

Put any policy value, such as the grace period, in a named constant marked as
a configured value, as in the at-risk example from the Week 5 lecture.
"""
"""Acceptance tests derived from AC-1, AC-2, and AC-3."""

from reference import reservation_disposition

CONFIGURED_GRACE_MINUTES = 15  # Test configuration, not settled lab policy.


def test_ac1_unchecked_reservation_becomes_releasable() -> None:
    # AC-1 / R-1: at 2:16 for a 2:00 start, no check-in and no staff hold.
    state = reservation_disposition(
        minutes_after_start=16,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=None,
    )
    assert state == "releasable"


def test_ac2_checked_in_reservation_remains_active() -> None:
    # AC-2 / R-2: checked in at 2:10; evaluated at 2:20.
    state = reservation_disposition(
        minutes_after_start=20,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=True,
        staff_hold_until=None,
    )
    assert state == "active"


def test_ac3_active_staff_hold_prevents_release() -> None:
    # AC-3 / R-3: evaluated at 2:20 with a staff hold until 2:25.
    state = reservation_disposition(
        minutes_after_start=20,
        grace_minutes=CONFIGURED_GRACE_MINUTES,
        checked_in=False,
        staff_hold_until=25,
    )
    assert state == "held"

