import pyodbc # thư viện kết nối với csdl

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={'10.0.0.39'};"    # địa chỉ máy chủ
    f"DATABASE={'DataV03'};"    # tên csdl
    f"UID={'sa'};"              # tên user
    f"PWD={'Ab@123456'}"        # mật khẩu
)

def data_sql():
    try:
        # thiết lập kết nối
        connection = pyodbc.connect(connection_string)
        # tạo 1 con trỏ để thực hiện các lệnh SQL và truy vấn kết quả
        cursor = connection.cursor()

        # CHỌN DATABASE CÂU 'data_ND' ?ĐIỀU 'data_ND_dieu' ?ĐOẠN   
        sql_query = "SELECT TOP 9000 * FROM [DataV03].[dbo].[Dataset_chunking]"  
        
        # Thực thi truy vấn
        cursor.execute(sql_query)
        # Lấy hàng từ tất cả
        rows = cursor.fetchall()

        data_json_new = []
        for row in rows:
            jsons = {
                'KeyPK': row[0],
                'ID': row[1],
                # 'LoaiVanBan': row[0],
                # 'NoiBanHanh': row[0],
                # 'NguoiKy': row[0],
                # 'NgayBanHanh': row[0],
                # 'NgayHieuLuc': row[0],
                # 'NgayCongBao': row[0],
                # 'SoCongBao': row[0],
                # 'TinhTrang': row[0],
                # 'UrlFile': row[0],
                # 'UrlFilePDF': row[0],
                'TrichYeu': row[2],
                # 'LinhVuc': row[0],
                'UrlFileDoc': row[3],
                'ChunkingText': row[4] 
            }
            data_json_new.append(jsons)
        return data_json_new
    
    except pyodbc.Error as ex:
        print("Error connecting to SQL Server:", ex)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__=='__main__':
        dataset=data_sql()
        for i in range(5):
            print(dataset[i]['ChunkingText'])