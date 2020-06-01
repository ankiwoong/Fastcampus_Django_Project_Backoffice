# MAC OS 기준 강의 -> Windows 기준 변경 방법
## MySQL 다운로드
* https://dev.mysql.com/downloads/windows/installer/5.7.html
* Windows (x86, 32-bit), MSI Installer Full Version

## 라이브러리 설치
* Mysqlclient
```python
pip install Mysqlclient
```
## MysqlDB Download
* https://github.com/datacharmer/test_db

## employees 설치
* C:\Program Files\MySQL\MySQL Server 5.6\bin
* cmd
```bash
mysql -u root -p -t < employees.sql
```

## DB 확인
* MySQL 5.6 Command Line Client - Unicode
* DB 확인
```bash
SHOW DATABASES;
```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| employees          |
| mysql              |
| performance_schema |
| sakila             |
| test               |
| world              |
+--------------------+
8 rows in set (0.00 sec)

## Python 
* DB 설정
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # mysql 엔진
        'NAME': 'employees',    # DB이름
        'USER': 'root',    # User 이름(기본 root)
        'PASSWORD': '1q2w3e4r5t',    # User 패스워드
        'HOST': 'localhost',    # 호스트
        'PORT': '3306'    # 포트
    }
}
```
