# MVC pattern
Tương tự classic app mình đã build, thư mục này chứa source code với các chức năng giống hoàn toàn app cũ, nhưng được cấu trúc theo mô hình MVC.

Cụ thể: 

file model.py dùng để quản lý CSDL của app

file services.py dùng để định nghĩa các hàm xử lý (handler) như render trang chủ, thêm, sửa, xóa thông tin.

các hàm xử lý của services.py sẽ được ánh xạ vào các URL tương ứng, nhờ đó Flask sẽ biết phải làm gì khi có yêu cầu đến 1 URL nhất định.

để hiện thực hóa, file controller.py thực hiện việc định tuyến cho phép định nghĩa hành vi của ứng dụng khi user gởi yêu cầu đến các địa chỉ (URL) nhất định (route).
