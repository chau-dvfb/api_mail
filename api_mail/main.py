from requests import session
from urllib3 import disable_warnings , exceptions
import re
import random
import time
import string
from .define import *

disable_warnings(exceptions.InsecureRequestWarning)
ss = session()
ss.verify = ss.trust_env = False
class Apimail:
    # Đường dẫn của file setup.txt
    setup_file_path = '.\\api_mail\\setup.txt'
    with open(setup_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        pattern = r'domain_mail=(.*)'
    match = re.search(pattern, content)
    if match:
        link = match.group(1)
    else:
        print("Không tìm thấy giá trị trong file setup.txt.")
    domain_mail = link
    @staticmethod
    def random_email(domain_mail):
        # Tạo một chuỗi ngẫu nhiên từ 6 ký tự chữ và số
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        # domain_mail = '@fanclub.pm'
        # Ghép chuỗi ngẫu nhiên với phần cố định của email
        email = random_part + domain_mail
        return email

    @staticmethod
    def reg_mail(email):
        domain_mail = email.split('@')[1]  # Lấy phần domain từ địa chỉ email
        email_prefix = email.split('@')[0]  # Lấy phần tiền tố của địa chỉ email
        url = f"https://m.kuku.lu/index.php?action=addMailAddrByManual&nopost=1&by_system=1&t=1708868552&csrf_token_check=ef3befb611fc1781b0ed3eac7d7a54c1&newdomain={domain_mail}&newuser={email_prefix}&recaptcha_token=&_=1708868552409"
        response = ss.get(url, headers=headers, data=payload)
        if "OK:" in response.text:
            return True
        else:
            return False

    @staticmethod
    def list_mail():
        url = "https://m.kuku.lu/recv.selectaddr.php?ajax=1&nopost=1&&_=1708954420867"
        response = ss.get(url, headers=headers, data=payload)
        # Biểu thức chính quy để tìm địa chỉ email
        email_pattern = r"filter_mailaddr',\s*'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)'"
        # Tìm và in ra các địa chỉ email từ phản hồi văn bản
        emails = re.findall(email_pattern, response.text)
        return emails

    @staticmethod
    def delete_mail(email):
        url = f"https://m.kuku.lu/index.php?action=delMailAddr&nopost=1&csrf_token_check=ef3befb611fc1781b0ed3eac7d7a54c1&csrf_subtoken_check=95ca1b14b8cef8c0d29309efd898da94&addr={email}&type="
        response = ss.post(url, headers=headers, data=payload)
        if "OK:" in response.text:
            return True
        else:
            return False
    @staticmethod
    def send_mail(email):
        url = f"https://m.kuku.lu/recv._ajax.php?&page=0&q={email}&nopost=1&csrf_token_check=ef3befb611fc1781b0ed3eac7d7a54c1&csrf_subtoken_check=95ca1b14b8cef8c0d29309efd898da94&_=1708954071007"
        response = ss.get(url, headers=headers, data=payload).text

        # Kiểm tra xem kết quả tìm kiếm trong mail_content có khác 0 không
        search_results = re.search(r"Search results: <span class='view_listcnt'>(\d+)</span>", response)

        if search_results:
            # Lấy số kết quả từ match object
            num_results = int(search_results.group(1))
            if num_results != 0:
                # Nếu số kết quả khác 0, in ra nội dung các tin nhắn
                messages = re.findall(r"<span style=\"overflow-wrap: break-word;word-break: break-all;\">(.*?)</span>", response)
                for message in messages:
                    print(message)
                    with open('.\\api_mail\\history_code.txt','a',encoding='utf-8') as f:
                        f.write(message + " --> " + email + "\n")

                # Biểu thức chính quy để tìm kiếm số code và từ khóa "Instagram"
                pattern = r"(\d+) is your Instagram code"

                # Tạo một danh sách lưu trữ các thông tin trích xuất
                extracted_info = []

                # Lặp qua các tiêu đề email
                for subject in messages:
                    match = re.search(pattern, subject)
                    if match:
                        # Nếu tìm thấy kết quả, thêm vào danh sách trích xuất
                        code_number = match.group(1)
                        extracted_info.append((int(code_number), "Instagram"))

                # Sắp xếp danh sách trích xuất theo số code giảm dần
                extracted_info.sort()

                # Lấy thông tin từ tin nhắn mới nhất
                if extracted_info:
                    latest_code, keyword = extracted_info[0]
                    print(f"Code mới nhất: {latest_code}, từ khóa: {keyword}")
                    # Nếu tìm thấy code, dừng lại
                    return latest_code
                else:
                    print(f"Không tìm thấy thông tin về mã code và từ khóa {keyword} trong các tiêu đề email.")

        else:
            print("Không tìm thấy thông tin tìm kiếm.")
        return

    @classmethod
    def get_code_mail(cls, random_email):  # Thêm đối số random_email
        domain_mail = cls.domain_mail  # Lấy domain_mail từ class
        start_time = time.time()
        while True:
            latest_code = cls.send_mail(random_email)
            if latest_code is not None:
                return latest_code  # Trả về latest_code nếu tìm thấy mã code
            current_time = time.time()
            # thời gian chờ nhận code
            if current_time - start_time >= 60:
                print("Đã chờ quá 60 giây, dừng kiểm tra.")
                result = Apimail.delete_mail(random_email)
                # Kiểm tra kết quả
                if result:
                    print(f"Xóa email {random_email} thành công!")
                else:
                    print(f"Không thể xóa email {random_email}!")
                break
            print("Chờ 2 giây để kiểm tra lại...")
            time.sleep(2)