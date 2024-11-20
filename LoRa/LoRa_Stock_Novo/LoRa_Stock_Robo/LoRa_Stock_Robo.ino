/* 
*   Projeto CELESC - UFU
*   Codigo referente ao Robo para remocao de Detritos
*
*   Autor: Murilo Rocioli
*/

#include "LoRaWan_APP.h"
#include "Arduino.h"


#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             14        // dBm

#define LORA_BANDWIDTH                              0         // [0: 125 kHz,
                                                              //  1: 250 kHz,
                                                              //  2: 500 kHz,
                                                              //  3: Reserved]
#define LORA_SPREADING_FACTOR                       7         // [SF7..SF12]
#define LORA_CODINGRATE                             1         // [1: 4/5,
                                                              //  2: 4/6,
                                                              //  3: 4/7,
                                                              //  4: 4/8]
#define LORA_PREAMBLE_LENGTH                        8         // Same for Tx and Rx
#define LORA_SYMBOL_TIMEOUT                         0         // Symbols
#define LORA_FIX_LENGTH_PAYLOAD_ON                  false
#define LORA_IQ_INVERSION_ON                        false


#define RX_TIMEOUT_VALUE                            1000
#define BUFFER_SIZE                                 30 // Define the payload size here

char txpacket[BUFFER_SIZE];
char rxpacket[BUFFER_SIZE];

static RadioEvents_t RadioEvents;

int16_t txNumber;

int16_t rssi,rxSize;

bool lora_idle = true;

//Motor translação motorredutor
#define MOTOR_A_PIN1 23
#define MOTOR_A_PIN2 17

//Motor translação amortecedor
#define MOTOR_B_PIN1 0
#define MOTOR_B_PIN2 22

//Motorredutor
#define MOTOR_C_PIN1 12
#define MOTOR_C_PIN2 13

//Motor pinças
#define MOTOR_D_PIN1 33
#define MOTOR_D_PIN2 35

//Motor movimentação
#define MOTOR_E_PIN1 1
#define MOTOR_E_PIN2 3



bool com_recuar = 0;
bool com_avancar = 0;

void setup() {
    Serial.begin(115200);
    Mcu.begin(HELTEC_BOARD,SLOW_CLK_TPYE);

    pinMode(MOTOR_A_PIN1, OUTPUT);
    pinMode(MOTOR_A_PIN2, OUTPUT);

    pinMode(MOTOR_B_PIN1, OUTPUT);
    pinMode(MOTOR_B_PIN2, OUTPUT);

    pinMode(MOTOR_C_PIN1, OUTPUT);
    pinMode(MOTOR_C_PIN2, OUTPUT);

    pinMode(MOTOR_D_PIN1, OUTPUT);
    pinMode(MOTOR_D_PIN2, OUTPUT);

    pinMode(MOTOR_E_PIN1, OUTPUT);
    pinMode(MOTOR_E_PIN2, OUTPUT);
    
    digitalWrite(MOTOR_A_PIN1, LOW);
    digitalWrite(MOTOR_A_PIN2, LOW);

    digitalWrite(MOTOR_B_PIN1, LOW);
    digitalWrite(MOTOR_B_PIN2, LOW);

    digitalWrite(MOTOR_C_PIN1, LOW);
    digitalWrite(MOTOR_C_PIN2, LOW);

    digitalWrite(MOTOR_D_PIN1, LOW);
    digitalWrite(MOTOR_D_PIN2, LOW);

    digitalWrite(MOTOR_E_PIN1, LOW);
    digitalWrite(MOTOR_E_PIN2, LOW);
    
    txNumber=0;
    rssi=0;
  
    RadioEvents.RxDone = OnRxDone;
    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetRxConfig( MODEM_LORA, LORA_BANDWIDTH, LORA_SPREADING_FACTOR,
                               LORA_CODINGRATE, 0, LORA_PREAMBLE_LENGTH,
                               LORA_SYMBOL_TIMEOUT, LORA_FIX_LENGTH_PAYLOAD_ON,
                               0, true, 0, 0, LORA_IQ_INVERSION_ON, true );
}



void loop()
{
  if(lora_idle)
  {
    lora_idle = false;
    Serial.println("into RX mode");
    Radio.Rx(0);
  }
  Radio.IrqProcess( );

  //Inserção dos comandos de avanço e recuo dos motores
  // Avanço
  /*if (com_avancar == 1) {
    digitalWrite(MOTOR_PIN1, LOW);
    digitalWrite(MOTOR_PIN2, HIGH);

    Serial.printf("Avancando \n");
  }

  //Recuo
  if (com_recuar == 1) {
    digitalWrite(MOTOR_PIN1, HIGH);
    digitalWrite(MOTOR_PIN2, LOW);

    Serial.printf("Recuando \n");
  }

  if(com_recuar == 0 && com_avancar == 0){
    digitalWrite(MOTOR_PIN1, LOW);
    digitalWrite(MOTOR_PIN2, LOW);
  }*/
}

