```
    _         _              _____            
   / \  _   _| |_ ___       | ____|_  ___ __  
  / _ \| | | | __/ _ \ _____|  _| \ \/ / '_ \
 / ___ \ |_| | || (_) |_____| |___ >  <| |_) |
/_/   \_\__,_|\__\___/      |_____/_/\_\ .__/                                 
				       |_|    
```
Auto-Exp
=============

关于Auto-Exp
-------------------------
Auto-Exp(Auto Exploit Framework,自动利用框架)，采用Python编写，底层数据库为MySQL

安装
------------------------
1）数据库

    1.建立数据库，并在auto_exp/config/config.py中更改数据库名
    
    2.在数据库中建立exploit表
        SQL: create table `exploit` (id int(4) not null primary key auto_increment , name char(20) not null , `desc` char(100) not null , level int(1) not null ,author char(10) not null);
	
	  3.建立url表
        SQL: create table `url` (id int(4) not null primary key auto_increment, url char(100) not null, exp int(20) not null);

    4.Data Table
        SQL:  create table `data` (taskid char(20) not null,data text not null);
2) 配置
   1.更改auto_exp/config/config.py中配置

使用
----------------------
详见help参数




