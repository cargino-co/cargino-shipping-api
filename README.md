# Cargino Shipping API

Public HTTP API for calculating shipping offers for parcels to Iran.  
Designed to be simple for developers and safe to use in AI assistants and chatbots.

- Website: https://cargino.com  
- Developer docs: https://cargino.com/developers.php  
- OpenAPI spec: https://cargino.com/.well-known/openapi.yaml  

> Note: This repository provides public documentation, OpenAPI definition, and code examples for integrating with the Cargino Shipping API.

---

## Overview

The Cargino Shipping API exposes an HTTP endpoint which returns one or more shipping offers for a parcel being sent from an origin country to a destination country (typically Iran).

Current focus:

- Shipping from **China (CN)** and other supported countries to **Iran (IR)**  
- JSON responses with one or more offers (standard / express)  
- Simple query parameters (`from_country`, `to_country`, `weight_kg`, dimensions, currency)

---

## Base URL

Production base URL:

```text
https://cargino.com
```

### Endpoint

```text
GET /api/shipping-rate.php
```

---

## Query parameters

### Required

- `from_country` (string, ISO 3166-1 alpha-2)  
  Origin country code, e.g. `CN`, `TR`, `AE`.

- `to_country` (string, ISO 3166-1 alpha-2)  
  Destination country code. Typically `IR` for Iran.

- `weight_kg` (number)  
  Parcel weight in kilograms. Must be greater than 0.

### Optional

- `length_cm` (number)  
- `width_cm` (number)  
- `height_cm` (number)  
  Parcel dimensions in centimeters (used for volumetric weight if needed).

- `currency` (string, ISO 4217)  
  Desired currency for display, e.g. `EUR`, `USD`. If not provided, defaults to Cargino’s primary currency.

---

## Example request

### curl

```bash
curl "https://cargino.com/api/shipping-rate.php?from_country=CN&to_country=IR&weight_kg=2.3&currency=EUR"
```

### JavaScript (fetch)

```js
fetch("https://cargino.com/api/shipping-rate.php?from_country=CN&to_country=IR&weight_kg=2.3&currency=EUR")
  .then(response => response.json())
  .then(data => {
    console.log("Offers:", data.offers);
  })
  .catch(error => {
    console.error("Error calling Cargino API:", error);
  });
```

### Python (requests)

```python
import requests

params = {
    "from_country": "CN",
    "to_country": "IR",
    "weight_kg": 2.3,
    "currency": "EUR",
}

resp = requests.get("https://cargino.com/api/shipping-rate.php", params=params)
data = resp.json()
print("Offers:", data.get("offers"))
```

---

## Example JSON response

```json
{
  "provider": "Cargino",
  "from_country": "CN",
  "to_country": "IR",
  "weight_kg": 2.3,
  "currency": "EUR",
  "offers": [
    {
      "service_code": "CARGINO_STD_CN_IR",
      "service_name": "Cargino Standard from China to Iran",
      "delivery_type": "standard",
      "total_price": 39.90,
      "estimated_delivery_days_min": 9,
      "estimated_delivery_days_max": 14
    },
    {
      "service_code": "CARGINO_EXP_CN_IR",
      "service_name": "Cargino Express from China to Iran",
      "delivery_type": "express",
      "total_price": 49.90,
      "estimated_delivery_days_min": 5,
      "estimated_delivery_days_max": 9
    }
  ],
  "meta": {
    "version": "1.1",
    "generated_at": "2025-12-02T10:15:00Z"
  }
}
```

> The above values are examples for documentation purposes.  
> In production, prices and services depend on the live configuration.

---

## OpenAPI specification

A machine-readable OpenAPI 3.0 definition is available at:

- Online: https://cargino.com/.well-known/openapi.yaml  
- This repo: [`openapi/cargino-openapi.yaml`](openapi/cargino-openapi.yaml)

You can import this definition into:

- Postman  
- Swagger UI  
- API clients  
- AI tools that support OpenAPI-based integrations

---

## Postman collection

You can also explore and test the API using the public Postman collection:

- Postman: https://www.postman.com/karimimahan-3064307/cargino-shipping-api/collection/n6vnac7/cargino-shipping-api?action=share&creator=50511952

Fork this collection into your own workspace to experiment with the endpoint and integrate it into your applications.

---

## Error handling

On invalid input, the API returns an error object:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "weight_kg is required",
    "details": {
      "field": "weight_kg"
    }
  }
}
```

Common error codes:

- `INVALID_REQUEST` – missing or invalid parameters  
- `RATE_LIMIT_EXCEEDED` – too many requests (if enabled)  
- `INTERNAL_ERROR` – unexpected server error  

---

## Use cases

- Websites that need to show real-time shipping costs from China (and other origins) to Iran  
- Back-office tools for logistics and operations  
- AI assistants and chatbots that answer questions about shipping to Iran  
- Price comparison tools and shipping calculators

---

## Contact & support

For production access, rate limits, or technical questions:

- Website: https://cargino.com  
- Developer docs: https://cargino.com/developers.php  
- Email: support@cargino.com <!-- replace with your real support email -->
