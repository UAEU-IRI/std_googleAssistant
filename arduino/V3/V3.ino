
#include <Servo.h>
//#include "if.h"



//#define victory_sign2()   t.write(THUMB_CLOSE);i.write(INDEX_OPEN);m.write(MIDDLE_OPEN);r.write(RING_CLOSE);p.write(PINKY_CLOSE)


unsigned long time , time_0, time_1, time_2, time_3, time_d, time_d_ ;

#define THUMB_PIN 5
#define THUMB_OPEN 10
#define THUMB_CLOSE 170

#define INDEX_PIN  6
#define INDEX_OPEN 10
#define INDEX_CLOSE 160

#define MIDDLE_PIN 7
#define MIDDLE_OPEN 0
#define MIDDLE_CLOSE 140

#define RING_PIN 8
#define RING_OPEN 10
#define RING_CLOSE 170

#define PINKY_PIN 9
#define PINKY_OPEN 10
#define PINKY_CLOSE 160

#define WRIST_PIN  4
#define WRIST_LEFT 140
#define WRIST_RIGHT 30
#define WRIST_CENTER 85

#define RELAX 70
#define RELAX_M 0

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
      t.write(THUMB_OPEN);
      i.write(INDEX_OPEN);
      m.write(MIDDLE_OPEN);
      r.write(RING_OPEN);
      p.write(PINKY_OPEN);

      delay(700);
      RelaxFingers();
      delay(2000);
    }


    if (c == 'c') {
      count_numbers();
       delay(20000);
    }
    if (c == 't') {
      Thumbs_up();
       delay(20000);
    }
    if (c == 'h') {
      hello();
       delay(20000);
    }
    if (c == 'b') {
      bye();
       delay(20000);
    }
    if (c == 'l') {
      closehand();
       delay(20000);
    }
    if (c == 'o') {
      openhand();
       delay(20000);
    }
    if (c == 'p') {
      Rock_paper_scissors();
       delay(20000);
    }
    if (c == 's') {
      Play_Memory_Sequence();
       delay(20000);
    }
    if ( c == 'm') {
      mohammed_sign();
       delay(20000);
    }

    if ( c == 'u') {
      out();
       delay(20000);
    }
    if ( c == 'y') {
      dance1();
       delay(20000);
    }
    if (c == 'z') {
      dance2();
      delay(20000);
    }
    
    

  }
   if ( !Serial.available() > 0 ) {
    delay(4000);
     alive(); 
    }
}
void alive() {

  w.write(WRIST_LEFT);

  delay(10000);

  w.write(WRIST_CENTER);

  delay(10000);

  w.write(WRIST_RIGHT);

  delay(10000);

  w.write(WRIST_CENTER);

  delay(10000);

  t.write(RELAX);

  i.write(RELAX);

  m.write(RELAX_M);

  r.write(RELAX);

  p.write(RELAX);

  delay(10000);

  t.write(THUMB_OPEN);

  i.write(INDEX_OPEN);

  m.write(MIDDLE_OPEN);

  r.write(RING_OPEN);

  p.write(PINKY_OPEN);

  delay(10000);

}




void dance1() {

  for(int f=0;f<5 ;f=f+1){

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

  p.write(PINKY_OPEN);

  delay(700);

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

  p.write(PINKY_OPEN);

  delay(700);


  w.write(WRIST_LEFT);

  delay(700);

  w.write(WRIST_RIGHT);


  delay(700);



  w.write(WRIST_LEFT);

  delay(700);

  w.write(WRIST_RIGHT);


  delay(1000);

}}






