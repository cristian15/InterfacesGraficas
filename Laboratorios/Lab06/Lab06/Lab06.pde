/*# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Recibe por serial datos de un joystick para mover el mouse
# -------------------------------------------------*/
import processing.serial.*;
import java.awt.*;
Serial ser;

Google google;

void setup()
{
  String com = Serial.list()[0];
  ser = new Serial(this, com, 2400);
  
  google = new Google();
  
}

void draw()
{
  String recibido, X="0", Y="0";
  try
  {
    while (ser.available()>0)
    {
          recibido = ser.readString();          
          
          String[] recv = recibido.split(" ");
          
          if(recibido != null)
          {
            if (recv.length > 1)
            {
              X = recv[0];
              Y = recv[1];
            }
            else
            { 
              println(recv[0]);
              if(recv[0].equals("START"))
                google.press(32);    // presiona SPACE
              if(recv[0].equals("L1"))
                google.press(33); // Re Pag (Acelera)
                google.press(33); // Re Pag (Acelera)
              if(recv[0].equals("R1"))
                google.press(34); // Re Pag (Frena)
            }
            println( recv);
            //println(recibido  );
               
            google.move(Float.parseFloat(X), Float.parseFloat(Y));
          }
    }
  }
  catch (Exception e)
  {
    println(e);
  }  
}

class Google
{
  Robot miRobot;
  int centerX, centerY;
  Google()
  {
    try{
      miRobot = new Robot();
    }
    catch(AWTException e){
      println(e);
    }
    // setea valores del centro de la pantalla
    Dimension screen = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
    centerY = (int) screen.getHeight() / 2;
    centerX = (int) screen.getWidth() / 2;
  }
  void move(float x,float y)
  {
    miRobot.mouseMove(centerX + 10*(int)x, centerY + 10*(int)y); 
  }
  void press(int keys)
  {
    miRobot.keyPress(keys);
  }
}
