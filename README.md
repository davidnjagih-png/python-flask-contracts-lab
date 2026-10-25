# Lab: Contractors Lab

---

## Overview

Now it is time for you to build your own request responses!

You are working for a company that manages contracts between two parties. You need to manage sensitive data, and as such, you need to build two requests:

- One for **customer information**
- One for **contract information**

You will be using two new response codes:

- **204**: Successful response but no data to send (e.g., confirming a customer exists without sharing data).
- **404**: Not found — we cannot find the requested data.

---

## Tasks

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `GET /contract/<id>`
  - **200**: Contract found — return contract information.
  - **404**: Contract not found.

- `GET /customer/<customer_name>`
  - **204**: Customer found — no information returned (sensitive).
  - **404**: Customer not found.

---

### Task 3: Develop the Code

- Initialize Flask
- Set up routes
- Configure responses

---

### Task 4: Test and Refine

- Debug and test during development using the provided test suite and Flask instance.

---

### Task 5: Document and Maintain

- Commit as you go with meaningful messages.
- Push commit history to GitHub periodically and when the lab is complete.

---

## Tools and Resources

- **GitHub Repo**: _Link to be provided_
- **Flask Quickstart**: [https://flask.palletsprojects.com/en/stable/quickstart/](https://flask.palletsprojects.com/en/stable/quickstart/)

---

## Instructions

### Set Up

Before coding:

1. **Fork and Clone**
   - Go to the provided GitHub repository link.
   - Fork the repository to your GitHub account.
   - Clone the forked repository to your local machine.

2. **Open and Run**
   - Open the project in VSCode.
   - Run `pipenv install` to install dependencies.
   - Run `pipenv shell` to activate the Python shell.

---

### Task 1: Define the Problem

Build the following routes:

- `/contract/<id>`
- `/customer/<customer_name>`

---

### Task 2: Determine the Design

#### App Routes:

- `/contract/<id>`
  - **200**: Contract found — return information
  - **404**: Contract not found

- `/customer/<customer_name>`
  - **204**: Customer found — return no information
  - **404**: Customer not found

---

### Task 3: Develop, Test, and Refine the Code

1. Create a **feature branch**.
2. Build the following routes:

#### `/contract/<id>`

- If the contract ID is found in the given array:
  - Return contract information with a **200** response.
- If not found:
  - Return a **404** response.

#### `/customer/<customer_name>`

- If the customer name is found:
  - Return a **204** response with an empty body.
- If not found:
  - Return a **404** response.

3. Push the feature branch and open a PR on GitHub.
4. Merge into `main`.

---

### Task 4: Document and Maintain

#### Best Practices:

- Add comments to explain logic and purpose.
- Clarify code intent for other developers.
- Include a screenshot of completed work in the README.
- Update the README to reflect functionality using [https://makeareadme.com](https://makeareadme.com).
- Delete stale branches on GitHub.
- Remove unnecessary or commented-out code.
- Update `.gitignore` if needed to exclude sensitive data

# Flask Contracts Lab

A small Flask API for a company that manages contracts between two parties. It exposes contract details on request, and confirms whether a customer exists without revealing any customer data, since that data is sensitive.

## Features

| Route                           | Response                       | Meaning                            |
| ------------------------------- | ------------------------------ | ---------------------------------- |
| `GET /contract/<id>`            | **200** + contract information | Contract with that id exists       |
| `GET /contract/<id>`            | **404**                        | No contract with that id           |
| `GET /customer/<customer_name>` | **204**, empty body            | Customer exists (details withheld) |
| `GET /customer/<customer_name>` | **404**                        | Customer not found                 |

Contracts and customers are held in in-memory lists in `server/app.py`.

## Setup

```bash
pipenv install
pipenv shell
```

## Usage

Start the server:

```bash
python server/app.py
```

It runs on `http://localhost:5555`. Example requests:

```bash
curl -i localhost:5555/contract/1      # 200 This contract is for John and building a shed
curl -i localhost:5555/contract/100    # 404
curl -i localhost:5555/customer/bob    # 204 (no body)
curl -i localhost:5555/customer/mario  # 404
```

## Testing

```bash
pytest
```

![All tests passing and route responses](assets/tests-passing.png)

## Status codes used

- **200 OK**: the request succeeded and the response carries data.
- **204 No Content**: the request succeeded, but there is deliberately no data to send.
- **404 Not Found**: the requested resource does not exist.
