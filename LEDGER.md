# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Add your entries below this line, starting with Entry 1.

---
## Entry 1
artifact:  evidence/schema.md (Part 1 – Evidence Log) at 2b3fc0890c8c337a3caae4ddb22021b8af55e8d5
tool:      OpenAI ChatGPT, GPT-6, 13 October 2026
prompts:   prompts/evidence-log-v1.md — Asked AI to review the interview transcript and create 10 evidence entries using E, A, and Q identifiers, with paragraph citations and the required schema.
review:    Reviewed the generated evidence log against transcripts/interview.txt and evidence/schema.md. Checked that evidence statements referenced actual interview paragraphs and that assumptions and open questions were identified separately. Kept the conflicting 15-minute and 20-minute grace periods unresolved rather than selecting one as the correct policy.
checks:    Manual review of the 10 generated entries against the interview and schema. Confirmed the draft contains 5 evidence entries, 2 assumptions, and 3 open questions. No automated tests were run.
evidence:  E-1 through E-5, A-1 through A-2, Q-1 through Q-3
risk:      The official grace period remains unconfirmed. Assumptions about automatic extensions and technician workflows still require stakeholder validation.

---

## Entry 2
artifact:  report/report.md (Part 2 – Evidence Audit) at d85605dfa61ba5ab10851068e717b0fdc23da54d
tool:      OpenAI ChatGPT, GPT-6, 13 October 2026
prompts:   prompts/evidence-audit-v1.md — Asked AI to identify contradictions, ambiguous statements, missing stakeholders, compliments, predictions, and a specific past event from the interview.
review:    Reviewed the seven audit classifications and their paragraph references. Checked that the contradiction between Jordan and Priya was not resolved without evidence. Distinguished the vague phrase "only a little late" from the unclear notification recipients and timing. Kept Priya's dashboard compliment and predicted button usage separate from evidence of actual behavior.
checks:    Manual inspection of the seven-row audit table. Checked that each requested category was represented and that explanations were limited to two sentences. No automated tests were run.
evidence:  E-2, E-4, E-5, A-1, A-2, Q-1, Q-2, Q-3; INT-01:P06, P07, P10, P12, P13, P14, P15, P19
risk:      The audit identifies uncertainties but does not resolve them. Equipment technicians have not been interviewed, and the official grace-period policy still requires confirmation.

---

## Entry 3

artifact:  report/report.md (Part 3 – Requirements and Acceptance Criteria) at d85605dfa61ba5ab10851068e717b0fdc23da54d
tool:      OpenAI ChatGPT, GPT-6, 14 October 2026
prompts:   prompts/requirements-v1.md — Asked AI to develop four Connextra user stories, structured requirements, evidence traces, INVEST checks, and three Given-When-Then acceptance criteria.
review:    Reviewed the four requirements for observable behavior, scope, and evidence traceability. Kept the grace period configurable rather than treating either interview value as settled policy. Selected reservation release, check-in protection, and staff hold protection for acceptance criteria because these behaviors can be tested by the reference module. Left technician workflow details open and did not create notification acceptance tests because the reference module cannot verify them.
checks:    Manual review confirmed four requirement slices (R-1 through R-4), six INVEST checks per requirement, and three acceptance criteria (AC-1 through AC-3) covering different requirements. No reference-module tests were executed at this stage.
evidence:  R-1 → E-2, Q-1; R-2 → E-1, E-2; R-3 → E-3; R-4 → E-4, Q-3; AC-1 → R-1; AC-2 → R-2; AC-3 → R-3
risk:      Acceptance criteria have not yet been executed against the reference module. The exact policy configuration, staff hold boundary behavior, and technician readiness workflow require further verification.

---

## Entry 4

artifact:  report/report.md (Part 4 – Implementation-Ready Specification for R-2) at d85605dfa61ba5ab10851068e717b0fdc23da54d
tool:      OpenAI ChatGPT, GPT-6, 14 October 2026
prompts:   prompts/implementation-spec-v1.md — Asked AI to convert one evidence-supported requirement into an implementation-ready specification with a typed Python interface, preconditions, postconditions, invariant, edge cases, non-goal, settled decisions, and unresolved questions.
review:    Reviewed the specification for R-2 (Student Check-In Protection) against the interview evidence and earlier requirements. Checked that the function signature uses appropriate Python types and that checked-in reservations remain active after the grace period. Kept the grace period configurable and identified unresolved policy decisions rather than allowing the implementation agent to assume them.
checks:    Manual review of the specification against spec/spec_template.md. Verified the presence of a typed function signature, explicit preconditions and postconditions, one invariant, six edge cases, exactly one non-goal, settled decisions, and open questions. No implementation code was written or automated tests executed.
evidence:  R-2, E-1, E-2, Q-1; INT-01:P02, INT-01:P17, INT-01:P21
risk:      The official grace period remains disputed. Simultaneous check-in and release events, hold expiration boundaries, and reactivation behavior require stakeholder confirmation before implementation.

---
## Entry 5 — AI Ambiguity Audit

artifact:  results/ambiguity_audit.md (Part 6 – AI Ambiguity Audit of INT-01) at 2b3fc0890c8c337a3caae4ddb22021b8af55e8d5
tool:      OpenAI ChatGPT, GPT-6, October 16, 2026
prompts:   prompts/ambiguity_audit_prompt.txt — Asked AI to identify up to eight ambiguities, incomplete requirements, and direct contradictions in the interview, with paragraph references and unsafe implementation decisions.
review:    Reviewed all eight AI findings against the original interview transcript. Classified each finding as a true positive or false positive based on supporting paragraph evidence. All eight were classified as true positives. Confirmed that the audit did not resolve disputed policies or introduce unsupported product requirements.
checks:    Manually verified paragraph references, quoted excerpts, defect classifications, and explanations against INT-01. Confirmed eight findings, eight true positives, and zero false positives. No automated tests were required.
evidence:  INT-01:P04, P06, P07, P09, P10, P12, P13, P17, P19, P21.
risk:      The official grace period, staff-hold expiration rules, notification requirements, equipment-readiness workflow, and waitlist handoff remain unresolved and require stakeholder clarification.
