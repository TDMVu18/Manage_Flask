# MVC pattern
Tương tự classic app mình đã build, thư mục này chứa source code với các chức năng giống hoàn toàn app cũ, nhưng được cấu trúc theo mô hình MVC.

Cụ thể: 

file model.py dùng để quản lý CSDL của app

file services.py dùng để định nghĩa các hàm xử lý (handler) như render trang chủ, thêm, sửa, xóa thông tin.

các hàm xử lý của services.py sẽ được ánh xạ vào các URL tương ứng, nhờ đó Flask sẽ biết phải làm gì khi có yêu cầu đến 1 URL nhất định.

để hiện thực hóa, file controller.py thực hiện việc định tuyến cho phép định nghĩa hành vi của ứng dụng khi user gởi yêu cầu đến các địa chỉ (URL) nhất định (route).

Vì có nhiều file nên để dễ dàng trong việc vận hành, mình đã đăng ký model Data như 1 Blueprint của Flask với đoạn mã sau trong controller.py và __ init __.py:
   ```
   datas = Blueprint("Data", __name__)
   app.register_blueprint(datas)
   ```
 Trong quá trình đăng ký, tất cả các thành phần bên trong blueprint sẽ được truyền vào ứng dụng. Bạn có thể hình dung blueprint như là một nơi lưu trữ tạm thời cho các chức năng của ứng dụng để tổ chức mã nguồn tốt hơn.

 Các bước cài đặt và thiết lập đều giống classic app, trừ phần tạo CSDL mình đã cập nhật luôn vào hàm create_app() nên giờ bạn chỉ cần mở Terminal lên và chạy:
   ```
   python app.py
   ```
Để run app và thực hiện tất cả chức năng y hệt app classic 1 cách bình thường ૮ ˶ᵔ ᵕ ᵔ˶ ა
