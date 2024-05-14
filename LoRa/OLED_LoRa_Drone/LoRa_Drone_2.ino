#include "heltec.h"

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

  Serial.begin(115200);

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

  //Define os pinos de saída
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(21, OUTPUT);
}

void loop()
{
  //*****************************************
  //*****************************************
  //ROTINA DE RECEPCAO DO SINAL DA LORA DA TERRA
  //*****************************************
  //*****************************************  
  
  int packetSize = LoRa.parsePacket();
  if (packetSize){cbk(packetSize);}

  packet = (char)LoRa.read();//LE MENSAGEM VINDA DA LORA DA TERRA

  //Serial.print(packet);
  //Serial.println(" "); // em s

      //Heltec.display->clear();
 // Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  //Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawStringMaxWidth(0, 32, 128, packet);
 // Heltec.display->drawString(0, 0, rssi);
 // Heltec.display->display();
  //    delay (10);

  if (packet == "1")
  {
      Serial.println("1");
      //delay(50);
      //delay(5);
      
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
      Serial.println("2");
      //delay(50);    
      //delay(5);

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

      //Serial.println("3");
      //Serial.println(" "); // em s      
      //delay(5);

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
      //Serial.println("4");
      //Serial.println(" "); // em s
      //delay(5);
      
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
      //Serial.println(" "); // em s      
      //delay(5);

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
      
      //Serial.println("6");
      //Serial.println(" "); // em s      
      //delay(5);

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
      
      //Serial.println("7");
      //Serial.println(" "); // em s      
      //delay(5);

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
      //Serial.println("8");
      //Serial.println(" "); // em s      
      //delay(5);

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
      Serial.println("9");
      //Serial.println(" "); // em s      
      //delay(5);

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
      Serial.println("0");
      //Serial.println(" "); // em s      
      //delay(5);

      Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  Heltec.display->drawStringMaxWidth(0, 32, 128, "V10");
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
      delay (10);
    }

  //Heltec.display->clear();
  //Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  //Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawStringMaxWidth(0, 32, 128, "RECEBIDO");
  //Heltec.display->drawString(0, 0, rssi);
  //Heltec.display->display();
/*
  Heltec.display->clear();
  Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawStringMaxWidth(0, 32, 128, "RETORNO");
  Heltec.display->drawString(0, 0, rssi);
  Heltec.display->display();
*/
//  delay(500);

  
  //*****************************************
  //*****************************************
  //ROTINA DE ENVIO DO SINAL PARA LORA DA TERRA
  //*****************************************
  //*****************************************  

  packet = (char)Serial.read(); //LE MENSAGEM VINDA DO RASPBERRY

  //Serial.print(packet);
  //Serial.println(" "); // em s

      //Heltec.display->clear();
 // Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
  //Heltec.display->setFont(ArialMT_Plain_24);
  //Heltec.display->drawStringMaxWidth(0, 32, 128, packet);
 // Heltec.display->drawString(0, 0, rssi);
 // Heltec.display->display();
  //    delay (10);

  if (packet == "a" and packet != packet_old)
  {

//ENVIO DO PACOTE PRA OUTRA LORA
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 'a';
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "DIST");
    Heltec.display->drawString(40, 26, "RUIM");
    Heltec.display->display();

    packet_old = packet;
    }
    
  if (packet == "b" and packet != packet_old)
  {
//ENVIO DO PACOTE PRA OUTRA LORA
    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 'b';
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "DIST");
    Heltec.display->drawString(40, 26, "MEDIA");
    Heltec.display->display();

    packet_old = packet;
      
    }

  if (packet == "c" and packet != packet_old)
  {
//ENVIO DO PACOTE PRA OUTRA LORA

    LoRa.beginPacket();
    LoRa.setTxPower(14, RF_PACONFIG_PASELECT_PABOOST);
    //LoRa.print("Pacote: ");
    num = 'c';
    LoRa.print(num);
    LoRa.endPacket();

    Heltec.display->clear();
    Heltec.display->setTextAlignment(TEXT_ALIGN_LEFT);
    Heltec.display->setFont(ArialMT_Plain_24);

    Heltec.display->drawString(20, 0, "DIST");
    Heltec.display->drawString(40, 26, "BOA");
    Heltec.display->display();

    packet_old = packet;
      
    }

    
 // flagsinal = 0;
}
