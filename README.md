# theatreAPI
theatreAPI is built using Django and Django Rest Framework (DRF) and it provides endpoints for booking tickets and getting details.

## Endpoints

### 1. occupy

 #### URL
* /occupy

####  Method
* It supports **POST** request only and requires data in JSON format 

#### Description
* Occupy seat - [Endpoint URL - /occupy/ ] The Endpoint will be given the person's name and ticket ID (this should be a UUID field, tickets will not contain information about the seat number beforehand) as input and outputs the seat number which will be occupied. If the seating is full, the appropriate error message is returned.

#### Request Body
```javascript
{
  "name" : string
}
```

#### Return Code
* It returns 200 Response code if the request is successfully executed
* It returns 400 Response code if the request data is not correct 

#### Response body

```javascript
{
  "seatnumber" : integer
}
```

### 2. vacate 
 #### URL
* /vacate/<seatnumber\>


#### Method
* It supports **DELETE** request only and requires valid seatnumber in url

#### Description
*  Vacate seat - [Endpoint URL - **/vacate/** ]: This endpoint takes the seat number which the person will be vacating and frees that slot up to be used by other people.


#### Return Code
* It returns 200 Response code if the request is successfully executed.
* It returns 404 Response code if the request seat number does not exist. 

#### Response body
* If successfull
```javascript
{
  "success" : "delete successful"
}
```
* if unsuccessful
```javascript
{
  "failure" : "delete failed"
}
```

### get_info

 #### URL
* /getinfo/<name or seatnumber or ticketid\>

#### Method
* It supports GET request only.

#### Description
* Get Person/Seat information - [Endpoint URL - /get_info/<NAME or SEATNUM or TICKETID> ]: This endpoint can take either the seat number or person’s name or ticket ID for the input and returns the person’s name, ticket ID, and slot number.

#### Return Code
* It returns 200 Response code if the request is successfully executed
* It returns 400 Response code if the request data is not correct 

#### Response body

```javascript
{
  "name" : string,
  "seatnumber" : integer,
  "ticket id" : uuid
  
}
```



## Status Codes

theatreAPI returns the following status codes in its API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

