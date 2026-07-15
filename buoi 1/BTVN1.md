Bài 1: Python là ngôn ngữ thông dịch hay biên dịch? Tại sao?
Python là ngôn ngữ thông dịch ( Interpreter language)
Nghĩa là : chương trình Python chạy mà không cần biên dịch toàn bộ thành tệp thực thi trước khi chạy .Thay vào đó Python sử dụng Interpreter(trình thông dịch) để đọc mã nguồn và thực thi chương trình.
Thực tế, Python không hoàn toàn chỉ là ngôn ngữ thông dịch . Vì khi Run, Python sẽ “tự động” biên dịch mã nguồn thành Bytecode trước, sau đó PVM (Python Virtual Machine ) sẽ chuyển Bytecode thành mã máy để CPU thực thi.
Quá trình trên được Python tự hiện tự động nên hầu như người lập trình sẽ không thấy
	Tuy nhiên Python vẫn được xếp vào ngôn ngữ thông dịch vì :
+ Người lập trình “không cần biên dịch thủ công” trước khi chạy
+ Chỉ cần viết mã nguồn , nhấn RUN , chương trình sẽ được thực hiện ngay
	SO SÁNH : 
JAVA : 
+ Dùng Interpreter (trình thông dịch ) để thực thi chương trình
+ Không cần biên dịch thủ công trước khi chạy
+ Mã nguồn được thực thi ngay sau khi ấn RUN
PYTHON : 
+ Dùng Compiler(trình biên dịch ) để biên dịch mã nguồn
+ Phải biên dịch thành Bytecode(.class) trước khi chạy
+ Bytecode được JVM(Java Virtual Machine) chuyển thành mã máy để thực thi

Bài 2:  Liệt kê:
•	Các kiểu dữ liệu trong Python
•	Các toán tử trong Python
•	Mệnh đề điều kiện và vòng lặp
•	Kiểu dữ liệu True, False
2.1 : Các kiểu dữ liệu trong Python
2.1.1 : Các kiểu dữ liệu cơ bản : 
int : số nguyên . Ví dụ : 99999999999999(Python không giới hạn kich thước như Java, có thể lưu số rất lớn)
+ Java: int → long → nếu vẫn chưa đủ thì dùng BigInteger. 
+  Python: chỉ cần int, Python sẽ tự mở rộng kích thước khi cần.
float : số thực . Ví dụ : 3.14 ( Python dùng dấu “.” Không dùng dấu “,”)
complex : số phức . Ví dụ : z = 2 + 3j ( đây là kiểu dữ liệu Java không có sẵn)
bool : Kiểu logic , chỉ có hai giá trị : True, False ( T,F viết hoa trong Python)
str : chuỗi . Ví dụ : name = “Christine”
None : biểu diễn “ Không có giá trị “  đây là giá trị đặc biệt
list : danh sách .Ví dụ [1,2]
tuple : Bộ dữ liệu .Ví dụ (1,2)
set : tập hợp .Ví dụ {1,2}
dict : từ điển .Ví dụ {“name” : “Thu”}
2.1.2 : 3 Điểm "Bẫy" cần lưu ý
1. Python phân biệt chữ hoa chữ thường
age = 18
Age = 20
Đây là hai biến khác nhau.
________________________________________
2. Không cần khai báo kiểu dữ liệu
int age = 18    Sai
Đây là cú pháp Java.
Python chỉ cần
age = 18
________________________________________
3. Không dùng dấu ;
print("Hello")    Đúng
Không cần : print(“Hello”);
2.1.3 : Ép kiểu dữ liệu : 
+ int() : Chuyển sang số nguyên
+ float() : Chuyển sang số thực
+ str() : Chuyển sang chuỗi 
+ bool() : Chuyển sang True/False
+ list() : Chuyển sang list
+ tuple() : Chuyển sang tuple 
+ set() : Chuyển sang set
2.1.4 : Nhập và xuất dữ liệu (Input & Output)
Python sử dụng hai hàm cơ bản:
•	print() để xuất dữ liệu. 
•	input() để nhập dữ liệu.
***Xuất dữ liệu : 
Thay vì : print("Hello Python")
Python có thể in nhiều giá trị, ví dụ : 
name = "Christine"
age = 18
print(name, age)
	Kết quả : Christine 18
***Nhập dữ liệu : 
name = input("Nhập tên: ")
print(name)
Khi chương trình chạy: Nhập tên: Christine
	Kết quả : Christine
