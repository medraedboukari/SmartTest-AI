
const products = [
    {
        id: 1,
        name: "ESP32-S3 DevKit",
        category: "Microcontrollers",
        price: 18.50,
        description: "ESP32-S3 development board with Wi-Fi and Bluetooth connectivity.",
        specifications: "Dual-core processor, 2.4 GHz Wi-Fi, Bluetooth 5 LE, 3.3V logic."
    },
    {
        id: 2,
        name: "LM7805 Voltage Regulator",
        category: "Power Management",
        price: 2.50,
        description: "Linear voltage regulator providing a stable 5V DC output.",
        specifications: "Input: 7V-20V, Output: 5V, Maximum current: 1A."
    },
    {
        id: 3,
        name: "AMS1117-3.3",
        category: "Power Management",
        price: 1.80,
        description: "Low dropout voltage regulator for 3.3V electronic circuits.",
        specifications: "Input: 4.5V-12V, Output: 3.3V, Maximum current: 800mA."
    },
    {
        id: 4,
        name: "Electrolytic Capacitor 1000uF",
        category: "Capacitors",
        price: 1.20,
        description: "Electrolytic capacitor used for filtering and voltage stabilization.",
        specifications: "Capacitance: 1000uF, Rated voltage: 25V."
    },
    {
        id: 5,
        name: "Resistor 220 Ohm",
        category: "Resistors",
        price: 0.10,
        description: "General-purpose resistor for electronic circuits.",
        specifications: "Resistance: 220 Ohm, Tolerance: 5%, Power: 0.25W."
    },
    {
        id: 6,
        name: "BME280 Sensor",
        category: "Sensors",
        price: 8.90,
        description: "Environmental sensor measuring temperature, humidity and pressure.",
        specifications: "Temperature, relative humidity and atmospheric pressure."
    }
];

const productList = document.getElementById("product-list");

products.forEach(product => {
    const card = document.createElement("div");

    card.className = "product-card";

    card.innerHTML = `
        <h3>${product.name}</h3>
        <p><strong>Category:</strong> ${product.category}</p>
        <p>${product.description}</p>
        <p><strong>Specifications:</strong> ${product.specifications}</p>
        <p class="price">$${product.price.toFixed(2)}</p>
    `;

    productList.appendChild(card);
});
