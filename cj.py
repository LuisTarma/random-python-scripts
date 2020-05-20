#Definicion de Montos de las cuentas
Monto_1 = 100000 #Cuenta Rut
Monto_2 = 200000 #Cuenta Corriente
Monto_3 = 300000 #Cuenta Vista

while 1==1: #Ciclo infinito, para el funcionamiento continuo del cajero

#Pantalla de bienvenida

 print 'CAJERO AUTOMATICO'.center(110, " ")
 j= raw_input('Presione ENTRAR para comenzar'.center(110, " "))
 if j == '':
  print 'Digite su clave'

#Definicion de variables importantes dentro de los ciclos y de la clave de usuario

 m= 0

 clave=2014

 conterr= 2

 cont=2

 c_ingresada=int(raw_input(""))

 while(cont>=1):    # Ingreso de clave
   
    if c_ingresada==clave:
        m = 1
        cont= cont = 0
       
    elif  c_ingresada != clave :
         print'Clave erronea. Intentos restantes:', conterr
         cont=cont-1
         c_ingresad = c_ingresada = int(raw_input(""))
         conterr= conterr - 1
         
         if cont == 0 and clave!=c_ingresada:
             print'Clave incorrecta. Exedio el numero de veces permitidas'
             print ''
             print ''
             print ''
             print ''
            
         if cont == 0  and clave==c_ingresada:
              m=1
             
###################################

 if m == 1:  # Si la clave es ingresada con exito Inprimira Bienvenido y comenzara el uso del cajero
  print 'Bienvenido'.center(110, " ")

  Operacion = 1 #Definimos operacion en 1 para que comience el funcionamiento
  while Operacion ==1 : # Comienzo de las operaciones del cajero
  
    if Monto_1 <0: #Advertencia en caso de que haya una deuda
     print 'Usted debe un total de',Monto_1 * (-1),'En la Cuenta Rut '
    if Monto_2 <0:
     print 'Usted debe un total de',Monto_2 * (-1),'En la Cuenta Corriente '
    if Monto_3 <0:
     print 'Usted debe un total de',Monto_3 * (-1),'En la Cuenta VISA ' 

# Seleccion de operacion
   
    print 'Seleccione la operacion a realizar'.center(110, " ")
    print 1,'    ', 'Consulta de saldo'
    print 2,'    ', 'Giro de dinero'
    print 3,'    ', 'Deposito de dinero'
    print 4,'    ', 'Transferencia'
    Operacion = Operacion = int(raw_input(''))
   
#Seleccion de Cuenta   
   
    print 'Estas son las cuentas a su nombre, porfavor seleccione una de ellas'.center(110, " ")
    print 1,'    ','Cuenta Rut'
    print 2,'    ','Cuenta Corriente'
    print 3,'    ','Cuenta VISA'
    Cuenta= int(raw_input(''))

###################################
   
# Consulta de Saldo
  
    if Operacion ==1: #Si la operacion es consulta de saldo
   
        if Cuenta ==1 :
            print 'Saldo disponible:  ','$',Monto_1
        elif Cuenta ==2:
            print 'Saldo disponible:  ','$',Monto_2
        elif Cuenta==3:
            print 'Saldo disponible:  ','$',Monto_3
       
####################################