Bẫy rất quan trọng của input() : 
Trong Python,input() luôn trả về kiểu str.
Nếu muốn dùng để tính toán, bạn phải ép kiểu:    age = int(input("Nhập tuổi: "))
Hoặc:
score = float(input("Nhập điểm: "))
Nếu quên ép kiểu. Chương trình sẽ báo lỗi vì đang cộng một chuỗi với một số nguyên!!
2.2 : Các toán tử trong python 
2.2.1 : Các nhóm toán tử phổ biến : 
Nhóm Số học:

**Toán tử: +  -  * /
Ý nghĩa: Cộng, Trừ, Nhân, Chia
Ví dụ: 10 / 3 = 3.333...

**Toán tử: //
Ý nghĩa: Chia lấy phần nguyên
Ví dụ: 10 // 3 = 3

**Toán tử: %
Ý nghĩa: Chia lấy dư
Ví dụ: 10 % 3 = 1

**Toán tử: 
Ý nghĩa: Lũy thừa
Ví dụ: 2 mũ 3 = 8

**Nhóm So sánh:

Toán tử: ==  !=  >  <  >=  <=
Ý nghĩa: So sánh hai giá trị
Ví dụ: 5 > 3 trả về True

**Nhóm Logic:

Toán tử: and  or  not
Ý nghĩa: Phép VÀ, HOẶC, PHỦ ĐỊNH
Ví dụ: True and False

**Nhóm Gán:

Toán tử: =  +=  -=  *=  /=  //=  %=  =
Ý nghĩa: Gán và gán kết hợp
Ví dụ: x += 5

**Nhóm Membership:

Toán tử: in, not in
Ý nghĩa: Kiểm tra phần tử có thuộc tập hợp hay không
Ví dụ: "a" in "Java"

**Nhóm Identity:

Toán tử: is, is not
Ý nghĩa: Kiểm tra hai biến có cùng đối tượng hay không
Ví dụ: a is b
!!!!LƯU Ý: 4 Điểm "Bẫy" cần lưu ý khi dùng toán tử
1. Dấu = và ==
x = 5 là phép gán.
x == 5 là phép so sánh.

2. Python không có toán tử ++ và --
Cách viết sai: x++
Cách viết đúng: x += 1 hoặc x = x + 1

