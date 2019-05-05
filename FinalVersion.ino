#include <Servo.h>
//#include "if.h"



//#define victory_sign2()   t.write(THUMB_CLOSE);i.write(INDEX_OPEN);m.write(MIDDLE_OPEN);r.write(RING_CLOSE);p.write(PINKY_CLOSE)


unsigned long time , time_0, time_1, time_2, time_3, time_d, time_d_ ;

#define THUMB_PIN 5
#define THUMB_OPEN 160
#define THUMB_CLOSE 0

#define INDEX_PIN  6
#define INDEX_OPEN 0
#define INDEX_CLOSE 170

#define MIDDLE_PIN 7
#define MIDDLE_OPEN 170
#define MIDDLE_CLOSE 0
 
#define RING_PIN 8
#define RING_OPEN 10
#define RING_CLOSE 150

#define PINKY_PIN 9
#define PINKY_OPEN 170
#define PINKY_CLOSE 0

#define WRIST_PIN  4
#define WRIST_LEFT 140
#define WRIST_RIGHT 30
#define WRIST_CENTER 85

#define RELAX_A 0
#define RELAX 170

#define BUTTON1_LED 38
#define BUTTON2_LED 40
#define BUTTON3_LED 42
#define BUTTON4_LED 44
#define BUTTON5_LED 46
#define BUTTON6_LED 48

#define BUTTON1_PIN  22
#define BUTTON2_PIN  24
#define BUTTON3_PIN  26
#define BUTTON4_PIN  28
#define BUTTON5_PIN  30
#define BUTTON6_PIN  32



Servo t;
Servo i;
Servo m;
Servo r;
Servo p;
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

  pinMode(BUTTON1_PIN, INPUT_PULLUP);
  pinMode(BUTTON2_PIN, INPUT_PULLUP);
  pinMode(BUTTON3_PIN, INPUT_PULLUP);
  pinMode(BUTTON4_PIN, INPUT_PULLUP);
  pinMode(BUTTON5_PIN, INPUT_PULLUP);
  pinMode(BUTTON6_PIN, INPUT_PULLUP);

  //we have to keep it same in the RP AND ARDUINO
  Serial.begin(9600);
  randomSeed(analogRead(0));

}

void loop() {
  // put your main code here, to run repeatedly:

  if ( Serial.available() > 0 ) {
    char c = Serial.read();
    if (c == 'v') {
      Victory_peace();
      delay(2000);

      t.write(THUMB_CLOSE);
      i.write(INDEX_CLOSE);
      m.write(MIDDLE_CLOSE);
      r.write(RING_CLOSE);
      p.write(PINKY_CLOSE);

      delay(2000);
    }
    if (c == '1') {
      shownumber1();
    }
    if (c == '2') {
      shownumber2();
    }
    if (c == '3') {
      shownumber3();
    }
    if (c == '4') {
      shownumber4();
    }
    if (c == '5') {
      shownumber5();
    }
    if (c == 'w') {
      Wake_UP();
    }
    if (c == 'r') {
      
      RelaxFingers();
      delay(2000);
    }
    if (c == 'c') {
      count_numbers();
    }
    if (c == 't') {
      Thumbs_up();
    }
    if (c == 'h') {
      hello();
    }
    if (c == 'b') {
      bye();
    }
    if (c == 'l') {
      closehand();
    }
    if (c == 'o') {
      openhand();
    }
  //  if (c == 'p') {
//      Rock_paper_scissors();
    //}
    if (c == 's') {
      Play_Memory_Sequence();
    }

  }
}
void Victory_peace() {
  t.write(THUMB_CLOSE);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
}
void Wake_UP() {

  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);


  w.write(WRIST_CENTER);
  delay(2000);




}
void count_numbers() {



  i.write(INDEX_CLOSE);

  m.write(MIDDLE_CLOSE);

  r.write(RING_CLOSE);

  p.write(PINKY_CLOSE);

  t.write(THUMB_CLOSE);

  delay(700);



  t.write(THUMB_OPEN);

  delay(700);

  i.write(INDEX_OPEN);
  delay(700);


  m.write(MIDDLE_OPEN);

  delay(700);

  r.write(RING_OPEN);
  delay(700);


  p.write(PINKY_OPEN);
  delay(700);



  Serial.write('c');


}
void Thumbs_up() {

  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(700);
  t.write(THUMB_OPEN);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);

  delay(2000);

  t.write(THUMB_CLOSE);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
  w.write(WRIST_CENTER);
  delay(2000);
  ;


}
void shownumber1() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(500);


  i.write(INDEX_OPEN);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
  t.write(THUMB_CLOSE);


}

