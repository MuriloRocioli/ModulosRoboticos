/* 
*   Projeto CELESC - UFU
*   Codigo referente ao controle do Robo para instalação
*   de amortecedores do tipo Pré-Formado
*
*   Autor: Murilo Rocioli
*/

#include "LoRaWan_APP.h"
#include "Arduino.h"
#include <Wire.h>  
#include "HT_SSD1306Wire.h"
#include "images.h"

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

static RadioEvents_t RadioEvents;
void OnTxDone( void );
void OnTxTimeout( void );
void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr );

int16_t txNumber;
int16_t Rssi,rxSize;
bool lora_idle=true;

// Definições dos pinos dos botões
const byte PIN_BUTTON_A = 22;
const byte PIN_BUTTON_B = 23;
const byte PIN_BUTTON_C = 0;
const byte PIN_BUTTON_D = 17;

const byte PIN_ANALOG_X = 12;
//const byte PIN_ANALOG_Y = 13;

//Definição dos pinos da bateria
#define Vbat_Read 37
#define ADC_Ctrl 21

//Configuração OLED
SSD1306Wire  factory_display(0x3c, 500000, SDA_OLED, SCL_OLED, GEOMETRY_128_64, RST_OLED); // addr , freq , i2c group , resolution , rst


void setup() {
  Serial.begin(115200);
  Mcu.begin(HELTEC_BOARD,SLOW_CLK_TPYE);

  // Inicialização do display
  factory_display.init();
  factory_display.clear();
  
  // Desenhar o logotipo no display
  factory_display.drawXbm(0, 0, 128, 53, logo_aneel); // Ajuste o tamanho se necessário
  factory_display.display();
  delay(2000); // Manter o logotipo na tela por 5 segundos antes de prosseguir
  factory_display.clear();

  factory_display.drawXbm(0, 0, 128, 53, logo_celesc); // Ajuste o tamanho se necessário
  factory_display.display();
  delay(2000); // Manter o logotipo na tela por 5 segundos antes de prosseguir
  factory_display.clear();

  factory_display.drawXbm(0, 0, 128, 53, logo_ufu); // Ajuste o tamanho se necessário
  factory_display.display();
  delay(2000); // Manter o logotipo na tela por 5 segundos antes de prosseguir
  factory_display.clear();

  //Declaração dos botões
  pinMode(PIN_BUTTON_A, INPUT);
  digitalWrite(PIN_BUTTON_A, HIGH);

  pinMode(PIN_BUTTON_B, INPUT);
  digitalWrite(PIN_BUTTON_B, HIGH);

  pinMode(PIN_BUTTON_C, INPUT);
  digitalWrite(PIN_BUTTON_C, HIGH);

  pinMode(PIN_BUTTON_D, INPUT);
  digitalWrite(PIN_BUTTON_D, HIGH);
	
  txNumber=0;
  Rssi=0;

  RadioEvents.TxDone = OnTxDone;
  RadioEvents.TxTimeout = OnTxTimeout;
  RadioEvents.RxDone = OnRxDone;

  Radio.Init( &RadioEvents );
  Radio.SetChannel( RF_FREQUENCY );
  Radio.SetTxConfig( MODEM_LORA, TX_OUTPUT_POWER, 0, LORA_BANDWIDTH,
                                   LORA_SPREADING_FACTOR, LORA_CODINGRATE,
                                   LORA_PREAMBLE_LENGTH, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   true, 0, 0, LORA_IQ_INVERSION_ON, 3000 );

  Radio.SetRxConfig( MODEM_LORA, LORA_BANDWIDTH, LORA_SPREADING_FACTOR,
                                   LORA_CODINGRATE, 0, LORA_PREAMBLE_LENGTH,
                                   LORA_SYMBOL_TIMEOUT, LORA_FIX_LENGTH_PAYLOAD_ON,
                                   0, true, 0, 0, LORA_IQ_INVERSION_ON, true );

  factory_display.init();
  factory_display.clear();
  factory_display.setFont(ArialMT_Plain_10);
  factory_display.setTextAlignment(TEXT_ALIGN_LEFT);

  pinMode(ADC_Ctrl,OUTPUT);
  pinMode(Vbat_Read,INPUT);
  analogReadResolution(12);
  readBatteryVoltage();
}

void loop() {
  if (lora_idle == true) {
        delay(1000);
        
        int buttonStateA = digitalRead(PIN_BUTTON_A);
        int buttonStateB = digitalRead(PIN_BUTTON_B);
        int buttonStateC = digitalRead(PIN_BUTTON_C);
        int buttonStateD = digitalRead(PIN_BUTTON_D);
        int joystickX = analogRead(PIN_ANALOG_X);
        //int buttonStateY = analogRead(PIN_ANALOG_Y);

        // Tratar os valores do joystick
        int pwmValueX = 0;

        Serial.print("X:");
        Serial.print(analogRead(PIN_ANALOG_X));
        Serial.print(" ");

        // Mapear o joystick X (controle para frente e para trás)
        pwmValueX = joystickX*510/2700 - 255;
        sprintf(txpacket, "%d",pwmValueX);
        Serial.print("Pwm:");
        Serial.print(pwmValueX);
        Serial.print(" ");

        if (buttonStateA == LOW) {
            sprintf(txpacket, "A");
        } else {
            //sprintf(txpacket, "Aguardando...");
            sprintf(txpacket, "%d",pwmValueX);
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

void OnRxDone( uint8_t *payload, uint16_t size, int16_t rssi, int8_t snr )
{
    Rssi=rssi;
    rxSize=size;
    memcpy(rxpacket, payload, size );
    rxpacket[size]='\0';
    Radio.Sleep( );

    Serial.printf("\r\nreceived packet \"%s\" with Rssi %d , length %d\r\n",rxpacket,Rssi,rxSize);
    Serial.println("wait to send next packet");

    //state=STATE_TX;
}

uint16_t readBatteryVoltage() {
  
  // ADC resolution
  const int resolution = 12;
  const int adcMax = pow(2,resolution) - 1;
  const float adcMaxVoltage = 3.3;
  
  // On-board voltage divider
  const int R1 = 220;
  const int R2 = 100;
  
  // Calibration measurements
  const float measuredVoltage = 4.2;
  const float reportedVoltage = 3.82;
  
  // Calibration factor
  const float factor = (adcMaxVoltage / adcMax) * ((R1 + R2)/(float)R2) * (measuredVoltage / reportedVoltage);
  digitalWrite(ADC_Ctrl,LOW);
  delay(100);
  int analogValue = analogRead(Vbat_Read);
  digitalWrite(ADC_Ctrl,HIGH);

  float floatVoltage = factor * analogValue;
  uint16_t voltage = (int)(floatVoltage * 1000.0);

  Serial.print("[readBatteryVoltage] ADC : ");
  Serial.println(analogValue);
  Serial.print("[readBatteryVoltage] Float : ");
  Serial.println(floatVoltage,3);
  Serial.print("[readBatteryVoltage] milliVolts : ");
  Serial.println(voltage);

  factory_display.clear();
  factory_display.drawString(0,5,"Battery Level");
  factory_display.display();
  factory_display.drawString(0,25, String(floatVoltage) + " Volts");
  factory_display.display();

  return voltage;
}