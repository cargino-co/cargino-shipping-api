# Example: Calling Cargino Shipping API from Python using requests

import requests

params = {
    "from_country": "CN",
    "to_country": "IR",
    "weight_kg": 2.3,
    "currency": "EUR",
}

response = requests.get("https://cargino.com/api/shipping-rate.php", params=params)

if response.status_code != 200:
    print("Error:", response.status_code, response.text)
else:
    data = response.json()
    print("Cargino shipping offers:")
    for offer in data.get("offers", []):
        print(
            "- {name} ({code}): {price} {currency}, {min}-{max} days".format(
                name=offer.get("service_name"),
                code=offer.get("service_code"),
                price=offer.get("total_price"),
                currency=data.get("currency"),
                min=offer.get("estimated_delivery_days_min"),
                max=offer.get("estimated_delivery_days_max"),
            )
        )
