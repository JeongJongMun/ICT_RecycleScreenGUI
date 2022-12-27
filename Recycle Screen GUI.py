from tkinter import *


win=Tk()
win.title("광고")
win.geometry("800x480")
win.resizable(False, False)

bg=PhotoImage(file=r"출력 사진들\4대원칙.png")
bg_bt=Button(win, image=bg, command=win.destroy)
bg_bt.pack()


window=Tk() # 가장 상위레벨의 윈도우 창 생성
    
window.title("메인메뉴") #제목
window.geometry("800x480") #윈도우 창의 너비와 높이, 초기 화면 위치의 x좌표와 y좌표를 설정
window.resizable(False, False) # 윈도우 창의 상하좌우 창 크기 가능 여부
window.configure(bg="oldlace")

    
def b1_click():
    window1=Tk()
    window1.title("분리배출 방법")
    window1.geometry("800x480")
    window1.resizable(False, False)
    window1.configure(bg="oldlace")
    
    b00=Button(window1, text="플라스틱", command=click_00)
    b01=Button(window1, text="페트")
    b02=Button(window1, text="종이", command=click_02)
    b03=Button(window1, text="종이팩", command=click_03)
    b10=Button(window1, text="캔류")
    b11=Button(window1, text="유리", command=click_11)
    b12=Button(window1, text="비닐류", command=click_12)
    b13=Button(window1, text="스티로폼")
    b20=Button(window1, text="일반")
    b21=Button(window1, text="음식물")
    b22=Button(window1, text="기타", command=click_22)
    b23=Button(window1, text="뒤로가기", command=window1.destroy)
    
    b00.configure(font=("", 15),bg="papayawhip")
    b01.configure(font=("", 15),bg="papayawhip")
    b02.configure(font=("", 15),bg="papayawhip")
    b03.configure(font=("", 15),bg="papayawhip")
    b10.configure(font=("", 15),bg="papayawhip")
    b11.configure(font=("", 15),bg="papayawhip")
    b12.configure(font=("", 15),bg="papayawhip")
    b13.configure(font=("", 15),bg="papayawhip")
    b20.configure(font=("", 15),bg="papayawhip")
    b21.configure(font=("", 15),bg="papayawhip")
    b22.configure(font=("", 15),bg="papayawhip")
    b23.configure(font=("", 15),bg="papayawhip")
    
    b00.grid(row=0, column=0, ipadx=40, ipady=50, padx=10, pady=10)
    b01.grid(row=0, column=1, ipadx=40, ipady=50, padx=10, pady=10)
    b02.grid(row=0, column=2, ipadx=40, ipady=50, padx=10, pady=10)
    b03.grid(row=0, column=3, ipadx=40, ipady=50, padx=10, pady=10)
    b10.grid(row=1, column=0, ipadx=40, ipady=50, padx=10, pady=10)
    b11.grid(row=1, column=1, ipadx=40, ipady=50, padx=10, pady=10)
    b12.grid(row=1, column=2, ipadx=40, ipady=50, padx=10, pady=10)
    b13.grid(row=1, column=3, ipadx=40, ipady=50, padx=10, pady=10)
    b20.grid(row=2, column=0, ipadx=40, ipady=50, padx=10, pady=10)
    b21.grid(row=2, column=1, ipadx=40, ipady=50, padx=10, pady=10)
    b22.grid(row=2, column=2, ipadx=40, ipady=50, padx=10, pady=10)
    b23.grid(row=2, column=3, ipadx=40, ipady=50, padx=10, pady=10)
    
def click_00():
    window00=Tk()
    window00.title("플라스틱")
    window00.geometry("800x480")
    window00.resizable(False,False)
    window00.configure(bg="oldlace")
    
    mesg='''* 합성 수지류
[PET, PVC, PE, PP, PS, PSP 재질 등의 용기 · 트레이류]

* 배출 방법
- 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출
(물로 헹굴 수 없는 구조의 용기류(치약용기 등)는 애용물을 비운 후 배출)
- 부착상표, 부속품 등 본체와 다른 재질은 제거한 후 배출

* 해당 품목
- 음료용기, 세정용기 등

* 비해당 품목
- 플라스틱 이외의 재질이 부착된 
완구 · 문구류, 옷걸이, 칫솔, 파일철, 전화기, 낚싯대, 유모차 · 보행기, CD · DVD 등
(종량제 봉투, 특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출)
'''
    plastic=Label(window00, text=mesg, bg="oldlace")

    plastic.pack()
    plastic.configure(font=("", 15))
    
    back=Button(window00, text="뒤로가기", command=window00.destroy)
    back.place(x=650, y= 400, height=80,width=150)
    back.configure(font=("",20), bg="papayawhip")
    
