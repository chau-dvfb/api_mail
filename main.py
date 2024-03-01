# Import module mail.py from project_one
from api_mail.main import Apimail
from api_mail.define import *
import sys
class ApimailProjectTwo:
    @classmethod
    def get_code_mail(cls):
        # Tạo random email từ project_one
        random_email = Apimail.random_email(Apimail.domain_mail)
        print("Địa chỉ email mới:", random_email)
        # Đăng ký email mới
        response_reg = Apimail.reg_mail(random_email)
        if response_reg:
            print("Đăng ký email thành công!")
        else:
            print("Đăng ký email không thành công!")
            sys.exit()
        # Kiểm tra email mới trong danh sách email từ project_two
        emails = Apimail.list_mail()
        if random_email in emails:
            print("Địa chỉ email đã được đăng ký:", random_email)
            # Nhận latest_code từ dự án "one"
            latest_code = Apimail.get_code_mail(random_email)

            # Kiểm tra nếu latest_code không None thì in ra
            if latest_code is not None:
                print("Mã code mới nhất:", latest_code)
            else:
                print("Không nhận được mã code. Đã xảy ra lỗi.")
                sys.exit()
        else:
            print("Địa chỉ email chưa được đăng ký hoặc có lỗi xảy ra.")
        print("Chương trình tiếp theo")
ApimailProjectTwo.get_code_mail()