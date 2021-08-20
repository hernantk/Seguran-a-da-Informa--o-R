import os
import platform
from datetime import date, datetime, time

class IpScanner(object):

    def __init__(self):
        self.totalActive = 0
        self.totalInactive = 0
        self.totalIps = 0
        self.network = input("Informe o Ip de rede :")

    def breakNetwork(self):
        breakNetwork = self.network.split('.')
        self.network = breakNetwork[0]+'.'+ breakNetwork[1]+'.'+ breakNetwork[2]+'.'
        print(self.network)

    def requestRangeIp(self):
        self.start = int(input("Informe o valor inicial do Ip: "))
        self.end = int(input("Informe o valor final do Ip: "))+1
        
    def checkOperationSystem(self):
        systemOperation = platform.system()
        print(systemOperation)

        if(systemOperation == "Windows"):
            self.cmdPing = "ping -w 1ms -n 1 "
            self.ttl="TTL"
        else:
            self.cmdPing = "ping -t 1 -c 1 "
            self.ttl="ttl"

    def executeIpScanner(self):

        for ip in range(self.start,self.end):
            addressIp = self.network + str(ip)
            command = self.cmdPing + addressIp
            response = os.popen(command)
            self.totalIps+=1

            for lineResponde in response.readlines():
                if(lineResponde.count(self.ttl)):
                    self.totalActive+=1
                    print("IP " + addressIp + "---> Ativo")
                elif(lineResponde.count("Host") or lineResponde.count("Esgotado")):
                    self.totalInactive+=1
                    print("IP " + addressIp + "---> Inativo")

    def printResult(self,timeTotal):
        print("A varredura foi executada em --> " + str(timeTotal))
        print("Total de Ips: " + str(self.totalIps))
        print("Total de Ips Ativos: " + str(self.totalActive))
        print("Total de Ips Inativos: " + str(self.totalInactive))


    
    def execute(self):
        self.breakNetwork()
        self.requestRangeIp()
        self.checkOperationSystem()
        timeInit = datetime.now()
        self.executeIpScanner()
        timeEnd = datetime.now()
        timeTotal = timeEnd-timeInit
        self.printResult(timeTotal)


       
        


if __name__ == "__main__":
    IpScanner = IpScanner()
    IpScanner.execute()