# CONNECT
from qdrant_client import QdrantClient,models
from model_embedding import embedding_text

import datetime

def searching_text_to_doc(text_query, my_collection, limit):
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
                #'NoiDung':i.payload['ChunkingText'], ################## noi dung
                
            }
            #answer_array.append(answer_json)
            if len(answer_array)==0:
                answer_array.append(answer_json)
            else:
                count = 0
                for answer in answer_array:
                    #id là của 1 văn bản , phải thêm chương, điều, mục
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
                #'NoiDung':i.payload['ChunkingText'], ################## noi dung
                
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
    text_query = ''' Đây là text anh Khương gửi'''
    #searching_text_to_doc(text_query, my_collection, 10)
    for i, answer in enumerate(searching_text_to_doc(text_query, my_collection, 5)):
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