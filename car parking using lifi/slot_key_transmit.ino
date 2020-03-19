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
char code[5];


void setup() {
  delay(1000);
  Serial.begin(9600);
  Serial.println("Keyboard Test:");
  GSerial.begin(400);
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.setCursor(0, 0);
  lcd.print(" LiFi - Wireless");
  lcd.setCursor(0, 1);
  lcd.print(" Communication  ");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" using Light    ");
  lcd.setCursor(0, 1);
  lcd.print(" TX TESTING ..  ");
  delay(3000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("  By The Geek Squad  ");
  lcd.setCursor(0,1); 
  lcd.print("    Electrothon 2020   ");
  delay(3000);
  lcd.clear();
  GSerial.print('&');
}

void loop() 
{    
  char customKey = customKeypad.getKey();
  if(customKey && (customKey !='='))
  {      
    if (customKey == '#') 
    {
      GSerial.print('^');
      lcd.setCursor(0, 1);
      lcd.print("                ");
      lcd.setCursor(0, 1);
    } 
    else if (customKey == '*') 
    {
      GSerial.print('&');
      lcd.clear();
    } 
    else 
    {
      // otherwise, just print all normal characters
      Serial.print(customKey);
      GSerial.print(customKey);
      lcd.print(customKey);
    }    
  }  
}
