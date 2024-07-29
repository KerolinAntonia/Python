def data(dia,mes,ano):
    m = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio",
6: "Junho", 7: "Julho", 8:"Agosto", 9: "Setembro", 10: "Outubro", 
11:"Novembro", 12: "Dezembro"}
    if mes in m:
        return print (dia,"de", m[mes], "de",ano)
    
(data(1,2,2000))