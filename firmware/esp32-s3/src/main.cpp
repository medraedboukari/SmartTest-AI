
#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Orange";
const char* password = "Raaaed03";

const char* serverUrl =
    "http://192.168.100.103:8000/measurements";

void setup() {
    Serial.begin(115200);

    WiFi.begin(ssid, password);

    Serial.print("Connecting to WiFi");

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nWiFi connected!");
    Serial.println(WiFi.localIP());
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {

        HTTPClient http;

        http.begin(serverUrl);
        http.addHeader("Content-Type", "application/json");

        // Valeurs simulees pour le premier test
        String json =
            "{\"voltage\":3.3,\"current\":0.15}";

        int responseCode = http.POST(json);

        Serial.print("HTTP response: ");
        Serial.println(responseCode);

        if (responseCode > 0) {
            Serial.println(http.getString());
        }

        http.end();
    }

    delay(5000);
}
