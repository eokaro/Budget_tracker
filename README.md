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

