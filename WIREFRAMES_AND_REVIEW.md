# Cafe Gharti Wireframes, Screen Flow, and HTML Review

The static pages in [`mockup/`](./mockup/) implement these labeled wireframe
specifications. Each specification can be redrawn in Excalidraw with boxes and
arrows; every heading, input, button, list, and list field is named so the
wireframe and HTML can be compared directly.

## Wireframe specifications

### Menu (`mockup/menu.html`)

- Header: Cafe Gharti logo/name; links **Menu**, **Your order**, **Order
  status**, **Staff board**.
- Main heading: **Good morning, Maya** and short instruction.
- Category navigation: **Hot drinks**, **Bakery**, **Breakfast**.
- Item cards: item name, description, price, and **Add to order** button.
- Sold-out card: **Ham croqueta**, price, sold-out label, disabled
  **Unavailable** button.
- Footer action: **View your order**.

### Your order (`mockup/order.html`)

- Header: Cafe Gharti name and the same customer links.
- Heading: **Your order** and review instruction.
- Items section: **Menu item** select, **Quantity** number input, and optional
  **Special notes** textarea.
- Customer section: required **Name for the order** input.
- Order summary: selected item, quantity, and total.
- Actions: **Place order** and **Back to menu**.

### Order confirmation (`mockup/confirmation.html`)

- Header: Cafe Gharti name and customer links.
- Confirmation card: **Order received!**, greeting, and explanation.
- Details list: order number, customer name, and received status.
- Items list: each item and price, followed by total.
- Actions: **Check order status** and **Order something else**.

### Order status (`mockup/status.html`)

- Header: Cafe Gharti name and customer links.
- Heading: **Check your order** and instruction.
- Required **Order number** input and **Show status** button.
- Status card: order number, current **Preparing** status, explanation, and
  four-step list: received, preparing, ready for pickup, picked up.
- Action: **Back to menu**.

### Kitchen board (`mockup/kitchen.html`)

- Staff header: Cafe Gharti kitchen; links **Board**, **Order history**, **Menu
  admin**, and **Customer view**.
- Heading: **Kitchen board**, date/time, and signed-in staff role.
- Four status columns: **Received**, **Preparing**, **Ready**, and **Picked
  up**.
- Each order card shows order number, time, customer, item list, and the next
  status button.
- Empty-state text appears in the picked-up column when it has no current
  orders.
- Footer action: **View recent order history**.

### Order history (`mockup/history.html`)

- Staff header with links to the board, history, menu admin, and customer view.
- Heading: **Recent order history** and date description.
- Table columns: order, customer, items, completed time, and status.
- Action: **Back to kitchen board**.

### Menu administration (`mockup/menu-admin.html`)

- Staff header with links to the board, history, menu admin, and customer view.
- Heading and note that this is a static mockup and changes are not saved.
- Add-item form: item name, description, price, category, and **Add item**
  button.
- Current-items table: item, price, availability, and **Edit** action.

## Screen flow

```text
Menu
  -> Your order
       -> Order confirmation
            -> Order status
                 -> Menu

Staff board <-> Order history
Staff board <-> Menu administration
Menu <----------------------> Staff board (role-based views)
```

The customer flow demonstrates browsing, selecting, submitting, confirming,
and checking status. The staff flow demonstrates viewing current work,
advancing an order, reviewing completed work, and maintaining the menu.

## Must-have story-to-screen check

| Must-have story | Screen that supports it |
|---|---|
| US-1 Browse the menu | Menu |
| US-2 Select an item and quantity | Your order |
| US-3 Submit an order with a customer name | Your order |
| US-4 Confirm an order | Order confirmation |
| US-5 See order status | Order status |
| US-6 View the kitchen board | Kitchen board |
| US-7 Move an order to its next status | Kitchen board |

US-8, preventing unauthorized status changes, is represented by the separate
customer and staff navigation plus the staff-only controls on the kitchen
board. US-9 is represented by Order history as a should-have screen.

## HTML prompts and review log

### Prompts used

The following prompt pattern was used once per page, changing the filename and
wireframe details:

> Context: static HTML mockup for the Cafe Gharti ordering prototype. No
> JavaScript and no backend. Create `mockup/[page].html` from the labeled
> wireframe. Use semantic HTML, realistic Cafe Gharti sample data, and Pico CSS
> from `https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css`.
> Preserve the listed headings, inputs, buttons, lists, and navigation links.
> Acceptance check: the page opens directly in a browser, matches every
> wireframe label, and every link follows the screen flow.

Page-specific prompts added these details:

- **Menu:** three category links, five realistic items, one sold-out item, and
  links to `order.html`.
- **Your order:** item select, positive quantity, optional notes, required name,
  order total, and link to `confirmation.html`.
- **Confirmation:** order number, customer, item list, received status, and
  link to `status.html`.
- **Status:** order-number field, four status steps, and a preparing sample.
- **Kitchen board:** four status columns, three sample orders, next-status
  controls, and empty-state text.
- **History:** completed-order table and link back to the board.
- **Menu admin:** add-item form and current-items availability table.

### Review prompt

> Here are my static HTML pages for a Flask prototype. Check each page against
> its wireframe and screen flow. List only mismatches involving missing
> headings, fields, buttons, data, Pico CSS, semantic HTML, or broken
> navigation. Do not redesign the pages.

### Review decisions

| Review flag | Decision | Reason |
|---|---|---|
| The kitchen action “Complete” was ambiguous. | Accepted | It was changed to the precise next-state labels “Mark ready” and “Mark picked up.” |
| The sold-out menu item still looked selectable. | Accepted | It now has a sold-out label and a disabled “Unavailable” button. |
| The status page did not explain the complete path. | Accepted | It now lists received, preparing, ready for pickup, and picked up in order. |
| Menu administration should be removed because it is not in the smallest customer flow. | Rejected | The original project scope lists menu administration as a must-have feature, so the screen remains available even though its form is static. |
| Static controls should pretend to save data. | Rejected | The assignment asks for a clickable mockup only; the admin page explicitly says changes are not saved. |

## Questions

### 1. Which part of a wireframe was hardest to describe in a prompt?

The kitchen board was hardest because it has four parallel status columns and
each order card needs the same fields plus a different next action. I solved
this by naming every column, giving each sample card an order number, time,
customer, and item list, and specifying the exact next-status button in the
prompt.

### 2. Give one example where the HTML did not match the wireframe.

The first kitchen-board wording used the generic action **Complete**, which did
not tell the user which status would follow. I changed the page to use
**Start preparing**, **Mark ready**, and **Mark picked up**, matching the
wireframe's next-state labels and making the flow easier to test.
