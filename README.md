# Manage Contacts (Flask)
### Chức năng: ###
   Quản lý thông tin liên lạc
   
   Thêm, đọc, sửa, xóa dữ liệu người dùng (CRUD)

### Languages: ###

   Front-end: *HTML*

   Back-end: *Python*

   Database: *MySQL*

   *Bootstrap, JQuery, Flask*

### Thiết lập app: ###
   **1. Clone repository về máy:**
   ```
   https://github.com/TDMVu18/Manage_Flask/tree/main
   ```
   Sau đó, bạn mở thư mục vừa clone với code editor.
   
   **2. Chạy Terminal, điều hướng đến thư mục của Project:**
   
   ```
   cd Manage_Flask
   ```
   **3. Thiết lập Virtual Enviroment (VE):**
      
Môi trường ảo là một công cụ để duy trì không gian riêng biệt cho một Project với các phụ thuộc và các thư viện của nó ở một nơi. Môi trường này thì riêng biệt cho một Project cụ thể và không ảnh hưởng đến các phụ thuộc của các Project khác.

Tạo môi trường ảo của Python cho Project:
   ```
   virtualenv venv
   ```
   Nếu chưa cài đặt gói virtualenv, bạn hãy thử dòng lệnh sau:
   ```
   pip install virtualenv
   ```
   Sau khi thiết lập VE, hãy kích hoạt nó:
   ```
   .\Scripts\activate
   ```
   **4. Cài đặt các gói**
      
Sau khi thiết lập VE, điều tiếp theo bạn cần thực hiện là cài đặt các gói Python mà app của chúng ta cần để hoạt động.
Mình đã đóng gói tất cả bằng lệnh pip freeze chạy trên VE, các gói cần thiết giờ đã nằm trong file ***requirement.txt*** nên việc bạn cần làm chỉ cần chạy dòng code sau:
   ```
   pip install -r requirement.txt
   ```

