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
```bash
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
```

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

## Migrate
```python
python manage.py migrate
```
```python
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

# inspectdb
```python
python manage.py inspectdb > fastadmin/models.py
```
