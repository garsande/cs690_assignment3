Name: Sandeep Garg

CS 690 Assignment 3 Report: Evidence to Executable Specification


## Part 1. Build an evidence log

| Evidence ID | Interview source | Evidence / question / assumption | Status | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **E-1** | INT-01:P02 | Students reserve equipment for a specific start time. Technicians prepare the kit, and desk staff verify the student's university ID before marking it picked up. | Stated | Media Lab staff |
| **E-2** | INT-01:P06<br>INT-01:P12 | Jordan states the current grace period is 15 minutes, while Priya reports being told it is 20 minutes. The interview establishes conflicting understandings of the policy. | Stated | Media Lab manager |
| **E-3** | INT-01:P04 | A student called at 2:08 about a 2:00 reservation. Staff manually extended the hold until 2:25, and the student collected the kit at 2:22. | Observed | Jordan Lee |
| **E-4** | INT-01:P09<br>INT-01:P17 | Releasing a reservation does not necessarily mean the equipment is ready for another student. Technicians may need to inspect accessories or prepare the kit before checkout. | Stated | Equipment technicians |
| **E-5** | INT-01:P13 | Priya's 3:00 reservation was released before she reached staff at 3:16. She received another kit at 3:38, and her interview started approximately 10 minutes late. | Observed | Priya Shah |
| **A-1** | INT-01:P15 | A self-service "running late" button would reliably replace phone calls and could automatically extend a reservation. Priya expressed interest, but automatic extensions and their rules were not established. | Assumption | Media Lab manager |
| **A-2** | INT-01:P19 | Equipment technicians could update preparation status through the same reservation dashboard used by desk staff. Their preferred workflow has not been investigated. | Assumption | Equipment technicians |
| **Q-1** | INT-01:P06<br>INT-01:P12 | What grace period is officially configured, and how should students be informed when the policy changes? | Open | Media Lab manager |
| **Q-2** | INT-01:P10<br>INT-01:P17<br>INT-01:P21 | When and through which channel should students receive release notifications, and what conditions must be satisfied before waitlisted students are notified? | Open | Media Lab manager |
| **Q-3** | INT-01:P09<br>INT-01:P19 | How will equipment technicians confirm that a released kit is physically ready for the next checkout, and how should that status be communicated to desk staff? | Open | Equipment technicians |

## Part 2. Audit the evidence

| Audit item | Interview paragraph(s) | Classification | Why this matters to requirements quality |
| :--- | :--- | :--- | :--- |
| **1. Direct factual contradiction** | INT-01:P06<br>INT-01:P12 | Contradiction | Jordan states the grace period is 15 minutes, while Priya says students are told it is 20 minutes. The Media Lab manager must confirm the official policy before implementing the release rule. |
| **2. Ambiguous statement 1** | INT-01:P07 | Ambiguous – Vague time | Jordan says students who are "only a little late" should not lose their equipment. The phrase does not specify how many minutes late is acceptable, making it unsuitable as a precise system requirement. |
| **3. Ambiguous statement 2** | INT-01:P10 | Ambiguous – Unclear recipient and timing | Jordan says "They should get a message before it goes to the waitlist," but does not clearly identify who should receive the message or exactly when it should be sent. These details must be clarified before implementing notifications. |
| **4. Missing stakeholder** | INT-01:P02<br>INT-01:P09<br>INT-01:P19 | Missing stakeholder | Equipment technicians prepare, inspect, and confirm equipment readiness, but none were interviewed. Their input is necessary to define an accurate equipment preparation and availability workflow. |
| **5. Compliment** | INT-01:P14 | Compliment – Not evidence | Priya says a reservation dashboard that fixed everything would be amazing. This expresses enthusiasm but does not establish actual user needs or validate specific dashboard features. |
| **6. Prediction about future use** | INT-01:P15 | Prediction – Not evidence | Priya predicts she would probably use a "running late" button whenever delayed. This does not prove students will actually use the feature or establish how it should work. |
| **7. Strongest specific past event** | INT-01:P13 | Observed past event | Priya describes a specific late pickup, including reservation time, attempted calls, release, waiting period, and delayed interview. This detailed account provides concrete evidence of workflow problems and their consequences. |

## Part 3. Write four requirements and three acceptance criteria

### Four requirement slices
### R-1: Grace Period and Release Eligibility

**User Story:** As a Media Lab checkout coordinator, I want reservations to follow the lab's configured grace period, so that late reservations can be released consistently.
**Structured Requirement:** The system shall classify a reservation as `releasable` when the configured grace period has elapsed, provided the student has not checked in and no active staff hold exists. This classification does not itself confirm that the reservation has been released.
**Trace:** E-2, Q-1
**INVEST Check:**
| Criterion | Result | Explanation |
| --- | --- | --- |
| Independent | Pass | Can be implemented separately from notifications and equipment preparation. |
| Negotiable | Pass | The grace period is configurable rather than hard-coded. |
| Valuable | Pass | Supports consistent reservation release decisions. |
| Estimable | Pass | Release conditions and required data are identifiable. |
| Small | Pass | Focuses on one reservation release rule. |
| Testable | Pass | Can verify release status using configured time and reservation state. |


