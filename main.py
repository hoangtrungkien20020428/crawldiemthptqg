#cao diem thi thpt qg 2021 voi thu vien beutifulsuop
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
list_sbd=[[]]
def crowl(matinh,start,end):
     concac = 1
     while concac:
          x=matinh*10000+start
          url="https://thanhnien.vn/ajax/diemthi.aspx?kythi=THPT&nam=2021&city=DDT&text="+str(x)
          req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
          web_byte = urlopen(req).read()
          webpage = web_byte.decode('utf-8')
          suop =BeautifulSoup(webpage,'html.parser')
          for tag in suop.find_all('tr'):
               list_=[]
               for ac in tag.find_all('td'):
                    list_.append(ac.text)
                    if ac.class_=="mobile-tab-content mobile-tab-2":
                         list_.append(float(ac.text))
                    if ac.class_=="mobile-tab-content mobile-tab-3":
                         list_.append(float(ac.text))         
               list_sbd.append(list_)
          start=start+1
          if start>end:
               concac=0
 #bacnhinh ma tinh bang 19                      
crowl(19,1,163)
import csv
with open('diemthinam2021_bacninh.csv','w',newline ='') as f:
     theweriter=csv.writer(f,delimiter=',',quoting=csv.QUOTE_ALL)
     theweriter.writerow(['stt','cum thi','ho ten','SBD','ngay sinh','gioi tinh','toan','van','ly','hoa','sinh','khtn','su','dia','giao duc','khxh','ngoai ngu'])
     theweriter.writerows(list_sbd)