3. Phép chia /
print(7 / 2) trả về kết quả 3.5.
Khác với Java, Python luôn trả về số thực khi dùng phép chia đơn /.
Nếu muốn lấy phần nguyên,phải dùng phép chia kép //:
print(7 // 2) trả về kết quả 3.

4. Phép toán lũy thừa dùng dấu 
print(2  5)
Không phải dùng dấu mũ ^ như: 2 ^ 5 (vì dấu ^ trong Python là toán tử XOR).
2.3: Mệnh đề điều kiện và vòng lặp : 
Python sử dụng câu lệnh điều kiện để đưa ra quyết định và sử dụng vòng lặp để thực hiện một công việc nhiều lần.

1. Câu lệnh if
Cú pháp:
if dieu_kien:
câu_lệnh

Ví dụ:
age = 20
if age >= 18:
print("Đủ tuổi")

2. Câu lệnh if...else
score = 7

if score >= 5:
print("Đạt")
else:
print("Trượt")

3. Câu lệnh if...elif...else
score = 8

if score >= 8:
print("Giỏi")
elif score >= 5:
print("Đạt")
else:
print("Chưa đạt")

4. Câu lệnh match...case (Từ phiên bản Python 3.10+).Cú pháp match-case tương tự như switch-case trong Java.
ví dụ : 
day = 3

match day:
case 2:
print("Thứ Hai")
case 3:
print("Thứ Ba")
case _:
print("Ngày khác")

Lưu ý: Ký tự gạch dưới "case _" tương đương với "default" trong Java.

5. Vòng lặp while
Dùng khi chưa biết trước số lần lặp.

i = 1

while i <= 5:
print(i)
i += 1

Kết quả lần lượt là:
1
2
3
4
5

6. Vòng lặp for
Python không sử dụng kiểu lặp truyền thống như Java: for(int i=0; i<10; i++)
Thay vào đó, Python dùng cấu trúc:
for i in range(5):
print(i)
Kết quả lần lượt là:
0
1
2
3
4

Tìm hiểu thêm về Hàm range():

Trường hợp range(stop):
range(5) tạo ra dãy số: 0, 1, 2, 3, 4

Trường hợp range(start, stop):
for i in range(2, 6):
print(i)
Kết quả lần lượt là: 2, 3, 4, 5

Trường hợp range(start, stop, step):
for i in range(2, 11, 2):
print(i)
Kết quả lần lượt là: 2, 4, 6, 8, 10

7. Duyệt danh sách List bằng vòng lặp for
numbers = [2, 4, 6, 8]

for value in numbers:
print(value)

Cách viết này tương tự như vòng lặp for-each trong Java.

8. Câu lệnh break
Dùng để dừng vòng lặp ngay lập tức.

for i in range(10):
if i == 5:
break
print(i)

Kết quả lần lượt là:
0
1
2
3
4

9. Câu lệnh continue
Dùng để bỏ qua lần lặp hiện tại và chuyển sang lần lặp kế tiếp.

for i in range(6):
if i == 3:
continue
print(i)

Kết quả lần lượt là:
0
1
2
4
5

10. Câu lệnh pass
Câu lệnh pass là một lệnh giữ chỗ, "không làm gì cả".
Thường dùng khi bạn muốn viết trước khung sườn cấu trúc và để trống khối lệnh bên trong.

if True:
pass

!!!!LƯU Ý: 4 Điểm "Bẫy" cần lưu ý khi dùng câu lệnh điều kiện và vòng lặp

**Python không dùng dấu ngoặc nhọn {} để bao bọc khối lệnh
Cách viết sai: if age >= 18 {
Cách viết đúng: if age >= 18:

**Phải thụt lề đầu dòng (Indentation) bắt buộc
Mọi khối lệnh con trong Python đều phải thụt đầu dòng thẳng hàng nhau.
if age >= 18:
print("OK")
Nếu bạn không thụt đầu dòng, hệ thống sẽ báo lỗi: IndentationError.

**Không bắt buộc dùng dấu ngoặc đơn () trong biểu thức điều kiện
Cách viết chuẩn Python: if age >= 18:
Viết thêm ngoặc như "if (age >= 18):" vẫn chạy được nhưng không cần thiết và không chuẩn phong cách Python.

**Cẩn thận vòng lặp while chạy vô hạn
Nếu điều kiện của while luôn đúng mà không có câu lệnh break để thoát ra, chương trình sẽ bị treo:
while True:
print("Hello")

2.4: KIỂU DỮ LIỆU True/False(Boolean)
Boolean là kiểu dữ liệu logic, chỉ nhận một trong hai giá trị sau:
True
False
****Lưu ý quan trọng:

+ Chữ cái đầu của True và False bắt buộc phải viết hoa.

+ Viết thường hoàn toàn như "true" hoặc "false" sẽ bị báo lỗi vì Python phân biệt chữ hoa và chữ thường.
Ví dụ:
is_student = True
is_login = False

print(is_student)
print(is_login)

2. Giá trị Truthy và Falsy
Trong Python, ngoài True và False thực sự, các giá trị khác khi đặt trong câu lệnh điều kiện cũng tự động được hiểu ngầm là Đúng (Truthy) hoặc Sai (Falsy).

***Các giá trị được xem là Sai (Falsy):
+ Giá trị: False (Ý nghĩa: Sai)
+ Giá trị: None (Ý nghĩa: Không có giá trị)
+ Giá trị: 0 (Ý nghĩa: Số nguyên 0)
+ Giá trị: 0.0 (Ý nghĩa: Số thực 0)
+ Giá trị: "" (Ý nghĩa: Chuỗi rỗng)
+ Giá trị: [] (Ý nghĩa: List rỗng)
+ Giá trị: () (Ý nghĩa: Tuple rỗng)
+ Giá trị: {} (Ý nghĩa: Dictionary rỗng)
+ Giá trị: set() (Ý nghĩa: Set rỗng)

Ví dụ thực tế:
if []:
print("Có dữ liệu")
else:
print("Danh sách rỗng")

Kết quả in ra màn hình: "Danh sách rỗng" vì danh sách rỗng [] là một giá trị Falsy.

Các giá trị được xem là Đúng (Truthy):
Hầu hết toàn bộ các giá trị còn lại ngoài danh sách Falsy bên trên đều được quy ước là Đúng (True).

Ví dụ:
bool(100) -> trả về True
bool("Python") -> trả về True
bool([1, 2, 3]) -> trả về True
bool(-5) -> trả về True

!!!!!LƯU Ý: 3 Điểm "Bẫy" cần lưu ý khi dùng kiểu Boolean

1.True và False phải luôn viết hoa chữ cái đầu tiên
Bắt buộc: True, False
Không được viết: true, false

2.Chuỗi chữ có nội dung "False" vẫn được xem là True
print(bool("False")) trả về kết quả True.
Giải thích: Vì "False" nằm trong dấu ngoặc kép là một chuỗi có chứa ký tự, không phải là giá trị logic False của hệ thống.

Chuỗi hoàn toàn không có gì mới là False
print(bool("")) trả về kết quả False (Chuỗi rỗng).
Nhưng nếu chuỗi có khoảng trắng như print(bool(" ")) thì vẫn trả về True vì nó chứa ký tự dấu cách.



