#include <Wire.h>
#include "i2c.h"
#include "i2c_MMA8451.h"
MMA8451 mma8451;

unsigned long currentTime = 0, timeAtFall = 0;
float currentAcc = 0;
int fallCount = 0;
float maxFallValue = 0;


void setup()
{
    Serial.begin(115200);

    Serial.print("Probe MMA8451: ");
    if (mma8451.initialize()) {
      Serial.println("Sensor found!");
      mma8451.setSensibility(8);
    }
    else
    {
        Serial.println("Sensor missing");
        while(1) {};
    }
}

void loop()
{   
    static float xyz_g[3];
    
    mma8451.getMeasurement(xyz_g);
    currentAcc = sqrt(pow(xyz_g[0], 2) + pow(xyz_g[1], 2) + pow(xyz_g[2], 2));

    // Suspected A fall happend (fall threshold: value >= 6)
    if (currentAcc >= 6.00 && fallCount == 0) {
      Serial.println(currentAcc);
      fallCount++;
      timeAtFall = millis();
      currentTime = millis();

      // Check for 2 seconds if an aftershock occured (aftershock threshold: value <=3
      while (currentTime - timeAtFall < 2000 ) {
        mma8451.getMeasurement(xyz_g);
        currentAcc = sqrt(pow(xyz_g[0], 2) + pow(xyz_g[1], 2) + pow(xyz_g[2], 2));
        Serial.println(currentAcc);
        if (maxFallValue < currentAcc) {
          maxFallValue = currentAcc;
        }
        currentTime = millis();
        delay(50);
      }

      // Take the maximun value of the testing above, if bigger then 3 suspected as an after shock
      if (maxFallValue >=3) {
        delay(50);
        mma8451.getMeasurement(xyz_g);
        currentAcc = sqrt(pow(xyz_g[0], 2) + pow(xyz_g[1], 2) + pow(xyz_g[2], 2));
        Serial.println(currentAcc);
        // Check if the currentAcc is below the aftershock threshold, if so a fall was detected.
        if (currentAcc < 3) {
          Serial.println("Fall Detected!");
        }
      }
      // Detected continuous movment and not a fall
      else if (maxFallValue >= 6) {
        fallCount = 0;
      }
    }
    
    delay(50);
}
