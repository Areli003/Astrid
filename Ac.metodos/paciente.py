class Paciente:
    total_paciente = 0
    
    def __init__(self, nombre, edad, tipo_sangre):
        self.nombre = nombre
        self.edad = edad
        self.tipo_sangre = tipo_sangre
        self.temperatura = 36.5
        self.presion = '120/80'
        self.medicamentos = []
        self.hospitalizado = False
        self.citas = 0 
        
    def mostrar_expediente(self):
      print('=' * 30)
      print('  EXPEDIENTE DEL PACIENTE')
      print('nombre ', self.nonbre)
      print("Edad ", self.edad, 'años')
      print('Tipo de sangre ', self.tipo_sangre)
      print('Temperatura ', self.temperatura)
      print('Presion ', self.presion)
      print('Hospitalizado ', self.hospitalizado)
      print('Citas generadas ', self.citas)
      
      
      if len(self.medicamentos) == 0:
          print("medicamentos: sin medicamentos asignados")
      else:
          print("Medicamentos: ")
          for med in self.medicamentos:
           print(' - ', med)
      print('=' * 30)



paciente1 = Paciente("Astrid", 25, "O+")
paciente1.medicamentos.append("Paracetamol")
paciente1.hospitalizado = True
paciente1.citas = 3

paciente1.mostrar_expediente()