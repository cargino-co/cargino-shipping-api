# Cargino API – `/api/shipping-rate.php` (Draft v1.1)

## Method & URL

- **Method:** `GET`  
- **Path:** `/api/shipping-rate.php`

## Purpose

Calculate shipping offers for a parcel being sent from a given origin country to a destination country (typically Iran), and return one or more priced offers.

## Query Parameters

- `from_country` (required, string, ISO2)  
  Origin country code, e.g. `CN`, `TR`, `AE`.

- `to_country` (required, string, ISO2)  
  Destination country code, e.g. `IR` for Iran.

- `weight_kg` (required, number)  
  Actual parcel weight in kilograms. Must be greater than 0.

- `length_cm` (optional, number)  
- `width_cm` (optional, number)  
- `height_cm` (optional, number)  
  Parcel dimensions in centimeters (used for volumetric weight if needed).

- `currency` (optional, string, ISO3)  
  Desired display currency, e.g. `EUR` or `USD`.  
  If not provided, defaults to Cargino’s primary currency.

## Example request

```bash
curl "https://cargino.com/api/shipping-rate.php?from_country=CN&to_country=IR&weight_kg=2.3&currency=EUR"
```

## Successful Response – 200 OK

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

## Error Response – 400 Bad Request

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

## Notes

- All responses are in JSON.  
- This is a mock/example contract; real prices depend on your live configuration.  
- For more details and OpenAPI spec, see: https://cargino.com/developers.php
