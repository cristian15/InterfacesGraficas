/*# -----------------------------------------------
# ----- Nombre: Cristian Beltran Concha ---------
# ----- Prof: Luis Caro Saldivia ----------------
# ----- Asignatura: Interfaces Graficas de Usuario ----------
# -----------------------------------------------
# ----- Descripcion: Juego similar a Guitar Hero con Kinect
# -------------------------------------------------*/
import java.util.Random;
import ddf.minim.*;
import SimpleOpenNI.*;

// ---- KINECT ----- //
SimpleOpenNI context;
PImage img;
//------------------//

int HEIGHT = 700, WIDTH = 1000, delay, Puntaje, MargenXKin =0, MargenYKin = 0;
int nA = 200, Paso = 1;  // numero de flechas
Arrow[] a = new Arrow[nA];
Arrow[] b = new Arrow[nA];
String[] l = new String[5];
long tInicio, tNow;  // tiempos  ms

boolean[] keys;  // teclas presionadas
// ----- Audio --- //
AudioPlayer player;
Minim minim;
// --------------- //

void anotar() // Hace saber al usuario que anotó
{
  fill(255,255,0, 80);
  strokeWeight(2);
  rect((int)WIDTH/2 -250, HEIGHT-110, 500, 100, 3);  
}

void setup()
{
  // --------- Kinect ------ //
  context = new SimpleOpenNI(this);
  context.enableDepth();
  context.enableUser();
  context.enableRGB();
  context.setMirror(true);
  img = createImage(640,480,RGB);
  img.loadPixels();
  // -----------------------//
  
  size(WIDTH, HEIGHT);
  // -------------- Reproduce Musica ----------- //
  minim = new Minim(this);
  //player = minim.loadFile("MarioM.mp3", 2048);
  //player.play();
  // -------------------------------------------//
  keys = new boolean[4]; // las 4 flechas
  for(int i=0; i<4;i++)
    keys[i] = false;    // inicia todas las teclas No presionadas
  
  l[0] = "Left";
  l[1] = "Right";
  l[2] = "Up";
  l[3] = "Down";
  l[4] = "None";
  
  tInicio = System.currentTimeMillis();
  
  Puntaje = 0; 
  Random r = new Random();
  
  for(int i=0; i< nA; i++)
  {
     a[i] = new Arrow((int) WIDTH/2 - 220, 10 + i*-150, 100, l[r.nextInt(5)], false);      
     b[i] = new Arrow((int) WIDTH/2 + 130, 10 + i*-150, 100, l[r.nextInt(5)], false);   
  }  
  
}
void draw()
{  
  
  background(255);  
  
  /*/ ------------ Fondo Flechas --------//
  fill(50,100,255);
  strokeWeight(5);
  rect((int)WIDTH/2-5, 5, (int)WIDTH/2-5, HEIGHT-10, 5);
  // ------------------------------------ /*/
  // ------ Cuadro anotacion ----------- //
  fill(125,255,130);
  strokeWeight(2);
  rect((int)WIDTH/2-250, HEIGHT-110, 500, 100, 3);
  // ------------------------------------ //

  fill(0);
  textSize(50);
  text("Puntaje: "+String.valueOf(Puntaje), WIDTH/2 - 100, HEIGHT - 200);
  tint(255);
  PImage logo = loadImage("logo.png");
  image(logo, 200, 50);
  
  // --------- ----------------------- KINECT ----------------------------------------------------- //
  context.update();
  PImage depthImage = context.depthImage();
  depthImage.loadPixels();
  int[] upix = context.userMap();
  
  //colorize users
  for(int i=0; i < upix.length; i++){
    if(upix[i] > 0){
      //there is a user on that position
      //NOTE: if you need to distinguish between users, check the value of the upix[i]
      img.pixels[i]=color(0,0,255);
    }else{
      //add depth data to the image
     img.pixels[i]=depthImage.pixels[i];
    }
  }
  
  img.updatePixels();
  tint(255,127);  // Transparencia
  image(context.rgbImage(), MargenXKin, MargenYKin, WIDTH, HEIGHT);
  //image(img,MargenXKin,MargenYKin);
  //get array of IDs of all users present 
  int[] users=context.getUsers();
 
  ellipseMode(CENTER);
 
  //iterate through users
  for(int i=0; i < users.length; i++){
    
    int uid=users[i];
    
    //draw center of mass of the user (simple mean across position of all user pixels that corresponds to the given user)
    PVector realCoM=new PVector();
    
    //get the CoM in realworld (3D) coordinates
    context.getCoM(uid,realCoM);
    PVector projCoM=new PVector();
    
    context.convertRealWorldToProjective(realCoM, projCoM);
    fill(255,0,0);
    ellipse((MargenXKin+projCoM.x)*(1.6),(MargenYKin+projCoM.y)*(1.6),50,50);
 
    //check if user has a skeleton
    if(context.isTrackingSkeleton(uid)){
      //draw head
      PVector realHead=new PVector();
      // obtiene el vector de las coordendas reales de la cabeza
      context.getJointPositionSkeleton(uid,SimpleOpenNI.SKEL_HEAD,realHead);  
      PVector projHead=new PVector();
      context.convertRealWorldToProjective(realHead, projHead);   // convierte el vector a projective para utilizarlas en la ventana
      tint(255); 
      PImage cabeza = loadImage("head.png");     
      image(cabeza, (MargenXKin+projHead.x-50)*1.6, (MargenYKin+projHead.y-35)*1.6, 200,200 );
      
      // left hand
      PVector realLHand=new PVector();
      context.getJointPositionSkeleton(uid,SimpleOpenNI.SKEL_LEFT_HAND,realLHand);
      PVector projLHand=new PVector();
      context.convertRealWorldToProjective(realLHand, projLHand);
      fill(255,255,0);
      ellipse((MargenXKin+projLHand.x)*1.6,(MargenYKin+projLHand.y)*1.6,30,30);
       
       // Rigth hand
      PVector realRHand=new PVector();
      context.getJointPositionSkeleton(uid,SimpleOpenNI.SKEL_RIGHT_HAND,realRHand);
      PVector projRHand=new PVector();
      context.convertRealWorldToProjective(realRHand, projRHand);
      fill(125,255,200);
      ellipse((MargenXKin+projRHand.x)*1.6, (MargenYKin+projRHand.y)*1.6, 30,30);             
      
      
      // ------------------- Movimiento de Manos ---------------------------------- //
      
      if( (projRHand.x - projCoM.x) >= 100 && (projRHand.y - projCoM.y) < 20 && (projRHand.y - projCoM.y) > -100 )
      {
        println("Flecha Derecha");        
        keys[2] = true;
      }
      if( (projCoM.x - projLHand.x) >= 100 && (projLHand.y - projCoM.y) < 20 && (projLHand.y - projCoM.y) > -100 )
      {
        println("Flecha Izquierda");
        keys[0] = true;
      }
      if( (projCoM.y - projRHand.y) >= 100 && (projCoM.x - projRHand.x) < 100 && (projCoM.x - projRHand.x) > -100  )
      {
        println("Flecha Up");
        keys[1] = true;
      }
      if( (projCoM.y - projLHand.y) >= 100 && (projCoM.x - projLHand.x) < 100 && (projCoM.x - projLHand.x) > -100  )
      {
        println("Flecha Up");
        keys[1] = true;
      }
      if( (projRHand.y - projCoM.y) > 100 && (projCoM.x - projRHand.x) < 100 && (projCoM.x - projRHand.x) > -100)
      {
        println("flecha Down");
        keys[3] = true;
      }
      if( (projLHand.y - projCoM.y) > 100 && (projCoM.x - projLHand.x) < 100 && (projCoM.x - projLHand.x) > -100)
      {
        println("Flecha Down");
        keys[3] = true;
      }
      
      // ------------------------------ Fin Movimiento Manos ---------------------------------------------------- //
       //println(projRHand.x);
    }
    
  }
  // ---------FIN KINECT------------------- //
  for(int i=0; i< nA; i++)
  {
    a[i].move();
    a[i].display();   
    
    if(b[i].side == a[i].side)  // no repetir flechas 
    {
      b[i].side = "None";
    }    
    b[i].move();  
    b[i].display();  
    
    // -------------------  Puntuaciones ---------------------------------------- //
    if(a[i].y <= HEIGHT && a[i].y >= HEIGHT-120) // si esta en la zona de anotacion
      {        
        if(a[i].side.equals("Left")) // si la flecha izquierda esta en la zona 
        {
          if(keys[0])// si esta presionada flecha Izq
          {
            if(b[i].side.equals("Right") && keys[2]) 
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Up") && keys[1])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Down") && keys[3])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("None"))
            {
              if(!a[i].anotado && !b[i].anotado && !keys[1] && !keys[2] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
                anotar();
              }
                            
            }
          }
        }
        else if(a[i].side.equals("Right")) // si la flecha derecha esta en la zona 
        {
          if(keys[2])// si esta presionada flecha Derecha
          {
            if(b[i].side.equals("Left") && keys[0]) 
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
                
              }
              anotar();
            }
            else if(b[i].side.equals("Up") && keys[1])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Down") && keys[3])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("None"))
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[1] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
                anotar();
              }
            }
          }
        }
        
        else if(a[i].side.equals("Up")) // si la flecha Arriba esta en la zona 
        {
          if(keys[1])// si esta presionada flecha UP
          {
            if(b[i].side.equals("Right") && keys[2]) 
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Left") && keys[0])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Down") && keys[3])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("None"))
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[2] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
                anotar();
              }
            }
          }
        }
        if(a[i].side.equals("Down")) // si la flecha izquierda esta en la zona 
        {
          if(keys[3])// si esta presionada flecha Down
          {
            if(b[i].side.equals("Right") && keys[2]) 
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Up") && keys[1])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Left") && keys[0])
            {
              if(!a[i].anotado && !b[i].anotado)
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("None"))
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[1] && !keys[2])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
                anotar();
              }
            }
          }
        }
        if(a[i].side.equals("None")) // si la flecha izquierda esta en la zona 
        {        
            
            if(b[i].side.equals("Right") && keys[2]) 
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[1] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Left") && keys[0]) 
            {
              if(!a[i].anotado && !b[i].anotado && !keys[1] && !keys[2] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Up") && keys[1])
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[2] && !keys[3])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }
            else if(b[i].side.equals("Down") && keys[3])
            {
              if(!a[i].anotado && !b[i].anotado && !keys[0] && !keys[1] && !keys[2])
              {
                Puntaje+=30;
                a[i].anotado = true;
                b[i].anotado = true;
              }
              anotar();
            }  
                        
        }    
        // 
        // deja todas las flechas como no presionadas
         keys[0] = false; 
         keys[1] = false; 
         keys[2] = false; 
         keys[3] = false;  
         
      }
      
      //println(keys);
      
      // --------------  Fin Puntuaciones ------------------------- //   
  }
  
  // --------- Calcula tiempo transcurrido --------- //
  tNow = System.currentTimeMillis() - tInicio;
  tNow = tNow/1000;
  // ----------------------------------------------- //
 
 
 // ------------- Aumenta la velocidad de caida ------- //
  if (tNow > 7 && Paso < 30)
  {
    Paso += 1;   
    tInicio = System.currentTimeMillis();
        
  }
  // ----------------------------------------------- //
  //println(tNow);
  
} // fin draw

