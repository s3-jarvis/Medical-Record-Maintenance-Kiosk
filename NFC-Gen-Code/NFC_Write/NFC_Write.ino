#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

#define RLED 4
#define GLED 5

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);

char serialData[10];
long pid = 0;
String dataSend = "PATIENT";

void setup(void) {
  Serial.begin(9600); 
  pinMode(RLED, OUTPUT);
  digitalWrite(RLED, LOW);
  pinMode(GLED, OUTPUT);
  digitalWrite(GLED, HIGH);  
  Serial.println("NFC Write Mode");
  nfc.begin();
}

void loop(void) {
  int c = 0;
  String padding = "";
  bool success;
  
  if(Serial.available()){
    delay(100);
    while(Serial.available() && c<10) {
      serialData[c++] = Serial.read();
    }
    serialData[c++] = '\0';
  }
  
  if(c>0){
  pid = atoi(serialData);
  }

  if(pid>0) {
    Serial.println("\nPlace an NFC Card/Tag on the reader.");
    digitalWrite(RLED, LOW);
    
    if(nfc.tagPresent()) {  
      digitalWrite(RLED, HIGH);
      digitalWrite(GLED, LOW);
      delay(500);
      digitalWrite(GLED, HIGH);
      success = nfc.clean();

      if(success) {
        digitalWrite(GLED, LOW);
        Serial.println("\nNFC Card/Tag cleared successfully!");
      }

      else {
        Serial.println("\nE101");
      }  

      delay(500);
      digitalWrite(GLED, HIGH);     
      success = nfc.format();

      if (success) {
        digitalWrite(GLED, LOW);
        Serial.println("\nNFC Card/Tag formated to NDEF.");
      }

      else {
        Serial.println("\nE102");
      }

      delay(500);
      digitalWrite(GLED, HIGH);

      switch(pid) {
        case 0 ... 9:
          padding = "000";
          break;
        case 10 ... 99:
          padding = "00";
          break;
        case 100 ... 999:
          padding = "0";
          break;
        default:
          padding = "";
          break;
      }
        
      NdefMessage message = NdefMessage();
      message.addTextRecord(dataSend + padding + String(pid));
      message.addTextRecord("ABC Hospital");
      success = nfc.write(message);   

      if (success) {
        digitalWrite(GLED, LOW);
        Serial.println("\nWrite Success!");
      }

      else {
        Serial.println("\nE103");
      }
      
      delay(4000);
      digitalWrite(GLED, HIGH);
      delay(2000);
      digitalWrite(RLED, LOW); 
      Serial.println("Done!");
      Serial.flush();
    }
  }
}
