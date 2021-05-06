from tkinter import *
import mysql.connector


mindatabase=mysql.connector.connect(host='localhost', port=3306, user='Eksamenssjef ',
passwd='oblig2021', db='oblig2021')

def window_1():
    window1 = Toplevel()
    window1.title('Legge til/Endre/Slette')
    window1.geometry("300x400")
    window1.resizable(0,0)

    def window_3():

        hent_eksamen=mindatabase.cursor()
        hent_eksamen.execute('SELECT * FROM Student')


        def hent_eksame1(event):
            valgt=lst_eksamen.get(lst_eksamen.curselection())
           
            
            student.set(valgt[0])
            navn.set(valgt[1])
            etter.set(valgt[2])
            email.set(valgt[3])
            tel.set(valgt[4])
            

        def registrer():
            registrerr=mindatabase.cursor()

            studentnr=student.get()
            navnn=navn.get()
            ettern=etter.get()
            mail=email.get()
            tell=tel.get()
            studen=studentt.get()

            ny_student=("INSERT INTO Student"
                        "(Studentnr, Fornavn, Etternavn, Epost, Telefon)"
                        "VALUES(%s, %s, %s, %s, %s)")
            new_student=(studentnr, navnn, ettern, mail, tell)

            registrerr.execute(ny_student, new_student)
            mindatabase.commit()

            registrerr.close()

        def endre():
            endree=mindatabase.cursor()

            studentnr=student.get()
            navnn=navn.get()
            ettern=etter.get()
            mail=email.get()
            tell=tel.get()
            studen=studentt.get()

            ny_student=('''UPDATE Student
                        SET Fornavn=%s, Etternavn=%s, Epost=%s, Telefon=%s
                        WHERE Studentnr=%s''')
            new_student=(navnn, ettern, mail, tell, studentnr)

            endree.execute(ny_student, new_student)
            mindatabase.commit()

            endree.close()

        def delete():
            deletee=mindatabase.cursor()

            studentnr=student.get()
            navnn=navn.get()
            ettern=etter.get()
            mail=email.get()
            tell=tel.get()
            studen=studentt.get()

            del_student=('''DELETE FROM Student WHERE studentnr =%s''')
            del_student2 = (studentnr,)
                        

            deletee.execute(del_student, del_student2)
            mindatabase.commit()

            deletee.close()
            
                
                

            
            
            
            





        
        window3 = Toplevel()
        window3.title('Student')
        window3.geometry("1000x400")
        
        lbl_student=Label(window3, text=' Studentnr:')
        lbl_student.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_navn=Label(window3, text=' Navn:')
        lbl_navn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_etter=Label(window3, text=' Etternavn:')
        lbl_etter.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        lbl_email=Label(window3, text=' E-mail:')
        lbl_email.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        lbl_tel=Label(window3, text=' Telefonr:')
        lbl_tel.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        #lbl_studentt=Label(window3, text=' Søk på studentnr')
        #lbl_studentt.grid(row=0, column=4, padx=5, pady=5, sticky=E)

        

        #
        
        student=StringVar()
        ent_student=Entry(window3, width=6, textvariable=student)
        ent_student.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        navn=StringVar()
        ent_navn=Entry(window3, width=9, textvariable=navn)
        ent_navn.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        
        etter=StringVar()
        ent_etter=Entry(window3, width=20, textvariable=etter)
        ent_etter.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        email=StringVar()
        ent_email=Entry(window3, width=40, textvariable=email)
        ent_email.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        
        tel=StringVar()
        ent_telefon=Entry(window3, width=8, textvariable=tel)
        ent_telefon.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        #studentt=StringVar()
        #ent_studentt=Entry(window3, width=9, textvariable=studentt)
        #ent_studentt.grid(row=0, column=5, padx=5, pady=5, sticky=W)
        
        eksamen=[]
        for row in hent_eksamen:
            eksamen +=[row]

        y_scroll=Scrollbar(window3, orient=VERTICAL)
        y_scroll.grid(row=0,column=3,rowspan=10,padx=(0,5),pady=5,sticky=NS)

        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window3,width=60,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=2,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(eksamen))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_eksame1)
        

        
        btn_aa = Button(window3, text='Lagre', command=registrer)
        btn_aa.grid(row=2,column=4, padx=5, pady=5, sticky=W)

        btn_bb = Button(window3, text='Endre', command=endre)
        btn_bb.grid(row=3,column=4, padx=5, pady=5, sticky=W)

        btn_cc = Button(window3, text='Slette', command=delete)
        btn_cc.grid(row=4,column=4, padx=5, pady=5, sticky=W)

        

        

    def window_6():
        window6 = Toplevel()
        window6.title('Eksamen')
        window6.geometry("800x400")

        hent_eksamen=mindatabase.cursor()
        hent_eksamen.execute('SELECT * FROM Eksamen')




        def hent_eksame1(event):
            valgt=lst_eksamen.get(lst_eksamen.curselection())
           
            
            emne.set(valgt[0])
            dato.set(valgt[1])
            rom.set(valgt[2])
                    
                    
            


        def registrer():
            registrerr=mindatabase.cursor()

            emnee=emne.get()
            datoo=dato.get()
            romnr=rom.get()


            ny_emne=("INSERT INTO Eksamen"
                     "(Emnekode, Dato, Romnr)"
                        "VALUES(%s, %s, %s)")
            new_emne=(emnee, datoo, romnr)

            registrerr.execute(ny_emne, new_emne)
            mindatabase.commit()

            registrerr.close()




        def endre():
            valgt=lst_eksamen.get(lst_eksamen.curselection())
            endree=mindatabase.cursor()

            emnee=emne.get()
            datoo=dato.get()
            romnr=rom.get()
            gammel_dato=valgt[1]

            
            


            ny_emne=('''UPDATE Eksamen
                     SET romnr=%s
                     WHERE Emnekode=%s AND DATO=%s''')
            new_emne=(romnr, emnee, gammel_dato)

            endree.execute(ny_emne, new_emne)
            mindatabase.commit()

            endree.close()

        def delete():
            deletee=mindatabase.cursor()

            emnee=emne.get()
            datoo=dato.get()
            romnr=rom.get()
            

            del_eksamen=('''DELETE FROM Eksamen WHERE Emnekode=%s''')
            del_eksamen2 = (emnee,)
                        

            deletee.execute(del_eksamen, del_eksamen2)
            mindatabase.commit()

            deletee.close()


            

        

        lbl_emne=Label(window6, text=' Emnekode:')
        lbl_emne.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_dato=Label(window6, text=' Dato:')
        lbl_dato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_rom=Label(window6, text=' Romnr:')
        lbl_rom.grid(row=2, column=0, padx=5, pady=5, sticky=E)


        emne=StringVar()
        ent_emne=Entry(window6, width=8, textvariable=emne)
        ent_emne.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        dato=StringVar()
        ent_dato=Entry(window6, width=10, textvariable=dato)
        ent_dato.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        rom=StringVar()
        ent_etter=Entry(window6, width=3, textvariable=rom)
        ent_etter.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        eksamen=[]
        for row in hent_eksamen:
            eksamen +=[row]

        y_scroll=Scrollbar(window6, orient=VERTICAL)
        y_scroll.grid(row=0,column=2,rowspan=10,padx=(0,5),pady=5,sticky=NS)

        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window6,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(eksamen))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_eksame1)
        


        btn_aa = Button(window6, text='Lagre', command=registrer)
        btn_aa.grid(row=2,column=3, padx=5, pady=5, sticky=W)

        btn_bb = Button(window6, text='Endre', command=endre)
        btn_bb.grid(row=3,column=3, padx=5, pady=5, sticky=W)

        btn_cc = Button(window6, text='Slette', command=delete)
        btn_cc.grid(row=4,column=3, padx=5, pady=5, sticky=W)


        

            

        
    
    def window_5():
        window5 = Toplevel()
        window5.title('Eksamensresultat')
        window5.geometry("800x400")

        def hent_eksamen(event):
            valgt=lst_eksamen.get(lst_eksamen.curselection())
            student.set(valgt[0])
            emne.set(valgt[1])
            dato.set(valgt[2])
            karakter.set(valgt[3])
            
                    



            

        

        def registrer():
            registrerr=mindatabase.cursor()

            studentnr=student.get()
            emnee=emne.get()
            datoo=dato.get()
            karakterr=karakter.get()


            ny_eksamenr=("INSERT INTO Eksamensresultat"
                     "(Studentnr, Emnekode, Dato, Karakter)"
                        "VALUES(%s, %s, %s, %s)")
            new_eksamenr=(studentnr, emnee, datoo, karakterr)

            registrerr.execute(ny_eksamenr, new_eksamenr)
            mindatabase.commit()

            registrerr.close()

        def endre():
            valgt=lst_eksamen.get(lst_eksamen.curselection())
            endree=mindatabase.cursor()

            studentnr=student.get()
            emnee=emne.get()
            datoo=dato.get()
            karakterr=karakter.get()
            

            ny_eksamenr=('''UPDATE Eksamensresultat
                        SET Emnekode=%s, Dato=%s, Karakter=%s
                        WHERE Studentnr=%s''')
            new_eksamenr=(emnee, datoo, karakterr, studentnr)

            endree.execute(ny_eksamenr, new_eksamenr)
            mindatabase.commit()

            endree.close()

        def delete():
            deletee=mindatabase.cursor()

            studentnr=student.get()
            emnee=emne.get()
            datoo=dato.get()
            karakterr=karakter.get()

            
            del_eksamen=('''DELETE FROM Eksamensresultat WHERE studentnr =%s''')
            del_eksamen2 = (studentnr,)
                        

            deletee.execute(del_eksamen, del_eksamen2)
            mindatabase.commit()

            deletee.close()

        eksamen_cursor=mindatabase.cursor()
        eksamen_cursor.execute('SELECT * FROM Eksamensresultat ORDER BY DATO')

        eksamen=[]
        for row in eksamen_cursor:
            eksamen +=[row]

            

        lbl_student=Label(window5, text=' Studentnr:')
        lbl_student.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_emne=Label(window5, text=' Emnekode:')
        lbl_emne.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_dato=Label(window5, text=' Dato:')
        lbl_dato.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        lbl_karakter=Label(window5, text=' Karakter:')
        lbl_karakter.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        
        student=StringVar()
        ent_student=Entry(window5, width=6, textvariable=student)
        ent_student.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        emne=StringVar()
        ent_emne=Entry(window5, width=8, textvariable=emne)
        ent_emne.grid(row=1, column=1, padx=5, pady=5, sticky=W)
        dato=StringVar()
        ent_dato=Entry(window5, width=10, textvariable=dato)
        ent_dato.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        karakter=StringVar()
        ent_karakter=Entry(window5, width=2, textvariable=karakter)
        ent_karakter.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        y_scroll=Scrollbar(window5, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,5),pady=5,sticky=NS)
        
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window5,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(eksamen))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_eksamen)

        btn_aa = Button(window5, text='Lagre', command=registrer)
        btn_aa.grid(row=2,column=5, padx=5, pady=5, sticky=W)

        btn_bb = Button(window5, text='Endre', command=endre)
        btn_bb.grid(row=3,column=5, padx=5, pady=5, sticky=W)

        btn_cc = Button(window5, text='Slette', command=delete)
        btn_cc.grid(row=4,column=5, padx=5, pady=5, sticky=W)

    btn_next1 = Button(window1, text ='Student', command=window_3)
    btn_next1.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_next2 = Button(window1, text ='Eksamen', command=window_6)
    btn_next2.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    btn_next3 = Button(window1, text ='Eksamensresultat', command=window_5)
    btn_next3.grid(row=3,column=0,padx=5,pady=5,sticky=W)




    
    

    btn_back1 = Button(window1, text = 'Tilbake til hovedmeny', command = window1.destroy)
    btn_back1.grid(row=4, column=0, padx=5, pady=25, sticky=E)