def click_02():
    window02=Tk()
    window02.title("종이류")
    window02.geometry("800x480")
    window02.resizable(False,False)
    window02.configure(bg="oldlace")
    
    mesg='''*종이류(고지류)
-종류 : 복사지, 사무용지, 청구서, 광고전단, 각종 포장지, 종이 쇼핑 백, 달력 등

#분리 배출 방법 : 물이나 오물에 젖지 않게 모아 30㎝정도로 묶어 보관·배출한다.
물기에 젖지 않도록 하고, 반듯하게 펴서 차곡차곡 쌓은 후 흩날리지 않도록 끈 등으로 묶어서 배출

비닐 코팅 종이(광고지, 치킨 속포장재 등), 금박·은박지, 벽지, 자석전단지, 이물질을 
제거하기 어려운 경우 등은 안내사항 종량제봉투로 배출
책자,노트,잡지,스프링 등 종이류와 다른 재질은 제거한 후 배출

#비해당품목 
비닐 코팅된 표지, 공책의 스프링, 상자에 붙어있는 테이프, 철핀 등
안내사항부속 재질에 따라 분리배출하거나 종량제봉투 등으로 배출한다.
종이컵의 경우 내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출
빨대,비닐 등 종이팩과 다른 재질은 제거한 후 배출한다.
상자류(종이박스,골판지 등) :테이프 등 종이류와 다른 재질은 제거한 후 배출한다.

#주의사항
->비닐코팅지나 쇼핑백의 비닐끈, 비닐덮개, 달력 스프링 등을 제거한 후 보관한다.
->벽지, 나염지, 인화지(사진)는 제외한다.

'''

    paper1=Label(window02, text=mesg, justify="left", bg="oldlace")
    paper1.pack()
    paper1.configure(font=("", 13))
    
    back=Button(window02, text="뒤로가기", command=window02.destroy)
    back.place(x=650, y= 400, height=80,width=150)
    back.configure(font=("",20), bg="papayawhip")
    
def click_03():
    window03=Tk() 
    window03.title("종이팩")
    window03.geometry("800x480")
    window03.resizable(False,False)
    window03.configure(bg="oldlace")

    paper2=Label(window03,bg="oldlace", text='종이팩\n\n-종류 : 우유팩, 음료수 팩, 1회용 종이컵, 두유팩, 소주팩, 쥬스팩\n\n- 분리배출방법 \n\n내용물을 비우고 물로 한번 헹군 후 납작하게 눌러 봉투에 넣거나 한데 \n묶어서 보관·배출한다.(그대로 말린 후 납작하게 눌러 묶어서 보관한다)\n빨대,비닐 등 종이팩과 다른 재질은 제거한 후 배출한다.\n일반 종이류와 혼합되지 않게 종이팩 전용수거함에 배출하도록 한다.\n종이팩 전용수거함이 없는 경우에는 종이류와 구분할 수 있도록 \n가급적 끈 등으로 묶은 후 종이류 수거함으로 배출하도록 한다.\n\n-비해당품목: 종이, 신문지 등 종이류, 종이컵 등 \n안내사항종이류 수거함으로 배출\n\n- 주의사항\n다른 종이류와 섞이지 않도록 별도의 분리 수거함을 마련토록 한다.\n우유팩이나 음료수팩 중 장기 보존용인 테트라팩은 재생이 안되므로 제외한다. '
)
    paper2.pack()
    paper2.configure(font=("", 15))
    
    back=Button(window03, text="뒤로가기", command=window03.destroy)
    back.place(x=650, y= 400, height=80,width=150)
    back.configure(font=("",20), bg="papayawhip")
    
