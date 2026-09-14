
const int PIN_LED = 2;
const int boton = 13;

void setup() {
  pinMode(boton, INPUT_PULLUP);
  pinMode(PIN_LED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int estado = digitalRead(boton);

  if (estado == LOW) {
    Serial.println("PULSADO");
    digitalWrite(PIN_LED, HIGH);
  } else {
    Serial.println("SUELTO");
    digitalWrite(PIN_LED, LOW);
  }

  delay(100);
}
