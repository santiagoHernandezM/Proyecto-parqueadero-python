class Automovil:
    def __init__(self, id_automovil = None, placa = None, id_marca = None, id_modelo = None, id_color = None, estado = None, id_persona = None):
        self.id_automovil = id_automovil
        self.placa = placa
        self.id_marca = id_marca
        self.id_modelo = id_modelo
        self.id_color = id_color
        self.estado = estado
        self.id_persona = id_persona

    def get_id_automovil(self):
        return self.id_automovil
    
    def get_Placa(self):
        return self.placa
    
    def set_Placa(self, placa):
        self.placa = placa

    def get_Marca(self):
        return self.id_marca
    
    def get_Modelo(self):
        return self.id_modelo
    
    def get_Color(self):
        return self.id_color
    
    def get_Estado(self):
        return self.estado
    
    def set_Estado(self, estado):
        self.estado = estado

    def get_id_persona(self):
        return self.id_persona
    
    def set_id_persona(self, id_persona):
        self.id_persona = id_persona
#Prueba
# if __name__ == '__main__':
#     Automovil1 = Automovil()
#     Automovil1.set_id_automovil(201)
#     Automovil1.set_Placa("BHK 065")
#     Automovil1.set_Marca("BMW")
#     Automovil1.set_Modelo(2024)
#     Automovil1.set_Color("Dorado")
#     Automovil1.set_Estado("Activo")
#     Automovil1.set_id_persona(1067958612)
#     print(Automovil1.get_id_automovil())
#     print(Automovil1.get_Placa())
#     print(Automovil1.get_Marca())
#     print(Automovil1.get_Modelo())
#     print(Automovil1.get_Color())
#     print(Automovil1.get_Estado())
#     print(Automovil1.get_id_persona())