# Giro de dinero

    if Operacion == 2: # Si la operacion es Giro
       
       print 'Seleccione el Monto a girar'.center(110, " ")
       print 1, '    ', '10 000','    ''    ''    ', 5,'    ', '70 000'
       print 2, '    ', '20 000','    ''    ''    ', 6,'    ', '80 000'
       print 3, '    ', '40 000','    ''    ''    ', 7,'    ', '100 000'
       print 4, '    ', '50 000','    ''    ''    ', 8,'    ', 'Otro Monto'
           
       Monto = int(raw_input(''))
      
       if Cuenta== 1:
         if Monto<=Monto_1:
            if Monto == 1:
             Monto_1 = Monto_1 - 10000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 2:
             Monto_1 = Monto_1 - 20000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 3:
             Monto_1 = Monto_1 - 40000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 4:
             Monto_1 = Monto_1 - 50000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 5:
             Monto_1 = Monto_1 - 70000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 6:
             Monto_1 = Monto_1 - 80000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 7:
             Monto_1 = Monto_1 - 100000
             print 'Nuevo Saldo Disponible:  ' , Monto_1
            elif Monto == 8:
             Otro_Monto = int(raw_input('Monto a retirar:   '))
             if Otro_Monto <= Monto_1:
               Monto_1 = Monto_1 - Otro_Monto
               print 'Su nuevo monto es: ', '$',Monto_1
             else:
                 print 'Saldo insuficiente'
         else:
           print'Saldo insuficiente'
       if Cuenta== 2:
         if Monto<=Monto_2:
            if Monto == 1:
             Monto_2 = Monto_2 - 10000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 2:
             Monto_2 = Monto_2 - 20000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 3:
             Monto_2 = Monto_2 - 40000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 4:
             Monto_2 = Monto_2 - 50000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 5:
             Monto_2 = Monto_2 - 70000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 6:
             Monto_2 = Monto_2 - 80000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 7:
             Monto_2 = Monto_2 - 100000
             print 'Nuevo Saldo Disponible:  ' , Monto_2
            elif Monto == 8:
             Otro_Monto = int(raw_input('Monto a retirar:   '))
             if Otro_Monto <= Monto_2:
               Monto_2 = Monto_2 - Otro_Monto
               print 'Su nuevo monto es: ','$', Monto_2
             else:
                 print 'Saldo insuficiente'
         else:
           print'Saldo insuficiente'
          
       if Cuenta== 3:
         if Monto<=Monto_3:       
            if Monto == 1:
             Monto_3 = Monto_3 - 10000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 2:
             Monto_3 = Monto_3 - 20000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 3:
             Monto_3 = Monto_3 - 40000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 4:
             Monto_3 = Monto_3 - 50000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 5:
             Monto_3 = Monto_3 - 70000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 6:
             Monto_3 = Monto_3 - 80000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 7:
             Monto_3 = Monto_3 - 100000
             print 'Nuevo Saldo Disponible:  ' , Monto_3
            elif Monto == 8:
             Otro_Monto = int(raw_input('Monto a retirar:   '))
             if Otro_Monto <= Monto_2:
               Monto_3 = Monto_3 - Otro_Monto
               print 'Su nuevo monto es: ', '$', Monto_3
             else:
                 print 'Saldo insuficiente'
         else:
           print'Saldo insuficiente'
       
#####################################
 
# Deposito de dinero
         
    if Operacion == 3: # Si la operacion es deposito
   
           
       Monto_Ingresado = int(raw_input('Monto Ingresado:            ')) #Ingresamos el monto a depositar
       if Cuenta== 1:
         
          Monto_1 = Monto_1 + Monto_Ingresado
          print 'Su nuevo monto es: ','$', Monto_1
       elif Cuenta== 2:
         
          Monto_2 = Monto_2 + Monto_Ingresado
          print 'Su nuevo monto es: ','$', Monto_2
       elif Cuenta== 3:
         
          Monto_3 = Monto_3 + Monto_Ingresado
          print 'Su nuevo monto es: ', '$', Monto_3          
#####################################

