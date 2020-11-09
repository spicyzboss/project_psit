"""Project PSIT Draft Version"""
import tkinter


def main():
    """Main Function"""
    # Window settings ======================================================

    height = 600  # ความสูง
    width = 800  # ความกว้าง
    window = tkinter.Tk()  # initialize tkinter

    # สร้าง canvas จาก size ที่กำหนด
    canvas = tkinter.Canvas(window, height=height, width=width)

    # Widget settings ======================================================

    # Label
    question = tkinter.Label(text="QUESTION_LABEL",
                             font="Sukhumvit_Set 50")

    # Button
    button_ans1 = tkinter.Button(canvas, text="1", font="Sukhumvit_Set 30")
    button_ans2 = tkinter.Button(canvas, text="2", font="Sukhumvit_Set 30")
    button_ans3 = tkinter.Button(canvas, text="3", font="Sukhumvit_Set 30")
    button_ans4 = tkinter.Button(canvas, text="4", font="Sukhumvit_Set 30")

    # Pack widget to canvas ================================================
    canvas.pack()  # การรวม Widget ที่ทำมาลง Canvas

    # วางตำแหน่งปุ่มคำตอบ
    button_ans1.place(height=125, width=250, x=100, y=180)
    button_ans2.place(height=125, width=250, x=450, y=180)
    button_ans3.place(height=125, width=250, x=100, y=360)
    button_ans4.place(height=125, width=250, x=450, y=360)

    # วางตำแหน่งคำถาม
    question.place(height=120, width=500, x=150, y=30)

    window.mainloop()  # รอการทำงานจาก User ================================


main()
