from tkinter import *
import random
import time;
import datetime
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk
from tkinter import filedialog
import os
import tempfile



class RestaurantLogin:
        
        def __init__(self, root):
                self.root=root
                self.root.geometry("1350x750+0+0")
                self.root.title("Safeway Management Systems")
                self.root.configure(background ='Cadet Blue')
                


                

                #=========BackGroud Image=============
                self.bg=ImageTk.PhotoImage(file="Images/284467.jpg")
                self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
                

                #========Login  Frame==================
                Frame_login = Frame(self.root, bg='White')
                Frame_login.place(x=450, y=150, width=500, height=400)


                title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#6162FF", bg="white")
                title.place(x=90, y=30)
                subtitle = Label(Frame_login, text="Staff Login Area", font=("Goudy Old Sytle", 15, "bold"), fg="#1d1d1d", bg="white")
                subtitle.place(x=90, y=100)


                lbl_User = Label(Frame_login, text="User", font=("Goudy Old Sytle", 15, "bold"), fg="grey", bg="white")
                lbl_User.place(x=90, y=140)
                self.username = Entry(Frame_login, font=("Goudy Old Sytle", 15), bg="#E7E6E6",cursor="hand2")
                self.username.place(x=90, y=170, width=320, height=35)


                lbl_Password = Label(Frame_login, text="Password", font=("Goudy Old Sytle", 15, "bold"), fg="grey", bg="white")
                lbl_Password.place(x=90, y=210)
                self.Password = Entry(Frame_login, font=("Goudy Old Sytle", 15),show='*',cursor="hand2", bg="#E7E6E6")
                self.Password.place(x=90, y=240, width=320, height=35)

                submit = Button(Frame_login, text="Login",command=self.pass_function,cursor="hand2", bd=0, font=("Goudy Old Sytle", 12, "bold"), bg="#6162FF", fg="white")
                submit.place(x=90, y=320, width=180, height=40)


        def pass_function(self):
                if self.username.get()=="" or self.Password.get()=="":
                        tkinter.messagebox.showerror("Error", "All fields are required", parent=self.root)
                elif self.username.get()!="Safeway" or self.Password.get()!="123456":
                        tkinter.messagebox.showerror("Error", "Invalid username or password", parent=self.root)
                else:
                        self.login_window()
                        
                


        

        def login_window(self):
                self.RestaurantWindow = Toplevel(self.root)
                self.app = RestaurantManagement(self.RestaurantWindow)








                


