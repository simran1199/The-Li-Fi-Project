#include <SoftwareSerial.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

LiquidCrystal lcd(4,5,6,7,8,9);
 
const byte ROWS = 4;
const byte COLS = 4;

char hexaKeys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {11,12,A0,A1}; 
byte colPins[COLS] = {A2,A3,A4,A5}; 
SoftwareSerial GSerial(2,3); 
Keypad customKeypad = Keypad( makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 
char keycount=0;
char code[16];
   


void setup() {
 
  Serial.begin(9600);
  Serial.println("Keyboard Test:");
  GSerial.begin(400);
   delay(1000);
  
}
int count =0;
void loop() 
{   String rec="";
    
   while(Serial.available()>0)
   {
    rec = Serial.readStringUntil('@');
    if(rec=="y")
    count=1;

    delay (100);
    if(count==1)
 { GSerial.print(rec);  
  Serial.print(rec);
  delay (50);}
}
    }
   
    
     
     

 
