import tkinter as tk #引入tkinter库
total_time=28*60+35 #定义变量，保存总时间间隔 28:35
isRunning=False #定义变量，保存倒计时是否开始启动
window=tk.Tk() #创建一个桌面应用窗口
window.title('摸鱼神器') #添加窗口标题
window.geometry('280x150') #设置窗口大小
l=tk.Label(window,text='距离下次巡逻：28：35',font=('微软雅黑',15)) #设置标签：老板巡逻时间
l.pack(pady=20) #如果是padx就是x轴横向的，然后标签上墙
def start_fish():
    #l.config(text='倒计时启动')
    global isRunning
    isRunning=True
    update_time()
def end_fish():
    global isRunning
    isRunning=False
    l.config(text='状态安全')
frame_btn=tk.Frame(window) #创建托盘
frame_btn.pack()
btn_start=tk.Button(frame_btn,text='开始摸鱼',command=start_fish) #按钮，定义变量btn_start
btn_start.grid(row=0,column=0,padx=10) #指定在托盘的什么位置,第一行第一列
btn_end=tk.Button(frame_btn,text='我不摸了',command=end_fish)
btn_end.grid(row=0,column=1,padx=10)
def update_time(): #启动倒计时功能函数
    global total_time,isRunning
    #61S===>1分钟：1秒
    if isRunning and total_time>0:
        m=total_time//60
        s=total_time%60
        l.config(text=f'距离下次巡逻：{m}分{s}秒')
        total_time-=1
        window.after(1000,update_time) #每隔一秒，让程序自动调用这个函数
    elif isRunning and total_time<=0:
        l.config(text='老板来了')
window.mainloop()#打开窗口
