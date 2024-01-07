from tkinter import *
import tkinter.font

root = Tk()
root.title("Konversi Suhu")
root.geometry("400x400")

thefont = tkinter.font.Font(size=15)

# frame baru
nwframe = LabelFrame(root,padx=10,pady=10)
nwframe.place(x =15 , y = 10 )

# judul
judul = Label(nwframe,text="Konversi Suhu").grid(row = 0, columnspan=3)
samde = Label(nwframe, text="=").grid(row = 1,column=1)

# kotak input nomor
e1 = Entry(nwframe,width=15)
e2 = Entry(nwframe,width=15)
e1["font"] = thefont
e2["font"] = thefont
e2.insert(0, "0")
e1.grid(row=1,column=0)
e2.grid(row=1, column=2)

# rumus dan semua fungsi
rmslbl = Label(nwframe,text="Formula",bg="green")
rmslbl.place(x = 1, y =90)

rmsnya = Label(nwframe,text="(...°C x 9/5) + 32 = ... °F")
rmsnya.place(x = 50 , y = 90)

chek = {"rumus","yes"}

def rumus(rm):
    # hapus kotak 2
    e2.delete(0,END)
    
    # mendapatkan nilai dari kotak
    suhu1 = cliked.get()
    suhu2 = cliked2.get()
    nomer1 = int(e1.get())

    # menghilangkan tulisan sebelumnya 
    global rmsnya
    if "rumus" in chek:
        rmsnya.place_forget()
    else:
        pass
      
    # menuliskan rumus dan menentukan hitungan
    if suhu1 == "celcius" and suhu2 == "fahrenheit":
        rmsnya = Label(nwframe,text="("+e1.get()+"°C × 9/5) + 32 = ... °F")
        hitungan = (nomer1 * 9/5) + 32
    elif suhu1 == "celcius" and suhu2 == "kelvin":
        rmsnya = Label(nwframe,text=e1.get()+"°C + 273.15 = ... K")
        hitungan = (nomer1 + 273.15)
    elif suhu1 == "celcius" and suhu2 == "reamur":
        rmsnya = Label(nwframe,text="(4/5 × "+e1.get()+"°C) = ... R")
        hitungan = (4/5 * nomer1)
    elif suhu1 == "fahrenheit" and suhu2 == "celcius":
        rmsnya = Label(nwframe,text="("+e1.get()+"°F - 32) × 5/9 = ... °C")
        hitungan = (nomer1 - 32) * 5/9
    elif suhu1 == "fahrenheit" and suhu2 == "kelvin":
        rmsnya = Label(nwframe,text="("+e1.get()+"°F - 32) × 5/9 + 273.15 = ... K")
        hitungan = (nomer1 - 32) * 5/9 + 273.15
    elif suhu1 == "fahrenheit" and suhu2 == "reamur":
        rmsnya = Label(nwframe,text="("+e1.get()+"F - 32) × 4/9 = ... R")
        hitungan = (nomer1 - 32) * 4/9
    elif suhu1 == "reamur" and suhu2 == "celcius":
        rmsnya = Label(nwframe,text="5/4 × "+e1.get()+"R) = ... °C")
        hitungan = (5/4 * nomer1)
    elif suhu1 == "reamur" and suhu2 == "fahrenheit":
        rmsnya = Label(nwframe,text="(9/4 × "+e1.get()+"R) + 32 = ... F")
        hitungan = (9/4 * nomer1) + 32
    elif suhu1 == "reamur" and suhu2 == "kelvin":
        rmsnya = Label(nwframe,text="(5/4 ×"+e1.get()+"R) + 273 = ... K")
        hitungan = (5/4 * nomer1) + 273
    elif suhu1 == "kelvin" and suhu2 == "celcius":
        rmsnya = Label(nwframe,text=e1.get()+"K - 273.15 = ... °C")
        hitungan = (nomer1 - 273.15)
    elif suhu1 == "kelvin" and suhu2 == "fahrenheit":
        rmsnya = Label(nwframe,text="("+e1.get()+"K - 273.15) × 9/5 + 32 = ... °F ")
        hitungan = (nomer1 - 273.15) * 9/5 + 32 
    elif suhu1 == "kelvin" and suhu2 == "reamur":
        rmsnya = Label(nwframe,text="("+e1.get()+"k - 273) × 4/5 = ... R")
        hitungan = (nomer1 - 273) * 4/5
    elif suhu1 == "celcius" and suhu2 == "celcius" or suhu1 == "fahrenheit" and suhu2 == "fahrenheit" or  suhu1 == "reamur" and suhu2 == "reamur" or suhu1 == "kelvin" and suhu2 == "kelvin" :
        rmsnya = Label(nwframe,text="tidak ada rumus kedua jenis suhu sama")
        hitungan = nomer1
    hasil = hitungan
    e2.insert(0,hasil)
    rmsnya.place(x = 50 , y = 90)
    

# memasukkan nilai untuk membuat pilihan suhu
pilih = ["celcius","fahrenheit","kelvin","reamur"]
cliked = StringVar()
cliked.set(pilih[0])
drop = OptionMenu(nwframe,cliked,*pilih,command=rumus)
drop.config(width=20)
drop.grid(row = 2,column=0)

cliked2 = StringVar()
cliked2.set(pilih[1])
drop2 = OptionMenu(nwframe,cliked2,*pilih,command=rumus)
drop2.config(width=20)
drop2.grid(row = 2,column=2)

# button hitung
btn = Button(nwframe,text="hitung",command=lambda:rumus("hitung"))
btn.grid(row = 3,column=2)


root.mainloop()