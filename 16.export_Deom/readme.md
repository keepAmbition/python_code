**readme**

FR24 Export/
|-- case/(目前case类代码已弃用)
|   |-- __init__.py
|   |-- b2b_case                #b2b接口case
|   |-- b2c_domestic_case       #b2c境内接口case
|   |-- b2b_overseas_case       #b2c境外接口case
|
|-- data/
|   |-- conf_dict.py               #账号密码等配置信息                    
|   |-- export_url.py              #接口url
|   |-- request_dict.py            #向接口请求的请求参数（如果要修改出发,到达城市,出发,到达日期,请在这个py文件中重新配置）
|   
|-- foo/
|   |-- B2B_Export_Logic.py          #B2B接口实现主逻辑
|   |-- B2C_Export_Logic.py          #B2C接口实现主逻辑
|   |-- database.py                  #数据库操作类
|   |-- log_print.py                 #日志打印类
|   |-- public_class.py              #公用函数类
|   |-- send_emaild.py        		 #发送邮件类	
|               
|-- log/
|   |-- B2BExport_log                  #保存上一次B2B接口运行日志
|   |-- B2CExport_log                  #保存上一次B2c接口运行日志
|   
|-- export_all_case_run.py           #测试case集合类


目前接口自动化脚本包含B2B接口平台采购8个case,代理采购8个case, B2C境内接口8个case,B2C境外接口8个case，MTN接口待补充，接口自动化脚本运行后，会生成接口测试报告，自动发送邮件给QA群组					

b2b\B2C函数内主要参数含义解释：b2b_export_logic("PF", "PP_AC_OW", "b2b", 2, "a") ----------b2c_export_logic("PP", "PP_AC_RT", "domestic", "b2c", 2, "a")
PP:平台代理        PF:采购代理
A:单个成人         AC:单个成人+单个儿童
OW:直飞航班        RT:中转航班
1: 直飞航班        2:中转航班
domestic:境内接口  overseas:境外接口
a:deva环境（如需其他环境，更改其他环境的简写字母，如b,c,d,x,不过其他接口url未配置）