# Cargino Shipping API – curl examples

## China → Iran quote in EUR

```bash
curl "https://cargino.com/api/shipping-rate.php?from_country=CN&to_country=IR&weight_kg=2.3&currency=EUR"
```

## China → Iran quote without currency parameter

The API will return prices in its primary currency (for example, EUR):

```bash
curl "https://cargino.com/api/shipping-rate.php?from_country=CN&to_country=IR&weight_kg=1.0"
```
