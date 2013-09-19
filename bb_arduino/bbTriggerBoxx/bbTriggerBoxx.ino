/* ? 2013 ByteBoxx LTD */

//libs
#include <time.h>

const int    gDELAY_VALUE = 500;//internal delay while cycling
const int    gFLASH_DURATION = 4; //default flash duration
const int    gFRAME_CYCLE = 10; //default number of frames to shoot
const int    gSAMPLES = 100;

int gFOCUS_PIN = 2;
int gFLASH_PIN = 4;
int gSHUTTER_PIN = 7;
int gRELEASE_PIN = 9;
int gFEEDBACK_PIN = 12;
char c;
//test


void setup()
{

    /* add setup code here */
    Serial.begin(9600);

    //pin configures
    pinMode(gFOCUS_PIN, OUTPUT);
    pinMode(gFLASH_PIN, OUTPUT);
    pinMode(gSHUTTER_PIN, OUTPUT);
    pinMode(gRELEASE_PIN, INPUT);
    pinMode(gFEEDBACK_PIN, INPUT);
    

}

void loop()
{
  
  while(Serial.available() > 0) // Don't read unless you know there is data
    {
        c = Serial.read(); // Read a character
        
        if( c == 'a')
        {
          triggerArray();
        }
        else if( c == 'b')
        {

      testShutterLag();
        }
    }

}

float testShutterLag()
{
    long    minLag, maxLag = 0;
        long    accumLag = 0;
    bool    lState;
    double    lShutterlag;
    int        lFallingEdge;
    long    lStartTime;

    for (int i = 0; i < gFRAME_CYCLE; i++)
    {
        lFallingEdge = 0;

        //deal with mirror lockup here?

        //trigger focus and shutter LOW
        digitalWrite(gFOCUS_PIN, LOW);   
        digitalWrite(gSHUTTER_PIN, LOW);
            
        //start our clock
        lStartTime = millis();
        Serial.print(lStartTime);

        for (int j = 0; j < gSAMPLES; j++)
        {
            //check for flash sync pulse feedback
            lState = digitalRead(gFEEDBACK_PIN);

            if (lState == 0 && lFallingEdge == 0)
            {
                //clock end - work out shutterlag
                lShutterlag = (millis() - lStartTime);
                Serial.print(lShutterlag);
                    
                if (lShutterlag > maxLag)
                    maxLag = lShutterlag;
                if (lShutterlag < maxLag)
                    minLag = lShutterlag;
                    
                //print "Sample - {0}, FIO6 state = {1}, Shutter Lag = {2} milliseconds\n".format(index, lState, shutterLag)
                accumLag += lShutterlag;
                lFallingEdge = 1;
            }

        }

        //reset focus and shutter HIGH
        digitalWrite(gFOCUS_PIN, HIGH);
        digitalWrite(gSHUTTER_PIN, HIGH);

        delay(gDELAY_VALUE);

    }

    float averageLag = accumLag/gFRAME_CYCLE;
    //printf("\n----Average shutterLag over {0} frames = {1} milliseconds\n".format(gFRAME_CYCLE, averageLag));
    //printf("----Min shutterLag over {0} frames = {1} milliseconds\n".format(gFRAME_CYCLE, minLag));
    //printf("----Max shutterLag over {0} frames = {1} milliseconds\n".format(gFRAME_CYCLE, maxLag));
    //printf("----ShutterLag variance over {0} frames = {1} milliseconds\n".format(gFRAME_CYCLE, (maxLag-minLag);
}

void triggerArray()
{
      //trigger focus and shutter LOW
    digitalWrite(gFOCUS_PIN, HIGH);   
    digitalWrite(gSHUTTER_PIN, HIGH);

    delay(80); //calculated delay

    digitalWrite(gFLASH_PIN, HIGH); //Flashing Bowens
            
        delay(gFLASH_DURATION);
            
            
          
        digitalWrite(gFLASH_PIN, LOW);  //Reset Bowens flash unit

    delay(gDELAY_VALUE);

    //reset focus and shutter HIGH
    digitalWrite(gFOCUS_PIN, LOW);
    digitalWrite(gSHUTTER_PIN, LOW);

    delay(gDELAY_VALUE);               // wait for half a second


}