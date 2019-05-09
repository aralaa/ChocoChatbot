
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup
from urllib.request import urlopen

url_base = 'https://www.kebhana.com/cont/mall/mall08/mall0805/index.jsp?_menuNo=62608'

html = urlopen(url_base)
soup = BeautifulSoup(html, "html.parser")

#soup


# In[14]:


# 정기 예금 리스트 출력
#print(soup.find_all('li', 'item type1'))


# In[15]:


#예금 개수 확인
#len(soup.find_all('li', 'item type1'))


# In[16]:


from urllib.request import urljoin

name = [] #상품명
url_add = [] #뒷부분 url
period = [] #기간
strong = [] #수수료
term = []

list_soup = soup.find_all('li', 'item type1')

for item in list_soup:
    #예금별 이름과 url 가져오기
    name.append(item.find('a').get_text())
    url_add.append(urljoin(url_base, item.find('a')['href']))
    #None 타입이 있어서 오류 남 -> none 타입일 때는 null로 출력 할 수 있도록 수정 필요
    #만약 NoneType 이라면 null로 출력하도록 
    #'NoneType' object has no attribute 'get_text'
    #period.append(item.find(class_='period').get_text())
    #strong.append(item.find('strong'))
    #term.append(item.find(class_='term'))


# In[17]:


url_add[:5]


# In[18]:


name[:5]


# In[19]:


import pandas as pd

data = {'Name':name, 'URL':url_add}
df = pd.DataFrame(data)
df.head()


# In[20]:


# 데이터 csv 형태로 저장
df.to_csv('../data/hana_list.csv', sep=',', encoding='UTF-8')


# In[21]:


# 첫번째 URL 가져옴
df['URL'][0]


# In[22]:


html = urlopen(df['URL'][0])
soup_tmp = BeautifulSoup(html, "html.parser")
# 1) 서버사이드랜더링 (서버에서 랜더링 할 시간 주고 html 받아오기) 
# 쓰레드나 타이머로 돌려서 바로 받지 말고 서버가 스크립트까지 다 실행된 다음에 받을 수 있는 방법으로
# 서버가 실행된 시간을 안준거
# 쓰레드, 비동기
# 2) 스크립트 태그를 스트링으로 긁어와서 Selenium의 excute 함수로 결과를 크롤링
#soup_tmp


# In[23]:


#print(soup_tmp.find('dl', 'prodcutInfo'))


# In[24]:


print(soup_tmp.find(class_='tbl_tbldiv'))

