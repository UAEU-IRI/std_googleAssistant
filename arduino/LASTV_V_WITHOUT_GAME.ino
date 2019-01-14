#include <Servo.h>

//LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
// I HAVE TO CHANGE THE PINS NUMBER BUT I'M NOT SHURE ABOUT IT
//LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

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


#define PINKY_PIN 9
#define PINKY_OPEN 10
#define PINKY_CLOSE 170


#define WRIST_PIN  4
#define WRIST_LEFT 170
#define WRIST_RIGHT 10
#define WRIST_CENTER 90

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
  Serial3.begin(9600);
  randomSeed(analogRead(0));
  //lcd.print("Let's start .. ");
  //delay(1000);

}


void loop() {
  // put your main code here, to run repeatedly:
  if ( Serial3.available() > 0) {
    char c = Serial3.read();
    if (c == 'v') {
      Victory_peace();
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
    if (c == 'p') {
      Rock_paper_scissors();
      // }
      // if (c == 's') {
      //  Sequence();
      //}
    }
  }
  void Victory_peace() {
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
  void Wake_UP() {

    t.write(THUMB_OPEN);
    i.write(INDEX_OPEN);
    m.write(MIDDLE_OPEN);
    r.write(RING_OPEN);
    p.write(PINKY_OPEN);

    w.write(WRIST_RIGHT);
    w.write(WRIST_RIGHT);
    w.write(WRIST_LEFT);
    w.write(WRIST_LEFT);



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


    t.write(THUMB_OPEN);
    i.write(INDEX_OPEN);
    m.write(MIDDLE_OPEN);
    r.write(RING_OPEN);
    p.write(PINKY_OPEN);

    delay(700);
    w.write(WRIST_CENTER);
    t.write(RELAX);
    i.write(RELAX);
    m.write(RELAX_M);
    r.write(RELAX);
    p.write(RELAX);

    delay(2000);


    delay(2000);
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
    //t.write(THUMB_CLOSE);
    //i.write(INDEX_CLOSE);
    //m.write(MIDDLE_CLOSE);
    //r.write(RING_CLOSE);
    // p.write(PINKY_CLOSE);

    //delay(2000);

   



    w.write(WRIST_LEFT);
    delay(1000);
    w.write(WRIST_RIGHT);

    delay(1000);

  }


  void bye() {
     t.write(THUMB_OPEN);
    i.write(INDEX_OPEN);
    m.write(MIDDLE_OPEN);
    r.write(RING_OPEN);
    p.write(PINKY_OPEN);

    delay(2000);


    w.write(WRIST_LEFT);
    delay(1000);
    w.write(WRIST_RIGHT);

    delay(1000);
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
