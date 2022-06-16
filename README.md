# newcombin_python
Desafio Back-end

# Manual de funcionamiento REST API TAXES

El objetivo de la API es disponibilizar endpoints para recibir
información transaccional en línea

# REST API

Los endpoints de la REST API  están descritos a continuación:

## Crear boleta

### Request

`POST /boleta/`

    {
            "tipo": "luz",
            "descripcion": "Edenor S.A.",
            "fecha": "2022-06-16",
            "importe": "100.00",
            "estado": "pending"
        }

### Response
Debería devolver el código de barras autogenerado
    {
            "codigoBarra": 1,
            "tipo": "luz",
            "descripcion": "Edenor S.A.",
            "fecha": "2022-06-16",
            "importe": "100.00",
            "estado": "pending"
        }

## Realizar pago

### Request

`POST /transaction/`

    
### Response

    {
      "payment_method": "debit_card",
      "credit_card_number": "1229292202022",
      "amount": "50.22",
      "barcode": "1",
      "payment_date": "2022-06-15"
    }

## Listar boletas impagas con / sin filtro

### Request

`GET /boletas/impagas` http://127.0.0.1:8000/boletas/impagas

### Response

    [
    {
        "tipo": "luz",
        "fecha": "2022-06-16",
        "importe": "0.00",
        "codigoBarra": 1
    },
    {
        "tipo": "luz",
        "fecha": "2022-06-16",
        "importe": "100.00",
        "codigoBarra": 6
    }
]

## Con filtro

### Request

`GET /boletas/impagas/luz`

    http://127.0.0.1:8000/boletas/impagas/luz

### Response
[
    {
        "fecha": "2022-06-16",
        "importe": "0.00",
        "codigoBarra": 1
    },
    {
        "fecha": "2022-06-16",
        "importe": "100.00",
        "codigoBarra": 6
    }
]

