# 第一个django app，part2

## 数据库的安装
打开项目文件夹下的settinig.py文件
DATABASES 下的设置

<pre><code>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
</code></pre>

ENGINE：  
1， 'django.db.backends.sqlite3',  
2， 'django.db.backends.postgresql',  
3， 'django.db.backends.mysql',  
4， 'django.db.backends.oracle'  

NAME： 数据库的名称


## 设置
TIME_ZONE 设置时区， 默认UTC， 北京时间 Asia/Shanghai


# 创建 models
创建好后，运行 python manage.py makemigrations xx
生成后运行 python manage.py migrate xx
