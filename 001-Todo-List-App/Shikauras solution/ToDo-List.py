todo_list = []


def showlist():
    print(todo_list)


def addinlist():
    todo_list.append(input("Geben Sie die zu Hinzufügende Todo Sache ein!: "))
    print("Erfolgreich Hinzugefügt!")


def deletelist():
    todo_list.clear()
    print("Liste wurde gelöscht!")


def soos():
    print("Wähle eine andere Zahl!")


auswahl = 8

while auswahl == 8:
    print("-------------------------------------")
    print("Liste anzeigen (1)")
    print("Wert zur Liste hinzufügen (2)")
    print("Liste löschen (3)")
    print("Programm beenden (0)")
    print("-------------------------------------")
    auswahl = (int(input("Bitte wählen: ")))

    if 8 < auswahl:
        soos()
        auswahl -= auswahl - 8
    elif auswahl == 1:
        showlist()
        auswahl = 8
    elif auswahl == 2:
        addinlist()
        auswahl = 8
    elif auswahl == 3:
        deletelist()
        auswahl = 8
    elif auswahl == 0:
        print("Programm wird beendet!")
        quit()