def click_11():
    window11=Tk()
    window11.title("유리")
    window11.geometry("800x480")
    window11.resizable(False,False)
    
    glass=Label(window11, text="유리병(유리병,기타병류)\n\n배출방법\n-내용물을 비우고 물로 헹구는 등 이물질을 제거하여 배출\n-담배꽁초등 이물질을 넣지 않고 배출\n-유리병이 깨지지 않도록 주의하며 배출\n-소주,맥주 등 빈용기보증금 대상 유리병은 소매점 등으로 반납하여 보증금 환급\n\n*해당품목\n-음료수 병, 와인 병, 양주 병, 드링크 병 등등 \n\n*비해당품목\n-깨진 유리제품은 신문지 등에 싸서 종량제 봉투 배출\n-코팅 및 다양한 색상이 들어간 유리제품, 내열 유리제품, 크리스탈 유리제품, 판유리, 조명기구 용 유리류, 사기/도자기류 등등\n(특수규격마대 또는 대형폐기물 처리 등 지자체 조례에 따라 배출)")
    glass.pack()
    
def click_12():
    window12=Tk()
    window12.title("비닐류")
    window12.geometry("800x480")
    window12.resizable(False,False)
    
    vinyl=Label(window12, text="비닐류\n일회용 비닐장갑\n포장용 에어캡\n비닐 충전재\n가정용 음식 포장 지퍼백\n비닐 택배\n\n아닌 예\n음식 포장용 랩\n돗자리\n천막\n식탁보")
    vinyl.pack()
    
def click_22():
    window22=Tk()
    window22.title("기타")
    window22.geometry("800x480")
    window22.resizable(False,False)
    
    etc=Label(window22, text="기타\n불연성 폐기물\n*불연성 폐기물 전용봉투에 담아서 배출\n백열전구\n깨진 유리\n내열 유리\n사기그릇 \n도자기\n화분\n타일\n건설폐기물\n뚝배기 냄비")
    etc.pack()
   
    
def b2_click():
    window2=Tk()
    window2.title("검색")
    window2.geometry("800x480")
    window2.resizable(False, False)
    window2.configure(bg="oldlace")
 
    text_entry1 = Entry(window2, bg = 'oldlace') # Entry 창
    text_entry1.insert(0,"원하시는 검색어를 입력하세요.")
    text_entry1.place(x=200, y=100, width=400, height=100)
 
    button = Button(window2, text = '검색', command = click_02) # 검색기능
    button.place(x=300, y=300, width=200, height=50)
    
    b2_close=Button(window2, text="뒤로가기", command=window2.destroy) # 뒤로가기
    b2_close.place(x=300, y=350, width=200, height=50)
    
    text_entry1.configure(font=("", 20)) # 폰트 조절
    button.configure(font=("", 15),bg="papayawhip")
    b2_close.configure(font=("", 15),bg="papayawhip")
    
    image=PhotoImage(file=r"출력 사진들\돋보기.png", master=window2)    
    lab=Label(window2, image=image2)
    lab.place(x=0, y=100, width=100, height=100) 
    
    
def b3_click():
    window3=Tk()
    window3.title("음성검색")
    window3.geometry("800x480")
    window3.resizable(False, False)
    window3.configure(bg="oldlace")

    
    b3_close=Button(window3, text="뒤로가기", command=window3.destroy)
    b3_close.place(x=300, y=350, width=200, height=50)
    b3_close.configure(font=("", 15),bg="papayawhip")
    
    image4=PhotoImage(file=r"출력 사진들\음성인식.gif", master=window3)
    sound=Label(window, image=image4)
    sound.pack()

    
image2=PhotoImage(file=r"출력 사진들\돋보기.png", master=window)    
image3=PhotoImage(file=r"출력 사진들\마이크.png", master=window)
        
b01=Button(window, text="분리배출 방법", command=b1_click) # 분리배출 방법 버튼 선언
b02=Button(window, image=image2, command=b2_click) # 검색기능 버튼 선언
b03=Button(window, image=image3, command=b3_click) # 음성검색기능 버튼 선언


b01.place(x=200, y=100, width=400, height=100) # 분리배출 방법 버튼 배치
b02.place(x=200, y=300, width=100, height=100) # 검색기능 버튼 배치
b03.place(x=500, y=300, width=100, height=100) # 음성검색기능 버튼 배치

b01.configure(font=("", 30), bg="papayawhip")
b02.configure(bg="papayawhip")
b03.configure(bg="papayawhip")


window.mainloop() # 윈도우 창을 종료할때까지 실행