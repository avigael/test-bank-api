# Test Bank API
This API generates a list of account in the following format

```json
{
	"date": "2020-05-13T21:53:23.108Z",
	"company": "Sample Company",
	"amount": 44.02
}
```

### Get a List of Accounts

**Definition**

`GET /api?amount={amn ∈ [0, 8]}`

**Response**

- `200 OK` on success

**Example**

`GET /api?amount=2`

```json
[
    {
		"date": "2020-05-13T21:53:23.108Z",
		"company": "Sample Company",
		"amount": 44.02
    },
    {
		"date": "2020-05-13T21:53:23.108Z",
		"company": "Sample & Sample LLC",
		"amount": 5100.22
    }
]
```