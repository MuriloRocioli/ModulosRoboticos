/* 
*   Projeto CELESC - UFU
*   Codigo referente ao controle do Robo para remocao de Detritos
*
*   Autor: Murilo Rocioli
*/

#include "LoRaWan_APP.h"
#include "Arduino.h"
#include <Wire.h>  
#include "HT_SSD1306Wire.h"


#define RF_FREQUENCY                                915000000 // Hz

#define TX_OUTPUT_POWER                             5        // dBm

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

double txNumber;

bool lora_idle=true;

// Definições dos pinos dos botões
#define BUTTON_RECUAR 23
#define BUTTON_AVANCAR 2
#define BUTTON_AUTOMACAO 17

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );

SSD1306Wire  factory_display(0x3c, 500000, SDA_OLED, SCL_OLED, GEOMETRY_128_64, RST_OLED); // addr , freq , i2c group , resolution , rst

void setup() {
    Serial.begin(115200);
    Mcu.begin(HELTEC_BOARD,SLOW_CLK_TPYE);

    factory_display.init();
	  factory_display.clear();
	  factory_display.display();
    factory_display.drawString(0, 10, "CELESC UFU");
    factory_display.drawString(0, 20, "Robo Remoção Detritos");
	  delay(300);
	  factory_display.clear();

     pinMode(BUTTON_RECUAR, INPUT_PULLUP);
     pinMode(BUTTON_AVANCAR, INPUT_PULLUP);
     pinMode(BUTTON_AUTOMACAO, INPUT_PULLUP);
	
    txNumber=0;

    RadioEvents.TxDone = OnTxDone;
    RadioEvents.TxTimeout = OnTxTimeout;
    
    Radio.Init( &RadioEvents );
    Radio.SetChannel( RF_FREQUENCY );
    Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 ); 
   }



void loop()
{
	if (lora_idle == true) {
        delay(1000);
        
        int buttonState1 = digitalRead(BUTTON_RECUAR);
        int buttonState2 = digitalRead(BUTTON_AVANCAR);
        int buttonState3 = digitalRead(BUTTON_AUTOMACAO);

        if (buttonState1 == LOW) { // Assuming button is pressed when LOW
            sprintf(txpacket, "Comando: Recuar");
        } 

        if (buttonState2 == LOW) { // Assuming button is pressed when LOW
            sprintf(txpacket, "Comando: Avancar");
        } 

        if (buttonState3 == LOW) { // Assuming button is pressed when LOW
            sprintf(txpacket, "Comando: Automacao");
        } 

        Serial.printf("\r\nSending packet \"%s\" , length %d\r\n", txpacket, strlen(txpacket));
        factory_display.drawString(0, 10, txpacket);
        factory_display.display();
        delay(10);
        factory_display.clear();
        Radio.Send((uint8_t *)txpacket, strlen(txpacket)); // Send the package out    
        lora_idle = false;
    }
  Radio.IrqProcess( );
}

void OnTxDone( void )
{
	Serial.println("TX done......");
	lora_idle = true;
}

void OnTxTimeout( void )
{
    Radio.Sleep( );
    Serial.println("TX Timeout......");
    lora_idle = true;
}