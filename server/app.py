#!/usr/bin/env python3

from flask import Flask, make_response

# In-memory "database" of contracts. Each contract has an id and its details.
contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]

# Known customers. Their details are sensitive, so we only confirm they exist.
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)


@app.route('/contract/<int:id>')
def get_contract(id):
    """Return a contract's information by id.

    200: contract found, body is the contract information.
    404: no contract with that id.
    """
    for contract in contracts:
        if contract["id"] == id:
            return make_response(contract["contract_information"], 200)
    return make_response("Contract not found", 404)


@app.route('/customer/<customer_name>')
def get_customer(customer_name):
    """Confirm whether a customer exists without exposing their data.

    204: customer found, empty body (customer data is sensitive).
    404: customer not found.
    """
    if customer_name in customers:
        return make_response("", 204)
    return make_response("Customer not found", 404)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
