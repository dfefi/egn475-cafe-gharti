# Cafe Gharti User Stories and Acceptance Criteria

These stories define the prototype backlog for Cafe Gharti. They use the
personas from the project README:

- **Maya:** a customer ordering coffee and breakfast before work.
- **Luis:** a kitchen staff member preparing orders and updating their status.

Priority meanings:

- **Must-have:** required for the prototype's basic ordering and kitchen flow.
- **Should-have:** valuable for a usable prototype, but the prototype can still
  demonstrate its core flow without it.
- **Could-have:** useful if time remains after the must-have and should-have
  work is complete.

## Backlog

### US-1 — Browse the menu

**Priority:** Must-have

**As a** customer, **I want** to see available menu items with their
descriptions and prices, **so that** I can choose breakfast quickly and
confidently.

**Acceptance criteria**

1. **Given** the menu contains available items, **when** the customer opens the
   menu, **then** each available item shows its name, description, and price.
2. **Given** an item is sold out, **when** the customer opens the menu, **then**
   that item is clearly marked unavailable and cannot be selected.

### US-2 — Select an item and quantity

**Priority:** Must-have

**As a** customer, **I want** to select an available item and quantity, **so
that** my order contains the food and drink I want.

**Acceptance criteria**

1. **Given** an item is available, **when** the customer selects a positive
   quantity, **then** the selected item and quantity appear in the order
   summary.
2. **Given** the quantity is empty, zero, or negative, **when** the customer
   tries to add the item, **then** the order is not updated and a message asks
   for a valid quantity.

### US-3 — Submit an order with a customer name

**Priority:** Must-have

**As a** customer, **I want** to provide my name and submit my order, **so
that** staff can identify it when it is ready.

**Acceptance criteria**

1. **Given** the order contains at least one available item and a non-blank
   customer name, **when** the customer submits it, **then** a new order is
   created with the items, name, and received status.
2. **Given** the customer name is empty or contains only spaces, **when** the
   customer submits the order, **then** the order is not created and a message
   asks for a name.

### US-4 — Confirm an order

**Priority:** Must-have

**As a** customer, **I want** to see an order confirmation with my order
details, **so that** I know the café received my request.

**Acceptance criteria**

1. **Given** a valid order has been submitted, **when** the submission
   completes, **then** the customer sees a confirmation containing the order
   identifier, name, items, and received status.
2. **Given** the submission fails, **when** the customer views the result, **then**
   no success confirmation is shown and the customer receives an explanation
   that the order was not created.

### US-5 — See order status

**Priority:** Must-have

**As a** customer, **I want** to see whether my order is received, preparing,
ready, or picked up, **so that** I know when to return for my food.

**Acceptance criteria**

1. **Given** a valid order identifier, **when** the customer checks the order,
   **then** the current status is shown as one of received, preparing, ready,
   or picked up.
2. **Given** the identifier is empty or does not match an order, **when** the
   customer checks the order, **then** no order details are shown and a
   not-found message is displayed.

### US-6 — View the kitchen board

**Priority:** Must-have

**As a** kitchen staff member, **I want** to see current orders grouped by
status, **so that** I can prepare them in an organized order.

**Acceptance criteria**

1. **Given** orders exist in different statuses, **when** Luis opens the
   kitchen board, **then** each current order appears with its customer name,
   items, and status in the matching status group.
2. **Given** there are no current orders, **when** Luis opens the kitchen
   board, **then** the board shows an empty-state message instead of an
   unexplained blank page.

### US-7 — Move an order to its next status

**Priority:** Must-have

**As a** kitchen staff member, **I want** to move an order to the next status,
**so that** customers receive an accurate progress update.

**Acceptance criteria**

1. **Given** a received order is on the kitchen board, **when** Luis selects
   Start preparing, **then** the order moves to preparing and the new status
   is visible on the board.
2. **Given** an order is already picked up, **when** anyone attempts to move it
   to another status, **then** the status does not change and an explanation
   says that a picked-up order is complete.

### US-8 — Prevent unauthorized status changes

**Priority:** Should-have

**As a** café owner, **I want** only kitchen staff to change order statuses,
**so that** customers cannot accidentally or intentionally change progress.

**Acceptance criteria**

1. **Given** a customer is viewing an order, **when** the customer tries to
   change its status, **then** the change is refused and the original status
   remains unchanged.
2. **Given** a user has no recognized role, **when** the user requests the
   status-change action, **then** the action is refused with a permission
   message and no order data is changed.

### US-9 — Review recently completed orders

**Priority:** Should-have

**As a** kitchen staff member, **I want** to review recently picked-up orders,
**so that** I can confirm what has already been completed during a busy shift.

**Acceptance criteria**

1. **Given** picked-up orders exist, **when** Luis opens order history, **then**
   the recent orders show their identifiers, customer names, items, and
   completion status.
2. **Given** no orders have been picked up, **when** Luis opens order history,
   **then** an empty-state message explains that there are no completed orders.

## INVEST review and decisions

The following prompt was used to request a review:

> Here are my user stories for a Flask prototype. Check each one against INVEST
> and tell me which are too big, vague or not testable. Do not rewrite them;
> list problems only.

The review identified these concerns:

1. **US-3 (original combined order story) was too large:** selecting items,
   entering a name, and submitting an order were separate behaviors. **Accepted.**
   The work was split into US-2 and US-3 so each story has one goal and can be
   tested independently.
2. **The original “manage the menu” story was too large:** adding, editing,
   pricing, and marking items unavailable represented several workflows.
   **Rejected for this iteration.** Menu administration is not necessary to
   demonstrate the customer-to-kitchen prototype, so it remains outside this
   backlog rather than being added as a vague oversized story.
3. **The original “keep customers informed” story was vague and not directly
   testable:** it did not identify which status was shown or how a customer
   looked it up. **Accepted.** It was made concrete as US-5, which names the
   four statuses and defines the invalid-identifier behavior.
4. **The original kitchen-board story combined viewing and updating orders.**
   **Accepted.** It became US-6 (view the board) and US-7 (move an order), each
   with one primary goal.
5. **The original order-history story was a lower-value enhancement rather than
   a core ordering slice.** **Accepted.** It is retained as a should-have so
   the prototype can defer it without blocking the main flow.

I accepted the flags that improved story size, specificity, or testability. I
rejected only the menu-administration flag as a backlog item: the concern is
valid, but the feature is intentionally outside the prototype's smallest
demonstrable flow.

## Questions

### 1. Which story did you split into smaller stories, and why?

I split the original story about placing an order into **US-2 (select an item
and quantity)** and **US-3 (submit an order with a customer name)**. Selecting
an item and submitting an order have different validation rules and different
failure cases. Splitting them makes each story independently testable and keeps
each one focused on one customer goal.

I also split the original kitchen workflow into **US-6 (view the kitchen
board)** and **US-7 (move an order to its next status)** because seeing work
and changing work are separate staff activities.

### 2. Which story was hardest to write acceptance criteria for?

**US-8, preventing unauthorized status changes,** was hardest because it has
two different failure situations: a recognized customer role and an unknown
role. The criteria had to verify both the visible permission result and the
important side effect that the order status remains unchanged. That made the
edge case more specific than simply saying “the user is denied.”
