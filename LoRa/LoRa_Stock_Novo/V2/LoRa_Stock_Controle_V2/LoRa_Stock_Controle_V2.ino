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
const byte PIN_BUTTON_A = 22;
const byte PIN_BUTTON_B = 23;
const byte PIN_BUTTON_C = 0;
const byte PIN_BUTTON_D = 17;

const byte PIN_ANALOG_X = 12;
const byte PIN_ANALOG_Y = 13;

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
	  delay(2000);
	  factory_display.clear();
  
    pinMode(PIN_BUTTON_A, INPUT);
    digitalWrite(PIN_BUTTON_A, HIGH);

    pinMode(PIN_BUTTON_B, INPUT);
    digitalWrite(PIN_BUTTON_B, HIGH);

    pinMode(PIN_BUTTON_C, INPUT);
    digitalWrite(PIN_BUTTON_C, HIGH);

    pinMode(PIN_BUTTON_D, INPUT);
    digitalWrite(PIN_BUTTON_D, HIGH);
	
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
        
        int buttonStateA = digitalRead(PIN_BUTTON_A);
        int buttonStateB = digitalRead(PIN_BUTTON_B);
        int buttonStateC = digitalRead(PIN_BUTTON_C);
        int buttonStateD = digitalRead(PIN_BUTTON_D);
        int buttonStateX = analogRead(PIN_ANALOG_X);
        int buttonStateY = analogRead(PIN_ANALOG_Y);

        if (buttonStateA == LOW) {
            sprintf(txpacket, "A");
        } else {
            sprintf(txpacket, "Aguardando...");
        }
        
        if (buttonStateB == LOW) {
            sprintf(txpacket, "B");
        }

        if (buttonStateC == LOW) {
            sprintf(txpacket, "C");
        }

        if (buttonStateD == LOW) {
            sprintf(txpacket, "D");
        }

        if (buttonStateX >= 2700) {
            sprintf(txpacket, "Avancar");
        }

        if (buttonStateX <= 100) {
            sprintf(txpacket, "Recuar");
        }

        Serial.print("X:");
        Serial.print(analogRead(PIN_ANALOG_X));
        Serial.print(" ");

        Serial.print("Y:");
        Serial.print(analogRead(PIN_ANALOG_Y));
        Serial.print(" ");
        

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