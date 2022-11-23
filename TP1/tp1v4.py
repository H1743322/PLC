import re


def formataString(list):
    for l in range(len(list)):
        list[l] = list[l].strip()
        list[l] = list[l].strip('""')
    return list


def conversor(PathCsv, PathJson, separador):
    file = open(PathCsv, encoding='utf8')

    cabcalho = file.readline()
    cabcalho = re.split(separador, cabcalho.strip())
    # print(cabcalho)
    cabcalho = formataString(cabcalho)
    # print(cabcalho)

    json = ""
    json += "[\n"
    for line in file:

        dados = re.split(separador, line.strip())
        dados = formataString(dados)
        if len(dados) == len(cabcalho):
            json += "\t"+"{\n"
            # print(dados)
            for i in range(len(cabcalho)):
                #print(cabcalho[i], dados[i])
                funcao = re.search(
                    r'(\*(?i:max))|(\*(?i:min))|(\*(?i:avg))|(\*(?i:sum))|(\*)', cabcalho[i])
                if(funcao):
                    match = re.findall(r'\d+(?:\.\d+|)', dados[i])
                    #print(dados, match)
                    match = [float(x)for x in match]
                    # max
                    if(funcao.group(1) is not None):
                        dados[i] = max(match)
                    # min
                    elif(funcao.group(2) is not None):
                        dados[i] = min(match)
                    # sum
                    elif(funcao.group(3) is not None):
                        dados[i] = sum(match)/len(match)
                    # avg
                    elif(funcao.group(4) is not None):
                        dados[i] = sum(match)
                    # *
                    elif(funcao.group(5) is not None):
                        dados[i] = str(match)
                    json += ("\t\t"+'"' + cabcalho[i] +
                             "\": " + str(dados[i]) + ",\n")
                # se nao for numero ou for vazio tem de ter " "
                elif(re.search(r'[^(.\d)]', dados[i]) or dados[i] == ''):
                    json += ("\t\t"+'"' + cabcalho[i] +
                             "\": " + '"' + str(dados[i])+'"' + ",\n")

                # se for numero nao tem " "
                else:
                    json += ("\t\t"+'"' + cabcalho[i] +
                             "\": " + str(dados[i]) + ",\n")

            json += "\t"+"},\n"
    json += ("]")
    # tira as virgulas a mais
    json = re.sub(r',\n\t}', r'\n\t}', json)
    json = re.sub(r'},\n]', r'}\n]', json)

    fileOut = open(PathJson, 'w')
    fileOut.write(json)
    fileOut.close()
    file.close()
    return json


PathCsv = input('CSV: ')+".csv"
PathJson = input('JSON: ')+".json"

separador = input("Escolha o separador: ")
if(conversor(PathCsv, PathJson, separador)):
    print("Convertido ")
