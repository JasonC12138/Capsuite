from flask import Flask, request, jsonify, render_template
import sqlite3
import json
import mysql.connector

app = Flask(__name__)
conn = mysql.connector.connect(
    user="root",
    password="for-root-test-only",
    host="localhost",
    port="3306",
    database="classicmodels",
)


@app.route("/")
def list_customer():
    query = "SELECT customerNumber, customerName, contactLastName, contactFirstName, creditLimit FROM customers ORDER BY creditLimit "
    cursor = conn.cursor()
    cursor.execute(query)
    customers = []
    for row in cursor:
        customers.append(
            {
                "customerNumber": row[0],
                "customerName": row[1],
                "contactLastName": row[2],
                "contactFirstName": row[3],
                "creditLimit": row[4],
            }
        )
    return jsonify(customers)

@app.route("/get_full", methods=["POST"])
def get_full():
    if request.method == ['POST']:
        customer_name = request.form['customer_name']
        query = "SELECT * FROM customers WHERE customer_name = " + customer_name
        cursor = conn.cursor()
        cursor.execute(query)
        get_full = []
        for row in cursor:
            get_full.append(
                {
                    "customerNumber": row[0],
                    "customerName": row[1],
                    "contactLastName": row[2],
                    "contactFirstName": row[3],
                    "phone": row[4],
                    "addressLine1": row[5],
                    "addressLine2": row[6],
                    "city": row[7],
                    "state": row[8],
                    "postalCode": row[9],
                    "country": row[10],
                    "salesRepEmployeeNumber": row[11],
                    "creditLimit": row[12],
                }
            )
        return jsonify(get_full)


@app.route("/update_cust", methods=["POST"])
def update_customer():
    if request.method == "POST":
        customer_number = request.form["id"]
        first_name = request.form["first name"]
        last_name = request.form["last name"]
        query = (
            "UPDATE customers SET customerName = "
            + last_name
            + " "
            + first_name
            + "WHERE customerNumber = "
            + customer_number
        )
        cursor = conn.cursor()
        cursor.execute(query)


if __name__ == "__main__":
    app.run(debug=True)
