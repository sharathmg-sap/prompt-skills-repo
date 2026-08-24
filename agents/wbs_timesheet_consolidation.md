---
name: amsrow-timesheet-consolidation
description: Consolidate time-sheet data. The timesheet data is the tiem booked for customer support and shared as an Excel workbook. Consolidate into a Timesheet grouped and consolidation sheet. Use this agent whenever a user provides time-sheet exports with employee, account-assignment/WBS or Ticket in short text field, hours, and activity descriptions and wants customer-specific, WBS-based effort consolidation, ticket-level summaries, manual non-WBS additions, or reconciliation of a effort tracker.
---

# Objective AMS ROW Timesheet Consolidation

Use this workflow to produce a traceable customer effort tracker. If customer name is provided in the prompt or explicitly stated in file, use it to name the sheet and content with that customer name. 
Consolidation of effort in time is done wither per WBS code or ticket number. 

Ask the user to confirm if the consolidation is to be done by ticket number or WBS code. 

Confirm the columns used for effort consolidation with the user. 

## Pre-reuisites - Input 

Expect a workbook containing a detailed source sheet of efforts for WBS code and ticket id. In ITP effort sheet, short text holds the ticket number. 
In ITP, extract the ticket id fromt he short text. Explain the extraction to the user. 

It may also contain an existing `Consolidated` sheet with curated ticket rows and manual activities.

Detect the header row; do not assume the first row is a header.

## Workflow 

1. Normalize text for matching: trim whitespace, case-fold, and replace en/em dashes with hyphens.
2. Consider the customer name prepareference fromt he user prompt. If prompt does not mention the customer, look through the input excel. Explicitly confirm the customer name, before creating the excel. 
2.1 If the customer is SOHAR, classify a source record as **Automated <<Customer name>> WBS** only when its normalized `Acct assgnt text` exactly matches the configured customer label. In the reference workbook the label is `<<Customer name>> Consolidated Efforts`.
3. In ITP effort data, the Short text holds the ticket ID. Extract the ticket IDs from the column of short text and accordingly consolidate the rows per ticket id. 
4. Retain the source WBS and receiver as audit fields. 
5. Never assign rows belonging to another custome merely because an employee, short text, or ticket number looks similar.
6. Consolidate the rows per ticket ID and WBS into a separate sheet. Ensure that hours match the source timesheet file data
7. In case user requests to compare two timesheet data efforts, then cosnolidate efforts from sheets and find the difference in effort booking. 
8. When unsure on the columns or process, ask the user to confirm the following: 
-Customer name
- consolidate by Ticket id or WBS
- Compare the consolidation efforts - yes or no?

## Automated consolidation

For all Automated WBS/Timesheet records:

1. Convert `Number (unit)` to a numeric hour value and exclude blank separator/subtotal rows.
2. Group first by employee and then by work item.
3. Derive the work-item key from the first 10-digit ticket number in `Short Text` or `Long text` (for example, `8000001020`). If no ticket is present, use the normalized activity description.
4. Sum hours by employee + work-item key. Preserve a representative description and retain original descriptions in an audit/detail tab or traceable note.
5. Create resource subtotals and the grand total using spreadsheet formulas, not typed totals.

## Manual / non-WBS handling

Create a clearly separated `Manual(Non-Ticket) Efforts` area or sheet with editable columns:

| Resource Name | Ticket / Activity | Hours | Reason | Evidence / Source | Approval Status |
|---|---|---:|---|---|---|

- Do not infer a manual ticket from an unrelated customer WBS.
- Preserve ticket numbers exactly when provided; otherwise use a clear activity description, such as `BASIS` or `ABAP additional effort`.
- Include manual hours in SOHAR totals only when `Approval Status` is `Approved` or the user explicitly directs inclusion.
- Keep rejected, missing, and pending entries out of the final total and surface them as exceptions.
- When using an existing `Consolidated` sheet as a manual source, treat populated ticket/activity rows not traceable to the SOHAR WBS filter as manual candidates. Do not silently convert them into automated WBS data.

## Output: SOHAR Consolidated

Create or refresh a `<<Customer name>> Consolidated` sheet with this layout:

| Resource Name | Ticket Description | No of hours | Total Effort | Master Tracker | Source Type | WBS / Receiver | Reconciliation Note |
|---|---|---:|---:|---|---|---|---|

- List each resource once at the start of its block.
- Show ticket/activity rows beneath it; `No of hours` is the item-level amount.
- Show the resource subtotal in `Total Effort` on the resource row using a `SUM` formula over its detail rows.
- Set `Master Tracker = Updated` only for included rows that passed reconciliation; otherwise use `Review required`.
- Add a grand-total formula at the end.

## Reconciliation controls

1. Automated detail hours must equal automated resource subtotals.
2. Included approved manual hours must equal manual subtotals.
3. Every automated row must have the confirmed account-assignment text or WBS code.
4. A ticket/activity cannot appear as both automated and manual unless the user documents an approved split; flag it otherwise.
5. When refreshing an existing consolidation, show `Current Total`, `Rebuilt Total`, and `Difference` by resource and overall. Do not force a match by altering source hours.
6. Flag missing resource names, blank/invalid hours, non-approved manual entries, unrecognized account assignments, and total differences.

## Deliverable behavior

When refreshing a workbook, preserve the raw source sheet unchanged, create or update the consolidated sheet, and add an `<<Customer name>> Reconciliation` sheet documenting totals, differences, manual inclusions, exclusions, and exceptions. Use formulas for all subtotals and totals so the workbook recalculates when inputs change.
