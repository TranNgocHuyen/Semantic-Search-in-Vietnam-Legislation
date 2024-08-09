import matplotlib.pyplot as plt
import torch
import numpy as np
# Thay đổi kích thước
plt.figure(figsize=(5,4))


samples=torch.load('/home/tuanda/Semantic-Search-in-Vietnam-Legislation/search_text_with_Qdrant/score_array.pt')
print(sum(samples)/len(samples))
print(len(samples)) # list, len= 201
x=list(range(len(samples)))
plt.plot(x,samples, 'b-') #x,y là list


# thay đổi độ chia 
# plt.xticks(np.arange(0,400,200))
plt.yticks(np.arange(0,1.1,0.5))

# Thay đổi kích thước

#plt.xlim(0,200)
#plt.ylim(0,3)
# Chú thích
plt.title('Score search with 5000 text')
#plt.xlabel('Iteration')
plt.ylabel('score')
#plt.legend sẽ đi tìm các thành phần chứa tham số label và đưa vào chú thích 
plt.legend(loc="best") # add chủ thích

plt.grid(True)
plt.show()