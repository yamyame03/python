import pymysql
import pandas as pd

# 테스트 서버
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="luckycatch"
)

cursor = db.cursor()

data = pd.read_excel('C:\\Dev\\project\\python\\excel(수정)\\20240625_상품정보.xlsx', sheet_name= 'Sheet1')
total = 0
for i in range(len(data)):
    sql = f"insert into `box_goods`  \
                (`bseq`, `box_type`, `grp_seq`, `goods_nm`, `goods_ea`, `goods_img`, `goods_price`, `goods_con`, `orig_price`, `point`, `delivery_price`, `use_yn`, `bundle_yn`, `open_type`) \
            values \
                ('{data['bseq'][i]}', '{data['box_type'][i]}', '{data['grp_seq'][i]}', '{data['상품명'][i]}', '', '{data['대표사진(썸네일)'][i]}','{data['소비자가'][i]:,}','<img src=\"https://www.luckycatch.kr/Uploads/{data['메인사진'][i]}\">', '{data['공급가(원가)'][i]:,}', '', '{data['배송비입력'][i]:,}', 'Y', '', 'A')"
    
    cursor.execute(sql)
    db.commit()
    total += 1

print(total, " 개의 데이터가 입력됨")