package cajeroautomatico;
import javax.swing.JOptionPane;
import java.util.Random;


public class CajeroAutomatico {

   
    public static void main(String[] args) {
        
        Random aleatorio = new Random(System.currentTimeMillis());
        aleatorio.setSeed(System.currentTimeMillis());
            //VARIABLES
            final int numCuenta = aleatorio.nextInt( 9999 );
            int saldo = aleatorio.nextInt( 1000000 );
            int cantIng;
            int numCuentaIng;
            int parMenu,parRetiro;
            boolean band = false;
            //char band2 = 'n' ;

    //Bienvenida
//JOptionPane.showMessageDialog( null , "Cajero BBVA\n¡Bienvenido!" );
//*Ingresar Numero de cuenta
numCuentaIng = Integer.parseInt(JOptionPane.showInputDialog( "Ingrese Su tarjeta  \n  \t\tNumero cuenta:  " + numCuenta));
if (numCuentaIng != numCuenta){
while (numCuentaIng != numCuenta){
    String numC = null;
numCuentaIng = Integer.parseInt(JOptionPane.showInputDialog( "\t\tNumero cuenta:  " +numC + "\n *¡Incorrecto!" + "\n\n-Digite su numero de cuenta: " ));
  }
}
//*Inicio de Cajero fase 2
JOptionPane.showMessageDialog( null , "   \n   Numero de cuenta correcto\n");







    do{
        //*Ingresar parametro del Menú
            parMenu = Integer.parseInt(JOptionPane.showInputDialog( "Menu Principal"
            + "\n\t 1 - Ver mi saldo"
            + "\n\t 2 - Retirar saldo"
                + "\n\t 3 - Depositar Saldo"
                + "\n\t  4 - Salir: " ));


        if ((parMenu < 0 )||(parMenu > 4 )){
                while ((parMenu < 0 )||(parMenu > 4 )){
                    parMenu = Integer.parseInt(JOptionPane.showInputDialog( "*Parametro incorrecto"
                      + "\n Menu Principal"
                        + "\n\t  1 - Ver mi saldo"
                            + "\n\t  2 - Retirar saldo"
                                + "\n\t  3 - Depositar Saldo"
                                    + "\n\t  4 - Salir: " ));
       }
}






      //*Inicio condicional switch con el parametro ParMenu
switch (parMenu){
    case 1 :
        //VER SALDO
        JOptionPane.showMessageDialog( null , "Ver Mi Saldo\n    Saldo:  " + saldo);
    break;
            case 2 :
                //RETIRAR SALDO
                JOptionPane.showMessageDialog( null , "Retirar Saldo" );
                    parRetiro = Integer.parseInt(JOptionPane.showInputDialog( "Opciones saldo:"
                        + "\n\t1 - 200.000\n2 - 40.0000"
                            + "\n\t3 - 600.000\n4 - 100.000"
                                + "\n\t5 - 2.000.0000\n6 - Cancelar" ));

        //*Comprobar parametro
            if ((parRetiro <= 0 )||(parRetiro > 6)){
               while((parRetiro <= 0 )||(parRetiro > 6)){
                    parRetiro = Integer.parseInt(JOptionPane.showInputDialog( "Opciones saldo:"
                    + "\n\t 1 - 200.000\n 2 - 400.0000"
                        + "\n\t 3 - 600.000\n 4 - 1.000.000"
                        + "\n\t5 - 2.000.0000\n6 - Cancelar" ));
                }   
        }






switch (parRetiro){
        case 1:
            if (saldo < 200.000 ){
                parRetiro = 6;
                System.out.println( "No tienes suficiente dinero" );
    }
        break;
    case 2:
            if (saldo< 400.0000 ){
                parRetiro = 6 ;
                System.out.println( "No tienes suficiente dinero" );
        }
            break;
              case 3:
                    if (saldo< 600.000 ){
                        parRetiro = 6 ;
                        System.out.println( "No tienes suficiente dinero" );
                }
                break;
                    case 4:
                        if (saldo< 1000.000 ){
                            parRetiro = 6 ;
                               System.out.println( "No tienes suficiente dinero" );
                    }
                    break;
                        case 5:
                            if (saldo< 2000.000 ){
                                  parRetiro = 6 ;
                                    System.out.println( "No tienes suficiente dinero" );
                    }
                    break;
}


switch (parRetiro){
   case 1: //20
      saldo -= 2000.000 ;
           JOptionPane.showMessageDialog( null , "Cant. retiro: 200.000 \nSaldo actual: " + saldo);
          break;
          case 2: //40
            saldo -= 400.000 ;
             JOptionPane.showMessageDialog( null , "Cant. retiro: 400.000 \nSaldo actual: " + saldo);
           break;
            case 3: //60
                 saldo -= 600.000 ;
                 JOptionPane.showMessageDialog( null , "Cant. retiro: 600.000   \nSaldo actual: " + saldo);
                break;
               case 4: //100
                   saldo -= 1000.000 ;
          {
          String sald = null;
       JOptionPane.showMessageDialog( null , "Cant. retiro: 1000.000\nSaldo actual:  " + sald);
           }
        break;
          case 5: //200
                  saldo -= 2000.000 ;
                   {
                            String sald = null;
                               JOptionPane.showMessageDialog( null , "Cant. retiro: 2000.000\nSaldo actual: " + sald);
                             }
                                  break;
                              case 6: //Cancelar
                                   System.out.println( "Cacelado." );
                                  break;
                        }
            }

//
char band2;
            band2 = JOptionPane.showInputDialog( null , "¿Deseas utilizar el programa otra vez?   \n   s / n:" ).charAt(0);
if ((band2 != 's' )&&(band2 != 'n' )){
     while ((band2 != 's' )&&(band2 != 'n' )){
         band2 = JOptionPane.showInputDialog( null ,"¿Deseas utilizar el programa otra vez?    \n  s / n" ).charAt(0);
 }
}
if (band2 == 's' ){
      band = true ;
   }
    else if (band2 == 'n' ){
        band = false ;
    }

} while(band == true );


    
   }
   
}

