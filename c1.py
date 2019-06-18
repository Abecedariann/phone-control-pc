import itchat
import os
from itchat.content import *
import requests
import sys
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isFriendChat=True)
def text_reply(msg):
	print(msg['User']['UserName'])
	if msg['User']['UserName']=='filehelper':
		print(msg['Content'])
		if msg['Content']=='calc':
			# os.system('start calc')
			itchat.send_msg('calc open...',toUserName='filehelper')
			# itchat.send_image('1.png',toUserName='filehelper')
		if msg['Content']=='shutdown':
			itchat.send_msg('Power off after 60 seconds...',toUserName='filehelper')
			os.system('shutdown -s -t 60')
		elif msg['Content']=='xiumian':
			itchat.send_msg('即将休眠...',toUserName='filehelper')
			os.system('shutdown -h')
		elif msg['Content']=='doff':
			itchat.send_msg('Desktop closed...',toUserName='filehelper')
			os.system('taskkill /f /im explorer.exe')
		elif msg['Content']=='don':
			itchat.send_msg('Desktop open...',toUserName='filehelper')
			os.system('start explorer.exe')
		elif msg['Content']=='face':
			itchat.send_msg('loading face recognition...',toUserName='filehelper')
			os.system('py -3 D:\\python program\\control_git\\face_comp.py')
		elif msg['Content']=='play':
			itchat.send_msg('music...',toUserName='filehelper')
			os.system('py -3 D:\\python program\\control_git\\music.py')
		elif msg['Content']=='next':
			itchat.send_msg('music next...',toUserName='filehelper')
			os.system('py -3 D:\\python program\\control_git\\music_next.py')
		elif msg['Content']=='up':
			itchat.send_msg('volume +...',toUserName='filehelper')
			os.system('D:\\python program\\control_git\\nircmd.exe changesysvolume 3000')
		elif msg['Content']=='down':
			itchat.send_msg('volume -...',toUserName='filehelper')
			os.system('D:\\python program\\control_git\\nircmd.exe changesysvolume -3000')
		elif msg['Content']=='pic':
			# itchat.send_msg('loading face recognition...',toUserName='filehelper')
			# os.system('py -3 D:\\python program\\control_git\\face_comp.py')
			try:
				html=requests.get('http://192.168.1.104:8080/?action=snapshot.jpg')
				with open('pic.jpg','wb') as file:
					file.write(html.content)
				itchat.send_image('pic.jpg',toUserName='filehelper')
			except Exception:
				itchat.send_msg('图片加载失败',toUserName='filehelper')
		# elif msg['Content']=='exit':
		# 	itchat.send_msg('bye...',toUserName='filehelper')
		# 	sys.exit()
		else:
			itchat.send_msg('error...\r\nplease try:\r\nshutdown\r\nxiumian\r\ndoff\r\ndon\r\nface\r\npic\r\nplay\r\nnext\r\nup\r\ndown',toUserName='filehelper')
	# if msg.text=='calc':
	# 	os.system('start calc')
itchat.auto_login(hotReload=True)
# a=itchat.send('hello',toUserName='filehelper')
# print(ms)
# print(a)
itchat.run()