import Data
def Queue(dict, list, j):
    image_address = Data.dict_of_ramka[list[j]]

    return image_address

def test_queue():
    dict = Data.dict_of_ramka
    list = Data.list_of_Notes
    j = 0
    assert  Queue(dict,list,j) == dict[list[j]]
def Tabela():
    file = open("Results", "r")
    dict = {}
    tablica_wynikow = []
    dict_ostateczny = {}
    for line in file:
        for i in range(0, len(line)):
            if line[i] == ":":
                nazwa = line[0:i]
                index = i
                i += 2
                for j in range(i, len(line)):
                    if line[j] == "\n":
                        wynik = line[index + 2:len(line) - 1]
                        dict[nazwa] = wynik
                        break

                break

    for i in dict.values():
        tablica_wynikow.append(int(i))
    while len(tablica_wynikow) != 0:
        max = tablica_wynikow[0]
        index = 0
        for i in range(0, len(tablica_wynikow)):
            if max < tablica_wynikow[i]:
                max = tablica_wynikow[i]
                index = i
        tablica_wynikow.pop(index)
        for i in dict:
            if dict[i] == str(max):
                dict_ostateczny[i] = max
    file.close()
    j = 1
    for i in dict_ostateczny:

        print(f"{j}.{i}: {dict_ostateczny[i]} pkt")
        j += 1
def Click(list, input, wyn ,j):
    if input == list[j]:
        return True
    else:
        return False

def test_Click():
    list = Data.list_of_Notes
    input = 0
    wyn = 0
    j = 0
    assert Click(list,input,wyn,j) == False
def test2_Click():
    list = Data.list_of_Notes
    j = 0
    input = list[j]
    wyn = 0

    assert Click(list,input,wyn,j) == True
    
def suma(a,b):
    return a + b
def test_suma():
    a = 2
    b = 4
    assert suma(a,b) == a + b


def iloczyn(a,b):
    return a * b
def test_iloczyn():
    a = 2
    b = 4
    assert iloczyn(a,b) == a * b
    

