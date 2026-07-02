# Number Analyzer

Mini project Python console đầu tiên trong quá trình học Python cơ bản.

## Mô tả

`Number Analyzer` là chương trình nhập vào một số nguyên dương `n`, sau đó phân tích một số tính chất cơ bản của `n` và dãy số từ `1` đến `n`.

Project này dùng để luyện các kiến thức nền tảng:

- `input()` / `print()`
- ép kiểu `int`
- `while` để bắt nhập lại dữ liệu sai
- `if / else` để rẽ nhánh điều kiện
- `for` + `range()` để duyệt dãy số
- biến đếm và biến tổng

## Chức năng

Chương trình hiện có các chức năng:

- Bắt người dùng nhập `n > 0`
- Kiểm tra `n` là số chẵn hay số lẻ
- Kiểm tra `n` có chia hết cho `3` không
- Kiểm tra `n` có chia hết cho `5` không
- Tính tổng các số từ `1` đến `n`
- Đếm số lượng số chẵn từ `1` đến `n`
- Đếm số lượng số lẻ từ `1` đến `n`

## Cách chạy

Mở terminal tại thư mục project rồi chạy:

```bash
python main.py
```

Hoặc trên Windows có thể dùng:

```bash
py main.py
```

## Ví dụ

Input:

```text
10
```

Output:

```text
10 la so chan
10 khong chia het cho 3
10 chia het cho 5
Tong cac so tu 1 den 10 = 55
So luong so chan tu 1 den 10 = 5
So luong so le tu 1 den 10 = 5
```

Nếu nhập sai:

```text
-5
0
10
```

Chương trình sẽ yêu cầu nhập lại đến khi `n > 0`.

## Cấu trúc project

```text
number_analyzer/
├─ main.py
└─ README.md
```

## Kiến thức đã luyện được

### 1. Vòng lặp `while`

Dùng để kiểm tra input và bắt nhập lại nếu dữ liệu không hợp lệ.

```python
while n <= 0:
    print("Vui long nhap n>0")
    n = int(input())
```

### 2. Câu điều kiện `if / else`

Dùng để kiểm tra chẵn/lẻ và chia hết.

```python
if n % 2 == 0:
    print("So chan")
else:
    print("So le")
```

### 3. Vòng lặp `for`

Dùng để duyệt từ `1` đến `n`.

```python
for i in range(1, n + 1):
    tong += i
```

## Hướng cải thiện sau này

Sau khi học thêm `function`, có thể tách project thành các hàm:

- `input_positive_number()`
- `check_even_odd(n)`
- `check_divisible(n, divisor)`
- `calculate_sum(n)`
- `count_even_odd(n)`

Sau khi học thêm `list`, có thể mở rộng thành project phân tích nhiều số cùng lúc.

## Trạng thái

Đã hoàn thành phiên bản cơ bản.
