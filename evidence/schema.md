# Evidence log schema

Use 8 to 10 entries. IDs must begin with E, A, or Q.

- E: real evidence from the interview transcript.
- A: an assumption that is not established by the interview.
- Q: an unresolved question that must be answered before the related decision is treated as settled.

Use this table shape:

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | OBS-02 | Rider waited 18 minutes for the next bus after a missed connection. | Observed | Student |

Status says how the claim is known: `Observed` for a specific past event someone described, `Stated` for a rule or fact a speaker asserted, `Assumption` for an A entry, and `Open` for a Q entry. Owner is the person or group who could confirm the claim or answer the question.

The worked row above is unrelated to the media-lab case. For this assignment, transcript sources must use the form `INT-01:Pxx`, for example `INT-01:P13`.

Do not cite `SYN-01` as real-user evidence. Synthetic-user material can generate a hypothesis, but it cannot establish actual user behavior, willingness, priorities, or requirements.

---

| ID | Source | Claim | Status | Owner |
| --- | --- | --- | --- | --- |
| E-1 | INT-01:P02 | Students reserve equipment for a specific start time. Technicians prepare the kit, and desk staff verify the student's university ID before marking it picked up. | Stated | Media Lab staff |
| E-2 | INT-01:P06, INT-01:P12 | Jordan states the current grace period is 15 minutes, while Priya reports being told it is 20 minutes. The interview establishes conflicting understandings of the policy. | Stated | Media Lab manager |
| E-3 | INT-01:P04 | A student called at 2:08 about a 2:00 reservation. Staff manually extended the hold until 2:25, and the student collected the kit at 2:22. | Observed | Jordan Lee |
| E-4 | INT-01:P09, INT-01:P17 | Releasing a reservation does not necessarily mean the equipment is ready for another student. Technicians may need to inspect accessories or prepare the kit before checkout. | Stated | Equipment technicians |
| E-5 | INT-01:P13 | Priya's 3:00 reservation was released before she reached staff at 3:16. She received another kit at 3:38, and her interview started approximately 10 minutes late. | Observed | Priya Shah |
| A-1 | INT-01:P15 | A self-service "running late" button would reliably replace phone calls and could automatically extend a reservation. Priya expressed interest, but automatic extensions and their rules were not established. | Assumption | Media Lab manager |
| A-2 | INT-01:P19 | Equipment technicians could update preparation status through the same reservation dashboard used by desk staff. Their preferred workflow has not been investigated. | Assumption | Equipment technicians |
| Q-1 | INT-01:P06, INT-01:P12 | What grace period is officially configured, and how should students be informed when the policy changes? | Open | Media Lab manager |
| Q-2 | INT-01:P10, INT-01:P17, INT-01:P21 | When and through which channel should students receive release notifications, and what conditions must be satisfied before waitlisted students are notified? | Open | Media Lab manager |
| Q-3 | INT-01:P09, INT-01:P19 | How will equipment technicians confirm that a released kit is physically ready for the next checkout, and how should that status be communicated to desk staff? | Open | Equipment technicians |