void shownumber2() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(500);

  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
  t.write(THUMB_CLOSE);
  delay(2000);
}
void shownumber3() {


  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(500);


  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_CLOSE);
  t.write(THUMB_CLOSE);
  delay(700);
}

void shownumber4() {

  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(500);


  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);
  t.write(THUMB_CLOSE);
  delay(2000);

}
void shownumber5() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(500);



}
void RelaxFingers() {
  t.write(RELAX);
  i.write(RELAX_A);
  m.write(RELAX_A);
  r.write(RELAX_A);
  p.write(RELAX);


}
void hello() {

  t.write(THUMB_OPEN);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);

  delay(700);

  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN );

  delay(2000);




  w.write(WRIST_LEFT);
  delay(1000);
  w.write(WRIST_RIGHT);

  delay(1000);


  t.write(THUMB_CLOSE);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
  w.write(WRIST_CENTER);
  delay(2000);
}


void bye() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

  delay(2000);


  w.write(WRIST_LEFT);
  delay(500);
  w.write(WRIST_RIGHT);
  delay(500);

  t.write(THUMB_CLOSE);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
  w.write(WRIST_CENTER);
  delay(2000);
}
void openhand() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);


}
void closehand() {

  t.write(THUMB_CLOSE);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);

}

int number_choose(int ch){
  if (ch==1){
  shownumber1(); 
  }
  if (ch==2){
   shownumber2();
  }
   if (ch==3){
   shownumber3();
  }
    if (ch==4){
   shownumber4();
  }
   if (ch==5){
   shownumber5();
  }
  return ch;
  
}
void Play_Memory_Sequence() {
  Serial.write('s');
//  while(result=='e'){
  digitalWrite(BUTTON6_LED, HIGH);


  while (digitalRead(BUTTON6_PIN) == 1) {}
 digitalWrite(BUTTON6_LED, LOW);
 
  digitalWrite(BUTTON1_LED, HIGH);
  digitalWrite(BUTTON2_LED, HIGH);
  digitalWrite(BUTTON3_LED, HIGH);
  digitalWrite(BUTTON4_LED, HIGH);
  digitalWrite(BUTTON5_LED, HIGH);

char Game = 'W';
 //how many numbers we have: and it change depend on the level.
 int l =3;
while(Game=='W' || l==8){
  int ch_a[ l];
for (int i = 0; i < l; i = i + 1) {
  ch_a[i]=number_choose(random(1, 6));
  delay(1500);
}
 while ((digitalRead(BUTTON1_PIN) == 1) && (digitalRead(BUTTON2_PIN) == 1) && (digitalRead(BUTTON3_PIN) == 1) && (digitalRead(BUTTON4_PIN) == 1)
&& (digitalRead(BUTTON5_PIN) == 1) && (digitalRead(BUTTON6_PIN) == 1))
  {}


  int ch_u[l];
for (int b = 0; b < l; b = b + 1) {
   int temp_1 = 1;
  int temp_2 = 1;
  int temp_3 = 1;
  int temp_4 = 1;
  int temp_5 = 1;

  while ((temp_1 == 1) && (temp_2 == 1) && (temp_3 == 1) && (temp_4 == 1) && (temp_5 == 1)) {
    temp_1= digitalRead(BUTTON1_PIN);
    temp_2= digitalRead(BUTTON2_PIN);
    temp_3= digitalRead(BUTTON3_PIN);
    temp_4= digitalRead(BUTTON4_PIN);
    temp_5= digitalRead(BUTTON5_PIN); 
  }
  if (temp_1 ==0){
    ch_u[l]==1;
    
  }
  if (temp_2 ==0){
    ch_u[l]==2;
  }
  if (temp_3 ==0){
    ch_u[l]==3;
  }
   if (temp_4 ==0){
   ch_u[l]==4;
  }
  if (temp_5 ==0){
   ch_u[l]==5;
  }
   }
   
 int s=1;
for (int c=0; c < l; c = c + 1){
  if (ch_u[c] == ch_a[c]){
    s = s +1;}
  }

if (s==l){
 Game= 'W';
 l= l+2;
 Serial.write('W');
}

else{
 Game= 'l';
  Serial.write('l');}

}
 digitalWrite(BUTTON1_LED, LOW);
  digitalWrite(BUTTON2_LED, LOW);
  digitalWrite(BUTTON3_LED, LOW);
  digitalWrite(BUTTON4_LED, LOW);
  digitalWrite(BUTTON5_LED, LOW);
}
