# 创建Django项目
```django-admin startproject Test(Test为项目名)```

# 切换到项目的根目录，启动项目
```python manage.py runserver 0.0.0.0:8000 或者 python manage.py runserver```


# Django数据库
```默认项目根目录下自动创建“db.sqlite3”文件，可以在settings.py里面指定“db.sqlite3”文件的存放路径或者更改成其他的数据库引擎，如MySQL```

# 访问Django的admin管理后台
```访问路径：127.0.0.1:8000/admin （开始无法访问，因为数据库还未初始化，提示没有这个表）
(1) 数据库迁移
makemigrations创建数据库迁移，产生SQL脚本，使用migrate命令把默认的model同步到数据库，
Django会自动为model建立数据库表。
python manage.py makemigrations
python manage.py migrate

(2) 创建后台管理员账号
python manage.py createsuperuser

(3) 配置文件settings.py解读
调试模式，应用注册，第三方库配置，国际化等
```