### R-2: Student Check-In Protection

**User Story:** As a student borrower, I want my checked-in reservation to remain active, so that I do not lose my equipment because the grace period expires.
**Structured Requirement:** The system shall prevent automatic release of a reservation when the student has already checked in, even if the configured grace period has elapsed.
**Trace:** E-1, E-2
**INVEST Check:**
| Criterion | Result | Explanation |
| --- | --- | --- |
| Independent | Pass | Check-in protection can be evaluated without staff holds or waitlist processing. |
| Negotiable | Pass | The check-in recording workflow can be refined. |
| Valuable | Pass | Prevents checked-in students from losing reservations. |
| Estimable | Pass | Requires checking the recorded check-in state. |
| Small | Pass | Addresses one specific exception to automatic release. |
| Testable | Pass | Can verify that a checked-in reservation remains active after the grace period. |


### R-3: Temporary Staff Hold

**User Story:** As a Media Lab checkout coordinator, I want to record a temporary hold on a reservation, so that students who contact the desk about delays do not lose their equipment before the approved hold expires.
**Structured Requirement:** The system shall prevent automatic release of a reservation while a recorded staff hold remains active, even if the configured grace period has elapsed. The system shall store the hold expiration time and reason.
**Trace:** E-3
**INVEST Check:**
| Criterion | Result | Explanation |
| --- | --- | --- |
| Independent | Pass | Hold protection can be evaluated separately from notifications and technician preparation. |
| Negotiable | Pass | Staff hold entry and expiration details can be refined. |
| Valuable | Pass | Supports documented exceptions for delayed students. |
| Estimable | Pass | Requires a hold expiration time and reservation state check. |
| Small | Pass | Limited to recording and enforcing a temporary hold. |
| Testable | Pass | Can verify that an active hold prevents automatic release. |


### R-4: Equipment Readiness for Waitlist

**User Story:** As a waitlisted student, I want to be offered only equipment that is ready for checkout, so that I do not travel to the desk for equipment that is still being prepared.
**Structured Requirement:** The system shall permit a released kit to be offered to the waitlist only when its preparation status indicates that it is ready for checkout.
**Trace:** E-4, Q-3
**Clarifying Question:** How will equipment technicians record and confirm that a kit is ready for the next checkout?
**INVEST Check:**
| Criterion | Result | Explanation |
| --- | --- | --- |
| Independent | Pass | Waitlist eligibility can be checked using an existing readiness status without implementing the technician interface. |
| Negotiable | Pass | The method of updating readiness status remains open. |
| Valuable | Pass | Prevents unavailable equipment from being offered to waitlisted students. |
| Estimable | Pass | Eligibility logic can be estimated independently of the technician interface. |
| Small | Pass | Focuses only on whether a released kit may be offered. |
| Testable | Pass | Can verify eligibility using reservation release and equipment readiness states. |

---

### Three acceptance criteria


### AC-1: Release Eligibility After Configured Grace Period

**Requirement:** R-1
**Given** a reservation started at 2:00 PM, the lab's configured grace period is G = 15 minutes, the current time is 2:16 PM, the student has not checked in, and no staff hold exists,
**When** the system evaluates the reservation for automatic release,
**Then** the reservation disposition shall be `releasable`.

### AC-2: Checked-In Reservation Remains Active

**Requirement:** R-2
**Given** a reservation started at 2:00 PM, the lab's configured grace period is G = 15 minutes, the current time is 2:20 PM, and the student checked in at 2:10 PM,
**When** the system evaluates the reservation for automatic release,
**Then** the reservation status shall remain `active`.

### AC-3: Active Staff Hold Prevents Release

**Requirement:** R-3
**Given** a reservation started at 2:00 PM, the lab's configured grace period is G = 15 minutes, the current time is 2:20 PM, the student has not checked in, and staff recorded a hold valid until 2:25 PM,
**When** the system evaluates the reservation for automatic release,
**Then** the reservation disposition shall be `held` because the staff hold has not expired.

## Part 4. Make one requirement implementation-ready

### Implementation-Ready Specification

### Selected requirement

Requirement ID: R-2 — Student Check-In Protection

Evidence trace: E-1, E-2; INT-01:P02, P06, P12, P17, P21.


### Behavior and scope

The system shall prevent automatic release of a reservation when the student has already checked in, regardless of whether the configured grace period has elapsed.

This specification evaluates reservation disposition using the configured grace period, check-in state, and an optional staff hold. It does not itself release equipment or update stored reservation records.

