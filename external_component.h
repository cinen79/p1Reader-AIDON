#pragma once
#include "esphome.h"

class MyCustomComponent : public Component {
 public:
   void setup() override {
     // Initialization code here
     ESP_LOGI("custom", "Custom Component Initialized!");
   }

   void loop() override {
     // Code to run in the main loop
   }
};
