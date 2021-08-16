#PING - PROTOCOLO ICMP / TCP
#ICMP REQUEST ----> <---- ICMP RESPONSE
import os
#CERTO Resposta de 38.104.74.129: bytes=32 tempo=128ms TTL=249   
#ERRADO Esgotado o tempo limite do pedido. // +   

#ipEntrada = input("Insira o Ip da Rede: ")
#ipInicial = int(input("Insira o Ip Inicial"))
#ipFinal = int(input("Insira o Final"))

ipEntrada = "192.168.1.0"
ipInicial = 1
ipFinal = 255

listIpsNãoExistentes=[]
listIpsExistentes=[]


for i in range(ipInicial,ipFinal+1):
    ipLeitura = ipEntrada.replace("0",str(i))
    response = os.popen("ping -n 1 "+ipLeitura)
    if(response.readlines()[2]=="Esgotado o tempo limite do pedido."):
      listIpsNãoExistentes.append(ipLeitura)
      print("ops"+str(i))
    else:
       listIpsExistentes.append(ipLeitura)
       print("ok"+str(i))

for i in listIpsExistentes:
    print(i)

 
    
