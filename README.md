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

### Previous work in Mortgage Calculators

Previous code I'll use to write the calculator.

- [cost_of_living_calculator](https://github.com/diogo-pessoa/coding-exercises/tree/main/cost_of_living_calculator)

## Dependencies

- Python 3.12
    - [requirements.txt](requirements.txt)
- React
    - react-native-cli, through `brew`

- Bootstrap, through `npm`

## run

### Frontend
```
npm install react-bootstrap
npm install react-bootstrap bootstrap bootswatch
npm run build

127.0.0.1:3000
```




## dependency scanning, static code Analysis

### locally

- `npm audit`
- `python safety`, `pip-audit` & `python bandit`

### Running back-end locally

```
 curl --location --request POST 'http://127.0.0.1:3001/calculate' \
--header 'Content-Type: application/json' \
--data-raw '{
    "principal": 200000,
    "annual_rate": 5,
    "years": 30
}'

```

## Using sam-cli and running it locally

```bash

commands you can use next:
=========================
[*] Create pipeline: cd mortgageCalculator && sam pipeline init --bootstrap
[*] Validate SAM template: cd mortgageCalculator && sam validate
[*] Test Function in the Cloud: cd mortgageCalculator && sam sync --stack-name {stack-name} --watch
```

-  sam local start-api  

## References

- [AWS Api-Gateway](https://docs.aws.amazon.com/apigateway/)
- [AWs Lambda](https://aws.amazon.com/lambda/)
- [AWS S3](https://aws.amazon.com/s3/)
- [React](https://reactjs.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [Cyborg bootswatch theme](https://bootswatch.com/cyborg/)
