# Salesperson Pay Calculator

## Project Overview

This Python program calculates a salesperson's pay based on their monthly sales, advanced pay, and applicable commission rate. It uses a tiered commission structure to determine the salesperson’s pay and includes robust error handling, input validation, and logging to ensure reliability and traceability in a real-world environment.

## Key Features

- **Sales Calculation**: The program calculates the pay by considering monthly sales, advance pay, and commission rates.
- **Commission Rate**: The commission rate is determined based on sales:
  - Sales less than $10,000: 10% commission
  - Sales between $10,000 and $14,999.99: 12% commission
  - Sales between $15,000 and $17,999.99: 14% commission
  - Sales between $18,000 and $21,999.99: 16% commission
  - Sales above $22,000: 18% commission
- **Advanced Pay**: Deducts any advanced pay from the total commission.
- **Error Handling & Input Validation**: Ensures that the program handles invalid inputs gracefully and prompts the user to enter valid data.
- **Logging**: Logs runtime information and errors to a log file.
- **User-Friendly Interface**: The program interacts with the user to collect necessary input for sales and advanced pay.

## Requirements

- Python 3.x

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/salesperson-pay-calculator.git
Navigate to the project directory:

bash
Copy
cd salesperson-pay-calculator
Run the program:

bash
Copy
python salesperson_pay_calculator.py
Usage
When you run the program, it will prompt you for:

Monthly sales amount.

The amount of advance pay (if any).

After entering the required data, the program calculates and displays the salesperson’s pay based on the sales and commission rate.

If the pay is negative, the program informs the user that the salesperson must reimburse the company.

The pay calculation is based on the following logic:

The program determines the applicable commission rate based on sales and calculates the commission.

It then subtracts the advanced pay from the total commission to calculate the net pay.

All logs and errors will be saved in the salesperson-pay-calculator.log file.

Code Structure
bash
Copy
salesperson-pay-calculator/
│
├── salesperson_pay_calculator.py  # Main logic for calculating pay
├── salesperson-pay-calculator.log  # Log file for errors and events
└── README.md                     # Project documentation
Example of Program Output
bash
Copy
Enter the amount of monthly sales: $15000
Enter the amount of advanced pay, or enter 0 if no advanced pay: $1000
The pay is $1,400.00
The salesperson has earned their pay.
Error Handling
If the user enters invalid data (e.g., a non-numeric value for sales or advanced pay), the program will catch the error, log it, and prompt the user to re-enter the correct data.

If the final pay is negative (i.e., the salesperson’s commission doesn’t cover the advanced pay), the program will notify the user that the salesperson must reimburse the company.

Logging
All significant events, including user inputs, commission rate calculations, and errors, are logged to salesperson-pay-calculator.log. This helps with debugging and provides traceable information about the program’s operations.

Future Enhancements
Unit Tests: Adding unit tests to ensure the correctness of commission calculations and input validation.

Web Interface: Implementing a web-based user interface to make the program more interactive and user-friendly.

Extended Commission Logic: Introducing more complex commission structures or multiple tiers based on different sales categories.

License
This project is licensed under the MIT License.

Acknowledgments
This project is designed to demonstrate fundamental Python programming techniques, including modularity, error handling, and logging.

Inspired by real-world scenarios in sales management and payroll systems.
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/salesperson-pay-calculator.git

