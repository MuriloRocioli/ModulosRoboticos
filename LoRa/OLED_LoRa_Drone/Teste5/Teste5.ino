#include "XL330.h"
#include "heltec.h"

XL330 robot;  // Name your robot

int servoID = 254;  // 254: broadcast; id value: 0~252

#include <SoftwareSerial.h>
SoftwareSerial mySerial(3, 1); // (RX, TX) both connected to the data pin of XL330

#define BAND 915E6 //you can set band here directly,e.g. 868E6,915E6

String rssi = "RSSI --";
String packSize = "--";
String packet;
String packet_old;
String pacote;

int pos; // Posição Servo
char num;
int flagsinal = 0; //avalia prioridade de recepcao do sinal da terra sobre a transmissao do sinal do sensor para a terra

void LoRaData()
{
  Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
}

void cbk(int packetSize)
{
  packet = "";
  packSize = String(packetSize, DEC);
  rssi = "RSSI " + String(LoRa.packetRssi(), DEC);
  LoRaData();
}

void setup() {

  //Serial.begin(115200);

  ////Start the serial you're using
  mySerial.begin(57600);
  robot.begin(mySerial);
  
  robot.TorqueOFF(servoID); //Servo needs to be torque off to change setting, broadcast to turn all servos off
  delay(100);

  //Set the mode to position control
  //Control Mode Options: 0: current; 1: velocity; 3: position; 4: extended position; 5: current-base position; 16: PWM
  robot.setControlMode(servoID, 16);
  delay(50);

  robot.TorqueON(servoID);  //Turn on the torque to control the servo
  delay(50);

  //Blink LED as testing
  robot.LEDON(servoID);
  delay(500);
  robot.LEDOFF(servoID);
  delay(50);
  
  Heltec.begin(true /*DisplayEnable Enable*/, true /*Heltec.Heltec.Heltec.LoRa Disable*/, true /*Serial Enable*/, true /*PABOOST Enable*/, BAND /*long BAND*/);

  Heltec.display->init();
  Heltec.display->flipScreenVertically();
  Heltec.display->setFont(ArialMT_Plain_16);

  Heltec.display->drawString(0, 0, "Tudo OK!");
  Heltec.display->drawString(0, 18, "Esperando Dados");
  Heltec.display->display();
  delay(5);
  LoRa.receive();

  //Define os pinos de saída
  pinMode(12, OUTPUT); //Pino Eletroímã
  pinMode(13, OUTPUT); //Pino maçarico
  pinMode(21, OUTPUT); //Pino maçarico

}

void loop() {  

  robot.setJointSpeed(servoID, 885);
  delay(3000);

  robot.setJointSpeed(servoID, 0);
  delay(3000);
  
  int packetSize = LoRa.parsePacket();
  if (packetSize){cbk(packetSize);}

  packet = (char)LoRa.read();//LE MENSAGEM VINDA DA LORA DA TERRA

  if (packet == "1")
  {
      //Avanca o robo
      robot.setJointSpeed(servoID, 885);
      delay(3000);
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V1");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }
    
  if (packet == "2")
  {
      //Recua o robo
      robot.setJointSpeed(servoID, -885);
      delay(3000);

      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V2");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }

  if (packet == "3")
  {
      //Automação - Acionar Maçarico
      //Recua atuador
      digitalWrite(13, HIGH);
      digitalWrite(21, LOW);

      //Aguarda 3 segundos
      delay(2000);

      //Avança atuador
      digitalWrite(13, LOW);
      digitalWrite(21, HIGH);

      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V3");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
     
    }
    
  if (packet == "4")
  {
      //Acionar Eletroímã
      digitalWrite(12, HIGH);
       
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V4");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }
    
  if (packet == "5")
  {
      Serial.println("5");
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V5");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }

  if (packet == "6")
  {
      //Avança Atuador
      digitalWrite(13, LOW);
      digitalWrite(21, HIGH);
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V6");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }
    
  if (packet == "7")
  {
      //Recua atuador
      digitalWrite(13, HIGH);
      digitalWrite(21, LOW);
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V7");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }

  if (packet == "8")
  {
      //Desacionar Eletroímã
      digitalWrite(12, LOW);
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V8");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }  

  if (packet == "9")
  {
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V9");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }

  if (packet == "0")
  {
      
      Heltec.display->clear();
      Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
      Heltec.display->setFont(ArialMT_Plain_24);
      Heltec.display->drawStringMaxWidth(0, 32, 128, "V10");
      Heltec.display->drawString(0, 0, rssi);
      Heltec.display->display();
      delay (10);
    }
}
