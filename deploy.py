



import paramiko
import os


def sftp_upload_with_key(username, hostname,local_path,remote_path, port=22, private_key_path=None ):
    
    if private_key_path is None:
        # 默认私钥文件路径
        private_key_path = os.path.expanduser("~/.ssh/id_rsa") 
        
    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

    # 建立SSH传输协议
    transport = paramiko.Transport((hostname, port))
    transport.connect(username=username, pkey=private_key)

    # 创建SFTP客户端
    sftp = paramiko.SFTPClient.from_transport(transport)

    # 上传文件
    sftp.put(local_path, remote_path)

    # 关闭连接
    sftp.close()
    transport.close()
    
if __name__ == "__main__":
    remote_path = "/home/hyp/app_comment_maker" 
    sftp_upload_with_key("hyp","lb-aidev1", "app_comment_maker.zip", remote_path + "/app_comment_maker.zip") 
    