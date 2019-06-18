# phone-control-pc
python3 树莓派  
暂时树莓派只出了个摄像头，用mjpg_streamer共享到windows  
功能是使用微信或者网页控制电脑 
网页css样式用的button库 html+jquery+ajax向后端nodejs发送get请求，nodejs执行命令或python脚本  
微信调用itchat库，向文件助手发消息获取树莓派摄像头实时状态
