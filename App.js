import React, { useState, useEffect } from 'react';

function App() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    fetch('/')
      .then(response => response.json())
      .then(data => setCustomers(data));
  }, []);

  return (
    <div>
      <h1>Customer List</h1>
      <table>
        <thead>
          <tr>
            <th>Customer Number</th>
            <th>Customer Name</th>
            <th>Contact Last Name</th>
            <th>Contact First Name</th>
            <th>Credit Limit</th>
          </tr>
        </thead>
        <tbody>
          {customers.map(customer => (
            <tr key={customer.customerNumber}>
              <td>{customer.customerNumber}</td>
              <td>{customer.customerName}</td>
              <td>{customer.contactLastName}</td>
              <td>{customer.contactFirstName}</td>
              <td>{customer.creditLimit}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;