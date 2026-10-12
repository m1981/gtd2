# GTD-App — Wymagania (EARS)

Wymagania systemowe w składni EARS, po angielsku; terminy pisane wielką literą pochodzą ze słownika (slownik.md, odpowiedniki angielskie w nawiasach). Każde wymaganie podaje tylko swoje źródło (P-03); wymagania pochodne i pokrycie pokazuje generowana macierz slad.md (P-04). Status `zatwierdzone` wymaga decyzji D-nn (P-08).

Wzorce: `ubiquitous` · `event` (When) · `state` (While) · `unwanted` (If…then) · `optional` (Where) · `complex`.

## Przechwytywanie

### CAP-01
- wzorzec: ubiquitous
- tekst: GTD-App shall store every captured Item in the Inbox without requiring a Project, Context or date.
- źródło: UC-01
- status: draft

### CAP-02
- wzorzec: event
- tekst: When the User submits a capture, GTD-App shall persist the Item within 1 s.
- źródło: UC-01
- status: draft
- uwagi: znaczenie „persist” otwarte (K-01)

### CAP-03
- wzorzec: unwanted
- tekst: If the device is offline during capture, then GTD-App shall store the Item locally and synchronise it upon reconnection.
- źródło: UC-01
- status: draft

### CAP-04
- wzorzec: event
- tekst: When the User saves a capture, GTD-App shall close the capture screen without proposing a further step.
- źródło: D-36
- status: draft

## Doprecyzowanie

### CLR-01
- wzorzec: event
- tekst: When the User marks an Item in the Inbox as non-actionable, GTD-App shall require its classification as Reference, Someday/Maybe or Trashed.
- źródło: UC-03
- status: draft

### CLR-02
- wzorzec: event
- tekst: When the User converts an Item into a Project, GTD-App shall require at least one Open Action for that Project.
- źródło: UC-03
- status: draft

### CLR-03
- wzorzec: unwanted
- tekst: If the User attempts to save a Project without an Open Action, then GTD-App shall reject the operation and indicate the missing Open Action.
- źródło: UC-03
- status: draft

### CLR-04
- wzorzec: ubiquitous
- tekst: GTD-App shall present "Do Now" as the first option of every Clarification.
- źródło: D-33
- status: draft

### CLR-05
- wzorzec: ubiquitous
- tekst: GTD-App shall present Items in the Inbox for Clarification from the oldest to the newest Capture.
- źródło: D-04
- status: draft

### CLR-06
- wzorzec: state
- tekst: While the Inbox is not Empty, GTD-App shall display the call to action "Process Inbox (N)" on the start screen, where N is the number of Items in the Inbox.
- źródło: D-32
- status: draft

## Projekty

### PRJ-01
- wzorzec: event
- tekst: When the last Open Action of an Active Project is completed, GTD-App shall prompt the User to define the next Action of that Project.
- źródło: ZP-01
- status: draft

### PRJ-02
- wzorzec: state
- tekst: While an Active Project has no Open Action, GTD-App shall display it as Stalled with the options "Add Next Action", "Move to Someday/Maybe" and "Complete Project".
- źródło: D-26
- status: draft

### PRJ-03
- wzorzec: state
- tekst: While every Open Action of an Active Project is Unprepared, GTD-App shall display the Project as Needs Preparation with the call to action "Prepare".
- źródło: D-19
- status: draft

### PRJ-04
- wzorzec: event
- tekst: When the User completes a Project, GTD-App shall display the call to action "Show Stalled Projects".
- źródło: D-35
- status: draft

## Czekam na

### WAI-01
- wzorzec: state
- tekst: While an Action is in Waiting For, GTD-App shall display its Delegate and Delegation Date.
- źródło: G-ELM-06
- status: draft

### WAI-02
- wzorzec: state
- tekst: While an Action in Waiting For is past its Follow-up Date, GTD-App shall display it as overdue with the options "Contact Delegate" and "Postpone Follow-up".
- źródło: D-30
- status: draft

## Przygotowanie

### PRZ-01
- wzorzec: state
- tekst: While an Action is Unprepared, GTD-App shall display it in Next Action Views with the call to action "Prepare".
- źródło: D-17
- status: draft

### PRZ-02
- wzorzec: event
- tekst: When the User selects "Prepare" on an Action, GTD-App shall open the Preparation View limited to that Action, with Purchase Items grouped by shop above Gather Items.
- źródło: UC-04, D-24
- status: draft

### PRZ-03
- wzorzec: event
- tekst: When the last Preparation Item of an Action is checked, GTD-App shall display the call to action "Start" for that Action.
- źródło: UC-04
- status: draft

### PRZ-04
- wzorzec: state
- tekst: While an Unprepared Action has a Scheduled Date within the preparation lead time, GTD-App shall display the call to action "Prepare" on the start screen.
- źródło: D-31
- status: draft

### PRZ-05
- wzorzec: ubiquitous
- tekst: GTD-App shall display, in the View of a Place of category Shop, the unchecked Purchase Items of all Actions in a section above the Actions.
- źródło: D-22, D-25
- status: draft

## Działanie i przegląd

### ENG-01
- wzorzec: ubiquitous
- tekst: GTD-App shall allow the User to filter Next Actions by Context, Time Estimate and Energy Level.
- źródło: G-ELM-13
- status: draft

### REV-01
- wzorzec: event
- tekst: When 7 days have passed since the last completed Weekly Review, GTD-App shall remind the User to perform one.
- źródło: G-OPR-13
- status: draft

### REV-02
- wzorzec: event
- tekst: When the User starts a Weekly Review, GTD-App shall guide the User through each Checklist Item in order and open the View of each system Checklist Item.
- źródło: D-34
- status: draft

### CAL-01
- wzorzec: optional
- tekst: Where calendar integration is enabled, GTD-App shall display Scheduled Actions in the External Calendar.
- źródło: UC-02
- status: draft
