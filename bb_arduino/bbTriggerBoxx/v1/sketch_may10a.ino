const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  13;      // the number of the LED pin
char c;

// variables will change:
int buttonState = 0;         // variable for reading the pushbutton status
boolean hasTriggered = false;

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);      
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);  
  Serial.begin(9600);  
}

void loop(){
  // read the state of the pushbutton value:
  
  while(Serial.available() > 0) // Don't read unless you know there is data
  {
    c = Serial.read(); // Read a character
        
        if( c == 'a')
        {
          digitalWrite(ledPin, HIGH);
          delay(2000);
        }
        else if( c == 'b')
        {

          digitalWrite(ledPin, LOW);
        }
    }
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed.
  // if it is, the buttonState is HIGH:
  if (buttonState == HIGH) {     
    // turn LED on:
    if (! hasTriggered){
      hasTriggered = true;
      Serial.write('c');
    }      
    digitalWrite(ledPin, HIGH);
    
  } 
  else {
    
    // turn LED off:
    digitalWrite(ledPin, LOW);
    hasTriggered = false; 
  }
}
