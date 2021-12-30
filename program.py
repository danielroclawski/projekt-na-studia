#from tkinter import *

#top = Tk()
#C = Canvas(top, bg="blue", height=1250, width=1300)
#filename = PhotoImage(file = "C:\\Users\\Daniel\\Downloads\\asd.png")
#background_label = Label(top, image = filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

#C.pack()
#C.mainloop()
#nazwa programu


#import biblioteki do wysyłania maili
from email import message
import smtplib

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

#tworzymy liste

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
    nowe_zadanie = input("podaj date nowego zadania oraz nazwę:    ")
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
    try:
        usun_zadanie = int(input("wybierz numer zadania które chcesz usunąć bo już je wykonałes. : "))
        lista_zadan.pop(usun_zadanie)
    except:
        print("wybierz poprawną opcje")

#kod menu 4 zapisz do pliku
def opcja4():
    print("zapisz do pliku")
    plik = open("zadania.txt", "w")
    for nowe_zadanie in lista_zadan:
        plik.write(nowe_zadanie+"\n")
    plik.close()

#otwieranie z zapisanego pliku
def otworz_plik():
    plik =open("zadania.txt")
    for line in plik.readlines():
        lista_zadan.append(line.strip())
    plik.close()
otworz_plik()

#kod menu 5 wyslij maila
def opcja5():
    print("wysyłanie maila")
    from email.mime.text import MIMEText
    from email.header import Header

    sender = "testpocztysmtp2@op.pl"
    password = "zaq1@WSX"
    receivers = 'samob90413@zherben.com'

    message = MIMEText('wiadomosc testowa', 'plain', 'utf-8')
    message['From'] = Header('test ten', 'utf-8')
    message['To'] = Header('test', 'utf-8')

    subject = 'Python SMTP test poczty'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL("smtp.poczta.onet.pl", 465) 
        smtpObj.login(sender, password)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("poczta wysłana pomyślnie")
    except smtplib.SMTPException as e:
        print("Error"+str(e))



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



