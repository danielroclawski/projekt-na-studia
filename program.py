#from tkinter import *

#top = Tk()
#C = Canvas(top, bg="blue", height=1250, width=1300)
#filename = PhotoImage(file = "C:\\Users\\Daniel\\Downloads\\asd.png")
#background_label = Label(top, image = filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

#C.pack()
#C.mainloop()
#nazwa programu
print("program do rozdawania zadań")
print(end="\n"*4)

#lista dostępnych zadań
print("    lista dostępnych zadań")
print("------------------------------\n")
opcje_menu={
    1:'dodaj zadanie.',
    2:'pokaz zadania.',
    3:'usun wykonane zadanie',
    4:'zapisz zadania do pliku',
    5:'wyslij zadanie na maila',
    0:'wyjście\n',
    }

#tworzymy słownik

lista_zadan = [];

#wyswietlenie zadań
def pokaz_zadania():
    numer_zadania=0
    for x in lista_zadan:
        print(str(numer_zadania)+" "+x)
        numer_zadania+=1
def print_menu():
    for key in opcje_menu.keys():
        print (key, '--', opcje_menu[key] )

#kod do menu 1 "dodaj zadanie"
def opcja1():
    print("wybrales opcje dodaj zadanie.")
    print("przykład: DD.MM.YYYY HH:MM: nowe_zadanie")
    nowe_zadanie = input("podaj date nowego zadania oraz nazwę./n")
    print("\n")
    lista_zadan.append(nowe_zadanie)
    

#kod do meunu 2 "pokaz mije zadania"
def opcja2():
    pokaz_zadania()
    print(end="\n"*4)

#kod menu 3 usun zadanie
def opcja3():
    print("wybrałes opcje usuń zadanie.")
    pokaz_zadania()
    usun_zadanie = int(input("wybierz numer zadania które chcesz usunąć bo już je wykonałes. : "))
    lista_zadan.pop(usun_zadanie)

#kod menu 4 zapisz do pliku
def opcja4():
    print("opcja4")

#kod menu 5 wyslij maila
def opcja5():
    print("opcja5")



#pętla wybierająca wybór użytkownika
while(True):
    print_menu()
    opcja=' '
    try:
        opcja=int(input('wybierz co chcesz zrobić: '))
    except:
        print("wybierz poprawną opcje")
    if opcja == 1:
        opcja1()
    elif opcja == 2:
        opcja2()
    elif opcja == 3:
        opcja3()
    elif opcja == 4:
        opcja4()
    elif opcja == 5:
        opcja5()
    elif opcja == 0:
        print("koniec programu.")
        exit()

