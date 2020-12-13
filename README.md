# Hệ thống chatbot hỗ trợ nhập môn lập trình
[![Rasa 2.1.0](https://img.shields.io/badge/Rasa-2.1.0-blueviolet)](https://github.com/RasaHQ/rasa/tree/2.1.x)
[![Python 3.7](https://img.shields.io/badge/Python-3.7-3776AB)](https://www.python.org/downloads/release/python-370/)

Hướng dẫn sử dụng:
1) Cài đặt:
```
pip3 install -U rasa==2.1.0
```
2) Sử dụng:
```
rasa shell
```
3) Kiểm tra performance:
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