### Typed interface or function signature

from typing import Literal
ReservationDisposition = Literal["active", "held", "releasable"]

def reservation_disposition(
minutes_after_start: int,
grace_minutes: int,
checked_in: bool,
staff_hold_until: int | None = None,
) -> ReservationDisposition:

...

minutes_after_start and staff_hold_until are measured in minutes relative to the reservation start; staff_hold_until is optional. The interface describes the Part 5 reference function.

### Preconditions

minutes_after_start and grace_minutes must be integers.
grace_minutes must be nonnegative and supplied from the lab's configured policy.
minutes_after_start is nonnegative for the evaluated scenarios.
checked_in must accurately represent whether the student has completed check-in.
staff_hold_until is an integer number of minutes after start or None.
The function evaluates a disposition, not an existing persisted reservation status.

### Postconditions

If checked_in is True, return "active", even when minutes_after_start exceeds grace_minutes.
If checked_in is False and an active staff hold extends beyond minutes_after_start, return "held".
If checked_in is False, no active hold exists, and minutes_after_start exceeds the configured grace period, return "releasable".
If checked_in is False and the configured grace period has not elapsed, return "held".
Return only "active", "held", or "releasable"; this result does not itself execute a release.

### Invariant

A checked-in reservation evaluates to "active", not "releasable", regardless of elapsed grace-period time.
Repeated evaluations must preserve this rule regardless of how much time has passed since the reservation started.

### Edge cases

Exactly at the grace-period boundary: Whether an unchecked-in reservation is already "releasable" at equality must be confirmed; do not infer the boundary policy from the tests.
Check-in before grace expiration: A reservation checked in before the deadline remains active after the deadline passes.
Check-in at the grace-period boundary: If check-in has already been recorded when evaluation occurs, the reservation remains active.
Active staff hold: A reservation with a hold extending beyond the evaluation time returns "held".
Already released reservation: The disposition function has no persisted-release input and cannot decide reinstatement; leave that workflow open.
Zero-minute grace period: Boundary behavior at the start time requires confirmation; do not assume an automatic release.

### Non-goal

This specification does not send notifications, release equipment, reinstate reservations, or define waitlist handoff.


### Settled decisions

The grace period must be supplied as a configurable value rather than hard-coded.
A reservation with a recorded check-in remains active during automatic release evaluation.
An active staff hold returns "held" and prevents a "releasable" disposition while it is active.
The disposition function does not decide whether an already released reservation can be reactivated.
The function returns an evaluation result rather than changing stored reservation records.


### Open questions the implementation agent may not answer

Official grace period: The interview contains conflicting statements of 15 and 20 minutes. The Media Lab manager must confirm the configured value.
Check-in after release: Should staff be able to reinstate a reservation that was released before the student arrived? The disposition function cannot answer this.
Simultaneous events: How should the system handle check-in and automatic release occurring at exactly the same time when their processing order is unclear?
Staff hold expiration: Should a hold remain valid at its exact expiration timestamp, or expire immediately when that time is reached? Grace-period equality likewise needs a policy decision.
These questions must be resolved by the appropriate stakeholders rather than by the implementation agent.

## Part 5. Turn three criteria into tests


### Test Implementation

Exactly three pytest test functions were added to tests/test_student_acceptance.py. The original reference implementation and smoke test were left unchanged. All reference functions were called with named arguments.


### Traceability

| Test Name | AC | Requirement | Evidence |
| --- | --- | --- | --- |
| test_ac1_unchecked_reservation_becomes_releasable | AC-1 | R-1 | E-2, Q-1 |
| test_ac2_checked_in_reservation_remains_active | AC-2 | R-2 | E-1, E-2 |
| test_ac3_active_staff_hold_prevents_release | AC-3 | R-3 | E-3 |


### Test Execution

Command executed from the reconstructed project root:

(venv) garsande@Garg:~/Assignment-3$ python -m pytest -q
....                                                                                                                                                                      [100%]
4 passed in 0.05s
(venv) garsande@Garg:~/Assignment-3$


### Policy and Verification Notes

CONFIGURED_GRACE_MINUTES = 15 is a named test configuration, not a resolved product-policy value.
AC-1 checks "releasable", AC-2 checks "active", and AC-3 checks "held".
The third test evaluates a hold before its expiration, without deciding the unresolved boundary rule.


## Part 6. Run one AI ambiguity audit and critique the synthetic user


### Audit adjudication