void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr )
{
    rssi=rssi;
    rxSize=size;
    memcpy(rxpacket, payload, size );
    rxpacket[size]='\0';
    Radio.Sleep( );
    Serial.printf("\r\nreceived packet \"%s\" with rssi %d , length %d\r\n",rxpacket,rssi,rxSize);
    
    if (strcmp(rxpacket, "Recuar") == 0) {
      com_recuar = 1;
    }
    else{
      com_recuar = 0;
    }

    if (strcmp(rxpacket, "Avancar") == 0) {
      com_avancar = 1;
    }
    else{
      com_avancar = 0;
    }

    //Eletroima
    if (strcmp(rxpacket, "A") == 0) {
        /*digitalWrite(AUTOMACAO_PIN1, HIGH);
        digitalWrite(AUTOMACAO_PIN2, LOW);

        delay(2500);

        digitalWrite(AUTOMACAO_PIN1, LOW);
        digitalWrite(AUTOMACAO_PIN2, HIGH);

        delay(2250);

        digitalWrite(AUTOMACAO_PIN1, LOW);
        digitalWrite(AUTOMACAO_PIN2, LOW);*/

        Serial.printf("Eletroima \n");  
    }  
    
    //Automacao
    if (strcmp(rxpacket, "C") == 0) {
        digitalWrite(MOTOR_A_PIN1, HIGH);
        digitalWrite(MOTOR_A_PIN2, LOW);

        delay(5000);

        digitalWrite(MOTOR_A_PIN1, LOW);
        digitalWrite(MOTOR_A_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_B_PIN1, HIGH);
        digitalWrite(MOTOR_B_PIN2, LOW);

        delay(3000);

        digitalWrite(MOTOR_B_PIN1, LOW);
        digitalWrite(MOTOR_B_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_C_PIN1, HIGH);
        digitalWrite(MOTOR_C_PIN2, LOW);

        delay(3000);

        digitalWrite(MOTOR_C_PIN1, LOW);
        digitalWrite(MOTOR_C_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_D_PIN1, HIGH);
        digitalWrite(MOTOR_D_PIN2, LOW);

        delay(3000);

        digitalWrite(MOTOR_D_PIN1, LOW);
        digitalWrite(MOTOR_D_PIN2, LOW);

        delay(5000);

        //Volta
        digitalWrite(MOTOR_A_PIN1, LOW);
        digitalWrite(MOTOR_A_PIN2, HIGH);

        delay(5000);

        digitalWrite(MOTOR_A_PIN1, LOW);
        digitalWrite(MOTOR_A_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_B_PIN1, LOW);
        digitalWrite(MOTOR_B_PIN2, HIGH);

        delay(3000);

        digitalWrite(MOTOR_B_PIN1, LOW);
        digitalWrite(MOTOR_B_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_C_PIN1, LOW);
        digitalWrite(MOTOR_C_PIN2, HIGH);

        delay(3000);

        digitalWrite(MOTOR_C_PIN1, LOW);
        digitalWrite(MOTOR_C_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_D_PIN1, LOW);
        digitalWrite(MOTOR_D_PIN2, HIGH);

        delay(3000);

        digitalWrite(MOTOR_D_PIN1, LOW);
        digitalWrite(MOTOR_D_PIN2, LOW);

        Serial.printf("Automacao \n");  
    } 

    //Avancar
    if (strcmp(rxpacket, "B") == 0) {
        digitalWrite(MOTOR_E_PIN1, HIGH);
        digitalWrite(MOTOR_E_PIN2, LOW);

        delay(1000);

        digitalWrite(MOTOR_E_PIN1, LOW);
        digitalWrite(MOTOR_E_PIN2, LOW);

        Serial.printf("Avancar \n");  
    }
    
    if (strcmp(rxpacket, "D") == 0) {
        digitalWrite(MOTOR_E_PIN1, LOW);
        digitalWrite(MOTOR_E_PIN2, HIGH);

        delay(1000);

        digitalWrite(MOTOR_E_PIN1, LOW);
        digitalWrite(MOTOR_E_PIN2, LOW);

        Serial.printf("Avancar \n");  
    } 
    
    
    lora_idle = true;
}