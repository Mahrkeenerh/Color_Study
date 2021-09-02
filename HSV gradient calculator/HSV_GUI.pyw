from tkinter import *
from tkinter import messagebox
import HSV_Calculator


objects = []
rectangles = []


def ShowError(message):
    messagebox.showerror(title="ERROR", message=message)


def SetAction():

    try:
        hsv1 = HSV_Calculator.RGB_to_HSV(HSV_Calculator.HEX_to_RGB(hex_1_text.get()))
        hsv2 = HSV_Calculator.RGB_to_HSV(HSV_Calculator.HEX_to_RGB(hex_2_text.get()))

        h1 = hsv1[0]
        s1 = hsv1[1]
        v1 = hsv1[2]

        h2 = hsv2[0]
        s2 = hsv2[1]
        v2 = hsv2[2]

        splits = int(splits_text.get())

    except:
        ShowError("Všetko musia byť celé čísla!")
        return

    if h1 > 360 or h2 > 360 or h1 < 0 or h2 < 0:
        ShowError("Hue musí byť z intervalu <0, 360>!")
        return

    if s1 > 100 or s2 > 100 or s1 < 0 or s2 < 0:
        ShowError("Sat musí byť z intervalu <0, 100>!")
        return

    if v1 > 100 or v2 > 100 or v1 < 0 or v2 < 0:
        ShowError("Val musí byť z intervalu <0, 100>!")
        return

    if splits < 0:
        ShowError("Splits musí byť z intervalu <0, ...>!")
        return

    for i in objects:
        i.destroy()

    for i in rectangles:
        canvas.delete(i)

    HSV_Calculator.SetPoints([h1, s1, v1], [h2, s2, v2])
    
    canvas.itemconfig(display1_rectangle, fill="#" + HSV_Calculator.RGB_to_HEX(HSV_Calculator.HSV_to_RGB(HSV_Calculator.first)))
    canvas.itemconfig(display2_rectangle, fill="#" + HSV_Calculator.RGB_to_HEX(HSV_Calculator.HSV_to_RGB(HSV_Calculator.second)))

    codes = HSV_Calculator.CalculateInterval(splits)

    for i in range(splits):
        l_i = Label(root, text="hsv:", font=21, fg=text_hex, bg=bg_hex)
        l_i.place(x=35 + 100 * i, y=360, width=45)

        objects.append(l_i)

        hsv = codes[i]
        rgb = HSV_Calculator.HSV_to_RGB(hsv)
        hex = HSV_Calculator.RGB_to_HEX(rgb)

        hue_i = Entry(root, textvariable=StringVar(value=str(hsv[0])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        hue_i.place(x=35 + 100 * i, y=385, height=21, width=45)
        sat_i = Entry(root, textvariable=StringVar(value=str(hsv[1])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        sat_i.place(x=35 + 100 * i, y=410, height=21, width=45)
        val_i = Entry(root, textvariable=StringVar(value=str(hsv[2])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        val_i.place(x=35 + 100 * i, y=435, height=21, width=45)

        objects.append(hue_i)
        objects.append(sat_i)
        objects.append(val_i)

        l_i = Label(root, text="rgb:", font=21, fg=text_hex, bg=bg_hex)
        l_i.place(x=35 + 100 * i, y=460, width=45)

        objects.append(l_i)

        r_i = Entry(root, textvariable=StringVar(value=str(rgb[0])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        r_i.place(x=35 + 100 * i, y=485, height=21, width=45)
        g_i = Entry(root, textvariable=StringVar(value=str(rgb[1])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        g_i.place(x=35 + 100 * i, y=510, height=21, width=45)
        b_i = Entry(root, textvariable=StringVar(value=str(rgb[2])), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        b_i.place(x=35 + 100 * i, y=535, height=21, width=45)

        objects.append(r_i)
        objects.append(g_i)
        objects.append(b_i)

        l_i = Label(root, text="hex:", font=21, fg=text_hex, bg=bg_hex)
        l_i.place(x=35 + 100 * i, y=560, width=45)

        objects.append(l_i)

        hex_i = Entry(root, textvariable=StringVar(value=hex), fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
        hex_i.place(x=35 + 100 * i, y=585, height=21, width=45)

        objects.append(hex_i)

        rectangle = canvas.create_rectangle(10 + 100 * i, 625, 110 + 100 * i, 725, outline="", fill="#" + hex)

        rectangles.append(rectangle)


def CalculateAction():

    try:
        h = int(hue_3_text.get())
        s = int(sat_3_text.get())
        v = int(val_3_text.get())

    except:
        ShowError("Všetko musia byť celé čísla!")
        return

    if h > 360 or h < -1:
        ShowError("Hue musí byť z intervalu <-1, 360>!")
        return

    if s > 100 or s < -1:
        ShowError("Sat musí byť z intervalu <-1, 100>!")
        return

    if v > 100 or v < -1:
        ShowError("Val musí byť z intervalu <-1, 100>!")
        return

    if not ((h != -1 and s == -1 and v == -1) or (h == -1 and s != -1 and v == -1) or (h == -1 and s == -1 and v != -1)):
        ShowError("HSV - jedno musí byť nerovné -1, zvyšné musia byť -1!")

    hsv = HSV_Calculator.CalculatePoint(h, s, v)
    rgb = HSV_Calculator.HSV_to_RGB(hsv)
    hex = HSV_Calculator.RGB_to_HEX(rgb)

    canvas.itemconfig(display3_rectangle, fill="#" + hex)

    hue_4_text_text.set(str(hsv[0]))
    sat_4_text_text.set(str(hsv[1]))
    val_4_text_text.set(str(hsv[2]))


bg_hex = "#333333"
text_hex = "#ffffff"

root = Tk()
root.configure()
root.title("HSV Calculator")

canvas = Canvas(root, width=10000, height=735, bg=bg_hex)
canvas.pack()

root.geometry("950x735")

canvas.create_rectangle(-1, 0, 549, 350, outline=text_hex, fill=bg_hex)
canvas.create_rectangle(549, 0, 952, 350, outline=text_hex, fill=bg_hex)

display1_rectangle = canvas.create_rectangle(10, 90, 250, 340, outline="", fill="red")
display2_rectangle = canvas.create_rectangle(299, 90, 539, 340, outline="", fill="red")
display3_rectangle = canvas.create_rectangle(600, 90, 840, 340, outline="", fill="#000000")


# POINTS + SPLITS
l0 = Label(root, text="Points:", font=21, fg=text_hex, bg=bg_hex)
l0.place(x=10, y=15)

l12 = Label(root, text="Splits:", font=21, fg=text_hex, bg=bg_hex)
l12.place(x=140, y=15, width=80)

splits_text = Entry(root, textvariable=StringVar(value="10"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
splits_text.place(x=210, y=15, height=21, width=34)

# FIRST POINT STUFF
l1 = Label(root, text="hex:", font=21, fg=text_hex, bg=bg_hex)
l1.place(x=10, y=50, width=40)

hex_1_text = Entry(root, textvariable=StringVar(value="000000"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
hex_1_text.place(x=50, y=50, height=21, width=45)


# SECOND POINT STUFF
l4 = Label(root, text="hex:", font=21, fg=text_hex, bg=bg_hex)
l4.place(x=300, y=50, width=40)

hex_2_text = Entry(root, textvariable=StringVar(value="ffffff"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
hex_2_text.place(x=340, y=50, height=21, width=45)


# SET POINT STUFF
l7 = Label(root, text="hue:", font=21, fg=text_hex, bg=bg_hex)
l7.place(x=600, y=15, width=40)

hue_3_text = Entry(root, textvariable=StringVar(value="-1"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
hue_3_text.place(x=640, y=15, height=21, width=34)

l8 = Label(root, text="sat:", font=21, fg=text_hex, bg=bg_hex)
l8.place(x=680, y=15, width=40)

sat_3_text = Entry(root, textvariable=StringVar(value="-1"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
sat_3_text.place(x=720, y=15, height=21, width=34)

l9 = Label(root, text="val:", font=21, fg=text_hex, bg=bg_hex)
l9.place(x=760, y=15, width=40)

val_3_text = Entry(root, textvariable=StringVar(value="-1"), fg=text_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center")
val_3_text.place(x=800, y=15, height=21, width=34)


# SET POINT OUT
l10 = Label(root, text="hue:", font=21, fg=text_hex, bg=bg_hex)
l10.place(x=600, y=50, width=40)

hue_4_text_text = StringVar(value="0")
hue_4_text = Entry(root, textvariable=hue_4_text_text, fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
hue_4_text.place(x=640, y=50, height=21, width=34)

l11 = Label(root, text="sat:", font=21, fg=text_hex, bg=bg_hex)
l11.place(x=680, y=50, width=40)

sat_4_text_text = StringVar(value="0")
sat_4_text = Entry(root, textvariable=sat_4_text_text, fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
sat_4_text.place(x=720, y=50, height=21, width=34)

l12 = Label(root, text="val:", font=21, fg=text_hex, bg=bg_hex)
l12.place(x=760, y=50, width=40)

val_4_text_text = StringVar(value="0")
val_4_text = Entry(root, textvariable=val_4_text_text, fg=bg_hex, bg=bg_hex, borderwidth=1, highlightcolor=text_hex, justify="center", state="readonly")
val_4_text.place(x=800, y=50, height=21, width=34)


# BUTTONS
setPointsButton = Button(root, text="Set", font=21, fg=bg_hex, bg=text_hex, command=SetAction)
setPointsButton.place(x=444, y=15, height=25, width=90)

calculatePointButton = Button(root, text="Calculate", font=21, fg=bg_hex, bg=text_hex, command=CalculateAction)
calculatePointButton.place(x=850, y=15, height=25, width=90)


SetAction()
root.mainloop()
