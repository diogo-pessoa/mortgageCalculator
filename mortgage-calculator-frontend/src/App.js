import React, { useState } from 'react';
import { Container, Form, Button, Row, Col, Alert } from 'react-bootstrap';

function App() {
  const [principal, setPrincipal] = useState('');
  const [annualRate, setAnnualRate] = useState('');
  const [years, setYears] = useState('');
  const [monthlyPayment, setMonthlyPayment] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await fetch('YOUR_API_GATEWAY_URL/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ principal, annual_rate: annualRate, years })
      });
      const data = await response.json();
      if (response.ok) {
        setMonthlyPayment(data.monthly_payment);
      } else {
        setError(data.error);
      }
    } catch (error) {
      setError('An error occurred. Please try again later.');
    }
  };

  return (
    <Container>
      <h1 className="my-4">Mortgage Calculator</h1>
      <Form onSubmit={handleSubmit}>
        <Form.Group as={Row} controlId="principal">
          <Form.Label column sm={2}>Principal</Form.Label>
          <Col sm={10}>
            <Form.Control
              type="number"
              value={principal}
              onChange={(e) => setPrincipal(e.target.value)}
              required
            />
          </Col>
        </Form.Group>
        <Form.Group as={Row} controlId="annualRate">
          <Form.Label column sm={2}>Annual Rate (%)</Form.Label>
          <Col sm={10}>
            <Form.Control
              type="number"
              value={annualRate}
              onChange={(e) => setAnnualRate(e.target.value)}
              required
            />
          </Col>
        </Form.Group>
        <Form.Group as={Row} controlId="years">
          <Form.Label column sm={2}>Years</Form.Label>
          <Col sm={10}>
            <Form.Control
              type="number"
              value={years}
              onChange={(e) => setYears(e.target.value)}
              required
            />
          </Col>
        </Form.Group>
        <Button type="submit" className="my-4">Calculate</Button>
      </Form>
      {monthlyPayment !== null && (
        <Alert variant="success">
          Monthly Payment: ${monthlyPayment.toFixed(2)}
        </Alert>
      )}
      {error && (
        <Alert variant="danger">
          {error}
        </Alert>
      )}
    </Container>
  );
}

export default App;
