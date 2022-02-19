from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n how are you New York?!"
    endmsg = "\r\n.\r\n"

    serverName = '127.0.0.1'
    serverPort = 1025

    sender_email = 'pb2685@nyu.edu'
    receiver_email = 'navyabhat007@gmail.com'

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))

    recv = clientSocket.recv(1024).decode()
    #print(recv) 
    #if recv[:3] != '220':
    #    print('220 reply not received from server.')


    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    mail_from_Command = 'MAIL FROM: <'+sender_email+'>\r\n'
    clientSocket.send(mail_from_Command.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')



    rcpt_to_Command = 'RCPT TO: <'+receiver_email+'>\r\n'
    clientSocket.send(rcpt_to_Command.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')


    data_start = 'DATA\r\n'
    clientSocket.send(data_start.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '354':
    #    print('354 reply not received from server.')


    clientSocket.send(msg.encode())
    


    clientSocket.send(endmsg.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    quit_conn = 'QUIT\r\n'
    clientSocket.send(quit_conn.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '221':
        print('221 reply not received from server.')


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')