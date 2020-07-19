## python_learn

  - 简单来讲，就是学习python过程中的资料以及成果，会持续开发.... 

### 0X00 ftp

  - ftp的学习，包括客户端与服务端的实现
     - 基于pyftpdlib，ftplib
  - 文件列表
     - easy_ftp_server.bat
     - ftp_client.py
     - ftp_client_gui.py
         - ftp的客户端，此脚本来自[内阁首辅](https://github.com/neigeshoufu)
     - ftp_server.py

### 0X01 host_scan

  - 主机发现脚本
     - 基于arp，icmp，udp以及tcp的ack发现
     - 支持地址端扫描，以及txt文档读取扫描
     - 基于scapy，socket
  - 文件列表
     - second_host_discovery.py
     - third_host_discovery.py
     - forth_host_discovery.py
     - ip_list.txt

### 0X02 port_scan

  - [scapy-2.4.3](https://github.com/secdev/scapy)
  - 端口扫描
     - 支持syn，tcp全连接，udp，socket，fin，null，xmac扫描
     - 单地址，多地址，端口段以及txt文档读取扫描
     - 使用pickle存储数据
     - 基于scapy，socket
  - 文件列表
     - common_port_list.pkl
     - port.txt
     - port_scan.py

### 0X03 python_blackhat

  - [paramiko](https://github.com/paramiko/paramiko)
  - python2.x
     - python_blackhat这本书的原答案，基于python2.x版本，后续具体展开
  - python3.x
     - 自修改python2.x的源码内容，基于python3.x版本，后续具体展开

### 0X04 scanner

  - 扫描器，结合主机发现和端口扫描，可扩展性大，打算继续维护，后期可能独立出来
  - 文件列表
     - __pycache__
     - common_port_list.pkl
     - host_scan.py
     - host_type.py
     - ip_list.txt
     - port_list.txt
     - port_scan.py
     - port_type.py
     - scanner.py

### 0X05 sniffer

  - 嗅探器，类似于Wireshark
     - 在pthon_blackhat上第二章sniffer_ip_heared_decode.py上的扩展，可嗅探HTTP，TLS，TCP，UDP，SSDP，DNS，OICQ等协议
     - 基于struct，threading，socket，ctypes
  - 文件列表
     - sniffer.py

### 0X06 socket

  - udp以及tcp的通讯模拟
     - 基于socket
  - 文件列表
     - tcp_client.py
     - tcp_server.py
     - udp_p2p.py
     - udp_p2p_other.py

### 0X07 tecent_class_qiandao

  - [Tencent_class_check_in](https://github.com/Suyixiu/Tencent_class_check_in)
  - 腾讯课堂的自动签到
     - 使用固定窗口，固定点击地址，模拟鼠标的点击
     - 基于win32gui，win32con，win32api
  - 文件列表
     - tx_qiandao.py

### 0X08 win32

  - [WinSpy](https://sourceforge.net/projects/winspyex/)
  - win32的操作
     - 基于win32gui，win32con，win32api，tkinter
  - 文件列表
     - power.py  ->  自写开机启动脚本，自动开启Tickeys，QQ，微信
     - time.py  ->  定时提醒小程序，倒计时，定时提醒等功能

### 0X09 Mail

  - mail客户端服务端
     - 实现邮件的发送以及接收，包括附件的发送以及解析
  - 文件列表
     - smtp.py
     - pop.py
     - Dan_mail_client.py
         - mail的客户端带GUI，此脚本来自[内阁首辅](https://github.com/neigeshoufu)
     - Dan_Mail.py
         - mail的发送接收一体带GUI，此脚本来自[内阁首辅](https://github.com/neigeshoufu)