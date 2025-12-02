// Example: Calling Cargino Shipping API from JavaScript (browser / Node.js)

const params = new URLSearchParams({
  from_country: "CN",
  to_country: "IR",
  weight_kg: "2.3",
  currency: "EUR",
});

fetch("https://cargino.com/api/shipping-rate.php?" + params.toString())
  .then((response) => {
    if (!response.ok) {
      throw new Error("HTTP error " + response.status);
    }
    return response.json();
  })
  .then((data) => {
    console.log("Cargino shipping offers:", data.offers);
  })
  .catch((error) => {
    console.error("Error calling Cargino Shipping API:", error);
  });
