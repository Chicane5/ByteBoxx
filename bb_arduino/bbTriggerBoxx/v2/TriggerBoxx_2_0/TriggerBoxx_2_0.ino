/*
TRIGGERBOXX V2.0
gary@byteboxx.com 01/03/2015
*/

// PINS - these dont change
const int led =  13;      // RED (FRONT)
const int trigger = 9;     
const int focus = 2;      // GREEN
const int shutter = 4;    // RED
const int flash = 7;      // BLUE


// variables
char c;                      //the command char sent from TriggerBoxx UI
int triggerState = 0;         // variable for reading the cable trigger status

void setup() {
 
  pinMode(led, OUTPUT); //debug led
  pinMode(trigger, INPUT); //cable trigger  
  pinMode(focus, OUTPUT); //cam focus (button half pressed) 
  pinMode(shutter, OUTPUT); //cam shutter
  pinMode(flash, OUTPUT); //strobes
  
  Serial.begin(9600);  
}

void loop(){
  
  //check for anything being sent over serial from Python

  if(Serial.available() > 0){ // Don't read unless you know there is data
  
    c = Serial.read(); // Read a character
        
    if( c == 'a'){
    
      //FIRE ARRAY
      fireArray();
      delay(2000);
    }
    else if( c == 'b'){
    
      //PRIME ARRAY
      primeArray();
      delay(2000); 
    }    
  }
   
  //if nothing from the UI, did we take a cable trigger?
  readCable();
    
}

void readCable(){
  //read the input of trigger pin
  triggerState = digitalRead(trigger);
  if (triggerState == HIGH){
    
   //PRIME
   primeArray();
   delay(2000);
   Serial.write('c');
   delay(3000); //delay while we do folder creation etc back in Python GUI
   fireArray();
   delay(2000);
   return;
  }
  else{
    return;
  }
}


void fireArray(){
  //func to actually trigger - depresses the shutter and fires strobes after dialled in delay
  digitalWrite(shutter, HIGH);
  delay(100);
  digitalWrite(shutter, LOW);
  delay(80); //dialled in delay
  digitalWrite(flash, HIGH);
 
  delay(100); //strobe on duration
 
  digitalWrite(flash, LOW);
  
}


void primeArray(){
  //func to suto-focus the lens (shutter half way) and ping mirror up
  digitalWrite(focus, HIGH);
  delay(100);
  digitalWrite(focus, LOW);
         
  digitalWrite(shutter, HIGH); //mirror lock
  delay(100);
  digitalWrite(shutter, LOW);
  
}
 
