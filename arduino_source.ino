#include <Tle493d_w2b6.h>

Tle493d_w2b6 Tle493dMagnetic3DSensor = Tle493d_w2b6();
void setup() {
  Serial.begin(9600);
  while (!Serial);
  // for bugs need to di this 
  Tle493dMagnetic3DSensor.begin();
  Tle493dMagnetic3DSensor.begin();
  Tle493dMagnetic3DSensor.disableTemp();
  // digitalWrite(14, HIGH);
  // digitalWrite(15, HIGH);
}

void loop() {
  Tle493dMagnetic3DSensor.updateData();
 // Serial.println(Tle493dMagnetic3DSensor.getPolar()*(180/3.1459)); // only polar angle
  Serial.println(Tle493dMagnetic3DSensor.getAzimuth()*(180/3.1459)); // Azimuth angle
  
  delay(500);
}

