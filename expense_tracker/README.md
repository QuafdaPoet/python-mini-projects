# Expense Tracker

A simple Python console mini project for tracking personal expenses.

This project allows users to input expense names, amounts, and categories, then calculates useful spending statistics such as total spending, average spending, category totals, highest expense, and lowest expense.

## Features

- Input the number of expenses
- Validate that the number of expenses is greater than 0
- Input expense names
- Input expense amounts
- Validate that each amount is greater than 0
- Input expense categories
- Validate expense categories:
  - `food`
  - `drink`
  - `transport`
  - `other`
- Print all expense records
- Calculate total spending
- Calculate average spending
- Count expenses by category
- Calculate total spending by category
- Find the highest expense amount
- Show all expense names with the highest amount
- Find the lowest expense amount
- Show all expense names with the lowest amount
- Count expenses greater than `100000` VND
- Count expenses less than or equal to `100000` VND

## Expense Categories

| Category | Meaning |
|---|---|
| `food` | Food expenses |
| `drink` | Drink expenses |
| `transport` | Transportation expenses |
| `other` | Other expenses |

## Project Structure

```text
expense_tracker/
│
├── main.py
└── README.md
```

## How to Run

Open terminal in the project folder:

```bash
cd D:\python-mini-projects\expense_tracker
python main.py
```

If `python` does not work, try:

```bash
py main.py
```

## Example Input

```text
Nhap so luong khoan chi = 5

Nhap ten khoan chi 1: An trua
Nhap so tien: 35000
Nhap loai chi tieu: food

Nhap ten khoan chi 2: Tra sua
Nhap so tien: 50000
Nhap loai chi tieu: drink

Nhap ten khoan chi 3: Xang xe
Nhap so tien: 70000
Nhap loai chi tieu: transport

Nhap ten khoan chi 4: Sach
Nhap so tien: 120000
Nhap loai chi tieu: other

Nhap ten khoan chi 5: Com toi
Nhap so tien: 45000
Nhap loai chi tieu: food
```

## Example Output

```text
An trua - 35000.0 - food
Tra sua - 50000.0 - drink
Xang xe - 70000.0 - transport
Sach - 120000.0 - other
Com toi - 45000.0 - food

Tong chi tieu la 320000.0

So khoan food: 2
So khoan drink: 1
So khoan transport: 1
So khoan other: 1

Tong chi tieu tung loai la:
 -food: 80000.0
 -drink: 50000.0
 -transport: 70000.0
 -other: 120000.0

Chi tieu trung binh la 64000.0

Khoan chi tieu lon nhat la 120000.0
Ten khoan chi la:
- Sach

Khoan chi tieu nho nhat la 35000.0
Ten khoan chi la:
- An trua

So khoan chi lon hon 100000 la 1
So khoan chi nho hon hoac bang 100000 la 4
```

## Concepts Practiced

This project practices core Python basics from Block 1 to Block 3:

- Variables
- Input and output
- `int()` and `float()`
- Lists
- `append()`
- `for` loops
- `while` loops
- `if` statements
- Input validation
- Parallel lists
- Manual total calculation
- Manual max/min search
- Counting items
- Grouping data by category

## Notes

This project does not use functions yet.  
It was built before learning Block 4: Functions.

The current version focuses on practicing basic Python logic using only fundamental concepts.

## Status

Completed as a Block 1-3 capstone mini project.