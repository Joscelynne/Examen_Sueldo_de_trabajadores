import csv
import random



trabajadores = ["Juan Pérez" , "María García", "Carlos López", "Ana Martínez","Pedro Rodríguez", "Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
guardados=[]

#diez empleados con diez sueldos random del e $300.000 y $2.500.000


def menu_principal(): #menu principal del codigo
    while True:
        print('''
    1. Asignar sueldos aleatorios
    2. Clasificar sueldos
    3. Ver estadísticas.
    4. Reporte de sueldos
    5. Salir del programa
    ''')
        opc=input("elije una opcion: ")
        if opc.isnumeric(): #verificar que la opc sea correcta
            opc=int(opc)

        if opc==1:
            asignar_sueldos()
        elif opc==2:
            clasificar_sueldos()
        elif opc==3:
            estadisticas()
        elif opc==4:
            reporte_sueldos()
            print("Guardado exitosamente!")

        elif opc==5:
            salir_programa()
            break
        else:
            print("Solo numero. 1 al 5.")




def asignar_sueldos():
    for persona in trabajadores:
        sueldo=random.randint(300000, 2500000) #asignamos valores aleatorios del 300000 al 2500000
        guardados.append({"nombre": persona ,
                          "sueldos": sueldo}) #se guardan correspondientemente junto el nombre + su sueldo dado
        
    print("sueldo asignado!")



def clasificar_sueldos():
    menor=[]
    entre=[]
    superior=[] #se crean las listas para clasificarlo dependiendo sus valores
    
    for datos in guardados:

        sueldos=datos["sueldos"]
        if sueldos<800000: #si el sueldo es mayor a tal cantidad se guarda en menor
            menor.append(datos)
        elif sueldos>800000 and sueldos<2000000:  #si cumple ambas condiciones de estar entre tales numeros se guarda aqui
            entre.append(datos)
        else:
            superior.append(datos) #y lo restante que seria superior se guardaria aca


    print(f'''
    sueldos menores a $800.000 TOTAL ={len(menor)}
    nombres de los empleados        Sueldos 
    ''') #encabezado 
    for i in menor:
        print(i, sep="            ")#se imprime los datos de las listas correspondientes
          
    print(f'''
    sueldos entre $800.000 TOTAL={len(entre)}
    nombres de los empleados        Sueldos
        ''')  
    for j in entre:
        print(j, sep="            ")                      
    
    print(f'''Sueldos superiores a $2.000.000 TOTAL={len(superior)}
    nombre de los empleados          Sueldos''')
    for x in superior:
        print(x, sep="            ")   


def estadisticas():
    masalto=0
    masbajo=0
    todos_los_sueldos=[] #se crean las variables necesarias para usar a continuacion
    
    for sueldo in guardados: #reccorimos los sueldos guardados 
        todos_los_sueldos.append(sueldo) #esta lista nos serviria para guardar los sueldos para luego hacer la suma y sacar el promedio

        comprobacion=sueldo["sueldos"]

        if comprobacion>masalto: #recorre y comprueba si es mas alto q el numero ya guardado, si es mas grande entonces lo guarda
            masalto=comprobacion

        if comprobacion<masalto: #y si no, se guarda en la lista de mas bajo, y asi hasta que tome todos los numeros
            masbajo=comprobacion

    total=0
    for a in todos_los_sueldos:#aca se supone que haria la suma de todas los sueldos
        if a==todos_los_sueldos:

            total+=a

            

    cant_sueldos=10
    prom_sueldos=total/cant_sueldos  #se saca el promedio gracias a la formula dada

    sueldo_media_geometrica=1 #1
    for i in range(cant_sueldos): #recorre la cantidad d la lista para dependiendo cuantas hayan haga la formula
        sueldo_media_geometrica*=i

    media_geometrica_cant=(sueldo_media_geometrica)**1/cant_sueldos #aqui se supone que sacaba la media geometrica con la formula 


    valor_total_de_sueldos=total*cant_sueldos #y aca se supone que el total se multiplica con las cantidades de sueldo para saber cuanto seria el dinero en total
    
    print(f'''
          Sueldo mas alto: {masalto}
          Sueldo mas bajo:{masbajo}
          promedio de sueldos:{prom_sueldos}
          medida geometrica:{media_geometrica_cant}
          valor total de sueldos:{valor_total_de_sueldos}
          '''
          ) #te los imprime correspondiendo el valor
        
def reporte_sueldos():
    with open("Reporte_de_sueldos.csv", "w", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(["Nombre","Sueldo base", "Descuento Salud", "Descuento AFP", "Sueldo liquido"]) #creamos el csv, junto su encabezado 

        for datos in guardados:
            nombre=datos["nombre"] 
            sueldobase=datos["sueldos"]
            descuentosalud=sueldobase*0.07
            descuentoAFP=sueldobase*0.12
            sueldo_liquido=sueldobase-descuentosalud-descuentoAFP #sacamos los calculos para poder brindar la informacion necesaria de los descuento y el sueldo base y liquido
            
            writer.writerow([nombre,sueldobase, descuentosalud, descuentoAFP, sueldo_liquido])

def salir_programa():
    print('''
          Finalizando programa...
          Desarrollado por Joscelynne Joice Dìaz Z.
          RUT 21.959.939-0''') #despedida



menu_principal()

    

        








