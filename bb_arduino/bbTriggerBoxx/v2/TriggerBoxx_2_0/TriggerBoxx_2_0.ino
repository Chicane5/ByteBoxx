/*
TRIGGERBOXX V2.0
*/

const int buttonPin = 9;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
int focus = 2;
int shutter = 4;
int flash = 7;


// variables will change:
char c;                      //the command char sent from TriggerBoxx UI
int buttonState = 0;         // variable for reading the pushbutton status
boolean hasTriggered = false;

void setup() {
 
  pinMode(ledPin, OUTPUT); //LED for testing only RED - FRONT
  
  pinMode(buttonPin, INPUT); //cable trigger  
  pinMode(focus, OUTPUT); //cam focus (button half pressed) GREEN 
  pinMode(shutter, OUTPUT); //cam shutter RED
  pinMode(flash, OUTPUT); //strobes BLUE
  
  Serial.begin(9600);  
}

void loop(){
  
  //digitalWrite(focus, HIGH);
  //digitalWrite(shutter, HIGH);
  //digitalWrite(flash, HIGH);
  
  
  // read the state of the pushbutton value:
  
  
  while(Serial.available() > 0) // Don't read unless you know there is data
  {
    c = Serial.read(); // Read a character
        
        if( c == 'a')
        {
          //firing array
          //digitalWrite(ledPin, HIGH);
          doTrigger();
          delay(2000);
        }
        else if( c == 'b')
        {
          //priming array
          digitalWrite(focus, HIGH);
          delay(10);
          digitalWrite(focus, LOW);
          
          digitalWrite(shutter, HIGH); //mirror lock
          //digitalWrite(ledPin, LOW);
        }
   }
   
   //did we take a cable trigger?
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {     
    // turn LED on:
    if (! hasTriggered){
      hasTriggered = true;
      Serial.write('c');
    }      
    //digitalWrite(ledPin, HIGH);
    doTrigger();
    delay(2000);
  } 
  else {
    
    // turn LED off:
    //digitalWrite(ledPin, LOW);
    hasTriggered = false; 
  }
  
}

void doTrigger(){
  //func to actually trigger
  digitalWrite(shutter, LOW);
  delay(80);
  digitalWrite(flash, HIGH);
  
  delay(20);
  digitalWrite(shutter, HIGH);
  digitalWrite(flash, LOW);
}
  
