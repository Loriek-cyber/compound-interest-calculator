# Compound Interest Calculator

## Description
This project is a simple Python program that calculates compound interest. Compound interest is the interest on a loan or deposit calculated based on both the initial principal and the accumulated interest from previous periods.

## Features
- User input for principal amount, interest rate, time period, and number of compounding periods per year.
- Calculation of compound interest.
- Display of the final amount.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
```bash
$ git clone https://github.com/username/compound_interest_calculator.git
```

2. Navigate to the project directory:
```bash
$ cd compound_interest_calculator
```

3. Run the script:
```bash
$ python compound_interest.py
```

## Usage
1. Run the program.
2. Input the principal amount (e.g., 1000).
3. Input the annual interest rate (e.g., 5 for 5%).
4. Input the time in years (e.g., 10).
5. Input the number of times interest is compounded per year (e.g., 4 for quarterly).

The program will output the final amount after the specified time period.

## Formula Used
The compound interest formula is:

\[ A = P \left(1 + \frac{r}{n}\right)^{nt} \]

Where:
- A = final amount
- P = principal amount
- r = annual interest rate (in decimal form)
- n = number of times interest is compounded per year
- t = time in years

## Example Output
```
Enter principal amount: 1000
Enter annual interest rate (in %): 5
Enter time in years: 10
Enter number of times interest is compounded per year: 4

The final amount is: 1647.01
```

## License
This project is licensed under the MIT License.

