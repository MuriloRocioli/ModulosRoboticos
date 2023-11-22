#include "heltec.h"
#include "images.h"
#include "BluetoothSerial.h"

char buf;
int a;

BluetoothSerial SerialBT;

#define BAND 915E6 //you can set band here directly,e.g. 868E6,915E6

unsigned int num = 0;
String rssi = "RSSI --";
String packSize = "--";
String packet;

int pos; // Posição Servo
int i=0;
int flag=0;

void LoRaData()
{
  Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawString(0 , 18 , "Pct="+ packSize + "b");
  //Heltec.display->drawStringMaxWidth(0, 32, 128, packet);
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
}

void cbk(int packetSize)
{
  packet = "";
  packSize = String(packetSize, DEC);
  //for (int i = 0; i < packetSize; i++)
  //{
  //  packet += (char)LoRa.read();
  //}
  //packet = (char)LoRa.read();
  rssi = "RSSI " + String(LoRa.packetRssi(), DEC);
  LoRaData();
}

void setup()
{

  pinMode(25, OUTPUT);
  digitalWrite(25, LOW);
  //pinMode(LED, OUTPUT);

  Serial.begin(115200);
  SerialBT.begin("LoRa_BT");
  
  Heltec.begin(true /*DisplayEnable Enable*/, true /*Heltec.Heltec.Heltec.LoRa Disable*/, true /*Serial Enable*/, true /*PABOOST Enable*/, BAND /*long BAND*/);

  Heltec.display->init();
  Heltec.display->flipScreenVertically();
  Heltec.display->setFont(ArialMT_Plain_16);
  //logo();
  //delay(1500);
  // Heltec.display->clear();

  Heltec.display->drawString(0, 0, "Tudo OK!");
  Heltec.display->drawString(0, 18, "Esperando Dados");
  Heltec.display->display();
  delay(5);
  LoRa.receive();
}

void loop()
{

  //ROTINA DE RECEPCAO DO SINAL BLUETOOTH DO CELULAR

  a = SerialBT.read();

  if (a == '1')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 1;
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "SERVO");
    Heltec.display->drawString(40, 26, "HIGH");
    Heltec.display->display();
  }

  if (a == '2')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 2;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "SERVO");
    Heltec.display->drawString(40, 26, "LOW");
    Heltec.display->display();
  }

  if (a == '3')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 3;
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(13, 0, "ATUADOR");
    Heltec.display->drawString(29, 26, "LIGADO");
    Heltec.display->display();

  }

  if (a == '4')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 4;
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "AVANCO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

  if (a == '5')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 5;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

    if (a == '6')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 6;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

    if (a == '7')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 7;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

    if (a == '8')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 8;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

    if (a == '9')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 9;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }

    if (a == '0')
  {
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 0;
    LoRa.print(num);
    LoRa.endPacket();
    
    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "RECUO");
    Heltec.display->drawString(40, 26, "RAPIDO");
    Heltec.display->display();
  }
  
  //ROTINA DE RECEPCAO DO SINAL VINDO DO DRONE

  i=i+1;
  delay(5);
  if (i>10){
    i = 0;
  }
  
  int packetSize = LoRa.parsePacket();
  if (packetSize){cbk(packetSize);}
  //delay(20);

  packet = (char)LoRa.read();

  if (packet == "c") //BIPE CONTINUO
  {
      flag = 0;
      //Serial.println("1");
      //Serial.println(" "); // em s
      //delay(5);

      digitalWrite(25, HIGH);
      
      Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  Heltec.display->drawStringMaxWidth(0, 32, 128, "AVANÇO");
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
      delay (10);
    }
    
  if (packet == "b") //DISTANCIA OTIMA
  {
      flag = 0;
      //Serial.println("3");
      //Serial.println(" "); // em s      
      //delay(5);

      digitalWrite(25, LOW);

      Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  Heltec.display->drawStringMaxWidth(0, 32, 128, "ATUADOR");
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
      //delay (10);
    }  
    
  if (packet == "a" or flag == 1) //BIPE INTERMITENTE
  {
      flag = 1;
      //Serial.println("2");
      //Serial.println(" "); // em s      
      //delay(5);

      if (i<5) {
        digitalWrite(25, HIGH);
      }

      if (i>=5) {
        digitalWrite(25, LOW);
      }

      Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  Heltec.display->drawStringMaxWidth(0, 32, 128, "RECUO");
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
      //delay (10);
    }

  //if (packet != "1" and packet != "2" and packet != "3") //VAZIO
  //{
  //    flag = 0;
  //    //Serial.println("3");
  //   //Serial.println(" "); // em s      
  //    //delay(5);

  //    Heltec.display->clear();
  //Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  //Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawStringMaxWidth(0, 32, 128, "RECEBE VAZIO");
  //Heltec.display->drawString(0, 0, rssi);
  //Heltec.display->display();
      //delay (10);
  //  }  

  //flagsinal = 0;
    
}
