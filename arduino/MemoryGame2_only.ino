

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


void setup() {

  pinMode(BUTTON1_PIN, INPUT_PULLUP);
  pinMode(BUTTON2_PIN, INPUT_PULLUP);
  pinMode(BUTTON3_PIN, INPUT_PULLUP);
  pinMode(BUTTON4_PIN, INPUT_PULLUP);
  pinMode(BUTTON5_PIN, INPUT_PULLUP);
  pinMode(BUTTON6_PIN, INPUT_PULLUP);

  pinMode(BUTTON1_LED, OUTPUT);
  pinMode(BUTTON2_LED, OUTPUT);
  pinMode(BUTTON3_LED, OUTPUT);
  pinMode(BUTTON4_LED, OUTPUT);
  pinMode(BUTTON5_LED, OUTPUT);
  pinMode(BUTTON6_LED, OUTPUT);


  Serial.begin(9600);
  randomSeed(analogRead(A1));


  int turn = 0;
  int ledorder[10];
  int button[5] = { BUTTON1_PIN, BUTTON2_PIN, BUTTON3_PIN, BUTTON4_PIN, BUTTON5_PIN };
  int ledpin[5] = { BUTTON1_LED, BUTTON2_LED, BUTTON3_LED, BUTTON4_LED, BUTTON5_LED };
  int numberleds[5] = { 4, 5, 6, 6, 7, 7, 8, 9, 10};
  boolean gameover = false;
  boolean nobuttonpressed = true;
  boolean buttonpressed = true;


}

void loop() {

  while (!gameover) {

    // sound for entering the game serial.write('');

    for (int z = 0; z < numberleds[turn]; z++) {
      ledorder[z] = random(5);
      digitalWrite(ledpin[ledorder[z]], HIGH );
      delay(500);
      digitalWrite(ledpin[ledorder[z]] , LOW );
      Serial.print(ledorder[z] + 1);
      delay(500);
    }
    Serial.println(" enter memory code " );

    for ( int lednumber = 0; lednumber < numberleds[turn]; lednumber++) //check num of leds
    {
      while (nobuttonpressed && !gameover) {
        for (int i = 0; i < 5; i++) //check all buttons once
        {
          if (digitalRead(button[i]) == LOW) {
            Serial.print(i + 1);
            nobuttonpressed = false;
            int buttonpresssed = i;

            if (buttonpressed != ledorder[lednumber]) {
              gameover = true;
              Serial.print(buttonpressed);
              Serial.print(ledorder[lednumber]);
              Serial.println("game over");
              // sound for losing
            }
          }
          while (digitalRead(button[i]) == LOW) { // do nothing wait for button to be released
          }
        }
      }
      if ( !gameover) {
        nobuttonpressed == true;
        Serial.println("correct!");
        // sound for winning
      }
      else { //gameover
      }
    } // next led, checked all leds in turn ,
    turn++;
  } // while !gameover, next turn
