const int LED = 17;
const int S_OK  = 0xaa;
const int S_ERR = 0xff;

void on_receive(void* event_handler_arg, esp_event_base_t event_base, int32_t event_id, void* event_data) {
  int val = USBSerial.read();
  // if (!(val < 255 && val > 0)) {
  //   USBSerial.write(S_ERR);
  //   return;
  // }

  analogWrite(LED, val);
  USBSerial.write(S_OK);

}
void setup() {
    pinMode(LED, OUTPUT);

    // for (int i = 0; i < 255; i++) {
    //   analogWrite(LED, i);
    //   delay(10);
    // }

    // for (int i = 255; i >= 0; i--) {
    //   analogWrite(LED, i);
    //   delay(10);
    // }
    
    // register "on_receive" as callback for RX event
    USBSerial.onEvent(ARDUINO_HW_CDC_RX_EVENT, on_receive);
    USBSerial.begin(9600);
}

void loop() { }