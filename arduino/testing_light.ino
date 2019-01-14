
#define BUTTON1_LED 38
#define BUTTON2_LED 40
#define BUTTON3_LED 42
#define BUTTON4_LED 44
#define BUTTON5_LED 46
#define BUTTON6_LED 48

#define BUTTON1_PIN 22
#define BUTTON2_PIN 24
#define BUTTON3_PIN 26
#define BUTTON4_PIN 28
#define BUTTON5_PIN 30
#define BUTTON6_PIN 32
void setup() {
  // put your setup code here, to run once:
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
}

void loop() {
  // put your main code here, to run repeatedly:
test();
delay(2000);
}
void test() {
  while (digitalRead(BUTTON6_PIN)) {
    digitalWrite(BUTTON1_LED, HIGH);
    delay(700);
    digitalWrite(BUTTON2_LED, HIGH);
    delay(700);
    digitalWrite(BUTTON3_LED, HIGH);
    delay(700);
    digitalWrite(BUTTON4_LED, HIGH);
delay(700);
digitalWrite(BUTTON5_LED, HIGH);
delay(700);
digitalWrite(BUTTON6_LED, HIGH);
delay(700);
digitalWrite(BUTTON1_LED, LOW);
delay(700);
digitalWrite(BUTTON2_LED, LOW);
delay(700);
digitalWrite(BUTTON3_LED, LOW);
delay(700);
digitalWrite(BUTTON4_LED, LOW);
delay(700);   
digitalWrite(BUTTON5_LED, LOW);
delay(700); 
digitalWrite(BUTTON6_LED, LOW);
delay(700); 
  }
  
  

}
