# Test Bank API

URL http://avigael-test-bank-api.herokuapp.com/

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

`GET /api?amount={number}`
note: only 8 accounts avalible

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