void keyPressed() // tecla presionada
{
  if(keyCode == 37) // Left
    keys[0]= true;
  if(keyCode == 38) // UP
    keys[1]= true;
  if(keyCode == 39) // Right
    keys[2]= true;
  if(keyCode == 40) // Down
    keys[3]= true;
} // fin keyPressed

void keyReleased()  // al soltar la tecla
{
  if(keyCode == 37) // Left
    keys[0]= false;
  if(keyCode == 38) // UP
    keys[1]= false;
  if(keyCode == 39) // Right
    keys[2]= false;
  if(keyCode == 40) // Down
    keys[3]= false;
    
} // Fin keyReleased

class Arrow
{
  int x, y, size;
  String side; 
  PImage img;
  boolean anotado;    
  
  Arrow(int ix, int iy,int isize, String iside, boolean ianotado)
  {
    x = ix;
    y = iy;
    size = isize;
    side = iside;   
    anotado = ianotado;
     // Imagen de la flecha a cargar 
    if(!side.equals("None")){
      if (side.equals("Left"))
      {
        img = loadImage("arrowL.png");
      }
      else if (side.equals("Right"))
      {
        img = loadImage("arrowR.png");
      }
      else if (side.equals("Up"))
      {
        img = loadImage("arrowU.png");
      }
      else if (side.equals("Down"))
      {
        img = loadImage("arrowD.png");
      }   
    } 
  }
  
  void display()
  {    
    if(!side.equals("None"))
    {
      image(img,x, y, size,size);  // muestra la flecha
    }
  }
  
  void move()
  {
    y += Paso;
  }
  
}

//is called everytime a new user appears
void onNewUser(SimpleOpenNI curContext, int userId)
{
  println("onNewUser - userId: " + userId);
  //asks OpenNI to start tracking a skeleton data for this user 
  //NOTE: you cannot request more than 2 skeletons at the same time due to the perfomance limitation
  //      so some user logic is necessary (e.g. only the closest user will have a skeleton)
  curContext.startTrackingSkeleton(userId);
}
 
//is called everytime a user disappears
void onLostUser(SimpleOpenNI curContext, int userId)
{
  println("onLostUser - userId: " + userId);
 
}