# Transferencia de dinero
         
    if Operacion == 4: # Si la operacion es transferencia
       
        if Cuenta==1: # Caso de la cuenta 1
           
            print 'Monto a transferir:'
            Transferencia = int(raw_input('')) # ingresamos el monto a transferir
            print 'Seleccione a cual de sus cuentas desea transferir el monto'
            print 1,'    ','Cuenta Corriente'
            print 2,'    ','Banco de Chile'
            Cuenta_Transferencia = int(raw_input(''))
            if Cuenta_Transferencia == 1:
              if Transferencia<=Monto_1:              
                Monto_1 = Monto_1 -  Transferencia
                Monto_2 = Monto_2 +  Transferencia
                print 'El saldo de su Cuenta Rut es ahora:  ' ,'$',Monto_1
                print 'El saldo de su Cuenta Corriente es ahora: ','$',Monto_2
              else:
                  print 'Saldo insuficiente'
            if Cuenta_Transferencia == 2:
              if Transferencia<=Monto_1:  
                Monto_1 = Monto_1 -  Transferencia
                Monto_3 = Monto_3 +  Transferencia
                print 'El saldo de su Cuenta Rut es ahora:  ' ,'$',Monto_1
                print 'El saldo de su Cuenta VISTA es ahora: ','$',Monto_3
              else:
                  print 'Saldo insuficiente'
       
        if Cuenta==2: # Caso de la cuenta 2
           
            print 'Monto a transferir:'
            Transferencia = int(raw_input(''))
            print 'Seleccione a cual de sus cuentas desea transferir el monto'
            print 1,'    ','Cuenta Rut'
            print 2,'    ','Cuenta VISTA'
            Cuenta_Transferencia = int(raw_input(''))
            if Cuenta_Transferencia == 1:
              if Transferencia<=Monto_2:  
                Monto_2 = Monto_2 -  Transferencia
                Monto_1 = Monto_1 +  Transferencia
                print 'El saldo de su Cuenta Corriente es ahora:  ' ,Monto_2
                print 'El saldo de su Cuenta Rut es ahora: ',Monto_1
              else:
                  print 'Saldo insuficiente'               
            if Cuenta_Transferencia == 2:
              if Transferencia<=Monto_2:  
                Monto_2 = Monto_2 -  Transferencia
                Monto_3 = Monto_3 +  Transferencia
                print 'El saldo de su Cuenta Corriente es ahora:  ' ,Monto_2
                print 'El saldo de su Cuenta VISTA es ahora: ',Monto_3
              else:
                  print 'Saldo insuficiente'
                 
        if Cuenta==3: #Caso de la cuenta 3
           
            print 'Monto a transferir:'
            Transferencia = int(raw_input(''))
            print 'Seleccione a cual de sus cuentas desea transferir el monto'
            print 1,'    ','Cuenta Rut'
            print 2,'    ','Cuenta Corriente'
            Cuenta_Transferencia = int(raw_input(''))
            if Cuenta_Transferencia == 1:
              if Transferencia<=Monto_3:  
                Monto_3 = Monto_3 -  Transferencia
                Monto_1 = Monto_1 +  Transferencia
                print 'El saldo de su cuenta Cuenta VISTA es ahora:  ' ,Monto_3
                print 'El saldo de su Cuenta Rut es ahora: ',Monto_1
              else:
                  print 'Saldo insuficiente'
            if Cuenta_Transferencia == 2:
              if Transferencia<=Monto_3:  
                Monto_3 = Monto_3 -  Transferencia
                Monto_2 = Monto_2 +  Transferencia
                print 'El saldo de su cuenta Cuenta VISTA es ahora:  ' ,Monto_3
                print 'El saldo de su Cuenta Corriente es ahora: ',Monto_2
              else:
                  print 'Saldo insuficiente'
                 
######################################

# Pregunta si desea otra operacion
 
    print 'Alguna otra operacion?'.center(110, " ")
    print 1,'    ', 'Si'
    print 2,'    ', 'No'
    Operacion = Operacion = int(raw_input('')) # Responde a la interrogante anterior
                                               #Si la respuesta es si, vuelve a preguntar la operacion
                                               #Sin cerrar la sesion
   
    if Operacion ==2: # Si no es asi finaliza la sesion
        print 'SESION FINALIZADA'.center(110, " ")
        print ''
        print ''
        print ''
        print ''
            
raw_input()