| # | Finding | Classification | Paragraph ID(s) | Explanation |
| --- | --- | --- | --- | --- |
| 1 | Conflicting Grace Periods | true positive | P06, P12 | Jordan states that the grace period is 15 minutes, while Priya reports being told it is 20 minutes, establishing a genuine contradiction in the reported policy. |
| 2 | Vague Late-Arrival Tolerance | true positive | P07 | Jordan uses the phrase "only a little late" without specifying a duration or explaining how this practice relates to the grace-period policy. |
| 3 | Unclear Notification Requirements | true positive | P10 | Jordan says "They should get a message" without identifying the recipient, delivery time, or notification trigger. |
| 4 | Unspecified Staff-Hold Rules | true positive | P04, P19, P21 | The interview confirms that staff can extend reservations but does not establish authorization limits, maximum hold durations, or exact expiration behavior. |
| 5 | Undefined Equipment-Readiness Process | true positive | P09, P17, P19, P21 | Jordan and Priya describe the importance of equipment readiness, but the technicians' confirmation process remains undefined because they have not been interviewed. |
| 6 | Unclear Reservation-Release Authority | true positive | P06, P13, P19 | Jordan says staff "can release" a reservation after the grace period, but the interview does not establish whether release is automatic or requires an explicit staff action. |
| 7 | Unspecified Check-In and Release Ordering | true positive | P06, P17, P21 | The interview establishes that checked-in reservations should remain active but does not specify how simultaneous check-in and release events or post-release check-ins are handled. |
| 8 | Undefined Waitlist Handoff | true positive | P09, P13, P17, P21 | The interview establishes that equipment must be ready before waitlist handoff but does not specify student selection, notification, or offer procedures. |

| Classification | Count |
| --- | --- |
| True positive | 8 |
| False positive | 0 |
| Total findings | 8 |

All eight findings identify genuine ambiguities, contradictions, or missing decisions supported by INT-01.


### Synthetic User Critique — SYN-01

The following table identifies each distinct unsupported claim, quotes the synthetic response, and explains why INT-01 does not support it.

| # | Synthetic Claim (Direct Quote) | Relevant INT-01 Paragraph(s) | Why the Claim Is Unsupported |
| --- | --- | --- | --- |
| 1 | "A likely student borrower wants the media lab reservation process to require as little staff contact as possible." | P02, P13, P15 | The interview describes interactions with desk staff and difficulties reaching them, but it does not establish a general preference for minimizing staff contact. |
| 2 | "Students probably prefer text-message alerts over email" | P10, P13, P17 | The interview mentions phone calls, email, and a desire to know reservation status, but nobody expresses a preference for SMS over email. |
| 3 | "because they are moving between classes." | P12, P13 | Priya describes traveling across campus and experiencing a class delay, but the interview does not establish that movement between classes explains students' notification preferences. |
| 4 | "A 10-minute grace period would likely feel fair for late arrivals." | P06, P12 | Jordan reports 15 minutes and Priya reports 20 minutes; neither participant suggests that 10 minutes would be fair or acceptable. |
| 5 | "The strongest feature would be a QR-code self-check-in" | P02, P17 | The interview describes university ID verification at the desk and the importance of check-in protection, but nobody requests or evaluates QR-code check-in. |
| 6 | "so a borrower can preserve a reservation without waiting for a desk worker." | P02, P17, P21 | The interview supports protecting checked-in reservations but does not establish that students should be able to check in independently or bypass desk staff. |
| 7 | "Students who lose a reservation are likely willing to accept a different brand of camera or light automatically" | P13 | Priya received a different lighting kit after losing her reservation, but the interview does not establish willingness to accept automatic substitutions or different brands. |
| 8 | "as long as the general equipment category is the same." | P13 | The interview does not establish equipment-category equivalence as an acceptable substitution rule. |
| 9 | "Equipment technicians would probably prefer to receive one batch of released-reservation updates" | P09, P19, P21 | Equipment technicians were not interviewed, so their preferences regarding notification frequency or batching are unknown. |
| 10 | "every 30 minutes instead of individual updates." | P19, P21 | The interview contains no evidence supporting a 30-minute update interval or a preference for batched rather than individual notifications. |

Conclusion: AI is useful for discovering potential gaps in requirements, but real stakeholder evidence must determine which findings are valid. SYN-01 should be retained only as a source of hypotheses for future interviews, not as a substitute for real-user evidence.


## Part 7. Traceability and ledger

Traceability matrix (completed from Part 5 acceptance tests):

| Evidence ID | Requirement ID | Acceptance Criterion ID | Test Name |
| --- | --- | --- | --- |
| E-2;Q-1 | R-1 | AC-1 | test_ac1_unchecked_reservation_becomes_releasable |
| E-1;E-2 | R-2 | AC-2 | test_ac2_checked_in_reservation_remains_active |
| E-3 | R-3 | AC-3 | test_ac3_active_staff_hold_prevents_release |

The seven-field provenance ledger is maintained separately in LEDGER.md.


### Verification

(venv) garsande@Garg:~/Assignment-3$ python -m pytest -q
....                                                                                                                                                                      [100%]
4 passed in 0.05s
(venv) garsande@Garg:~/Assignment-3$