void dance2() {

  
  for(int f=0;f<3 ;f=f+1){
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

  delay(700);
  t.write(THUMB_OPEN);

  i.write(INDEX_OPEN);

  m.write(MIDDLE_OPEN);

  r.write(RING_OPEN);

  p.write(PINKY_OPEN);

  delay(700);


  w.write(WRIST_LEFT);

  delay(400);

  w.write(WRIST_CENTER);


  delay(400);


  w.write(WRIST_LEFT);

  delay(700);

  w.write(WRIST_CENTER);


  delay(700);


  w.write(WRIST_LEFT);

  delay(700);

  w.write(WRIST_CENTER);


  delay(1000);
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
void out() {

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

  Serial.write('u');
}

void love() {
  t.write(THUMB_OPEN);

  i.write(INDEX_OPEN);

  m.write(MIDDLE_CLOSE);

  r.write(RING_CLOSE);

  p.write(PINKY_CLOSE);

}

void win() {
  
  t.write(THUMB_CLOSE);

  i.write(INDEX_CLOSE);

  m.write(MIDDLE_CLOSE);

  r.write(RING_CLOSE);

  p.write(PINKY_CLOSE);
  delay(700);

  t.write(THUMB_OPEN);

  i.write(INDEX_OPEN);

  m.write(MIDDLE_OPEN);

  r.write(RING_CLOSE);

  p.write(PINKY_CLOSE);
}

void mohammed_sign() {

    Serial.write('e');
      love();

    delay(7000);

    Serial.write('v');
      Victory_peace();

    delay(7000);

    Serial.write('i');
        win();

    delay(7000);
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

  delay(700);


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

  delay(700);

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

  delay(2000);


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

  delay(700);


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

  delay(2000);



}
void RelaxFingers() {

  delay(700);
  w.write(WRIST_CENTER);
  t.write(RELAX);
  i.write(RELAX);
  m.write(RELAX_M);
  r.write(RELAX);
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
//Rock
void Rock() {
  t.write(THUMB_CLOSE);
  i.write(INDEX_CLOSE);
  m.write(MIDDLE_CLOSE);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);
}
//paper
void paper() {
  t.write(THUMB_OPEN);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_OPEN);
  p.write(PINKY_OPEN);

}
//scissors
void scissors() {
  t.write(THUMB_CLOSE);
  i.write(INDEX_OPEN);
  m.write(MIDDLE_OPEN);
  r.write(RING_CLOSE);
  p.write(PINKY_CLOSE);

}
int choose(int ch) {
  if (ch == 1) {
    Rock();
  }
  if (ch == 2) {
    paper();
  }
  if (ch == 3) {
    scissors();
  }
  return ch;

}
int delay_(unsigned long time) {
  int temp_1 = 1;
  int temp_2 = 1;
  int temp_3 = 1;
  time_1 = millis(); time_d = 0;
  while (time_d <= time && (temp_1 == 1) && (temp_2 == 1) && (temp_3 == 1)) {
    temp_1 = digitalRead(BUTTON1_PIN);
    temp_2 = digitalRead(BUTTON2_PIN);
    temp_3 = digitalRead(BUTTON3_PIN);
    time_d = millis() - time_1;

  }
  if (temp_1 == 0) {
    return 1;

  }
  if (temp_2 == 0) {
    return 2;
  }
  if (temp_3 == 0) {
    return 3;
  }
  return 0;
}

int delay_start(unsigned long time) {
  int temp = 1;
  time_0 = millis(); time_d = 0;
  while (time_d <= time && (temp == 1)) {
    temp = digitalRead(BUTTON6_PIN);
    time_d = millis() - time_0;
  }
  return temp;
}

void Rock_paper_scissors() {

  // Serial.write('s');
  char result = 'e' ;
  while (result == 'e') {
    digitalWrite(BUTTON6_LED, HIGH);
    while (digitalRead(BUTTON6_PIN) == 1) {}

    digitalWrite(BUTTON6_LED, LOW);

    digitalWrite(BUTTON1_LED, HIGH);
    digitalWrite(BUTTON2_LED, HIGH);
    digitalWrite(BUTTON3_LED, HIGH);

    int b1 = 1;
    int b2 = 1;
    int b3 = 1;
    int h;
    while ((b1 == 1) && (b2 == 1) && (b3 == 1)) {
      Rock();
      h = delay_(1000);
      if (h != 0) {
        break;
      }
      paper();
      h = delay_(1000);
      if (h != 0) {
        break;
      }
      scissors();
      h = delay_(1000);
      if (h != 0) {
        break;
      }
    }
    int ch = random(1, 4);
    int choi = choose(ch);
    delay(2000);

    digitalWrite(BUTTON1_LED, LOW);
    digitalWrite(BUTTON2_LED, LOW);
    digitalWrite(BUTTON3_LED, LOW);


    //the user choose same thing no one won "they will do high five"

    if (choi == 1 && h == 1) {
      ;
     // Serial.write('t');
      openhand();
      result = 'e';

    }

    if (choi == 2 && h == 2) {
     // Serial.write('t');
      openhand();
      result = 'e';
    }

    if (choi == 3  && h == 3) {
     // Serial.write('t');
      openhand();
      result = 'e';
    }

    //the user win  :the arm fingers look sad so -->Relax function

    if (choi == 1 && b2 == 2) {
     // Serial.write('w');
      RelaxFingers();
      result = 'w';

    }
    if (choi == 2 && h == 3) {
     // Serial.write('w');
      RelaxFingers();
      result = 'w';
    }
    if (choi == 3 && h == 1) {
     // Serial.write('w');
      RelaxFingers();
      result = 'w';
    }


    //the user loss  : the arm fingers look happy so -->victory_peace function

    if (choi == 2 && h == 1) {
     // Serial.write('l');
      Victory_peace();
      result = 'l';
    }
    if (choi == 3 && h == 2) {
     // Serial.write('l');
      Victory_peace();
      result = 'l';
    }
    if (choi == 1 && h == 3) {
     // Serial.write('l');
      Victory_peace();
      result = 'l';
    }


    delay(5000);
  }
}

int number_choose(int ch) {
  if (ch == 1) {
    shownumber1();
  }
  if (ch == 2) {
    shownumber2();
  }
  if (ch == 3) {
    shownumber3();
  }
  if (ch == 4) {
    shownumber4();
  }
  if (ch == 5) {
    shownumber5();
  }
  return ch;

}
void Play_Memory_Sequence() {
  // Serial.write('s');

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
  int l = 3;
  while (Game == 'W') {
    int ch_a[ l];
    for (int i = 0; i < l; i = i + 1) {
      ch_a[i] = number_choose(random(1, 6));
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
        temp_1 = digitalRead(BUTTON1_PIN);
        temp_2 = digitalRead(BUTTON2_PIN);
        temp_3 = digitalRead(BUTTON3_PIN);
        temp_4 = digitalRead(BUTTON4_PIN);
        temp_5 = digitalRead(BUTTON5_PIN);
      }
      if (temp_1 == 0) {
        ch_u[l] == 1;

      }
      if (temp_2 == 0) {
        ch_u[l] == 2;
      }
      if (temp_3 == 0) {
        ch_u[l] == 3;
      }
      if (temp_4 == 0) {
        ch_u[l] == 4;
      }
      if (temp_5 == 0) {
        ch_u[l] == 5;
      }
    }

    int s = 1;
    for (int c = 0; c < l; c = c + 1) {
      if (ch_u[c] == ch_a[c]) {
        s = s + 1;
      }
    }

    if (s == l) {
      Game = 'W';
      l = l + 2;
      Serial.write('w');
    }

    else {
      Game = 'l';
      Serial.write('l');
    }
    digitalWrite(BUTTON1_LED, LOW);
    digitalWrite(BUTTON2_LED, LOW);
    digitalWrite(BUTTON3_LED, LOW);
    digitalWrite(BUTTON4_LED, LOW);
    digitalWrite(BUTTON5_LED, LOW);
  }


}
