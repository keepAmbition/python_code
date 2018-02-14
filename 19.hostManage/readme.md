#hostManage目录结构:
```
hostMange:		
├── app                             # 项目app
│   ├── migrations    
│       ├── __init__.py 
│   ├── admin.py                    # admin页面
|   ├── apps.py                     # app配置页面
│   ├── models.py                   # 创建数据库表结构
|   ├── test.py                     # 单元测试
│   ├── urls.py                     # app中的路由分配配置
|   ├── views.py                    # app的后台业务逻辑
|
├── hostManage                  
│   ├── __init__.py
|   ├── settings.py                 # 配置文件
│   ├── urls.py                     # Django整体路由分配    
|   ├── wsgi.py                     # WSIG规范
│
├── static                      
│   ├── font-awesome-4.7.0          # 引用样式
|   ├── img                         # 图片
│   ├── app.css                     # app页面样式
|   ├── app.js                      # app页面行为
│   ├── host.css                    # app页面样式
|   ├── host.js                     # app页面行为
│   ├── jquery-1.12.4.js            # 引用jQuery
|   
├── templates
│   ├── app.html                    # app页面结构
|   ├── host.html                   # host页面结构
│   ├── host_detail.html            # host_detail页面结构
│
├── manage.py                       # Django管理程序
```
#hostManage流程图:
![](https://images2017.cnblogs.com/blog/1088183/201802/1088183-20180214144913718-1991538045.png)