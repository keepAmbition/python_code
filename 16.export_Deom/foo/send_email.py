import os
import smtplib
import email.mime.multipart
import email.mime.text
from email import encoders
from data.conf_dict import ConfData


class SendEmail(object):
    def __init__(self):
        self.conf_data = ConfData()
        self.sender = self.conf_data.get_conf_data("email")["sender"]
        self.receiver = self.conf_data.get_conf_data("email")["receiver"]
        self.SMTP_server = self.conf_data.get_conf_data("email")["SMTP_server"]
        self.username = self.conf_data.get_conf_data("email")["username"]
        self.password = self.conf_data.get_conf_data("email")["password"]
        self.content = self.conf_data.get_conf_data("email")["content"]

    def create_msg(self):
        """
        此函数主要构建收发邮件联系人、邮件正文、邮件附件、邮件标题
        :return:
        """
        #构建邮件正文
        msg = email.mime.multipart.MIMEMultipart()
        msg["from"] = self.sender
        msg["to"] = self.sender
        msg['subject'] = "FR接口自动化测试报告"
        txt = email.mime.text.MIMEText(self.content)
        msg.attach(txt)

        #构建邮件附件之一：自动化测试报告
        report_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "report.html")
        report = email.mime.text.MIMEText(open(report_path, "rb")
                                          .read(), 'html', 'utf-8')
        report["Content-Type"] = 'application/octet-stream'
        report.add_header('Content-Disposition', 'attachment', filename=('gbk', '', "report.html"))
        encoders.encode_base64(report)
        msg.attach(report)

        #构建邮件附件之一：B2B测试日志
        log_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "log"), "B2BExport_log")
        # log_path = "C:/Users/dell/PycharmProjects/untitled/FR24_Export/log/B2BExport_log"
        b2b_log = email.mime.text.MIMEText(open(log_path, 'rb').read(), 'base64', 'utf-8')
        b2b_log["Content-Type"] = 'application/octet-stream'
        b2b_log.add_header('Content-Disposition', 'attachment', filename=('gbk', '', "B2B_log.txt"))
        encoders.encode_base64(b2b_log)
        msg.attach(b2b_log)

        #构建邮件附件之一：B2C测试日志
        log_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "log"), "B2CExport_log")
        # log_path = "C:/Users/dell/PycharmProjects/untitled/FR24_Export/log/B2BExport_log"
        b2c_log = email.mime.text.MIMEText(open(log_path, 'rb').read(), 'base64', 'utf-8')
        b2c_log["Content-Type"] = 'application/octet-stream'
        b2c_log.add_header('Content-Disposition', 'attachment', filename=('gbk', '', "B2C_log.txt"))
        encoders.encode_base64(b2c_log)
        msg.attach(b2c_log)
        return msg

    def send_email(self):
        """
        创建实例，发送邮件
        :return:
        """
        msg = self.create_msg()
        smtp = smtplib.SMTP_SSL(self.SMTP_server, 465)
        # smtp.connect(self.SMTP_server, 465)
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.sender, msg.as_string())
        smtp.quit()


if __name__ == "__main__":
    s = SendEmail()
    s.send_email()