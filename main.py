#-----------variaveis----------------
ListaDeMassa = []
ListaDeVolume = []
opcao = ""
#-----------funções----------------
def PegarMassaEVolume():
  print("Digite sua massa: ")    
  ListaDeMassa.append(float(input()))   
  print("Digite seu volume: ")  
  ListaDeVolume.append(float(input()))

def ListarMassaEVolumeEMedia():
  tamanho = len(ListaDeMassa)  
  for i in range(tamanho):      
    print("massa: ",ListaDeMassa[i])     
    print("volume: ",ListaDeVolume[i])    
    print("densidade: ",float(ListaDeMassa[i])/float(ListaDeVolume[i]))  
    print("----------------------")
  somaDasMassas = sum(ListaDeMassa)
  somaDosVolumes = sum(ListaDeVolume)
  numeroDeMassas = len(ListaDeMassa)
  numeroDeVolumes = len(ListaDeVolume)
  print("media das massas: ",somaDasMassas/numeroDeMassas)
  print("media dos volumes: ",somaDosVolumes/numeroDeVolumes)  
  print("media das densidades: ",(somaDasMassas/numeroDeMassas)/(somaDosVolumes/numeroDeVolumes))
#----------------Classe main----------------
while(opcao != "3"):
  print("-----------------------------------------------------")
  print("1 - Adcionar uma nova massa e volume")
  print("2 - ver as respectivas densidades e a media dos valores") 
  print("3 - Sair") 
  print("-----------------------------------------------------")  
  opcao = input()
  if(opcao == "1"):    
    PegarMassaEVolume()
  if(opcao == "2"):    
    ListarMassaEVolumeEMedia()
  if(opcao == "3"):   
    break
