#include <Servo.h>

//LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
// I HAVE TO CHANGE THE PINS NUMBER BUT I'M NOT SHURE ABOUT IT 
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int randNumber;

#define THUMB_PIN 5
#define THUMB_OPEN 10
#define THUMB_CLOSE 170



#define INDEX_PIN  6 
#define INDEX_OPEN 10
#define INDEX_CLOSE 170


#define MIDDLE_PIN 7
#define MIDDLE_OPEN 0
#define MIDDLE_CLOSE 170

#define RING_PIN 8
#define RING_OPEN 10
#define RING_CLOSE 170


#define PINKY_PIN 9/
#define PINKY_OPEN 10
#define PINKY_CLOSE 17


#define WRIST_PIN  10
#define WRIST_LEFT 170
#define WRIST_RIGHT 10


#define RELAX 70

#define BUTTON1_LED 38
#define BUTTON2_LED 40
#define BUTTON3_LED 42
#define BUTTON4_LED 44
#define BUTTON5_LED 46
#define BUTTON6_LED 48

#define BUTTON1_PIN 28
#define BUTTON2_PIN 30
#define BUTTON3_PIN 32
#define BUTTON4_PIN 34
#define BUTTON5_PIN 36



Servo t;
Servo i;
Servo m;
Servo r;
Servo p;
Servo r;
Servo w;
 

void setup() {
  // put your setup code here, to run once:

t.attach(THUMB_PIN);
i.attach(INDEX_PIN);
m.attach(MIDDLE_PIN);
r.attach(RING_PIN);
p.attach(PINKY_PIN);
w.attach(WRIST_PIN);

pinMode(BUTTON1_LED, OUTPUT);
pinMode(BUTTON2_LED, OUTPUT);
pinMode(BUTTON3_LED, OUTPUT);
pinMode(BUTTON4_LED, OUTPUT);
pinMode(BUTTON5_LED, OUTPUT);
pinMode(BUTTON6_LED, OUTPUT);

INPUT(BUTTON1_PIN);
INPUT(BUTTON2_PIN);
INPUT(BUTTON3_PIN);
INPUT(BUTTON4_PIN);
INPUT(BUTTON5_PIN);
INPUT(BUTTON6_PIN);

 lcd.print("Let's start .. ");
 delay(1000);
}


void loop() {
  // put your main code here, to run repeatedly:
  
}
void Victory_peace(){
 t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN);

 delay(2000);
}

void Thumbs_up(){
 t.write(THUMBS_OPEN);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN);

 delay(2000);
 
}
void count_numbers(){
 t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);

 delay(2000);
 
t.write(THUMB_OPEN);
delay(1000);
 i.write(INDEX_OPEN);
 delay(1000);
 m.write(MIDDLE_OPEN);
 delay(1000);
 r.write(RING_OPEN);
 delay(1000);
 p.write(PINKY_OPEN);
 
 delay(2000);
  
}
void shownumber1(){
 t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);

 delay(2000);
 
t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000)
}

void shownumber2(){
  t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN);
 
 delay(2000);
}
void shownumber3(){
  t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_CLOSE); 
 
 delay(2000);
}

  void shownumber4(){
    
  t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN); 
 
 delay(2000);
    
  }
  void shownumber5(){
    t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
 
t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN); 
 
 delay(2000);
  }
  void RelaxFingers(){
    t.write(RELAX);
    i.write(RELAX);
    m.write(RELAX)
    r.write(RELAX);
    p.write(RELAX); 
      
    delay(2000);
    
 t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN); 

 delay(2000);
  }
  void hello(){

 t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(2000);
  
 t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN); 
      
 delay(2000);
    
 w.write(WRIST_LEFT);
 delay(1000);
 w.write(WRIST_RIGHT);

 delay(2000);
 
  }
    

void bye(){
 t.write(THUMB_OPEN);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
 
 delay(1000);
  
 t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN ); 
      
 delay(2000);
    
}
void openhand(){
  t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN);
 
}
void closehand(){

 t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);
  
}
//Rock
void Rock{
   t.write(THUMB_CLOSE);
 i.write(INDEX_CLOSE);
 m.write(MIDDLE_CLOSE);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE); 
   }
  //paper
  void paper{
   t.write(THUMB_OPEN);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_OPEN);
 p.write(PINKY_OPEN);  

  }
  //scissors
  void scissors{
    t.write(THUMB_CLOSE);
 i.write(INDEX_OPEN);
 m.write(MIDDLE_OPEN);
 r.write(RING_CLOSE);
 p.write(PINKY_CLOSE);

  }

 void choose(int randNumber){
if (randNumber==1){
Rock();
delay(5000)
}
if (randNumber==2){
paper();
delay(5000)
if (randNumber==3){
scissors();
delay(5000)
}
}
void beginning(){
  digitalWrite(BUTTON1_LED, HIGH);
    delay(2000);
    digitalWrite(BUTTON1_LED, HIGH);
    delay(2000);
    digitalWrite(BUTTON1_LED, HIGH);
    delay(2000);
    
    digitalWrite(BUTTON1_LED, HIGH);
    digitalWrite(BUTTON1_LED, HIGH);
    digitalWrite(BUTTON1_LED, HIGH);
    
    int i=2;
    if(i<=0){
      Rock();
       delay(50000);
      paper();
       delay(5000);
      scissors();
       delay(5000);
     }
}
  void Rock_paper_scissors(){
    int i=0;
    beginning();
     randNumber = random(1,3);

     
     while (button is pressed or something){
choose(randNumber);
if (choose==1&& user_choose button1){
  i=i+1;
  lcd.print(i);
}
if (choose==1&&user_choose button2){
  i=i+1;
   lcd.print("Your Score ("+i+")");
}
if (choose==2&&user_choose button2){
  i=i+1;
  lcd.print("Your Score ("+i+")");
}
if (choose==2&& user_choose button3){
  i=i+1;
    lcd.print("Your Score ("+i+")");
}
if (choose==3&&user_choose button1){
  i=i+1;
  lcd.print("Your Score ("+i+")");
  }
if (choose==3&&user_choose button3){
  i=i+1;
  lcd.print("Your Score ("+i+")");
}
     }
   
      
  
  void Sequence(){}
    
  
}
//void close_index(){
 // o.write(140);
  //delay(2000);de
 // o.write(0);
 // delay(2000);
}