class RestaurantManagement:
        def __init__(self, root):
                self.root=root
                self.root.geometry("1350x750+0+0")
                self.root.title("Safeway Management Systems")
                self.root.configure(background ='Cadet Blue')
                
                Main_frame = Frame(self.root, bg='#f5c84e',bd=10)
                Main_frame.pack(side=TOP,expand=1,fill=BOTH)
                Main_frame2 = Frame(self.root, bg='#f5c84e')
                Main_frame2.pack(side=BOTTOM, expand=1,fill=BOTH)



                breakfast_F = Frame(Main_frame, bg='Powder Blue', bd=10, relief=RIDGE)
                breakfast_F.pack(side=LEFT, anchor='nw',expand=1,fill=BOTH)
                breakfast_C = Canvas(breakfast_F)
                breakfast_C.pack(side=LEFT, fill=BOTH,expand=1)

                my_scrollbar = ttk.Scrollbar(breakfast_F, orient=VERTICAL, command=breakfast_C.yview)
                my_scrollbar.pack(side= RIGHT,fill=Y)

                breakfast_C.configure(yscrollcommand= my_scrollbar.set)
                breakfast_C.bind('<Configure>', lambda e:breakfast_C.configure(scrollregion=breakfast_C.bbox("all")))

                first_frame = Frame(breakfast_C)
                breakfast_C.create_window((0,0), window=first_frame)



                mainmeal_F = Frame(Main_frame, bg='Powder Blue', bd=10, relief=RIDGE)
                mainmeal_F.pack(side=LEFT,anchor='n',expand=1,fill=BOTH)
                mainmeal_C = Canvas(mainmeal_F)
                mainmeal_C.pack(side=LEFT, fill=BOTH,expand=1)

                my_scrollbar2 = ttk.Scrollbar(mainmeal_F, orient=VERTICAL, command=mainmeal_C.yview)
                my_scrollbar2.pack(side= RIGHT,fill=Y)

                mainmeal_C.configure(yscrollcommand= my_scrollbar2.set)
                mainmeal_C.bind('<Configure>', lambda e:mainmeal_C.configure(scrollregion=mainmeal_C.bbox("all")))

                second_frame = Frame(mainmeal_C)
                mainmeal_C.create_window((0,0), window=second_frame)



                drinks_F = Frame(Main_frame, bg='Powder Blue', bd=10, relief=RIDGE)
                drinks_F.pack(side=LEFT,anchor='ne',expand=1,fill=BOTH)
                drinks_C = Canvas(drinks_F)
                drinks_C.pack(side=LEFT, fill=BOTH,expand=1)

                my_scrollbar3 = ttk.Scrollbar(drinks_F, orient=VERTICAL, command=drinks_C.yview)
                my_scrollbar3.pack(side= RIGHT,fill=Y)

                drinks_C.configure(yscrollcommand= my_scrollbar3.set)
                drinks_C.bind('<Configure>', lambda e:drinks_C.configure(scrollregion=drinks_C.bbox("all")))

                third_frame = Frame(drinks_C)
                drinks_C.create_window((0,0), window=third_frame)

                footer_F=Frame(Main_frame2, bg='#6ec231', relief=RAISED,height=1, bd=10)
                footer_F.pack(side=LEFT,expand=1)
                payment_F=buttons_F =Frame(footer_F, bg='#6ec231', relief=RAISED)
                payment_F.pack()
                buttons_F =Frame(footer_F, bg='#6ec231', relief=RAISED)
                buttons_F.pack()



                #========================================Variables===========================================================================
                Var1=IntVar()
                Var2=IntVar()
                Var3=IntVar()
                Var4=IntVar()
                Var5=IntVar()
                Var6=IntVar()
                Var7=IntVar()
                Var8=IntVar()
                Var9=IntVar()
                Var10=IntVar()
                Var11=IntVar()
                Var12=IntVar()
                Var13=IntVar()
                Var14=IntVar()
                Var15=IntVar()
                Var16=IntVar()
                Var17=IntVar()
                Var18=IntVar()
                Var19=IntVar()
                Var20=IntVar()
                Var21=IntVar()
                Var22=IntVar()
                Var23=IntVar()
                Var24=IntVar()
                Var25=IntVar()
                Var26=IntVar()
                Var27=IntVar()
                Var28=IntVar()
                Var29=IntVar()
                Var30=IntVar()
                Var31=IntVar()
                Var32=IntVar()
                Var33=IntVar()
                Var34=IntVar()
                Var35=IntVar()
                Var36=IntVar()
                Var37=IntVar()
                Var38=IntVar()
                Var39=IntVar()
                Var40=IntVar()
                Var41=IntVar()
                Var42=IntVar()
                Var43=IntVar()
                Var44=IntVar()
                Var45=IntVar()
                Var46=IntVar()
                Var47=IntVar()
                Var48=IntVar()
                Var49=IntVar()
                Var50=IntVar()
                Var51=IntVar()
                Var52=IntVar()
                Var53=IntVar()
                Var54=IntVar()
                Var55=IntVar()
                Var56=IntVar()
                Var57=IntVar()
                Var58=IntVar()
                Var59=IntVar()
                Var60=IntVar()

                PaidTax = StringVar()
                SubTotal = StringVar()
                TotalCost = StringVar()



                text_input = StringVar()
                operator = ""



                E_Tea = StringVar()
                E_Tea_Masala = StringVar()
                E_Black_Tea = StringVar()
                E_White_Coffee = StringVar()
                E_Black_Coffee = StringVar()
                E_Special_Tea = StringVar()
                E_Chapati_Brown = StringVar()
                E_Chapati = StringVar()
                E_Andazi = StringVar()
                E_Mahamri = StringVar()
                E_Sausage = StringVar()
                E_Smokie = StringVar()
                E_Boiled_Eggs = StringVar()
                E_Spanish_Omllete = StringVar()
                E_Scrambled_Eggs = StringVar()
                E_Fried_Eggs = StringVar()
                E_Macho_Egg = StringVar()
                E_Half_Cake = StringVar()
                E_Doughnut = StringVar()
                E_Samosa = StringVar()

                E_Tea.set("0")
                E_Tea_Masala.set("0")
                E_Black_Tea.set("0")
                E_White_Coffee.set("0")
                E_Black_Coffee.set("0")
                E_Special_Tea.set("0")
                E_Chapati_Brown.set("0")
                E_Chapati.set("0")
                E_Andazi.set("0")
                E_Mahamri.set("0")
                E_Sausage.set("0")
                E_Smokie.set("0")
                E_Boiled_Eggs.set("0")
                E_Spanish_Omllete.set("0")
                E_Scrambled_Eggs.set("0")
                E_Fried_Eggs.set("0")
                E_Macho_Egg.set("0")
                E_Half_Cake.set("0")
                E_Doughnut.set("0")
                E_Samosa.set("0")



                E_Chips = StringVar()
                E_Chips_Kuku = StringVar()
                E_Stew_Kuku_Kienyeji = StringVar()
                E_Sima = StringVar()
                E_Brown_Ugali = StringVar()
                E_Sima_Tilapia = StringVar()
                E_Tilapia = StringVar()
                E_Beans = StringVar()
                E_Pojo = StringVar()
                E_Wali = StringVar()
                E_Mwangani_Saga = StringVar()
                E_Managu = StringVar()
                E_Matumbo = StringVar()
                E_Beef_Stew = StringVar()
                E_Beef_Fry = StringVar()
                E_Mchicha = StringVar()
                E_Skumawiki_Cabbage = StringVar()
                E_Mboga_Special = StringVar()
                E_Pilau = StringVar()
                E_Nyama_Choma_1_4 = StringVar()
                E_Omena = StringVar()
                E_Githeri = StringVar()
                E_Githeri_Special = StringVar()
                E_Maini = StringVar()
                E_Matoke = StringVar()
                E_Bone_Soup = StringVar()

                E_Chips.set("0")
                E_Chips_Kuku.set("0")
                E_Stew_Kuku_Kienyeji.set("0")
                E_Sima.set("0")
                E_Brown_Ugali.set("0")
                E_Sima_Tilapia.set("0")
                E_Tilapia.set("0")
                E_Beans.set("0")
                E_Pojo.set("0")
                E_Wali.set("0")
                E_Mwangani_Saga.set("0")
                E_Managu.set("0")
                E_Matumbo.set("0")
                E_Beef_Stew.set("0")
                E_Beef_Fry.set("0")
                E_Mchicha.set("0")
                E_Skumawiki_Cabbage.set("0")
                E_Mboga_Special.set("0")
                E_Pilau.set("0")
                E_Nyama_Choma_1_4.set("0")
                E_Omena.set("0")
                E_Githeri.set("0")
                E_Githeri_Special.set("0")
                E_Maini.set("0")
                E_Matoke.set("0")
                E_Bone_Soup.set("0")




                E_Soda_300ml = StringVar()
                E_Soda_500ml = StringVar()
                E_Mango_Juice_60 = StringVar()
                E_Mango_Juice_100 = StringVar()
                E_Passion_Juice_60 = StringVar()
                E_Passion_Juice_100 = StringVar()
                E_Beetroot_Juice_60 = StringVar()
                E_Beetroot_Juice_100 = StringVar()
                E_Minute_Maid_400ml = StringVar()
                E_Minute_Maid_1L = StringVar()
                E_Dasani_1_2L = StringVar()
                E_Dasani_1L = StringVar()
                E_Fresh_Milk_Glass = StringVar()
                E_Mala = StringVar()

                E_Soda_300ml.set("0")
                E_Soda_500ml.set("0")
                E_Mango_Juice_60.set("0")
                E_Mango_Juice_100.set("0")
                E_Passion_Juice_60.set("0")
                E_Passion_Juice_100.set("0")
                E_Beetroot_Juice_60.set("0")
                E_Beetroot_Juice_100.set("0")
                E_Minute_Maid_400ml.set("0")
                E_Minute_Maid_1L.set("0")
                E_Dasani_1_2L.set("0")
                E_Dasani_1L.set("0")
                E_Fresh_Milk_Glass.set("0")
                E_Mala.set("0")



                #==========================================Function Declaration==============================================================
                def iExit():
                        iExit = tkinter.messagebox.askyesno("Exit Restaurant System","Confirm if you want to exit")
                        if iExit>0:
                                root.destroy()
                                return

                def iReset():
                        
                

                

                        Var1.set(0)
                        Var2.set(0)
                        Var3.set(0)
                        Var4.set(0)
                        Var5.set(0)
                        Var6.set(0)
                        Var7.set(0)
                        Var8.set(0)
                        Var9.set(0)
                        Var10.set(0)
                        Var11.set(0)
                        Var12.set(0)
                        Var13.set(0)
                        Var14.set(0)
                        Var15.set(0)
                        Var16.set(0)
                        Var17.set(0)
                        Var18.set(0)
                        Var19.set(0)
                        Var20.set(0)
                        Var21.set(0)
                        Var22.set(0)
                        Var23.set(0)
                        Var24.set(0)
                        Var25.set(0)
                        Var26.set(0)
                        Var27.set(0)
                        Var28.set(0)
                        Var29.set(0)
                        Var30.set(0)
                        Var31.set(0)
                        Var32.set(0)
                        Var33.set(0)
                        Var34.set(0)
                        Var35.set(0)
                        Var36.set(0)
                        Var37.set(0)
                        Var38.set(0)
                        Var39.set(0)
                        Var40.set(0)
                        Var41.set(0)
                        Var42.set(0)
                        Var43.set(0)
                        Var44.set(0)
                        Var45.set(0)
                        Var46.set(0)
                        Var47.set(0)
                        Var48.set(0)
                        Var49.set(0)
                        Var50.set(0)
                        Var51.set(0)
                        Var52.set(0)
                        Var53.set(0)
                        Var54.set(0)
                        Var55.set(0)
                        Var56.set(0)
                        Var57.set(0)
                        Var58.set(0)
                        Var59.set(0)
                        Var60.set(0)


                        E_Tea.set("0")
                        E_Tea_Masala.set("0")
                        E_Black_Tea.set("0")
                        E_White_Coffee.set("0")
                        E_Black_Coffee.set("0")
                        E_Special_Tea.set("0")
                        E_Chapati_Brown.set("0")
                        E_Chapati.set("0")
                        E_Andazi.set("0")
                        E_Mahamri.set("0")
                        E_Sausage.set("0")
                        E_Smokie.set("0")
                        E_Boiled_Eggs.set("0")
                        E_Spanish_Omllete.set("0")
                        E_Scrambled_Eggs.set("0")
                        E_Fried_Eggs.set("0")
                        E_Macho_Egg.set("0")
                        E_Half_Cake.set("0")
                        E_Doughnut.set("0")
                        E_Samosa.set("0")


                        E_Chips.set("0")
                        E_Chips_Kuku.set("0")
                        E_Stew_Kuku_Kienyeji.set("0")
                        E_Sima.set("0")
                        E_Brown_Ugali.set("0")
                        E_Sima_Tilapia.set("0")
                        E_Tilapia.set("0")
                        E_Beans.set("0")
                        E_Pojo.set("0")
                        E_Wali.set("0")
                        E_Mwangani_Saga.set("0")
                        E_Managu.set("0")
                        E_Matumbo.set("0")
                        E_Beef_Stew.set("0")
                        E_Beef_Fry.set("0")
                        E_Mchicha.set("0")
                        E_Skumawiki_Cabbage.set("0")
                        E_Mboga_Special.set("0")
                        E_Pilau.set("0")
                        E_Nyama_Choma_1_4.set("0")
                        E_Omena.set("0")
                        E_Githeri.set("0")
                        E_Githeri_Special.set("0")
                        E_Maini.set("0")
                        E_Matoke.set("0")
                        E_Bone_Soup.set("0")

                        E_Soda_300ml.set("0")
                        E_Soda_500ml.set("0")
                        E_Mango_Juice_60.set("0")
                        E_Mango_Juice_100.set("0")
                        E_Passion_Juice_60.set("0")
                        E_Passion_Juice_100.set("0")
                        E_Beetroot_Juice_60.set("0")
                        E_Beetroot_Juice_100.set("0")
                        E_Minute_Maid_400ml.set("0")
                        E_Minute_Maid_1L.set("0")
                        E_Dasani_1_2L.set("0")
                        E_Dasani_1L.set("0")
                        E_Fresh_Milk_Glass.set("0")
                        E_Mala.set("0")

                        txtTea.config(state=DISABLED)
                        txtTea_Masala.config(state=DISABLED)
                        txtBlack_Tea.config(state=DISABLED)
                        txtWhite_Coffee.config(state=DISABLED)
                        txtBlack_Coffee.config(state=DISABLED)
                        txtSpecial_Tea.config(state=DISABLED)
                        txtChapati_Brown.config(state=DISABLED)
                        txtChapati.config(state=DISABLED)
                        txtAndazi.config(state=DISABLED)
                        txtMahamri.config(state=DISABLED)
                        txtSausage.config(state=DISABLED)
                        txtSmokie.config(state=DISABLED)
                        txtBoiled_Eggs.config(state=DISABLED)
                        txtSpanish_Omllete.config(state=DISABLED)
                        txtScrambled_Eggs.config(state=DISABLED)
                        txtFried_Eggs.config(state=DISABLED)
                        txtMacho_Egg.config(state=DISABLED)
                        txtHalf_Cake.config(state=DISABLED)
                        txtDoughnut.config(state=DISABLED)
                        txtSamosa.config(state=DISABLED)
                        txtChips.config(state=DISABLED)
                        txtChips_Kuku.config(state=DISABLED)
                        txtStew_Kuku_Kienyeji.config(state=DISABLED)
                        txtSima.config(state=DISABLED)
                        txtBrown_Ugali.config(state=DISABLED)
                        txtSima_Tilapia.config(state=DISABLED)
                        txtTilapia.config(state=DISABLED)
                        txtBeans.config(state=DISABLED)
                        txtPojo.config(state=DISABLED)
                        txtWali.config(state=DISABLED)
                        txtMwangani_Saga.config(state=DISABLED)
                        txtManagu.config(state=DISABLED)
                        txtMatumbo.config(state=DISABLED)
                        txtBeef_Stew.config(state=DISABLED)
                        txtBeef_Fry.config(state=DISABLED)
                        txtMchicha.config(state=DISABLED)
                        txtSkumawiki_Cabbage.config(state=DISABLED)
                        txtMboga_Special.config(state=DISABLED)
                        txtPilau.config(state=DISABLED)
                        txtNyama_Choma_1_4.config(state=DISABLED)
                        txtOmena.config(state=DISABLED)
                        txtGitheri.config(state=DISABLED)
                        txtGitheri_Special.config(state=DISABLED)
                        txtMaini.config(state=DISABLED)
                        txtMatoke.config(state=DISABLED)        
                        txtBone_Soup.config(state=DISABLED)

                        txtSoda_300ml.config(state=DISABLED)
                        txtSoda_500ml.config(state=DISABLED)
                        txtMango_Juice_60.config(state=DISABLED)
                        txtMango_Juice_100.config(state=DISABLED)                
                        txtPassion_Juice_60.config(state=DISABLED)
                        txtPassion_Juice_100.config(state=DISABLED)
                        txtBeetroot_Juice_60.config(state=DISABLED)
                        txtBeetroot_Juice_100.config(state=DISABLED)
                        txtMinute_Maid_400ml.config(state=DISABLED)               
                        txtMinute_Maid_1L.config(state=DISABLED)
                        txtDasani_1_2L.config(state=DISABLED)
                        txtDasani_1L.config(state=DISABLED)
                        txtFresh_Milk_Glass.config(state=DISABLED)
                        txtMala.config(state=DISABLED)


                        PaidTax.set("")
                        SubTotal.set("")
                        TotalCost.set("")



                def subtotalcost():
                        global subTotal,PriceOfFood,PriceOfDrinks,cost
                        item1=int(E_Tea.get())
                        item2=int(E_Tea_Masala.get())
                        item3=int(E_Black_Tea.get())
                        item4=int(E_White_Coffee.get())
                        item5=int(E_Black_Coffee.get())
                        item6=int(E_Special_Tea.get())
                        item7=int(E_Chapati_Brown.get())
                        item8=int(E_Chapati.get())
                        item9=int(E_Andazi.get())
                        item10=int(E_Mahamri.get())
                        item11=int(E_Sausage.get())
                        item12=int(E_Smokie.get())
                        item13=int(E_Boiled_Eggs.get())
                        item14=int(E_Spanish_Omllete.get())
                        item15=int(E_Scrambled_Eggs.get())
                        item16=int(E_Fried_Eggs.get())
                        item17=int(E_Macho_Egg.get())
                        item18=int(E_Half_Cake.get())
                        item19=int(E_Doughnut.get())
                        item20=int(E_Samosa.get())
                        item21=int(E_Chips.get())
                        item22=int(E_Chips_Kuku.get())
                        item23=int(E_Stew_Kuku_Kienyeji.get())
                        item24=int(E_Sima.get())
                        item25=int(E_Brown_Ugali.get())
                        item26=int(E_Sima_Tilapia.get())
                        item27=int(E_Tilapia.get())
                        item28=int(E_Beans.get())
                        item29=int(E_Pojo.get())
                        item30=int(E_Wali.get())
                        item31=int(E_Mwangani_Saga.get())
                        item32=int(E_Managu.get())
                        item33=int(E_Matumbo.get())
                        item34=int(E_Beef_Stew.get())
                        item35=int(E_Beef_Fry.get())
                        item36=int(E_Mchicha.get())
                        item37=int(E_Skumawiki_Cabbage.get())
                        item38=int(E_Mboga_Special.get())
                        item39=int(E_Pilau.get())
                        item40=int(E_Nyama_Choma_1_4.get())
                        item41=int(E_Omena.get())
                        item42=int(E_Githeri.get())
                        item43=int(E_Githeri_Special.get())
                        item44=int(E_Maini.get())
                        item45=int(E_Matoke.get())
                        item46=int(E_Bone_Soup.get())



                        item47=int(E_Soda_300ml.get())
                        item48=int(E_Soda_500ml.get())
                        item49=int(E_Mango_Juice_60.get())
                        item50=int(E_Mango_Juice_100.get())
                        item51=int(E_Passion_Juice_60.get())
                        item52=int(E_Passion_Juice_100.get())
                        item53=int(E_Beetroot_Juice_60.get())
                        item54=int(E_Beetroot_Juice_100.get())
                        item55=int(E_Minute_Maid_400ml.get())
                        item56=int(E_Minute_Maid_1L.get())
                        item57=int(E_Dasani_1_2L.get())
                        item58=int(E_Dasani_1L.get())
                        item59=int(E_Fresh_Milk_Glass.get())
                        item60=int(E_Mala.get())


                        PriceOfFood=(item1*30)+(item2*50)+(item3*30)+(item4*60)+(item5*40)+(item6*60)+(item7*20)+(item8*20)+(item9*10)+(item10*5) \
                                +(item11*40)+(item12*25)+(item13*25)+(item14*100)+(item15*100)+(item16*60)+(item17*100)+(item18*20)+(item19*20)+(item20*30)\
                                +(item21*100)+(item22*250)+(item23*270)+(item24*30)+(item25*50)+(item26*300)+(item27*270)+(item28*70)+(item29*70)+(item30*80)\
                                +(item31*100)+(item32*100)+(item33*100)+(item34*150)+(item35*100)+(item36*70)+(item37*50)+(item38*150)+(item39*150)+(item40*150)\
                                +(item41*90)+(item42*80)+(item43*150)+(item44*150)+(item45*150)+(item46*140)

                        PriceOfDrinks=(item47*40)+(item48*70)+(item49*60)+(item50*100)+(item51*60)+(item52*100)+(item53*60)+(item54*100)+(item55*100)+(item56*200) \
                                +(item57*50)+(item58*100)+(item59*70)+(item60*100)

                        
                        cost=(PriceOfFood)+(PriceOfDrinks)
                        SubTotal.set('Ksh'+ str(cost))

                def Balance():
                        global pay1,balance
                        pay1=int(PaidTax.get())

                        balance= (pay1)-(cost)

                        TotalCost.set('Ksh'+str(balance))

        





                def fTea():
                        if Var1.get()==1:
                                txtTea.config(state=NORMAL)
                                txtTea.delete(0,END)
                                txtTea.focus()
                        else:
                                txtTea.config(state=DISABLED)
                                E_Tea.set('0')

                def fTeaMasala():
                        if Var2.get()==1:
                                txtTea_Masala.config(state=NORMAL)
                                txtTea_Masala.delete(0,END)
                                txtTea_Masala.focus()
                        else:
                                txtTea_Masala.config(state=DISABLED)
                                E_Tea_Masala.set('0')

                def fBlackTea():
                        if Var3.get()==1:
                                txtBlack_Tea.config(state=NORMAL)
                                txtBlack_Tea.delete(0,END)
                                txtBlack_Tea.focus()
                        else:
                                txtBlack_Tea.config(state=DISABLED)
                                E_Black_Tea.set('0')

                def fWhiteCoffee():
                        if Var4.get()==1:
                                txtWhite_Coffee.config(state=NORMAL)
                                txtWhite_Coffee.delete(0,END)
                                txtWhite_Coffee.focus()
                        else:
                                txtWhite_Coffee.config(state=DISABLED)
                                E_White_Coffee.set('0')

                def fBlackCoffee():
                        if Var5.get()==1:
                                txtBlack_Coffee.config(state=NORMAL)
                                txtBlack_Coffee.delete(0,END)
                                txtBlack_Coffee.focus()
                        else:
                                txtBlack_Coffee.config(state=DISABLED)
                                E_Black_Coffee.set('0')

                def fSpecialTea():
                        if Var6.get()==1:
                                txtSpecial_Tea.config(state=NORMAL)
                                txtSpecial_Tea.delete(0,END)
                                txtSpecial_Tea.focus()
                        else:
                                txtSpecial_Tea.config(state=DISABLED)
                                E_Special_Tea.set('0')

                def fChapatiBrown():
                        if Var7.get()==1:
                                txtChapati_Brown.config(state=NORMAL)
                                txtChapati_Brown.delete(0,END)
                                txtChapati_Brown.focus()
                        else:
                                txtChapati_Brown.config(state=DISABLED)
                                E_Chapati_Brown.set('0')

                def fChapati():
                        if Var8.get()==1:
                                txtChapati.config(state=NORMAL)
                                txtChapati.delete(0,END)
                                txtChapati.focus()
                        else:
                                txtChapati.config(state=DISABLED)
                                E_Chapati.set('0')

                def fAndazi():
                        if Var9.get()==1:
                                txtAndazi.config(state=NORMAL)
                                txtAndazi.delete(0,END)
                                txtAndazi.focus()
                        else:
                                txtAndazi.config(state=DISABLED)
                                E_Andazi.set('0')

                def fMahamri():
                        if Var10.get()==1:
                                txtMahamri.config(state=NORMAL)
                                txtMahamri.delete(0,END)
                                txtMahamri.focus()
                        else:
                                txtMahamri.config(state=DISABLED)
                                E_Mahamri.set('0')

                def fSausage():
                        if Var11.get()==1:
                                txtSausage.config(state=NORMAL)
                                txtSausage.delete(0,END)
                                txtSausage.focus()
                        else:
                                txtSausage.config(state=DISABLED)
                                E_Sausage.set('0')

                def fSmokie():
                        if Var12.get()==1:
                                txtSmokie.config(state=NORMAL)
                                txtSmokie.delete(0,END)
                                txtSmokie.focus()
                        else:
                                txtSmokie.config(state=DISABLED)
                                E_Smokie.set('0')

                def fBoiledEggs():
                        if Var13.get()==1:
                                txtBoiled_Eggs.config(state=NORMAL)
                                txtBoiled_Eggs.delete(0,END)
                                txtBoiled_Eggs.focus()
                        else:
                                txtBoiled_Eggs.config(state=DISABLED)
                                E_Boiled_Eggs.set('0')

                def fSpanishOmllete():
                        if Var14.get()==1:
                                txtSpanish_Omllete.config(state=NORMAL)
                                txtSpanish_Omllete.delete(0,END)
                                txtSpanish_Omllete.focus()
                        else:
                                txtSpanish_Omllete.config(state=DISABLED)
                                E_Spanish_Omllete.set('0')

                def fScrambledEggs():
                        if Var15.get()==1:
                                txtScrambled_Eggs.config(state=NORMAL)
                                txtScrambled_Eggs.delete(0,END)
                                txtScrambled_Eggs.focus()
                        else:
                                txtScrambled_Eggs.config(state=DISABLED)
                                E_Scrambled_Eggs.set('0')

                def fFriedEggs():
                        if Var16.get()==1:
                                txtFried_Eggs.config(state=NORMAL)
                                txtFried_Eggs.delete(0,END)
                                txtFried_Eggs.focus()
                        else:
                                txtFried_Eggs.config(state=DISABLED)
                                E_Fried_Eggs.set('0')

                def fMachoEgg():
                        if Var17.get()==1:
                                txtMacho_Egg.config(state=NORMAL)
                                txtMacho_Egg.delete(0,END)
                                txtMacho_Egg.focus()
                        else:
                                txtMacho_Egg.config(state=DISABLED)
                                E_Macho_Egg.set('0')

                def fHalfCake():
                        if Var18.get()==1:
                                txtHalf_Cake.config(state=NORMAL)
                                txtHalf_Cake.delete(0,END)
                                txtHalf_Cake.focus()
                        else:
                                txtHalf_Cake.config(state=DISABLED)
                                E_Half_Cake.set('0')

                def fDoughnut():
                        if Var19.get()==1:
                                txtDoughnut.config(state=NORMAL)
                                txtDoughnut.delete(0,END)
                                txtDoughnut.focus()
                        else:
                                txtDoughnut.config(state=DISABLED)
                                E_Doughnut.set('0')

                def fSamosa():
                        if Var20.get()==1:
                                txtSamosa.config(state=NORMAL)
                                txtSamosa.delete(0,END)
                                txtSamosa.focus()
                        else:
                                txtSamosa.config(state=DISABLED)
                                E_Samosa.set('0')

                def fChips():
                        if Var21.get()==1:
                                txtChips.config(state=NORMAL)
                                txtChips.delete(0,END)
                                txtChips.focus()
                        else:
                                txtChips.config(state=DISABLED)
                                E_Chips.set('0')

                def fChipsKuku():
                        if Var22.get()==1:
                                txtChips_Kuku.config(state=NORMAL)
                                txtChips_Kuku.delete(0,END)
                                txtChips_Kuku.focus()
                        else:
                                txtChips_Kuku.config(state=DISABLED)
                                E_Chips_Kuku.set('0')

                def fStewKukuKienyeji():
                        if Var23.get()==1:
                                txtStew_Kuku_Kienyeji.config(state=NORMAL)
                                txtStew_Kuku_Kienyeji.delete(0,END)
                                txtStew_Kuku_Kienyeji.focus()
                        else:
                                txtStew_Kuku_Kienyeji.config(state=DISABLED)
                                E_Stew_Kuku_Kienyeji.set('0')

                def fSima():
                        if Var24.get()==1:
                                txtSima.config(state=NORMAL)
                                txtSima.delete(0,END)
                                txtSima.focus()
                        else:
                                txtSima.config(state=DISABLED)
                                E_Sima.set('0')

                def fBrownUgali():
                        if Var25.get()==1:
                                txtBrown_Ugali.config(state=NORMAL)
                                txtBrown_Ugali.delete(0,END)
                                txtBrown_Ugali.focus()
                        else:
                                txtBrown_Ugali.config(state=DISABLED)
                                E_Brown_Ugali.set('0')

                def fSimaTilapia():
                        if Var26.get()==1:
                                txtSima_Tilapia.config(state=NORMAL)
                                txtSima_Tilapia.delete(0,END)
                                txtSima_Tilapia.focus()
                        else:
                                txtSima_Tilapia.config(state=DISABLED)
                                E_Sima_Tilapia.set('0')

                def fTilapia():
                        if Var27.get()==1:
                                txtTilapia.config(state=NORMAL)
                                txtTilapia.delete(0,END)
                                txtTilapia.focus()
                        else:
                                txtTilapia.config(state=DISABLED)
                                E_Tilapia.set('0')

                def fBeans():
                        if Var28.get()==1:
                                txtBeans.config(state=NORMAL)
                                txtBeans.delete(0,END)
                                txtBeans.focus()
                        else:
                                txtBeans.config(state=DISABLED)
                                E_Beans.set('0')

                def fPojo():
                        if Var29.get()==1:
                                txtPojo.config(state=NORMAL)
                                txtPojo.delete(0,END)
                                txtPojo.focus()
                        else:
                                txtPojo.config(state=DISABLED)
                                E_Pojo.set('0')

                def fWali():
                        if Var30.get()==1:
                                txtWali.config(state=NORMAL)
                                txtWali.delete(0,END)
                                txtWali.focus()
                        else:
                                txtWali.config(state=DISABLED)
                                E_Wali.set('0')

                def fMwangani_Saga():
                        if Var31.get()==1:
                                txtMwangani_Saga.config(state=NORMAL)
                                txtMwangani_Saga.delete(0,END)
                                txtMwangani_Saga.focus()
                        else:
                                txtMwangani_Saga.config(state=DISABLED)
                                E_Mwangani_Saga.set('0')

                def fManagu():
                        if Var32.get()==1:
                                txtManagu.config(state=NORMAL)
                                txtManagu.delete(0,END)
                                txtManagu.focus()
                        else:
                                txtManagu.config(state=DISABLED)
                                E_Managu.set('0')

                def fMatumbo():
                        if Var33.get()==1:
                                txtMatumbo.config(state=NORMAL)
                                txtMatumbo.delete(0,END)
                                txtMatumbo.focus()
                        else:
                                txtMatumbo.config(state=DISABLED)
                                E_Matumbo.set('0')

                def fBeefStew():
                        if Var34.get()==1:
                                txtBeef_Stew.config(state=NORMAL)
                                txtBeef_Stew.delete(0,END)
                                txtBeef_Stew.focus()
                        else:
                                txtBeef_Stew.config(state=DISABLED)
                                E_Beef_Stew.set('0')

                def fBeefFry():
                        if Var35.get()==1:
                                txtBeef_Fry.config(state=NORMAL)
                                txtBeef_Fry.delete(0,END)
                                txtBeef_Fry.focus()
                        else:
                                txtBeef_Fry.config(state=DISABLED)
                                E_Beef_Fry.set('0')

                def fMchicha():
                        if Var36.get()==1:
                                txtMchicha.config(state=NORMAL)
                                txtMchicha.delete(0,END)
                                txtMchicha.focus()
                        else:
                                txtMchicha.config(state=DISABLED)
                                E_Mchicha.set('0')

                def fSkumawiki_Cabbage():
                        if Var37.get()==1:
                                txtSkumawiki_Cabbage.config(state=NORMAL)
                                txtSkumawiki_Cabbage.delete(0,END)
                                txtSkumawiki_Cabbage.focus()
                        else:
                                txtSkumawiki_Cabbage.config(state=DISABLED)
                                E_Skumawiki_Cabbage.set('0')

                def fMbogaSpecial():
                        if Var38.get()==1:
                                txtMboga_Special.config(state=NORMAL)
                                txtMboga_Special.delete(0,END)
                                txtMboga_Special.focus()
                        else:
                                txtMboga_Special.config(state=DISABLED)
                                E_Mboga_Special.set('0')

                def fPilau():
                        if Var39.get()==1:
                                txtPilau.config(state=NORMAL)
                                txtPilau.delete(0,END)
                                txtPilau.focus()
                        else:
                                txtPilau.config(state=DISABLED)
                                E_Pilau.set('0')

                def fNyamaChoma1_4():
                        if Var40.get()==1:
                                txtNyama_Choma_1_4.config(state=NORMAL)
                                txtNyama_Choma_1_4.delete(0,END)
                                txtNyama_Choma_1_4.focus()
                        else:
                                txtNyama_Choma_1_4.config(state=DISABLED)
                                E_Nyama_Choma_1_4.set('0')

                def fOmena():
                        if Var41.get()==1:
                                txtOmena.config(state=NORMAL)
                                txtOmena.delete(0,END)
                                txtOmena.focus()
                        else:
                                txtOmena.config(state=DISABLED)
                                E_Omena.set('0')

                def fGitheri():
                        if Var42.get()==1:
                                txtGitheri.config(state=NORMAL)
                                txtGitheri.delete(0,END)
                                txtGitheri.focus()
                        else:
                                txtGitheri.config(state=DISABLED)
                                E_Githeri.set('0')

                def fGitheriSpecial():
                        if Var43.get()==1:
                                txtGitheri_Special.config(state=NORMAL)
                                txtGitheri_Special.delete(0,END)
                                txtGitheri_Special.focus()
                        else:
                                txtGitheri_Special.config(state=DISABLED)
                                E_Githeri_Special.set('0')

                def fMaini():
                        if Var44.get()==1:
                                txtMaini.config(state=NORMAL)
                                txtMaini.delete(0,END)
                                txtMaini.focus()
                        else:
                                txtMaini.config(state=DISABLED)
                                E_Maini.set('0')

                def fMatoke():
                        if Var45.get()==1:
                                txtMatoke.config(state=NORMAL)
                                txtMatoke.delete(0,END)
                                txtMatoke.focus()
                        else:
                                txtMatoke.config(state=DISABLED)
                                E_Matoke.set('0')

                def fBoneSoup():
                        if Var46.get()==1:
                                txtBone_Soup.config(state=NORMAL)
                                txtBone_Soup.delete(0,END)
                                txtBone_Soup.focus()
                        else:
                                txtBone_Soup.config(state=DISABLED)
                                E_Bone_Soup.set('0')

                def fSoda300ml():
                        if Var47.get()==1:
                                txtSoda_300ml.config(state=NORMAL)
                                txtSoda_300ml.delete(0,END)
                                txtSoda_300ml.focus()
                        else:
                                txtSoda_300ml.config(state=DISABLED)
                                E_Soda_300ml.set('0')

                def fSoda500ml():
                        if Var48.get()==1:
                                txtSoda_500ml.config(state=NORMAL)
                                txtSoda_500ml.delete(0,END)
                                txtSoda_500ml.focus()
                        else:
                                txtSoda_500ml.config(state=DISABLED)
                                E_Soda_500ml.set('0')

                def fMangoJuice60():
                        if Var49.get()==1:
                                txtMango_Juice_60.config(state=NORMAL)
                                txtMango_Juice_60.delete(0,END)
                                txtMango_Juice_60.focus()
                        else:
                                txtMango_Juice_60.config(state=DISABLED)
                                E_Mango_Juice_60.set('0')

                def fMangoJuice100():
                        if Var50.get()==1:
                                txtMango_Juice_100.config(state=NORMAL)
                                txtMango_Juice_100.delete(0,END)
                                txtMango_Juice_100.focus()
                        else:
                                txtMango_Juice_100.config(state=DISABLED)
                                E_Mango_Juice_100.set('0')

                def fPassionJuice60():
                        if Var51.get()==1:
                                txtPassion_Juice_60.config(state=NORMAL)
                                txtPassion_Juice_60.delete(0,END)
                                txtPassion_Juice_60.focus()
                        else:
                                txtPassion_Juice_60.config(state=DISABLED)
                                E_Passion_Juice_60.set('0')

                def fPassionJuice100():
                        if Var52.get()==1:
                                txtPassion_Juice_100.config(state=NORMAL)
                                txtPassion_Juice_100.delete(0,END)
                                txtPassion_Juice_100.focus()
                        else:
                                txtPassion_Juice_100.config(state=DISABLED)
                                E_Passion_Juice_100.set('0')

                def fBeetrootJuice60():
                        if Var53.get()==1:
                                txtBeetroot_Juice_60.config(state=NORMAL)
                                txtBeetroot_Juice_60.delete(0,END)
                                txtBeetroot_Juice_60.focus()
                        else:
                                txtBeetroot_Juice_60.config(state=DISABLED)
                                E_Beetroot_Juice_60.set('0')

                def fBeetrootJuice100():
                        if Var54.get()==1:
                                txtBeetroot_Juice_100.config(state=NORMAL)
                                txtBeetroot_Juice_100.delete(0,END)
                                txtBeetroot_Juice_100.focus()
                        else:
                                txtBeetroot_Juice_100.config(state=DISABLED)
                                E_Beetroot_Juice_100.set('0')

                def fMinuteMaid400ml():
                        if Var55.get()==1:
                                txtMinute_Maid_400ml.config(state=NORMAL)
                                txtMinute_Maid_400ml.delete(0,END)
                                txtMinute_Maid_400ml.focus()
                        else:
                                txtMinute_Maid_400ml.config(state=DISABLED)
                                E_Minute_Maid_400ml.set('0')

                def fMinuteMaid1L():
                        if Var56.get()==1:
                                txtMinute_Maid_1L.config(state=NORMAL)
                                txtMinute_Maid_1L.delete(0,END)
                                txtMinute_Maid_1L.focus()
                        else:
                                txtMinute_Maid_1L.config(state=DISABLED)
                                E_Minute_Maid_1L.set('0')

                def fDasani1_2L():
                        if Var57.get()==1:
                                txtDasani_1_2L.config(state=NORMAL)
                                txtDasani_1_2L.delete(0,END)
                                txtDasani_1_2L.focus()
                        else:
                                txtDasani_1_2L.config(state=DISABLED)
                                E_Dasani_1_2L.set('0')

                def fDasani1L():
                        if Var58.get()==1:
                                txtDasani_1L.config(state=NORMAL)
                                txtDasani_1L.delete(0,END)
                                txtDasani_1L.focus()
                        else:
                                txtDasani_1L.config(state=DISABLED)
                                E_Dasani_1L.set('0')

                def fFreshMilkGlass():
                        if Var59.get()==1:
                                txtFresh_Milk_Glass.config(state=NORMAL)
                                txtFresh_Milk_Glass.delete(0,END)
                                txtFresh_Milk_Glass.focus()
                        else:
                                txtFresh_Milk_Glass.config(state=DISABLED)
                                E_Fresh_Milk_Glass.set('0')

                def fMala():
                        if Var60.get()==1:
                                txtMala.config(state=NORMAL)
                                txtMala.delete(0,END)
                                txtMala.focus()
                        else:
                                txtMala.config(state=DISABLED)
                                E_Mala.set('0')







                #==================================breakfast=====================================================================================
                Tea=Checkbutton(first_frame, text="Tea", onvalue=1, offvalue=0, variable=Var1, command=fTea, font=('arial',18,'bold'),\
                                ).grid(row=0, sticky=W)
                Tea_Masala=Checkbutton(first_frame, text="Tea Masala", variable=Var2, onvalue=1, offvalue=0, command=fTeaMasala,font=('arial',18,'bold'),\
                                ).grid(row=1, sticky=W)
                Black_Tea=Checkbutton(first_frame, text="Black Tea", variable=Var3, onvalue=1, offvalue=0, command=fBlackTea,font=('arial',18,'bold'),\
                                ).grid(row=2, sticky=W)
                White_Coffee=Checkbutton(first_frame, text="White Coffee", variable=Var4, onvalue=1, offvalue=0, command=fWhiteCoffee,font=('arial',18,'bold'),\
                                ).grid(row=3, sticky=W)
                Black_Coffee=Checkbutton(first_frame, text="Black Coffee", variable=Var5, onvalue=1, offvalue=0, command=fBlackCoffee,font=('arial',18,'bold'),\
                                ).grid(row=4, sticky=W)
                Special_Tea=Checkbutton(first_frame, text="Special Tea", variable=Var6, onvalue=1, offvalue=0, command=fSpecialTea,font=('arial',18,'bold'),\
                                ).grid(row=5, sticky=W)
                Chapati_Brown=Checkbutton(first_frame, text="Chapati Brown", variable=Var7, onvalue=1, offvalue=0, command=fChapatiBrown,font=('arial',18,'bold'),\
                                ).grid(row=6, sticky=W)
                Chapati=Checkbutton(first_frame, text="Chapati", variable=Var8, onvalue=1, offvalue=0, command=fChapati,font=('arial',18,'bold'),\
                                ).grid(row=7, sticky=W)
                Andazi=Checkbutton(first_frame, text="Andazi", variable=Var9, onvalue=1, offvalue=0, command=fAndazi,font=('arial',18,'bold'),\
                                ).grid(row=8, sticky=W)
                Mahamri=Checkbutton(first_frame, text="Mahamri", variable=Var10, onvalue=1, offvalue=0, command=fMahamri,font=('arial',18,'bold'),\
                                ).grid(row=9, sticky=W)
                Sausage=Checkbutton(first_frame, text="Sausage", variable=Var11, onvalue=1, offvalue=0, command=fSausage,font=('arial',18,'bold'),\
                                ).grid(row=10, sticky=W)
                Smokie=Checkbutton(first_frame, text="Smokie", variable=Var12, onvalue=1, offvalue=0, command=fSmokie,font=('arial',18,'bold'),\
                                ).grid(row=11, sticky=W)
                Boiled_Eggs=Checkbutton(first_frame, text="Boiled Eggs", variable=Var13, onvalue=1, offvalue=0, command=fBoiledEggs,font=('arial',18,'bold'),\
                                ).grid(row=12, sticky=W)
                Spanish_Omllete=Checkbutton(first_frame, text="Spanish Omllete", variable=Var14, onvalue=1, offvalue=0, command=fSpanishOmllete,font=('arial',18,'bold'),\
                                ).grid(row=13, sticky=W)
                Scrambled_Eggs=Checkbutton(first_frame, text="Scrambled Eggs", variable=Var15, onvalue=1, offvalue=0, command=fScrambledEggs,font=('arial',18,'bold'),\
                                ).grid(row=14, sticky=W)
                Fried_Eggs=Checkbutton(first_frame, text="Fried Eggs", variable=Var16, onvalue=1, offvalue=0, command=fFriedEggs,font=('arial',18,'bold'),\
                                ).grid(row=15, sticky=W)
                Macho_Egg=Checkbutton(first_frame, text="Macho Egg", variable=Var17, onvalue=1, offvalue=0, command=fMachoEgg,font=('arial',18,'bold'),\
                                ).grid(row=16, sticky=W)
                Half_Cake=Checkbutton(first_frame, text="Half Cake", variable=Var18, onvalue=1, offvalue=0, command=fHalfCake,font=('arial',18,'bold'),\
                                ).grid(row=17, sticky=W)
                Doughnut=Checkbutton(first_frame, text="Doghnut", variable=Var19, onvalue=1, offvalue=0, command=fDoughnut,font=('arial',18,'bold'),\
                                ).grid(row=18, sticky=W)
                Samosa=Checkbutton(first_frame, text="Samosa", variable=Var20, onvalue=1, offvalue=0, command=fSamosa,font=('arial',18,'bold'),\
                                ).grid(row=19, sticky=W)
                #===================================ENTRY BOX FOR breakfast======================================================================
                txtTea=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Tea)
                txtTea.grid(row=0, column=1)

                txtTea_Masala=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Tea_Masala)
                txtTea_Masala.grid(row=1, column=1)

                txtBlack_Tea=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Black_Tea)
                txtBlack_Tea.grid(row=2, column=1)

                txtWhite_Coffee=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_White_Coffee)
                txtWhite_Coffee.grid(row=3, column=1)

                txtBlack_Coffee=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Black_Coffee)
                txtBlack_Coffee.grid(row=4, column=1)

                txtSpecial_Tea=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Special_Tea)
                txtSpecial_Tea.grid(row=5, column=1)

                txtChapati_Brown=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Chapati_Brown)
                txtChapati_Brown.grid(row=6, column=1)

                txtChapati=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Chapati)
                txtChapati.grid(row=7, column=1)

                txtAndazi=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Andazi)
                txtAndazi.grid(row=8, column=1)

                txtMahamri=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mahamri)
                txtMahamri.grid(row=9, column=1)

                txtSausage=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Sausage)
                txtSausage.grid(row=10, column=1)

                txtSmokie=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Smokie)
                txtSmokie.grid(row=11, column=1)

                txtBoiled_Eggs=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Boiled_Eggs)
                txtBoiled_Eggs.grid(row=12, column=1)

                txtSpanish_Omllete=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Spanish_Omllete)
                txtSpanish_Omllete.grid(row=13, column=1)

                txtScrambled_Eggs=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Scrambled_Eggs)
                txtScrambled_Eggs.grid(row=14, column=1)

                txtFried_Eggs=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Fried_Eggs)
                txtFried_Eggs.grid(row=15, column=1)

                txtMacho_Egg=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Macho_Egg)
                txtMacho_Egg.grid(row=16, column=1)

                txtHalf_Cake=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Half_Cake)
                txtHalf_Cake.grid(row=17, column=1)

                txtDoughnut=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Doughnut)
                txtDoughnut.grid(row=18, column=1)

                txtSamosa=Entry(first_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Samosa)
                txtSamosa.grid(row=19, column=1)



                #===================================Main Meal===========================================================
                Chips=Checkbutton(second_frame, text="Chips", onvalue=1, offvalue=0, variable=Var21, command=fChips, font=('arial',18,'bold'),\
                                ).grid(row=0, sticky=W)
                Chips_Kuku=Checkbutton(second_frame, text="Chips Kuku", variable=Var22, onvalue=1, offvalue=0, command=fChipsKuku,font=('arial',18,'bold'),\
                                ).grid(row=1, sticky=W)
                Stew_Kuku_Kienyeji=Checkbutton(second_frame, text="Stew Kuku Kienyeji", variable=Var23, onvalue=1, offvalue=0, command=fStewKukuKienyeji,font=('arial',18,'bold'),\
                                ).grid(row=2, sticky=W)
                Sima=Checkbutton(second_frame, text="Sima", variable=Var24, onvalue=1, offvalue=0, command=fSima,font=('arial',18,'bold'),\
                                ).grid(row=3, sticky=W)
                Brown_Ugali=Checkbutton(second_frame, text="Brown Ugali", variable=Var25, onvalue=1, offvalue=0, command=fBrownUgali,font=('arial',18,'bold'),\
                                ).grid(row=4, sticky=W)
                Sima_Tilapia=Checkbutton(second_frame, text="Sima Tilapia", variable=Var26, onvalue=1, offvalue=0, command=fSimaTilapia,font=('arial',18,'bold'),\
                                ).grid(row=5, sticky=W)
                Tilapia=Checkbutton(second_frame, text="Tilapia", variable=Var27, onvalue=1, offvalue=0, command=fTilapia,font=('arial',18,'bold'),\
                                ).grid(row=6, sticky=W)
                Beans=Checkbutton(second_frame, text="Beans", variable=Var28, onvalue=1, offvalue=0, command=fBeans,font=('arial',18,'bold'),\
                                ).grid(row=7, sticky=W)
                Pojo=Checkbutton(second_frame, text="Pojo", variable=Var29, onvalue=1, offvalue=0, command=fPojo,font=('arial',18,'bold'),\
                                ).grid(row=8, sticky=W)
                Wali=Checkbutton(second_frame, text="Wali", variable=Var30, onvalue=1, offvalue=0, command=fWali,font=('arial',18,'bold'),\
                                ).grid(row=9, sticky=W)
                Mwangani_Saga=Checkbutton(second_frame, text="Mwangani/Saga", variable=Var31, onvalue=1, offvalue=0, command=fMwangani_Saga,font=('arial',18,'bold'),\
                                ).grid(row=10, sticky=W)
                Managu=Checkbutton(second_frame, text="Managu", variable=Var32, onvalue=1, offvalue=0, command=fManagu,font=('arial',18,'bold'),\
                                ).grid(row=11, sticky=W)
                Matumbo=Checkbutton(second_frame, text="Matumbo", variable=Var33, onvalue=1, offvalue=0, command=fMatumbo,font=('arial',18,'bold'),\
                                ).grid(row=12, sticky=W)
                Beef_Stew=Checkbutton(second_frame, text="Beef Stew", variable=Var34, onvalue=1, offvalue=0, command=fBeefStew,font=('arial',18,'bold'),\
                                ).grid(row=13, sticky=W)
                Beef_Fry=Checkbutton(second_frame, text="Beef Fry", variable=Var35, onvalue=1, offvalue=0, command=fBeefFry,font=('arial',18,'bold'),\
                                ).grid(row=14, sticky=W)
                Mchicha=Checkbutton(second_frame, text="Mchicha", variable=Var36, onvalue=1, offvalue=0, command=fMchicha,font=('arial',18,'bold'),\
                                ).grid(row=15, sticky=W)
                Skumawiki_Cabbage=Checkbutton(second_frame, text="Skumawiki/Cabbage", variable=Var37, onvalue=1, offvalue=0, command=fSkumawiki_Cabbage,font=('arial',18,'bold'),\
                                ).grid(row=16, sticky=W)
                Mboga_Special=Checkbutton(second_frame, text="Mboga Special", variable=Var38, onvalue=1, offvalue=0, command=fMbogaSpecial,font=('arial',18,'bold'),\
                                ).grid(row=17, sticky=W)
                Pilau=Checkbutton(second_frame, text="Pilau", variable=Var39, onvalue=1, offvalue=0, command=fPilau,font=('arial',18,'bold'),\
                                ).grid(row=18, sticky=W)
                Nyama_Choma_1_4=Checkbutton(second_frame, text="Choma 1/4", variable=Var40, onvalue=1, offvalue=0, command=fNyamaChoma1_4,font=('arial',18,'bold'),\
                                ).grid(row=19, sticky=W)
                Omena=Checkbutton(second_frame, text="Omena", variable=Var41, onvalue=1, offvalue=0, command=fOmena,font=('arial',18,'bold'),\
                                ).grid(row=20, sticky=W)
                Githeri=Checkbutton(second_frame, text="Githeri", variable=Var42, onvalue=1, offvalue=0, command=fGitheri,font=('arial',18,'bold'),\
                                ).grid(row=21, sticky=W)
                Githeri_Special=Checkbutton(second_frame, text="Githeri Special", variable=Var43, onvalue=1, offvalue=0, command=fGitheriSpecial,font=('arial',18,'bold'),\
                                ).grid(row=22, sticky=W)
                Maini=Checkbutton(second_frame, text="Maini", variable=Var44, onvalue=1, offvalue=0, command=fMaini,font=('arial',18,'bold'),\
                                ).grid(row=23, sticky=W)
                Matoke=Checkbutton(second_frame, text="Matoke", variable=Var45, onvalue=1, offvalue=0, command=fMatoke,font=('arial',18,'bold'),\
                                ).grid(row=24, sticky=W)
                Bone_Soup=Checkbutton(second_frame, text="Bone Soup", variable=Var46, onvalue=1, offvalue=0, command=fBoneSoup,font=('arial',18,'bold'),\
                                ).grid(row=25, sticky=W)


                #======================================Entry MainMeal==================================================
                txtChips=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Chips)
                txtChips.grid(row=0, column=1)

                txtChips_Kuku=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Chips_Kuku)
                txtChips_Kuku.grid(row=1, column=1)

                txtStew_Kuku_Kienyeji=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Stew_Kuku_Kienyeji)
                txtStew_Kuku_Kienyeji.grid(row=2, column=1)

                txtSima=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Sima)
                txtSima.grid(row=3, column=1)

                txtBrown_Ugali=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Brown_Ugali)
                txtBrown_Ugali.grid(row=4, column=1)

                txtSima_Tilapia=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Sima_Tilapia)
                txtSima_Tilapia.grid(row=5, column=1)

                txtTilapia=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Tilapia)
                txtTilapia.grid(row=6, column=1)

                txtBeans=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Beans)
                txtBeans.grid(row=7, column=1)

                txtPojo=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Pojo)
                txtPojo.grid(row=8, column=1)

                txtWali=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Wali)
                txtWali.grid(row=9, column=1)

                txtMwangani_Saga=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mwangani_Saga)
                txtMwangani_Saga.grid(row=10, column=1)

                txtManagu=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Managu)
                txtManagu.grid(row=11, column=1)

                txtMatumbo=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Matumbo)
                txtMatumbo.grid(row=12, column=1)

                txtBeef_Stew=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Beef_Stew)
                txtBeef_Stew.grid(row=13, column=1)

                txtBeef_Fry=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Beef_Fry)
                txtBeef_Fry.grid(row=14, column=1)

                txtMchicha=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mchicha)
                txtMchicha.grid(row=15, column=1)

                txtSkumawiki_Cabbage=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Skumawiki_Cabbage)
                txtSkumawiki_Cabbage.grid(row=16, column=1)

                txtMboga_Special=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mboga_Special)
                txtMboga_Special.grid(row=17, column=1)

                txtPilau=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Pilau)
                txtPilau.grid(row=18, column=1)

                txtNyama_Choma_1_4=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Nyama_Choma_1_4)
                txtNyama_Choma_1_4.grid(row=19, column=1)

                txtOmena=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Omena)
                txtOmena.grid(row=20, column=1)

                txtGitheri=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Githeri)
                txtGitheri.grid(row=21, column=1)

                txtGitheri_Special=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Githeri_Special)
                txtGitheri_Special.grid(row=22, column=1)

                txtMaini=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Maini)
                txtMaini.grid(row=23, column=1)

                txtMatoke=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Matoke)
                txtMatoke.grid(row=24, column=1)

                txtBone_Soup=Entry(second_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Bone_Soup)
                txtBone_Soup.grid(row=25, column=1)

                #======================================DRINKS==========================================================================================
                Soda_300ml=Checkbutton(third_frame, text="Soda 300ml", variable=Var47, onvalue=1, offvalue=0, command=fSoda300ml,font=('arial',18,'bold'),\
                                ).grid(row=1, sticky=W)
                Soda_500ml=Checkbutton(third_frame, text="Soda 500ml", variable=Var48, onvalue=1, offvalue=0, command=fSoda500ml,font=('arial',18,'bold'),\
                                ).grid(row=2, sticky=W)
                Mango_Juice_60=Checkbutton(third_frame, text="Mango Juice 60", variable=Var49, onvalue=1, offvalue=0, command=fMangoJuice60,font=('arial',18,'bold'),\
                                ).grid(row=3, sticky=W)
                Mango_Juice_100=Checkbutton(third_frame, text="Mango Juice 100", variable=Var50, onvalue=1, offvalue=0, command=fMangoJuice100,font=('arial',18,'bold'),\
                                ).grid(row=4, sticky=W)
                Passion_Juice_60=Checkbutton(third_frame, text="Passion Juice 60", variable=Var51, onvalue=1, offvalue=0, command=fPassionJuice60,font=('arial',18,'bold'),\
                                ).grid(row=5, sticky=W)
                Passion_Juice_100=Checkbutton(third_frame, text="Passion Juice 100", variable=Var52, onvalue=1, offvalue=0, command=fPassionJuice100,font=('arial',18,'bold'),\
                                ).grid(row=6, sticky=W)
                Beetroot_Juice_60=Checkbutton(third_frame, text="Beetroot Juice 60", variable=Var53, onvalue=1, offvalue=0, command=fBeetrootJuice60,font=('arial',18,'bold'),\
                                ).grid(row=7, sticky=W)
                Beetroot_Juice_100=Checkbutton(third_frame, text="Beetroot Juice 100", variable=Var54, onvalue=1, offvalue=0, command=fBeetrootJuice100,font=('arial',18,'bold'),\
                                ).grid(row=8, sticky=W)
                Minute_Maid_400ml=Checkbutton(third_frame, text="Minute Maid 400ml", variable=Var55, onvalue=1, offvalue=0, command=fMinuteMaid400ml,font=('arial',18,'bold'),\
                                ).grid(row=9, sticky=W)
                Minute_Maid_1L=Checkbutton(third_frame, text="Minute Maid 1L", variable=Var56, onvalue=1, offvalue=0, command=fMinuteMaid1L,font=('arial',18,'bold'),\
                                ).grid(row=10, sticky=W)
                Dasani_1_2L=Checkbutton(third_frame, text="Dasani 1/2L", variable=Var57, onvalue=1, offvalue=0, command=fDasani1_2L,font=('arial',18,'bold'),\
                                ).grid(row=11, sticky=W)
                Dasani_1L=Checkbutton(third_frame, text="Dasani 1L", variable=Var58, onvalue=1, offvalue=0, command=fDasani1L,font=('arial',18,'bold'),\
                                ).grid(row=12, sticky=W)
                Fresh_Milk_Glass=Checkbutton(third_frame, text="Fresh Milk Glass", variable=Var59, onvalue=1, offvalue=0, command=fFreshMilkGlass,font=('arial',18,'bold'),\
                                ).grid(row=13, sticky=W)
                Mala=Checkbutton(third_frame, text="Mala", variable=Var60, onvalue=1, offvalue=0, command=fMala,font=('arial',18,'bold'),\
                                ).grid(row=14, sticky=W)

                #==============================ENTRY FOR DRINKS=============================================================================
                txtSoda_300ml=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Soda_300ml)
                txtSoda_300ml.grid(row=1, column=1)

                txtSoda_500ml=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Soda_500ml)
                txtSoda_500ml.grid(row=2, column=1)

                txtMango_Juice_60=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mango_Juice_60)
                txtMango_Juice_60.grid(row=3, column=1)

                txtMango_Juice_100=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Mango_Juice_100)
                txtMango_Juice_100.grid(row=4, column=1)

                txtPassion_Juice_60=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Passion_Juice_60)
                txtPassion_Juice_60.grid(row=5, column=1)

                txtPassion_Juice_100=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Passion_Juice_100)
                txtPassion_Juice_100.grid(row=6, column=1)

                txtBeetroot_Juice_60=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Beetroot_Juice_60)
                txtBeetroot_Juice_60.grid(row=7, column=1)

                txtBeetroot_Juice_100=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Beetroot_Juice_100)
                txtBeetroot_Juice_100.grid(row=8, column=1)

                txtMinute_Maid_400ml=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Minute_Maid_400ml)
                txtMinute_Maid_400ml.grid(row=9, column=1)

                txtMinute_Maid_1L=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Minute_Maid_1L)
                txtMinute_Maid_1L.grid(row=10, column=1)

                txtDasani_1_2L=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Dasani_1_2L)
                txtDasani_1_2L.grid(row=11, column=1)

                txtDasani_1L=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED,textvariable=E_Dasani_1L)
                txtDasani_1L.grid(row=12, column=1)

                txtFresh_Milk_Glass=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Fresh_Milk_Glass)
                txtFresh_Milk_Glass.grid(row=13, column=1)

                txtMala=Entry(third_frame,font=('arial',16,'bold'), bd=8, width=6, justify='left',state=DISABLED, textvariable=E_Mala)
                txtMala.grid(row=14, column=1)


                #===================================Total Functions======================================================













                #===================================Receipt Window==========================================================================
                def iReceipt():
                        top = Toplevel()
                        top.title("Receipt")
                        txtreceipt_F = Frame(top, bg='Powder Blue', bd=10, relief=RIDGE)
                        txtreceipt_F.pack(side=LEFT,anchor='n',expand=1,fill=BOTH)
                        txtreceipt_C = Canvas(txtreceipt_F)
                        txtreceipt_C.pack(side=LEFT, fill=BOTH,expand=1)
                        receipt_scrollbar = ttk.Scrollbar(txtreceipt_F, orient=VERTICAL, command=txtreceipt_C.yview)
                        receipt_scrollbar.pack(side= RIGHT,fill=Y)
                        txtreceipt_C.configure(yscrollcommand= receipt_scrollbar.set)
                        txtreceipt_C.bind('<Configure>', lambda e:txtreceipt_C.configure(scrollregion=txtreceipt_C.bbox("all")))
                        receipt_F = Frame(txtreceipt_C)
                        txtreceipt_C.create_window((0,0), window=receipt_F)

                        rbuttons_F=Frame(top,height=1,width=67)
                        rbuttons_F.pack(side=BOTTOM)


                                

                        txtReceipt=Text(receipt_F, font=('arial', 12,'bold'),bd=3,bg="#c69c6d", width=42, height=14)
                        txtReceipt.grid(row=0,column=0)

                        txtReceipt.delete(1.0,END)

                        x=random.randint(100,10000)
                        bill_numbers='Bill'+str(x)
                        date=time.strftime('%d/%m/%y')
                        
                        txtReceipt.insert(END,'Receipt Ref:\t\t '+bill_numbers+'\t\t'+date+'\n')
                        txtReceipt.insert(END,'**************************************************************\n')
                        txtReceipt.insert(END,'Items:\t\t '+'Cost Of Item(Ksh)\n')
                        txtReceipt.insert(END,'**************************************************************\n')
                        if E_Tea.get()!='0':
                                txtReceipt.insert(END,F'Tea \t\t\t{int(E_Tea.get())*30}\n\n')
                        if E_Tea_Masala.get()!='0':
                                txtReceipt.insert(END,F'Tea Masala \t\t\t{int(E_Tea_Masala.get())*50}\n\n')
                        if E_Black_Tea.get()!='0':
                                txtReceipt.insert(END,F'Black Tea \t\t\t{int(E_Black_Tea.get())*30}\n\n')
                        if E_White_Coffee.get()!='0':
                                txtReceipt.insert(END,F'White Coffee \t\t\t{int(E_White_Coffee.get())*60}\n\n')
                        if E_Black_Coffee.get()!='0':
                                txtReceipt.insert(END,F'Black Coffee \t\t\t{int(E_Black_Coffee.get())*40}\n\n')
                        if E_Special_Tea.get()!='0':
                                txtReceipt.insert(END,F'Special Tea \t\t\t{int(E_Special_Tea.get())*60}\n\n')
                        if E_Chapati_Brown.get()!='0':
                                txtReceipt.insert(END,F'Chapati Brown \t\t\t{int(E_Chapati_Brown.get())*20}\n\n')
                        if E_Chapati.get()!='0':
                                txtReceipt.insert(END,F'Chapati \t\t\t{int(E_Chapati.get())*20}\n\n')
                        if E_Andazi.get()!='0':
                                txtReceipt.insert(END,F'Andazi \t\t\t{int(E_Andazi.get())*10}\n\n')
                        if E_Mahamri.get()!='0':
                                txtReceipt.insert(END,F'Mahamri \t\t\t{int(E_Mahamri.get())*5}\n\n')
                        if E_Sausage.get()!='0':
                                txtReceipt.insert(END,F'Sausage \t\t\t{int(E_Sausage.get())*40}\n\n')
                        if E_Smokie.get()!='0':
                                txtReceipt.insert(END,F'Smokie \t\t\t{int(E_Smokie.get())*25}\n\n')
                        if E_Boiled_Eggs.get()!='0':
                                txtReceipt.insert(END,F'Boiled Eggs \t\t\t{int(E_Boiled_Eggs.get())*25}\n\n')
                        if E_Spanish_Omllete.get()!='0':
                                txtReceipt.insert(END,F'Spanish Omllete \t\t\t{int(E_Spanish_Omllete.get())*100}\n\n')
                        if E_Scrambled_Eggs.get()!='0':
                                txtReceipt.insert(END,F'Scrambled Eggs \t\t\t{int(E_Scrambled_Eggs.get())*100}\n\n')
                        if E_Fried_Eggs.get()!='0':
                                txtReceipt.insert(END,F'Fried Eggs \t\t\t{int(E_Fried_Eggs.get())*60}\n\n')
                        if E_Macho_Egg.get()!='0':
                                txtReceipt.insert(END,F'Macho Egg \t\t\t{int(E_Macho_Egg.get())*100}\n\n')
                        if E_Half_Cake.get()!='0':
                                txtReceipt.insert(END,F'Half Cake \t\t\t{int(E_Half_Cake.get())*20}\n\n')
                        if E_Doughnut.get()!='0':
                                txtReceipt.insert(END,F'Doughnut \t\t\t{int(E_Doughnut.get())*20}\n\n')
                        if E_Samosa.get()!='0':
                                txtReceipt.insert(END,F'Samosa \t\t\t{int(E_Samosa.get())*30}\n\n')
                        if E_Chips.get()!='0':
                                txtReceipt.insert(END,F'Chips \t\t\t{int(E_Chips.get())*100}\n\n')
                        if E_Chips_Kuku.get()!='0':
                                txtReceipt.insert(END,F'Chips Kuku \t\t\t{int(E_Chips_Kuku.get())*250}\n\n')
                        if E_Stew_Kuku_Kienyeji.get()!='0':
                                txtReceipt.insert(END,F'Stew Kuku Kienyeji\t\t\t{int(E_Stew_Kuku_Kienyeji.get())*270}\n\n')
                        if E_Sima.get()!='0':
                                txtReceipt.insert(END,F'Sima \t\t\t{int(E_Sima.get())*30}\n\n')
                        if E_Brown_Ugali.get()!='0':
                                txtReceipt.insert(END,F'Brown Ugali \t\t\t{int(E_Brown_Ugali.get())*50}\n\n')
                        if E_Sima_Tilapia.get()!='0':
                                txtReceipt.insert(END,F'Sima Tilapia \t\t\t{int(E_Sima_Tilapia.get())*300}\n\n')
                        if E_Tilapia.get()!='0':
                                txtReceipt.insert(END,F'Tilapia \t\t\t{int(E_Tilapia.get())*270}\n\n')
                        if E_Beans.get()!='0':
                                txtReceipt.insert(END,F'Beans \t\t\t{int(E_Beans.get())*70}\n\n')
                        if E_Pojo.get()!='0':
                                txtReceipt.insert(END,F'Pojo \t\t\t{int(E_Pojo.get())*70}\n\n')
                        if E_Wali.get()!='0':
                                txtReceipt.insert(END,F'Wali \t\t\t{int(E_Wali.get())*80}\n\n')
                        if E_Mwangani_Saga.get()!='0':
                                txtReceipt.insert(END,F'Mwangani/Saga \t\t\t{int(E_Mwangani_Saga.get())*100}\n\n')
                        if E_Managu.get()!='0':
                                txtReceipt.insert(END,F'Managu \t\t\t{int(E_Managu.get())*100}\n\n')
                        if E_Matumbo.get()!='0':
                                txtReceipt.insert(END,F'Matumbo \t\t\t{int(E_Matumbo.get())*100}\n\n')
                        if E_Beef_Stew.get()!='0':
                                txtReceipt.insert(END,F'Beef Stew \t\t\t{int(E_Beef_Stew.get())*150}\n\n')
                        if E_Beef_Fry.get()!='0':
                                txtReceipt.insert(END,F'Beef Fry \t\t\t{int(E_Beef_Fry.get())*100}\n\n')
                        if E_Mchicha.get()!='0':
                                txtReceipt.insert(END,F'Mchicha \t\t\t{int(E_Mchicha.get())*70}\n\n')
                        if E_Skumawiki_Cabbage.get()!='0':
                                txtReceipt.insert(END,F'Skumawiki/Cabbage \t\t\t{int(E_Skumawiki_Cabbage.get())*50}\n\n')
                        if E_Mboga_Special.get()!='0':
                                txtReceipt.insert(END,F'Mboga Special \t\t\t{int(E_Mboga_Special.get())*150}\n\n')
                        if E_Pilau.get()!='0':
                                txtReceipt.insert(END,F'Pilau \t\t\t{int(E_Pilau.get())*150}\n\n')
                        if E_Nyama_Choma_1_4.get()!='0':
                                txtReceipt.insert(END,F'NyamaChoma 1/4 \t\t\t{int(E_Nyama_Choma_1_4.get())*150}\n\n')
                        if E_Omena.get()!='0':
                                txtReceipt.insert(END,F'Omena \t\t\t{int(E_Omena.get())*90}\n\n')
                        if E_Githeri.get()!='0':
                                txtReceipt.insert(END,F'Githeri \t\t\t{int(E_Githeri.get())*80}\n\n')
                        if E_Githeri_Special.get()!='0':
                                txtReceipt.insert(END,F'Githeri Special \t\t\t{int(E_Githeri_Special.get())*150}\n\n')
                        if E_Maini.get()!='0':
                                txtReceipt.insert(END,F'Maini \t\t\t{int(E_Maini.get())*150}\n\n')
                        if E_Matoke.get()!='0':
                                txtReceipt.insert(END,F'Matoke \t\t\t{int(E_Matoke.get())*150}\n\n')
                        if E_Bone_Soup.get()!='0':
                                txtReceipt.insert(END,F'BoneSoup \t\t\t{int(E_Bone_Soup.get())*140}\n\n')
                        if E_Soda_300ml.get()!='0':
                                txtReceipt.insert(END,F'Soda 500ml \t\t\t{int(E_Soda_300ml.get())*40}\n\n')
                        if E_Soda_500ml.get()!='0':
                                txtReceipt.insert(END,F'Soda 500ml \t\t\t{int(E_Soda_500ml.get())*70}\n\n')
                        if E_Mango_Juice_60.get()!='0':
                                txtReceipt.insert(END,F'MangoJuice 60 \t\t\t{int(E_Mango_Juice_60.get())*60}\n\n')
                        if E_Mango_Juice_100.get()!='0':
                                txtReceipt.insert(END,F'MangoJuice 100 \t\t\t{int(E_Mango_Juice_100.get())*100}\n\n')
                        if E_Passion_Juice_60.get()!='0':
                                txtReceipt.insert(END,F'PassionJuice 60 \t\t\t{int(E_Passion_Juice_60.get())*60}\n\n')
                        if E_Passion_Juice_100.get()!='0':
                                txtReceipt.insert(END,F'PassionJuice 100 \t\t\t{int(E_Passion_Juice_100.get())*100}\n\n')
                        if E_Beetroot_Juice_60.get()!='0':
                                txtReceipt.insert(END,F'BeetrootJuice 60 \t\t\t{int(E_Beetroot_Juice_60.get())*60}\n\n')
                        if E_Beetroot_Juice_100.get()!='0':
                                txtReceipt.insert(END,F'BeetrootJuice 100 \t\t\t{int(E_Beetroot_Juice_100.get())*100}\n\n')
                        if E_Minute_Maid_400ml.get()!='0':
                                txtReceipt.insert(END,F'MinuteMaid 400ml \t\t\t{int(E_Minute_Maid_400ml.get())*100}\n\n')
                        if E_Minute_Maid_1L.get()!='0':
                                txtReceipt.insert(END,F'MinuteMaid 1L \t\t\t{int(E_Minute_Maid_1L.get())*200}\n\n')
                        if E_Dasani_1_2L.get()!='0':
                                txtReceipt.insert(END,F'Dasani 1/2L \t\t\t{int(E_Dasani_1_2L.get())*50}\n\n')
                        if E_Dasani_1L.get()!='0':
                                txtReceipt.insert(END,F'Dasani 1L \t\t\t{int(E_Dasani_1L.get())*100}\n\n')
                        if E_Fresh_Milk_Glass.get()!='0':
                                txtReceipt.insert(END,F'Fresh Milk \t\t\t{int(E_Fresh_Milk_Glass.get())*70}\n\n')
                        if E_Mala.get()!='0':
                                txtReceipt.insert(END,F'Mala \t\t\t{int(E_Mala.get())*100}\n\n')
                        txtReceipt.insert(END,'**************************************************************\n')
                        txtReceipt.insert(END,f'Cost of Food\t\t\tksh{PriceOfFood}\n\n')
                        txtReceipt.insert(END,f'Cost of Drinks\t\t\tksh{PriceOfDrinks}\n\n')
                        txtReceipt.insert(END,f'Total\t\t\tksh{((PriceOfFood)+(PriceOfDrinks))}\n\n') 
                        txtReceipt.insert(END,f'Paid\t\t\tksh{pay1}\n\n')
                        txtReceipt.insert(END,f'Balance\t\t\tksh{balance}\n\n')


                #==================================Receipt Buttons================================================================
                        def isave(txt):
                                url=tempfile.mktemp('.txt')
                                open(url, 'w').write(txt)
                                os.startfile(url, 'print')


                                
                        
                        
                        
                        
                        btnsave=Button(rbuttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Print&Save", 
                                bg="Powder Blue",command=lambda:isave(txtReceipt.get('1.0', END)),cursor="hand2").grid(row=0, column=0,padx=28,pady=16)
                        







                        top.mainloop()







                #===================================Payment Information====================================================================================
                lblPaidTax = Label(payment_F,font=('arial',14,'bold'),text = "\tPaid \t",bg='Powder Blue',fg='Black')
                lblPaidTax.grid(row=0,column=1, sticky=W, padx=4)
                txtPaidTax=Entry(payment_F, insertwidth=2, bg='white', bd=7,font=('arial',14,'bold'), textvariable=PaidTax,justify=LEFT)
                txtPaidTax.grid(row=0, column=2)

                lblSubTotal = Label(payment_F,font=('arial',14,'bold'),text = "\tSub Total",bg='Powder Blue',fg='Black')
                lblSubTotal.grid(row=0,column=4, sticky=W, padx=4)
                txtSubTotal=Entry(payment_F, insertwidth=2, bg='white', bd=7,font=('arial',14,'bold'), textvariable=SubTotal,state='readonly',justify=LEFT)
                txtSubTotal.grid(row=0, column=5)

                lblTotalCost = Label(payment_F,font=('arial',14,'bold'),text = "\tBalance",bg='Powder Blue',fg='Black')
                lblTotalCost.grid(row=0,column=6, sticky=W, padx=4)
                txtTotalCost=Entry(payment_F, insertwidth=2, bg='white', bd=7,font=('arial',14,'bold'), textvariable=TotalCost,state='readonly',justify=LEFT)
                txtTotalCost.grid(row=0, column=7, padx=2)

                #============================================Buttons==================================================================================
                btnTotal=Button(buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Total", 
                        bg="Powder Blue", command=Balance,cursor="hand2").grid(row=0, column=0,padx=28,pady=16)
                btnSub_Total=Button(buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Sub Total", 
                        bg="Powder Blue",command=subtotalcost,cursor="hand2").grid(row=0, column=1,padx=28,pady=16)
                btnReceipt=Button(buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Receipt", 
                        bg="Powder Blue", command=iReceipt,cursor="hand2").grid(row=0, column=2, padx=28,pady=16)
                btnReset=Button(buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Reset", 
                        bg="Powder Blue", command = iReset,cursor="hand2").grid(row=0, column=3, padx=28, pady=16)
                btnExit=Button(buttons_F, padx=16, pady=1, bd=7, fg="black", font=('arial',16,'bold'), text="Exit", 
                        bg="Powder Blue", command = iExit,cursor="hand2").grid(row=0, column=4, padx=28,pady=16)

















root= Tk()
obj=RestaurantLogin(root)
root.mainloop()

