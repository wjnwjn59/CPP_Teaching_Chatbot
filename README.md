# Hệ thống chatbot hỗ trợ nhập môn lập trình
[![Build Status](https://travis-ci.com/anhquan075/cpp_learning_chatbot.svg?branch=mainbranch)](https://travis-ci.com/anhquan075/cpp_learning_chatbot)
[![Rasa 2.1.0](https://img.shields.io/badge/Rasa-2.1.0-blueviolet)](https://github.com/RasaHQ/rasa/tree/2.1.x)
[![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB)](https://www.python.org/downloads/release/python-370/)

## Hướng dẫn sử dụng:
1) Cài đặt:
- Đối với các bạn dùng anaconda:
```
conda create -n <tên env> --file requirements.txt
```
- Hoặc đơn giản hơn bạn chỉ cần chạy dòng lên sau:
```
pip3 install rasa==2.1.0
```
2) Sử dụng:
```
rasa run actions
rasa shell
```
3) Kiểm tra performance:
- Đối với bộ dữ liệu ít, mình khuyên dùng:
```
rasa test --cross-validation
```
- Nếu bạn có thể tạo cho mình bộ test ưng ý chỉ cần chạy lệnh:
```
rasa test
```

## Docker:
- Ngoài ra bên mình còn build hai docker container:
  + Container action: https://hub.docker.com/repository/docker/nguyenquang7501/rasa-sdk
  + Container rasa: https://hub.docker.com/repository/docker/nguyenquang7501/rasa
- Để kết nối hai container với nhau, ta sử dụng lệnh:
```
docker create network <tên network bạn muốn tạo>
```
- Tiếp theo ta chạy lên phía bên dưới để kết nối link action server tới network ta vừa tạo:
```
docker run -d -v $(pwd)/actions:/app/actions --net <tên network bạn vừa tạo> --name <tên liên kết giữa action server và rasa> rasa/rasa-sdk:2.1.2
```
- Với tên liên kết giữa action server và rasa vừa tạo phía trên, ta chỉnh sửa một tí trong file endpoints.yml như sau:
```
action_endpoint:
  url: "http://<tên liên kết giữa action server và rasa>:5055/webhook"
```
- Cuối cùng ta chạy lệnh sau để kết nối 2 docker với nhau:
```
docker run -it -v $(pwd):/app -p 5005:5005 --net <tên network bạn vừa tạo> rasa/rasa:2.1.2-full shell
```
