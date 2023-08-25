# Manage Contacts (Flask) - ૮ ˶ᵔ ᵕ ᵔ˶ ა
### Chức năng: ###
   Quản lý thông tin liên lạc
   
   Thêm, xem, sửa, xóa dữ liệu người dùng (CRUD)

### Languages: ###

   Front-end: *HTML*

   Back-end: *Python, MySQL*

   Framework và thư viện: *Bootstrap, JQuery, Flask*

### Thiết lập app: ###
   **1. Clone repository về máy:**
   ```
   https://github.com/TDMVu18/Manage_Flask/tree/main
   ```
   Sau đó, bạn mở thư mục vừa clone với code editor.
   
   **2. Chạy Terminal, điều hướng đến thư mục của Project:**
   
   ```
   cd Manage_Flask/classic_app
   ```
   **3. Thiết lập Virtual Enviroment (VE):**
      
Môi trường ảo là một công cụ để duy trì không gian riêng biệt cho một Project với các phụ thuộc và các thư viện của nó ở một nơi. Môi trường này thì riêng biệt cho một Project cụ thể và không ảnh hưởng đến các phụ thuộc của các Project khác •̀⩊•́ .

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
   .venv\Scripts\activate
   ```
   **4. Cài đặt các gói**
      
Sau khi thiết lập VE, điều tiếp theo bạn cần thực hiện là cài đặt các gói Python mà app của chúng ta cần để hoạt động.
Mình đã đóng gói tất cả bằng lệnh pip freeze chạy trên VE, các gói cần thiết giờ đã nằm trong file ***requirement.txt*** nên việc bạn cần làm chỉ cần chạy dòng code sau:
   ```
   pip install -r requirement.txt
   ```
   **5. Khởi tạo cơ sở dữ liệu (CSDL)**

Sau khi thực hiện các bước trên, bạn hãy mở file app.py ra, và quan sát dòng code sau:
   ```
   app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/crud'
   ```
Ở đây SQLALCHEMY_DATABASE_URI dùng để xác định đường dẫn đến CSDL của bạn, như trên URI đã cung cấp thì server của mình là *localhost*, username đang lấy theo tài khoản mặc định là *root*, với mật khẩu để trống là *' '* và *crud* là tên của CSDL mình đã đặt. CSDL mình sử dụng là mysql nên URI sẽ được xác định theo đúng định dạng này, bạn có thể sửa đổi lại cho đúng với tài khoản và server của mình.

Tiếp theo, để app có thể làm việc, thêm, xóa, sửa, lấy dữ liệu thì hiển nhiên ta cần phải tạo một CSDL trên máy của bạn. Mở Terminal lên và chúng ta sẽ thực hiện theo các bước sau đây:
   ```
   python
   ```
   ```
   from app import app, db
   ```
Tại file app.py chúng ta đã khai báo 2 biến app và db, với app = Flask(__ name __) nhằm tạo một web server để chuyển các yêu cầu từ client tới ứng dụng web, và db = SQLAlchemy(app) như một ORM để mapping dữ liệu từ CSDL đến các class của python, giờ ta có thể sử dụng để tạo CSDL trên localhost của bạn, lưu ý hãy mở Xampp, và truy cập phpmyadmin trước (˚0˚)!!
   ```
   app.app_context().push()
   db.create_all()
   ```
**6. Chạy app**

Sau khi thực hiện tất cả các bước trên, điều cuối cùng bạn cần làm là tạo Terminal mới, và chạy app bằng đoạn mã sau:
   ```
   python app.py
   ```
Sau đó hãy thực hiện thêm dữ liệu, xem, cập nhật và xóa dữ liệu ngay trên trang URL mà app cung cấp, thường sẽ là http://localhost:5000/

Dưới đây là đoạn video các chức năng chính của App, see ya ˶ˆ꒳ˆ˵ !! 



https://github.com/TDMVu18/Manage_Flask/assets/74062885/e3a56600-f223-49a6-9403-bc8ea72cbe5e


