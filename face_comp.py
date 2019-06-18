import face_recognition
import cv2
import os
import sys
import time

video_capture = cv2.VideoCapture()
img=face_recognition.load_image_file('D:\\python program\\control_git\\3.jpg')
img_encoding=face_recognition.face_encodings(img)[0]

face_locations=[]
face_encodings=[]
face_names=[]
process_this_frame=True
a=None
haveone=False
ex=False
while True:
	ret,frame=video_capture.read()
	small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
	if process_this_frame:
		face_locations=face_recognition.face_locations(small_frame,1)
		face_encodings=face_recognition.face_encodings(small_frame,face_locations)
		# print('len',len(face_encodings))
		# if len(face_encodings)>0:
		# 	haveone=True
		# else:
		# 	haveone=False
		haveone=False
		face_names=[]
		for face_encoding in face_encodings:
			match=face_recognition.compare_faces([img_encoding],face_encoding,tolerance=0.5)
			face_distances = face_recognition.face_distance([img_encoding],face_encoding)
			a=face_distances
			print(face_distances)
			if match[0]:
				haveone=True
				name='me'
				print(name)
				ex=True
				# print(face_encoding)
				
				
				# sys.exit()		
			else:
				haveone=True
				name='unknown'
				print(name)
			face_names.append(name)
	process_this_frame=not process_this_frame
	for (top,right,bottom,left),name in zip(face_locations,face_names):
		top*=4
		right*=4
		bottom*=4
		left*=4
		cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),2)
		cv2.rectangle(frame,(left,bottom-35),(right,bottom),(0,0,255),2)
		font=cv2.FONT_HERSHEY_DUPLEX
		# a=str(a[0])
		# print(a)
		# a=a[0:4]
		# print('a',a)
		cv2.putText(frame,name,(left+6,bottom-6),font,1.0,(255,255,255),1)
	# if haveone==True:
	# 	cv2.imshow('video',frame)
	# 	cv2.waitKey(1)
	# 	time.sleep(1)
	# 	sys.exit()
	# 	# cv2.waitKey(1) & 0xFF ==ord('q'):
	# 	# 	break
	# else:
	# 	cv2.destroyAllWindows()
	cv2.imshow('video',frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
	if ex==True:
		time.sleep(1)
		os.system('start explorer.exe')
		sys.exit()
	

		# if
# os.system('pause')
video_capture.release()
cv2.destroyAllWindows()