\# Student Score Analyzer



A simple Python console mini project for managing student scores.



This project allows users to input student names and scores, validate the scores, calculate class statistics, and classify students based on their performance.



\## Features



\- Input the number of students

\- Validate that the number of students is greater than 0

\- Input student names

\- Input student scores

\- Validate scores from 0 to 10

\- Store student names and scores in lists

\- Calculate average score

\- Find the highest score

\- Show all students with the highest score

\- Find the lowest score

\- Show all students with the lowest score

\- Classify students into:

&#x20; - Excellent

&#x20; - Good

&#x20; - Average

&#x20; - Weak

\- Count passed students

\- Count failed students



\## Score Classification



| Score Range | Classification |

|---|---|

| `score >= 8` | Excellent |

| `6.5 <= score < 8` | Good |

| `5 <= score < 6.5` | Average |

| `score < 5` | Weak |



\## Pass / Fail Rule



| Score Range | Result |

|---|---|

| `score >= 5` | Passed |

| `score < 5` | Failed |



\## Project Structure



```text

student\_score\_analyzer/

│

├── main.py

└── README.md

```



\## How to Run



Open terminal in the project folder:



```bash

cd D:\\python-mini-projects\\student\_score\_analyzer

python main.py

```



If `python` does not work, try:



```bash

py main.py

```



\## Example Input



```text

Nhap so luong hoc sinh = 5



Ten hoc sinh thu 1 la : An

Nhap diem hoc sinh thu 1 = 9



Ten hoc sinh thu 2 la : Binh

Nhap diem hoc sinh thu 2 = 7.5



Ten hoc sinh thu 3 la : Cuong

Nhap diem hoc sinh thu 3 = 4



Ten hoc sinh thu 4 la : Dung

Nhap diem hoc sinh thu 4 = 6



Ten hoc sinh thu 5 la : Hoa

Nhap diem hoc sinh thu 5 = 10

```



\## Example Output



```text

Danh sach ten = \['An', 'Binh', 'Cuong', 'Dung', 'Hoa']

Danh sach diem = \[9.0, 7.5, 4.0, 6.0, 10.0]



Diem trung binh = 7.3



Diem cao nhat la 10.0

Hoc sinh co diem cao nhat:

\-Hoa



Diem thap nhat la 4.0

Hoc sinh co diem thap nhat:

\-Cuong



So hoc sinh gioi la 2

So hoc sinh kha la 1

So hoc sinh trung binh la 1

So hoc sinh yeu la 1



So hoc sinh qua mon la 4

So hoc sinh rot mon la 1

```



\## Concepts Practiced



This project practices basic Python programming concepts:



\- Variables

\- Input and output

\- `int()` and `float()`

\- Lists

\- `append()`

\- `for` loops

\- `while` loops

\- `if / elif / else`

\- Basic validation

\- Finding max and min manually

\- Counting categories



\## Status



Completed as a Block 3 mini project before learning functions.

