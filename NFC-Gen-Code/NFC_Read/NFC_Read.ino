#include <Wire.h>
#include <PN532_I2C.h>
#include <PN532.h>
#include <NfcAdapter.h>

#define RLED 4
#define GLED 5

PN532_I2C pn532_i2c(Wire);
NfcAdapter nfc = NfcAdapter(pn532_i2c);
char Data[5];

void setup() {
  Serial.begin(9600);
  pinMode(RLED, OUTPUT);
  digitalWrite(RLED, LOW);
  pinMode(GLED, OUTPUT);
  digitalWrite(GLED, HIGH);  
  Serial.println("NFC Read Mode");
  nfc.begin();
}

void loop() {
  int c = 0;

  if(Serial.available()) {
    delay(100);

    while(Serial.available() && c<5) {
      Data[c++] = Serial.read(); 
    }

    Data[c++]='\0';
  }

  if(Data[0] == 'R'){   
    Serial.println("\nPlace an NFC Card/Tag on the reader.");
    digitalWrite(RLED, LOW);

    if(nfc.tagPresent()) {  
      digitalWrite(RLED, HIGH);
      digitalWrite(GLED, LOW);
      NfcTag tag = nfc.read();
      Serial.print("UID: ");Serial.println(tag.getUidString());

      if (tag.hasNdefMessage()) {
        NdefMessage message = tag.getNdefMessage();
        int recordCount = message.getRecordCount();

        for (int i = 0; i < recordCount; i++) {
          Serial.print("\nNDEF Record ");Serial.println(i+1);
          NdefRecord record = message.getRecord(i);
          int payloadLength = record.getPayloadLength();
          byte payload[payloadLength];
          record.getPayload(payload);
          String payloadAsString = "";

          for (int c = 3; c < payloadLength; c++) {
            payloadAsString += (char)payload[c];
          }

          Serial.print(" Data: ");
          Serial.println(payloadAsString);
        }
        
        delay(3000);
        digitalWrite(GLED, HIGH);
        delay(2000);
        digitalWrite(RLED, LOW);
        Serial.println("\nDone!");
        Serial.flush();
      }
    }
  }
}
