#define RELAY_PIN 7

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');
    command.trim();
    
    if (command == "0") {
      digitalWrite(RELAY_PIN, HIGH);
    } else if (command == "1") {
      digitalWrite(RELAY_PIN, LOW);
    }
  }
}
