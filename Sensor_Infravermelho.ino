/*
 * Sensor Infravermelho
 *
 * Circuito:
 * - Arduino 5V -> Sensor's pin 1 (Vcc)
 * - Arduino GND -> Sensor's pin 2 (GND)
 * - Arduino pin A0 -> Sensor's pin 3 (Output)
 * 
 */

//import the library in the sketch
#include <SharpIR.h>

//Create a new instance of the library
//Call the sensor "sensor"
//The model of the sensor is "GP2YA41SK0F"
//The sensor output pin is attached to the pin A0
SharpIR sensor( SharpIR::GP2Y0A41SK0F, A0 );

void setup()
{
  Serial.begin( 9600 ); //Enable the serial comunication
}

void loop()
{
  int distance = sensor.getDistance(); //Calculate the distance in centimeters and store the value in a variable

 Serial.print("Distância medida: "); //IMPRIME O TEXTO NA SERIAL
  Serial.print(distance); //IMPRIME NA SERIAL A DISTÂNCIA MEDIDA PELO SENSOR
  Serial.println("cm"); //IMPRIME O TEXTO NA SERIAL
  delay(500); //INTERVALO DE 500 MILISSEGUNDOS
}
