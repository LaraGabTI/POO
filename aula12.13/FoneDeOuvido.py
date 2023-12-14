class FoneDeOuvido:
    #sem o construtor "init"
    def get_volume(self): #mostra
        return self.__volume
    
    def set_volume(self, novo_volume):#mmuda
        self.__volume = novo_volume
    
    #serve pra usar o atributo sem ter que fazer a chamada do metodo
    volume = property(get_volume, set_volume) #temm que ter o get e o set

fone = FoneDeOuvido() #instancia de fone de ouvido
fone.volume = 200 #set
print(fone.volume) #get

