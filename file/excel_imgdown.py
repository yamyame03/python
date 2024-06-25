import openpyxl.workbook
import pandas as pd
import requests
import urllib.request as urllib
from urllib.parse import urlparse
from datetime import datetime
import openpyxl

now = datetime.now()
now_strftime1 = now.strftime("%Y%m%d")
now_strftime2 = now.strftime("%Y%m%d%H%M%S")

save_excel_path = "C:\\Dev\\project\\python\\excel(수정)"
save_excel_name = now_strftime1 + "_상품정보.xlsx"
save_file_name = save_excel_path + save_excel_name

excel_data = []
data = pd.read_excel('C:\\Dev\\project\\python\\excel(원본)\\20240625_product.xlsx', sheet_name= 'Sheet1')
thumnail_save_location = "C:\\Dev\\project\\python\\image\\thumnail\\"
detail_save_location = "C:\\Dev\\project\\python\\image\\detail\\"

for i in range(len(data)):
    product_name        = data['상품명'][i]
    thumnail_image_url  = data['이미지등록(상세)'][i]
    detail_image_url    = data['상품 상세설명'][i]
    product_Price       = data['소비자가'][i]
    product_orgPrice    = data['공급가'][i]
    product_delPrice    = data['배송비입력'][i]
    try:
        urllib.urlretrieve(thumnail_image_url, f'{thumnail_save_location}{now_strftime2}_t{i}.jpg')
        urllib.urlretrieve(detail_image_url, f'{detail_save_location}{now_strftime2}_d{i}.jpg')
        excel_data.append([f"{product_name}", f"{now_strftime2}_t{i}.jpg", f"{now_strftime2}_d{i}.jpg", f"{product_Price}", f"{product_orgPrice}", f"{product_delPrice}"])
        print(f"이미지 다운로드 완료")

    except Exception as e:
        print(f"이미지 다운로드 중 오류 발생: {e}")

df = pd.DataFrame(excel_data, columns=["상품명", "대표사진(썸네일)", "메인사진", "소비자가", "공급가(원가)", "배송비입력"])        

df.to_excel(f"{save_file_name}", index=False)