def window_2():
    window2 = Toplevel()
    window2.title('Visning')

    def window_3():

        
        window3 = Toplevel()
        window3.title('Eksamen')
        window3.geometry("800x400")

        def hent_eksamen(event):
            valgt=lst_eksamen.get(lst_eksamen.curselection())

            hent_eksamenn=mindatabase.cursor()
            hent_eksamenn.execute('SELECT * FROM Eksamen')
            print(valgt[1])

            liste=[]
            for row in hent_eksamenn:
                liste += [row]
            
            for row in liste:
                print(row[1])
                if str(valgt[1]) == str(row[1]):
                    emne.set(row[0])
                    emne_kode.set(row[1])
                    rom.set(row[2])
                    
            hent_eksamenn.close()
                    








            

        eksamen_cursor=mindatabase.cursor()
        eksamen_cursor.execute('SELECT * FROM Eksamen ORDER BY DATO')

        eksamen=[]
        for row in eksamen_cursor:
            eksamen +=[row]

            

        lbl_sort=Label(window3, text=' Sortering etter dato:')
        lbl_sort.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_emne=Label(window3, text=' Emne:')
        lbl_emne.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_emne_kode=Label(window3, text=' Dato:')
        lbl_emne_kode.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        lbl_rom=Label(window3, text=' Romnr:')
        lbl_rom.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        
        emne=StringVar()
        ent_emne=Entry(window3, width=8,state='readonly', text='tekst:', textvariable=emne)
        ent_emne.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        emne_kode=StringVar()
        ent_emne_kode=Entry(window3,width=10, state='readonly', text='tekst:', textvariable=emne_kode)
        ent_emne_kode.grid(row=2, column=1, padx=2, pady=2, sticky=W)
        rom=StringVar()
        ent_rom=Entry(window3,width=3, state='readonly', text='tekst:', textvariable=rom)
        ent_rom.grid(row=3, column=1, padx=2, pady=2, sticky=W)

        y_scroll=Scrollbar(window3, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)
        
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window3,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(eksamen))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_eksamen)
        
        

        

        

        

        


    def window_6():
        window6 = Toplevel()
        window6.title('Eksamensresultater')
        window6.geometry("800x400")


        def hent_eksamenresultat(event):
            valgt=lst_eksamen.get(lst_eksamen.curselection())

            hent_eksamenn=mindatabase.cursor()
            hent_eksamenn.execute('SELECT * FROM Eksamensresultat')
            print(valgt[1])

            liste=[]
            for row in hent_eksamenn:
                liste += [row]
            print(len(liste))
            
            for row in liste:
                print(row[1])
                if str(valgt[0]) == str(row[0]):
                    studentnr.set(valgt[0])
                    emne_k.set(valgt[1])
                    datoo.set(valgt[2])
                    karakterr.set(valgt[3])
                    
            hent_eksamenn.close()
                    








            

        eksamen_cursor=mindatabase.cursor()
        eksamen_cursor.execute('SELECT * FROM Eksamensresultat ORDER BY Studentnr')

        eksamen=[]
        for row in eksamen_cursor:
            eksamen +=[row]

        
        

        
    
        lbl_student=Label(window6, text=' Studentnr:')
        lbl_student.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_emne=Label(window6, text=' Emnekode:')
        lbl_emne.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_dato=Label(window6, text=' Dato:')
        lbl_dato.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        lbl_karakter=Label(window6, text=' Karakter:')
        lbl_karakter.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        

        
        studentnr=StringVar()
        ent_student=Entry(window6, width=6, textvariable=studentnr)
        ent_student.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        emne_k=StringVar()
        ent_emne=Entry(window6, width=8,state='readonly', text='tekst:', textvariable=emne_k)
        ent_emne.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        datoo=StringVar()
        ent_dato=Entry(window6, width=10,state='readonly', text='tekst:', textvariable=datoo)
        ent_dato.grid(row=2, column=1, padx=2, pady=2, sticky=W)
        karakterr=StringVar()
        ent_karakter=Entry(window6, width=2,state='readonly', text='tekst:', textvariable=karakterr)
        ent_karakter.grid(row=3, column=1, padx=2, pady=2, sticky=W)
        #Sortering etter studentnr

        y_scroll=Scrollbar(window6, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)
        
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window6,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(eksamen))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_eksamenresultat)
        

        

        

        

        

        

        

    def window_5():
        window5 = Toplevel()
        window5.title('Karakterstatistikk')
        window5.geometry("800x400")
        eksamen_cursor=mindatabase.cursor()

        def hent_emne_kode(event):
            hent_emne=mindatabase.cursor()
            
            valgt=lst_eksamen.get(lst_eksamen.curselection())

            emnekode=valgt[0]
            dato=valgt[1]
            romnr=valgt[2]

            
            test = (emnekode,dato)
            

            
            #Visning av karakterstatistikk
            #a

            test_a=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='A'
                     ''')
            
            hent_emne.execute(test_a, test)

            kara=[]
            for row in hent_emne:
                kara += [row]

            data_a.set(len(kara))
            #b
            

            test_b=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='B'
                     ''')
            
            hent_emne.execute(test_b, test)

            karb=[]
            for row in hent_emne:
                karb += [row]

            data_b.set(len(karb))
            #c
            

            test_c=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='C'
                     ''')
            
            hent_emne.execute(test_c, test)

            karc=[]
            for row in hent_emne:
                karc += [row]

            data_c.set(len(karc))
            #d
            

            test_d=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='D'
                     ''')
            
            hent_emne.execute(test_d, test)

            kard=[]
            for row in hent_emne:
                kard += [row]

            data_d.set(len(kard))
            #e
            

            test_e=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='E'
                     ''')
            
            hent_emne.execute(test_e, test)

            kare=[]
            for row in hent_emne:
                kare += [row]

            data_e.set(len(kare))
            #f
            

            test_f=('''SELECT * FROM Eksamensresultat
                     WHERE Emnekode = %s AND Dato = %s AND Karakter ='F'
                     ''')
            
            hent_emne.execute(test_f, test)

            karf=[]
            for row in hent_emne:
                karf += [row]

            data_f.set(len(karf))





            
            

            
                      

            
            #hent_emne_kode=mindatabase.cursor()
            #hent_emne_kode.execute('SELECT Emnekode FROM Eksamen')
            #print(valgt[1])


           
                          
                           
        eksamen_cursor.execute('SELECT * FROM Eksamen ORDER BY SUBSTRING(emnekode,4)')                
        innhold=[]
        for row in eksamen_cursor:
            innhold += [row]
        #lbl_emne=Label(window5, text=' Oppgi emnekode:')
        #lbl_emne.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_aa=Label(window5, text=' Antall som fikk karakter A:')
        lbl_aa.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        lbl_ab=Label(window5, text=' Antall som fikk karakter B:')
        lbl_ab.grid(row=2, column=0, padx=5, pady=5, sticky=E)

        lbl_ac=Label(window5, text=' Antall som fikk karakter C:')
        lbl_ac.grid(row=3, column=0, padx=5, pady=5, sticky=E)

        lbl_ad=Label(window5, text=' Antall som fikk karakter D:')
        lbl_ad.grid(row=4, column=0, padx=5, pady=5, sticky=E)

        lbl_ae=Label(window5, text=' Antall som fikk karakter E:')
        lbl_ae.grid(row=5, column=0, padx=5, pady=5, sticky=E)

        lbl_af=Label(window5, text=' Antall som fikk karakter F:')
        lbl_af.grid(row=6, column=0, padx=5, pady=5, sticky=E)

        y_scroll=Scrollbar(window5, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)
        
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window5,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(innhold))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent_emne_kode)

        #ent_emne=Entry(window5, width=6, textvariable=emnekode)
        #ent_emne.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        data_a=StringVar()
        ent_aa=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_a)
        ent_aa.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        data_b=StringVar()
        ent_ab=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_b)
        ent_ab.grid(row=2, column=1, padx=2, pady=2, sticky=W)
        data_c=StringVar()
        ent_ac=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_c)
        ent_ac.grid(row=3, column=1, padx=2, pady=2, sticky=W)
        data_d=StringVar()
        ent_ad=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_d)
        ent_ad.grid(row=4, column=1, padx=2, pady=2, sticky=W)
        data_e=StringVar()
        ent_ae=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_e)
        ent_ae.grid(row=5, column=1, padx=2, pady=2, sticky=W)
        data_f=StringVar()
        ent_af=Entry(window5, width=2,state='readonly', text='tekst:', textvariable=data_f)
        ent_af.grid(row=6, column=1, padx=2, pady=2, sticky=W)


    
    

    btn_next1 = Button(window2, text ='Eksamen', command=window_3)
    btn_next1.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_next2 = Button(window2, text ='Eksamensresultater', command=window_6)
    btn_next2.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    btn_next3 = Button(window2, text ='Karakterstatistikk', command=window_5)
    btn_next3.grid(row=3,column=0,padx=5,pady=5,sticky=W)





    btn_back1 = Button(window2, text = 'Tilbake til hovedmeny', command = window2.destroy)
    btn_back1.grid(row=4, column=0, padx=5, pady=25, sticky=E)



    


def window_11():
    window11 = Toplevel()
    window11.title('Utskrift')

    def window_3():
        window3 = Toplevel()
        window3.title('Eksamensresultater')
        window3.geometry("800x400")

        def hent():
            hent=mindatabase.cursor()
            

            studentnr=student.get()

            hente = ('''SELECT * FROM Eksamensresultat
                     WHERE Studentnr = %s
                     ORDER BY Dato''')

            test = (studentnr,)

            hent.execute(hente, test)

            liste=[]
            for row in hent:
                liste += [row]

            innhold_i_lst_eksamen.set(tuple(liste))

            velg = (''' SELECT DISTINCT Emnekode, Studiepoeng
                        FROM Eksamensresultat JOIN Emne USING(Emnekode)
                        WHERE Studentnr = %s AND Karakter IS NOT NULL ''')
            hent.execute(velg, test)

            poeng = 0

            for row in hent:
                poeng += float(row[1])

            poengg.set(poeng)
            

            
        

        lbl_student=Label(window3, text=' Oppgi studentnr:')
        lbl_student.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_poeng=Label(window3, text=' Antall studiepoeng:')
        lbl_poeng.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        

        student=StringVar()
        ent_student=Entry(window3, width=9, textvariable=student)
        ent_student.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        poengg=StringVar()
        ent_poeng=Entry(window3, width=4,state='readonly', text='tekst:', textvariable=poengg)
        ent_poeng.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        sjekk=StringVar()
        btn_next1 = Button(window3, text ='Sjekk eksamen:', command=hent)
        btn_next1.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        

        y_scroll=Scrollbar(window3, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)
        liste=[]
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window3,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(liste))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent)
        




    

        

    def window_6():
        window6 = Toplevel()
        window6.title('Vitnemål')
        window6.geometry("800x400")

        def hent():
            hent=mindatabase.cursor()
            

            studentnr=student.get()

            test = (studentnr,)
            


            velg = (''' SELECT  Studentnr, Emnekode, min(Karakter)                        
                        FROM Eksamensresultat                        
                        WHERE Studentnr = %s AND Karakter <= 'F'                        
                        GROUP BY Emnekode                            
                        ORDER BY SUBSTRING(emnekode,4)''')
            hent.execute(velg, test)
            liste=[]
            for row in hent:
                liste += [row]
            innhold_i_lst_eksamen.set(tuple(liste))
            

            
            velgg = (''' SELECT DISTINCT Emnekode, Studiepoeng
                        FROM Eksamensresultat JOIN Emne USING(Emnekode)
                        WHERE Studentnr = %s AND Karakter IS NOT NULL ''')
            hent.execute(velgg, test)

            poeng = 0

            for row in hent:
                poeng += float(row[1])

            poengg.set(poeng)         

            
        

        lbl_student=Label(window6, text=' Oppgi studentnr:')
        lbl_student.grid(row=0, column=0, padx=5, pady=5, sticky=E)

        lbl_poeng=Label(window6, text=' Antall studiepoeng:')
        lbl_poeng.grid(row=1, column=0, padx=5, pady=5, sticky=E)

        

        student=StringVar()
        ent_student=Entry(window6, width=9, textvariable=student)
        ent_student.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        poengg=StringVar()
        ent_poeng=Entry(window6, width=4,state='readonly', text='tekst:', textvariable=poengg)
        ent_poeng.grid(row=1, column=1, padx=2, pady=2, sticky=W)
        sjekk=StringVar()
        btn_next1 = Button(window6, text ='Sjekk vitnemål:', command=hent)
        btn_next1.grid(row=2,column=1,padx=5,pady=5,sticky=W)


        

        y_scroll=Scrollbar(window6, orient=VERTICAL)
        y_scroll.grid(row=2,column=4,rowspan=10,padx=(0,100),pady=5,sticky=NS)
        liste=[]
        innhold_i_lst_eksamen=StringVar()
        lst_eksamen=Listbox(window6,width=50,height=10,listvariable=innhold_i_lst_eksamen,yscrollcommand=y_scroll.set)
        lst_eksamen.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
        innhold_i_lst_eksamen.set(tuple(liste))
        y_scroll["command"]=lst_eksamen.yview
        lst_eksamen.bind("<<ListboxSelect>>",hent)
        

        

        

        

        



        


    btn_next1 = Button(window11, text ='Eksamensresultater', command=window_3)
    btn_next1.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btn_next2 = Button(window11, text ='Vitnemål', command=window_6)
    btn_next2.grid(row=2,column=0,padx=5,pady=5,sticky=W)


    

    btn_back22 = Button(window11, text = 'Tilbake til hovedmeny', command = window11.destroy)
    btn_back22.grid(row=3, column=0, padx=5, pady=25, sticky=E)

    



    


def main():
    main_window = Tk()
    main_window.title('Hovedvindu - meny')
    main_window.geometry("300x400")
    main_window.resizable(0,0)
    
    #knapp for å åpne vindu 1
    btn_window1 = Button(main_window, text ='Legge til/Endre/Slette', command=window_1)
    btn_window1.grid(row=0,column=0,padx=5,pady=5,sticky=W)

    

    #knapp for å åpne vindu 2
    btn_window2 = Button(main_window, text ='Visning', command=window_2)
    btn_window2.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    #knapp for å åpne vindu 3
    btn_window11 = Button(main_window, text ='Utskrift', command=window_11)
    btn_window11.grid(row=2,column=0,padx=5,pady=5,sticky=W)


    

main()


