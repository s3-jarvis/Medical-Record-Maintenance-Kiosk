import paramiko

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.207.96',username='tejas',password='trp17kpl',port=22)
sftp_client=ssh.open_sftp()
sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Image_capture\\PID_2\\2.png",'/home/tejas/share/PID_1/2.png')
sftp_client.put("C:\\Users\\tejas\\Capstone-Project-T229\\UI-Design-Code\\UI Test\\Image_capture\\PID_2\\OCR_1.jpg",'/home/tejas/share/PID_1/OCR_1.jpg')
sftp_client.put("Data.log", '/home/tejas/share/PID_1/Data.txt')

sftp_client.close()
ssh.close()