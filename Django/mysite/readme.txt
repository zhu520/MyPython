Django是使用Python开发的开源Web开发框架
wget http://labfile.oss.aliyuncs.com/courses/1127/mysite.zip

MVC，是模型（Model）-视图（View）-控制器（Controller）的缩写
MTV模式：M代表模型(Model)，T代表模板(Template)，V代表视图(View)
models.py, urls.py, views.py HTML模板文件

1 安装-测试
$ sudo pip3 install Django==2.0.6
$ python3
>>> import django
>>> print(django.get_version())
2.0.6

2 创建Django项目
$ django-admin startproject mysite

3 启动Django
$ cd /home/shiyanlou/Code/mysite
$ python3 manage.py runserver

4 创建应用
$ cd /home/shiyanlou/Code/mysite
$ python3 manage.py startapp lib

5 模型文件修修迁移
$ python3 manage.py makemigrations lib
查看内容
$ python3 manage.py sqlmigrate lib 0001	
应用
$ python3 manage.py migrate 

6 API
$ python3 manage.py shell
