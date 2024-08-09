# CONNECT
from qdrant_client import QdrantClient,models
from model_embedding import embedding_text, model_embedding

import datetime

def searching_text_to_doc(text_query, my_collection, limit, tokenizer, model):
    client=QdrantClient(url="http://localhost:6333")
    search_result=client.search(
        collection_name=my_collection,
        query_vector= embedding_text(text_query, tokenizer, model),
        # query_filter=models.Filter(
        #    must=[models.FieldCondition(key="dieu", match=models.MatchValue(value="2"))]
        # ),
        limit=limit,
        search_params=models.SearchParams(
                exact=True,  # Turns on the exact search mode KNN
            ),
   )

    #print question
    if len(search_result)==0:
        print("Không có thông tin tìm kiếm")
    else:
        #print("Kết quả thông tin tìm kiếm là:")
        answer_array=[]
        for i in search_result:
            answer_json={
                #'ID_vecto':i.id,
                #'Key_PK':i.payload['KeyPK'],
                'id':i.payload['ID'],
                'score':i.score,
                #'ChunkingText':i.payload['ChunkingText'], ################## noi dung
                
            }
            if len(answer_array)==0:
                answer_array.append(answer_json)
            else:
                count = 0
                for answer in answer_array:
                    if (answer['id'] == answer_json['id']):
                        count=count+1
                if count==0:
                    answer_array.append(answer_json)   
    return answer_array

def searching_text_full(text_query, my_collection, limit):
    client=QdrantClient(url="http://localhost:6333")
    search_result=client.search(
        collection_name=my_collection,
        query_vector= embedding_text(text_query),
        # query_filter=models.Filter(
        #    must=[models.FieldCondition(key="dieu", match=models.MatchValue(value="2"))]
        # ),
        limit=limit,
        search_params=models.SearchParams(
                exact=True,  # Turns on the exact search mode KNN
            ),
   )

    #print question
    if len(search_result)==0:
        print("Không có thông tin tìm kiếm")
    else:
        print("Kết quả thông tin tìm kiếm là:")
        answer_array=[]
        for i in search_result:
            answer_json={
                #'ID_vecto':i.id,
                #'Key_PK':i.payload['KeyPK'],
                'id':i.payload['ID'],
                'score':i.score,
                'ChunkingText':i.payload['ChunkingText'], ################## noi dung
                
            }
            answer_array.append(answer_json)
            # if len(answer_array)==0:
            #     answer_array.append(answer_json)
            # else:
            #     count=0
            #     for answer in answer_array:
            #         #id là của 1 văn bản , phải thêm chương, điều, mục
            #         if (answer_json['index']==answer['index']):
            #             count=count+1
            #         if count==0:
            #             answer_array.append(answer_json)   
    return answer_array

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    
    my_collection="Chunking_text_VBPL"
    text_query = ''' Số lượng hồ sơ: 01 bộ
    4. Thời hạn giải quyết:.Trường hợp diện tích rừng tạm sử dụng thuộc phạm vi quản lý của Ủy ban nhân dân cấp tỉnh: 12 ngày làm việc, kể từ ngày Sở Nông nghiệp và Phát triển nông thôn nhận được hồ sơ hợp lệ.Trường hợp diện tích rừng tạm sử dụng thuộc phạm vi quản lý của chủ rừng là các đơn vị trực thuộc các bộ, ngành chủ quản: 20 ngày làm việc, kể từ ngày Sở Nông nghiệp và Phát triển nông thôn nhận được hồ sơ hợp lệ.
    5. Đối tượng thực hiện thủ tục hành chính: Chủ đầu tư dự án.
    6. Cơ quan giải quyết thủ tục hành chính: Sở Nông nghiệp và Phát triển nông thôn.
    7. Cơ quan/người có thẩm quyền quyết định: Chủ tịch Uỷ ban nhân dân cấp tỉnh.
    8. Kết quả thực hiện thủ tục hành chính: Quyết định về việc phê duyệt Phương án tạm sử dụng rừng (hoặc điều chỉnh Phương án tạm sử dụng rừng) theo Phụ lục III ban hành kèm theo Nghị định số 27/2024/NĐ-CP.
    9. Phí, lệ phí (nếu có): Không.
    10. Tên mẫu đơn, mẫu tờ khai: Văn bản đề nghị phê duyệt Phương án tạm sử dụng rừng hoặc điều chỉnh Phương án tạm sử dụng rừng của chủ đầu tư dự án theo Phụ lục I ban hành kèm theo Nghị định số 27/2024/NĐ-CP; Phương án tạm sử dụng rừng hoặc điều chỉnh Phương án tạm sử dụng rừng do chủ đầu tư lập theo Phụ lục II ban hành kèm theo Nghị định số 27/2024/NĐ-CP.'''


    tokenizer, model = model_embedding()
    for i, answer in enumerate(searching_text_to_doc(text_query, my_collection, 5, tokenizer, model)):
        print("Tìm kiếm thứ ", i, " là: ==================================")
        print(answer)

    # Kết thúc đo thời gian
    end_time = datetime.datetime.now()
    # Tính toán thời gian thực thi
    elapsed_time = end_time - start_time
    # Tính giờ, phút, giây
    hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Thời gian chạy: {int(hours)} giờ {int(minutes)} phút {seconds:.2f} giây")