# mortgageCalculator

Basic mortgage calculator (Python) deployed in AWS Api Gateway and Lambda

## Summary

The setup below, is deliberate. My goal is to experiment with React, AWS Gateway
(with a Python backend).
A front-end. Using a React app styled with Bootstrap. Interacting with a backend API
Gateway endpoint.

- **Front-end** hosted in AWS S3

- **Back-end** with AWS Api-Gateway and AWS Lambda.

As an experiment, I've used a bit of _LLMs_ to create the boilerplate code during the
initial setup. :ok_hand: Saved quite a lot of time.

## Dependencies

- Python 3.12
    - [requirements.txt](requirements.txt)
- React
    - react-native-cli, through `brew`

- Bootstrap, through `npm`

## run

```
npm run build

```

## dependency scanning, static code Analysis

### locally

- `npm audit`
- `python safety`, `pip-audit` & `python bandit`