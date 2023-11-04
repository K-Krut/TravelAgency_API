# Internationalization

На проекте доступно два языка - uk / ru - то есть украинский и русский соответственно. 

Для того, что бы контент приходил на определенном языке, одном из доступных, нужно определить хедер Accept-Language в запросе и в value добавить код языка.

### Headers:

Accept-Language: uk / ru 

По дефолту контент будет приходить на украинском, но можно явно указывать код `uk`. Если нужно что бы контент приходил на русском, то `Accept-Language` должно быть установлено как `ru`. Если указать какой-то другой код, то будет так же приходить на украинском.

# Tours List

## General

Method: GET

Endpoint: /api/v1/tours

### Query params:

`season → str → filter response by season` 

`duration → int → filter response by duration date_start and date_end` 
`ordering → str → ordering response according to the selected parameter` 

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**400** - *error*

### Response Fields:

? - optional 

- id
- name
- date_start
- date_end
- price
- free_places
- season
- ? images

### Response Example:

```jsx
/api/tours

{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "Brendachester",
            "date_start": "2023-10-01",
            "date_end": "2023-10-08",
            "price": 7664,
            "free_places": 48,
            "season": "Летний"
        },
        {
            "id": 4,
            "name": "Leeview",
            "date_start": "2023-10-04",
            "date_end": "2023-10-09",
            "price": 1376,
            "free_places": 21,
            "season": "Летний"
        },
        {
            "id": 6,
            "name": "New Williamburgh",
            "date_start": "2023-10-12",
            "date_end": "2023-10-17",
            "price": 4194,
            "free_places": 5,
            "season": "Осенний"
        },
        {
            "id": 5,
            "name": "Patrickshire",
            "date_start": "2023-10-23",
            "date_end": "2023-10-30",
            "price": 6271,
            "free_places": 6,
            "season": "Осенний",
            "images": "https://images.unsplash.com/photo-1672238387412-f45ad4b2a1da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2FycGF0aGlhbiUyMG1vdW50YWlufGVufDB8MHwwfHx8Mg%3D%3D&w=1000&q=80"
        },
        {
            "id": 2,
            "name": "West Jared",
            "date_start": "2023-10-28",
            "date_end": "2023-10-31",
            "price": 4559,
            "free_places": 0,
            "season": "Зимний"
        },
        {
            "id": 1,
            "name": "asd",
            "date_start": "2023-10-14",
            "date_end": "2023-10-14",
            "price": 12,
            "free_places": 12,
            "season": "Летний"
        }
    ]
}
```

---

## Pagination

Method: GET

EndPoint: /api/v1/tours?page={page_number}

### Query params:

**all** **parameters of past urls**

### Response status:

**200** - *success*

**400** - *error*

### Request Example:

Pagination page - 1

 /api/v1/tours

- Response example:
    
    ```jsx
    {
        "count": 46,
        "next": "http://127.0.0.1:8000/api/v1/tours?page=2",
        "previous": null,
        "results": [
            {
                "id": 32,
                "name": "Alexanderberg",
                "date_start": "2023-10-06",
                "date_end": "2023-10-13",
                "price": 2915,
                "free_places": 10,
                "season": "Летний"
            },
            {
                "id": 38,
                "name": "Anthonymouth",
                "date_start": "2023-10-28",
                "date_end": "2023-11-04",
                "price": 1907,
                "free_places": 25,
                "season": "Зимний"
            },
            {
                "id": 21,
                "name": "Benjaminport",
                "date_start": "2023-10-29",
                "date_end": "2023-11-03",
                "price": 2855,
                "free_places": 39,
                "season": "Весенний"
            },
            {
                "id": 3,
                "name": "Brendachester",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 7664,
                "free_places": 48,
                "season": "Летний"
            },
            {
                "id": 30,
                "name": "Briannafort",
                "date_start": "2023-10-27",
                "date_end": "2023-10-30",
                "price": 3184,
                "free_places": 17,
                "season": "Зимний",
                "images": "https://images.unsplash.com/photo-1484911579927-b3f008130467?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8Y2FycGF0aGlhbiUyMG1vdW50YWlufGVufDB8MHwwfHx8Mg%3D%3D&w=1000&q=80"
            },
            {
                "id": 7,
                "name": "Brittneyton",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 2370,
                "free_places": 15,
                "season": "Весенний"
            },
            {
                "id": 25,
                "name": "Coxborough",
                "date_start": "2023-10-23",
                "date_end": "2023-10-30",
                "price": 6643,
                "free_places": 50,
                "season": "Весенний"
            },
            {
                "id": 27,
                "name": "Craigfort",
                "date_start": "2023-10-24",
                "date_end": "2023-10-27",
                "price": 8297,
                "free_places": 31,
                "season": "Осенний"
            }
        ]
    }
    ```
    

Paginaton page - 2

/api/v1/tours?page=2

- Response example:
    
    ```jsx
    {
        "count": 46,
        "next": "http://127.0.0.1:8000/api/v1/tours?page=3",
        "previous": "http://127.0.0.1:8000/api/v1/tours",
        "results": [
            {
                "id": 34,
                "name": "Cynthiamouth",
                "date_start": "2023-10-20",
                "date_end": "2023-10-24",
                "price": 6340,
                "free_places": 41,
                "season": "Летний",
                "images": "https://images.unsplash.com/photo-1476400424721-e25994a9f0ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fG1vdW50YWlucyUyMGZvcmVzdHxlbnwwfDB8MHx8fDI%3D&w=1000&q=80"
            },
            {
                "id": 13,
                "name": "Danielport",
                "date_start": "2023-10-06",
                "date_end": "2023-10-13",
                "price": 9042,
                "free_places": 29,
                "season": "Летний"
            },
            {
                "id": 36,
                "name": "East Felicia",
                "date_start": "2023-10-02",
                "date_end": "2023-10-06",
                "price": 3118,
                "free_places": 1,
                "season": "Летний"
            },
            {
                "id": 28,
                "name": "East Michaelland",
                "date_start": "2023-10-27",
                "date_end": "2023-11-01",
                "price": 4875,
                "free_places": 41,
                "season": "Зимний",
                "images": "https://images.unsplash.com/photo-1528659670414-57f81928182d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTh8fGNhcnBhdGhpYW4lMjBtb3VudGFpbnxlbnwwfDB8MHx8fDI%3D&w=1000&q=80"
            },
            {
                "id": 44,
                "name": "Edwardfurt",
                "date_start": "2023-10-27",
                "date_end": "2023-10-30",
                "price": 4624,
                "free_places": 21,
                "season": "Осенний"
            },
            {
                "id": 8,
                "name": "Gilmoreberg",
                "date_start": "2023-10-06",
                "date_end": "2023-10-09",
                "price": 8480,
                "free_places": 6,
                "season": "Зимний"
            },
            {
                "id": 45,
                "name": "Jennifermouth",
                "date_start": "2023-10-28",
                "date_end": "2023-11-04",
                "price": 7486,
                "free_places": 1,
                "season": "Весенний"
            },
            {
                "id": 16,
                "name": "Jesustown",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1393,
                "free_places": 76,
                "season": "Летний"
            }
        ]
    }
    ```
    

---

## Filtering

Endpoint:  /api/v1/tours?{filter_field}={filter_param}

### Query params:

`season → str → filter response by season` 

`duration → int → filter response by duration date_start and date_end` 

### Request exemple

/api/v1/tours?season=Летний

- Response Example
    
    ```jsx
    /api/v1/tours?season=Летний
    {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 3,
                "name": "Brendachester",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 7664,
                "free_places": 48,
                "season": "Летний"
            },
            {
                "id": 4,
                "name": "Leeview",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1376,
                "free_places": 21,
                "season": "Летний"
            },
            {
                "id": 1,
                "name": "asd",
                "date_start": "2023-10-14",
                "date_end": "2023-10-14",
                "price": 12,
                "free_places": 12,
                "season": "Летний"
            }
        ]
    }
    ```
    

/api/v1/tours?season=Летний&duration=3

- Response Example
    
    ```jsx
    /api/v1/tours?season=Летний&duration=3
    
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name": "West Jared",
                "date_start": "2023-10-28",
                "date_end": "2023-10-31",
                "price": 4559,
                "free_places": 0,
                "season": "Зимний"
            }
        ]
    }
    ```
    

---

## Sorting

Endpoint: /api/v1/tours?ordering={order_parameter}

### Query params:

- id - sort by id
- name - sort by name tour
- date_start - sort by date_start
- date_end - sort by date_end
- price - sort by price
- free_places - sort by free places
- season - sort by season
- images - sort by images

### Прямой порядок:

/api/v1/tours?ordering=price

- Response Example:
    
    ```jsx
    /api/v1/tours?ordering=price
    
    {
        "count": 6,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "asd",
                "date_start": "2023-10-14",
                "date_end": "2023-10-14",
                "price": 12,
                "free_places": 12,
                "season": "Летний"
            },
            {
                "id": 4,
                "name": "Leeview",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1376,
                "free_places": 21,
                "season": "Летний"
            },
            {
                "id": 6,
                "name": "New Williamburgh",
                "date_start": "2023-10-12",
                "date_end": "2023-10-17",
                "price": 4194,
                "free_places": 5,
                "season": "Осенний"
            },
            {
                "id": 2,
                "name": "West Jared",
                "date_start": "2023-10-28",
                "date_end": "2023-10-31",
                "price": 4559,
                "free_places": 0,
                "season": "Зимний"
            },
            {
                "id": 5,
                "name": "Patrickshire",
                "date_start": "2023-10-23",
                "date_end": "2023-10-30",
                "price": 6271,
                "free_places": 6,
                "season": "Осенний",
                "images": "https://images.unsplash.com/photo-1672238387412-f45ad4b2a1da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2FycGF0aGlhbiUyMG1vdW50YWlufGVufDB8MHwwfHx8Mg%3D%3D&w=1000&q=80"
            },
            {
                "id": 3,
                "name": "Brendachester",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 7664,
                "free_places": 48,
                "season": "Летний"
            }
        ]
    }
    ```
    

/api/v1/tours?ordering=free_places

- Response Example:
    
    ```jsx
    /api/v1/tours?ordering=free_places
    
    {
        "count": 6,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name": "West Jared",
                "date_start": "2023-10-28",
                "date_end": "2023-10-31",
                "price": 4559,
                "free_places": 0,
                "season": "Зимний"
            },
            {
                "id": 6,
                "name": "New Williamburgh",
                "date_start": "2023-10-12",
                "date_end": "2023-10-17",
                "price": 4194,
                "free_places": 5,
                "season": "Осенний"
            },
            {
                "id": 5,
                "name": "Patrickshire",
                "date_start": "2023-10-23",
                "date_end": "2023-10-30",
                "price": 6271,
                "free_places": 6,
                "season": "Осенний",
                "images": "https://images.unsplash.com/photo-1672238387412-f45ad4b2a1da?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Y2FycGF0aGlhbiUyMG1vdW50YWlufGVufDB8MHwwfHx8Mg%3D%3D&w=1000&q=80"
            },
            {
                "id": 1,
                "name": "asd",
                "date_start": "2023-10-14",
                "date_end": "2023-10-14",
                "price": 12,
                "free_places": 12,
                "season": "Летний"
            },
            {
                "id": 4,
                "name": "Leeview",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1376,
                "free_places": 21,
                "season": "Летний"
            },
            {
                "id": 3,
                "name": "Brendachester",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 7664,
                "free_places": 48,
                "season": "Летний"
            }
        ]
    ```
    

### Обратный порядок

/api/v1/tours?ordering=-price

- Response Example:
    
    ```jsx
    {
        "count": 46,
        "next": "http://127.0.0.1:8000/api/v1/tours?ordering=-price&page=2",
        "previous": null,
        "results": [
            {
                "id": 22,
                "name": "South Courtneyport",
                "date_start": "2023-10-30",
                "date_end": "2023-11-06",
                "price": 9957,
                "free_places": 31,
                "season": "Осенний"
            },
            {
                "id": 41,
                "name": "Taylorton",
                "date_start": "2023-10-29",
                "date_end": "2023-11-01",
                "price": 9723,
                "free_places": 51,
                "season": "Осенний"
            },
            {
                "id": 20,
                "name": "Wardburgh",
                "date_start": "2023-10-11",
                "date_end": "2023-10-14",
                "price": 9569,
                "free_places": 12,
                "season": "Зимний"
            },
            {
                "id": 10,
                "name": "Lake Sara",
                "date_start": "2023-10-21",
                "date_end": "2023-10-28",
                "price": 9473,
                "free_places": 18,
                "season": "Осенний"
            },
            {
                "id": 13,
                "name": "Danielport",
                "date_start": "2023-10-06",
                "date_end": "2023-10-13",
                "price": 9042,
                "free_places": 29,
                "season": "Летний"
            },
            {
                "id": 8,
                "name": "Gilmoreberg",
                "date_start": "2023-10-06",
                "date_end": "2023-10-09",
                "price": 8480,
                "free_places": 6,
                "season": "Зимний"
            },
            {
                "id": 15,
                "name": "Warnershire",
                "date_start": "2023-10-10",
                "date_end": "2023-10-15",
                "price": 8357,
                "free_places": 38,
                "season": "Зимний",
                "images": "https://images.unsplash.com/photo-1678904595514-570132b4a661?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8Y2FycGF0aGlhbiUyMG1vdW50YWlufGVufDB8MHwwfHx8Mg%3D%3D&w=1000&q=80"
            },
            {
                "id": 27,
                "name": "Craigfort",
                "date_start": "2023-10-24",
                "date_end": "2023-10-27",
                "price": 8297,
                "free_places": 31,
                "season": "Осенний"
            }
        ]
    }
    ```
    

/api/v1/tours?ordering=-free_places

- Response Example:
    
    ```jsx
    {
        "count": 46,
        "next": "http://127.0.0.1:8000/api/v1/tours?ordering=-free_places&page=2",
        "previous": null,
        "results": [
            {
                "id": 37,
                "name": "North Rhonda",
                "date_start": "2023-10-06",
                "date_end": "2023-10-11",
                "price": 7491,
                "free_places": 95,
                "season": "Осенний",
                "images": "https://images.unsplash.com/photo-1484910697931-0c8e7194d937?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGNhcnBhdGhpYW4lMjBtb3VudGFpbnxlbnwwfDB8MHx8fDI%3D&w=1000&q=80"
            },
            {
                "id": 42,
                "name": "South Ryan",
                "date_start": "2023-10-05",
                "date_end": "2023-10-08",
                "price": 3176,
                "free_places": 78,
                "season": "Осенний"
            },
            {
                "id": 16,
                "name": "Jesustown",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1393,
                "free_places": 76,
                "season": "Летний"
            },
            {
                "id": 14,
                "name": "Port Robert",
                "date_start": "2023-10-03",
                "date_end": "2023-10-06",
                "price": 8141,
                "free_places": 71,
                "season": "Зимний",
                "images": "https://images.unsplash.com/photo-1581545089841-9423c2ec0548?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8Y2FycGF0aGlhbnN8ZW58MHx8MHx8fDI%3D&w=1000&q=80"
            },
            {
                "id": 31,
                "name": "North Cynthiaport",
                "date_start": "2023-10-08",
                "date_end": "2023-10-13",
                "price": 1332,
                "free_places": 64,
                "season": "Осенний"
            },
            {
                "id": 41,
                "name": "Taylorton",
                "date_start": "2023-10-29",
                "date_end": "2023-11-01",
                "price": 9723,
                "free_places": 51,
                "season": "Осенний"
            },
            {
                "id": 25,
                "name": "Coxborough",
                "date_start": "2023-10-23",
                "date_end": "2023-10-30",
                "price": 6643,
                "free_places": 50,
                "season": "Весенний"
            },
            {
                "id": 3,
                "name": "Brendachester",
                "date_start": "2023-10-01",
                "date_end": "2023-10-08",
                "price": 7664,
                "free_places": 48,
                "season": "Летний"
            }
        ]
    }
    ```
    

### Несколько параметров

/api/v1/tours?ordering=free_places&ordering=price

Сортировка сначала по цене в прямом порядке, а потом 

по количеству свободных мест в прямом порядке

- Response Example:
    
    ```jsx
    {
        "count": 46,
        "next": "http://127.0.0.1:8000/api/v1/tours?ordering=free_places&ordering=price&page=2",
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "asd",
                "date_start": "2023-10-14",
                "date_end": "2023-10-14",
                "price": 12,
                "free_places": 12,
                "season": "Летний"
            },
            {
                "id": 31,
                "name": "North Cynthiaport",
                "date_start": "2023-10-08",
                "date_end": "2023-10-13",
                "price": 1332,
                "free_places": 64,
                "season": "Осенний"
            },
            {
                "id": 4,
                "name": "Leeview",
                "date_start": "2023-10-04",
                "date_end": "2023-10-09",
                "price": 1376,
                "free_places": 21,
                "season": "Летний"
            }
        ]
    }
    ```
    

---

# Featured Tours List

Method: GET

Endpoint: /api/v1/tours/featured

### Query params:

`null`

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**400** - *error*

### Response Fields:

? - optional 

- id
- name
- date_start
- date_end
- price
- free_places
- season
- ? images

### Response example:

```jsx
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 3,
            "name": "Brendachester",
            "date_start": "2023-10-01",
            "date_end": "2023-10-08",
            "price": 7664,
            "free_places": 48,
            "season": "Летний"
        },
        {
            "id": 4,
            "name": "Leeview",
            "date_start": "2023-10-04",
            "date_end": "2023-10-09",
            "price": 1376,
            "free_places": 21,
            "season": "Летний"
        },
        {
            "id": 6,
            "name": "New Williamburgh",
            "date_start": "2023-10-12",
            "date_end": "2023-10-17",
            "price": 4194,
            "free_places": 5,
            "season": "Осенний"
        },
        {
            "id": 1,
            "name": "asd",
            "date_start": "2023-10-14",
            "date_end": "2023-10-14",
            "price": 12,
            "free_places": 12,
            "season": "Летний"
        }
    ]
}
```

---

# Tours Search

Method: GET

Endpoint: /api/v1/tours/?search={search_word}

### Query params:

`search -> str > important words for name or id` 

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**400** - *error*

### Response Fields:

? - optional 

- id
- name
- date_start
- date_end
- price
- free_places
- season
- ? images

### Response example

/api/v1/tours/?search=2

- Response example:
    
    ```jsx
    /api/v1/tours/?search=2
    
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "name": "West Jared",
                "date_start": "2023-10-28",
                "date_end": "2023-10-31",
                "price": 4559,
                "free_places": 0,
                "season": "Зимний"
            }
        ]
    }
    
    ```
    

/api/v1/tours/?search=asd

- Response example:
    
    ```jsx
    127.0.0.1:8000/api/v1/tours/?search=asd
    
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "name": "asd",
                "date_start": "2023-10-14",
                "date_end": "2023-10-14",
                "price": 12,
                "free_places": 12,
                "season": "Летний"
            }
        ]
    }
    ```
    

---

# Tours Details

METHOD: GET

Endpoint: /api/v1/tours/{tour_id}

### Query params:

`id -> int -> primary key id for tour`

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**400** - *error*

### Response Fields:

? - optional 

- id
- name
- date_start
- date_end
- price
- free_places
- season
- ? images
- landmarks
- program
- options
- additional_options
- duration

### Response example:

/api/v1/tours/4/

- Response example:
    
    ```jsx
    /api/v1/tours/4/
    
    {
        "id": 2,
        "name": "West Jared",
        "date_start": "2023-10-28",
        "date_end": "2023-10-31",
        "price": 4559,
        "free_places": 0,
        "season": "Зимний",
        "duration": 3,
        "images": [],
        "landmarks": [
            {
                "name": "Переїзд",
                "image_url": "https://images.unsplash.com/photo-1600298882525-1ac025c98b68?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OXx8bGFrZSUyMG1vdW50YWlucyUyMGZvcmVzdHxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80"
            },
            {
                "name": "Екскурсійна програма",
                "image_url": "https://images.unsplash.com/photo-1551906993-e173e9c1466c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8bW91bnRhaW5zJTIwc2F1bmF8ZW58MHx8MHx8fDA%3D&w=1000&q=80"
            }
        ],
        "program": [
            {
                "name": "1",
                "options": [
    								"Спортивне спорядження",
                    "Спортивне спорядження",
                    "Пікнік з вершинами",
                    "Спортивне спорядження",
                    "Супровід гіда протягом всього туру",
                    "Спортивне спорядження",
                    "Виселення",
                    "Вечеря",
                    "Переїзд",
                    "Фотозвіт",
                    "Трансфер",
                    "Супровід гіда протягом всього туру",
                    "Супровід гіда протягом всього туру",
                    "Супровід гіда протягом всього туру",
                    "Спортивне спорядження",
                    "Виселення",
                    "Виселення",
                    "Вечеря"
                ]
            },
            {
                "name": "2",
                "options": [
                    "Виселення",
                    "Фотозвіт",
                    "Дорога додому",
                    "Дорога додому",
                    "Вечеря",
                    "Сніданок в готелі",
                    "Виселення",
                    "Сніданок в готелі",
                    "Пікнік з вершинами",
                    "Спортивне спорядження",
                    "Дорога додому"
                ]
            },
            {
                "name": "3",
                "options": [
                    "Сніданок в готелі",
                    "Сніданок в готелі",
                    "Пікнік з вершинами",
                    "Вечеря",
                    "Чани",
                    "Виселення",
                    "Пікнік з вершинами"
                ]
            },
            {
                "name": "4",
                "options": [
                    "Фотозвіт",
                    "Трансфер",
                    "Фотозвіт",
                    "Сніданок в готелі",
                    "Обід",
                    "Сніданок в готелі"
                ]
            },
            {
                "name": "5",
                "options": [
                    "Супровід гіда протягом всього туру",
                    "Пікнік з вершинами",
                    "Вечеря",
                    "Обід",
                    "Фотозвіт"
                ]
            },
            {
                "name": "6",
                "options": [
                    "Трансфер",
                    "Трансфер",
                    "Переїзд",
                    "Спортивне спорядження",
                    "Чани",
                    "Трансфер"
                ]
            },
            {
                "name": "7",
                "options": [
                    "Пікнік з вершинами",
                    "Супровід гіда протягом всього туру",
                    "Трансфер",
                    "Чани",
                    "Трансфер",
                    "Пікнік з вершинами"
                ]
            }
        ],
        "options": [
            {
                "name": "Переїзд",
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/bed.svg"
            },
            {
                "name": "Екскурсійна програма",
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/cheese.svg"
            },
            {
                "name": "Харчування",
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/cheese.svg"
            }
        ],
        "additional_options": [
            {
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/bus.svg",
                "name": "Харчування"
            },
            {
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/guide.svg",
                "name": "Спортивне спорядження"
            },
            {
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/other.svg",
                "name": "Проживання"
            },
            {
                "icon": "https://github.com/ivmitcompany/TravelAgency_API/blob/dev/images_faking/icons/options/breakfast.svg",
                "name": "Екскурсійна програма"
            }
        ]
    }
    ```
    

---

# Tours Details for Order

Method: GET

Endpoint: /api/v1/tours/{tour_id}/order/info

### Query params:

`id -> int -> primary key id for tour`

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**404** - *error,* Tour not found

500 - error, Server Error

503 - error, Request timeout

### Response Fields:

? - optional 

- id
- name
- date_start
- date_end
- price
- free_places
- season
- ? images

### Response example:

/api/v1/tours/4/order/info

```jsx
/api/v1/tours/4/order/info

{
    "id": 4,
    "name": "Leeview",
    "date_start": "2023-10-04",
    "date_end": "2023-10-09",
    "price": 1376,
    "free_places": 30,
    "season": "Літо",
    "images": "https://images.unsplash.com/photo-1623785745260-e07bd6754e82?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGNhcnBhdGhpYW4lMjBtb3VudGFpbnxlbnwwfDB8MHx8fDI%3D&w=1000&q=80"
}
```

---

# Make Order

Method: POST

Endpoint: /api/v1/tours/{tour_id}/order/payment

### Description:

Это первый ендпоинт, который нужно прокинуть при заказе. Если нет ошибок, то будет создана новая запись в таблице заказов: сгенерированный уникальный код заказа, добавлена информация о выбранном туре и ожидаемой к оплате стоимостью, статус оплаты 

### Body:

```python
{
    "tour_id": 4, // айди тура
    "cost": 9000, // должно проверяться 
    "passengers": [ // все пассажиры с формы ордера
        {
            "name": "User_name", // имя пассажира 
            "surname": "User_surname", // фамилия пассажира
            "phone": "+380730000000", // мобильный номер пассажира
            "is_primary_contact": true, // для главного пассажира, тот, кто оформляет заказ (есть номер мобильного)
        },
        {
            "name": "User_name_2", // имя пассажира
            "surname": "User_surname_2", // фамилия пассажира
        },
        {
            "name": "User_name_2",
            "surname": "User_surname_2",
        }
    ]
}
```

### Headers:

Accept-Language: uk / ru 

### Response status:

**200** - *success*

**400** - error*:*

- Number of passengers must be more than 1 - Если в боди не передаем пустой массив `passengers` или вообще не передаем параметр `passengers`
- Not enough available places in this tour for your order - *Если приходит попытка добавить заказ с большим количеством пассажиров, чем сейчас доступно на туре*
- You are trying to pay with incorrect cost - Если пришел запрос, где общая сумма к оплате (параметр `cost`) не соответствует реальной сумме для этого тура подсчитанной для переданного количества пассажиров (`passengers`)

404 - error:

- Tour not found - Тура с таким айди не существует
- Неправильный запрос

500 - error :

- Failed Order creation in DB - Если по какой-то причине не вышло создать запись Order в БД
- Attempt to retrieve data for payment from Liqpay failed - Если не вышло получить обьект для оплаты через Liqpay

### Response Fields:

Параметры, которые нужно передавать на страницу для оплаты через Liqpay

? - optional 

- data
- signature

### Response Example:

```json
{
    "data": "eyJhY3Rpb24iOiAicGF5IiwgImFtb3VudCI6IDQxMjgsICJjdXJyZW5jeSI6ICJVQUgiLCAiZGVzY3JpcHRpb24iOiAiXHUwNDIyXHUwNDQzXHUwNDQwIExlZXZpZXcgXHUwNDM0XHUwNDNiXHUwNDRmIDMgXHUwNDNmXHUwNDMwXHUwNDQxXHUwNDMwXHUwNDM2XHUwNDM4XHUwNDQwXHUwNDU2XHUwNDMyIiwgIm9yZGVyX2lkIjogMzE1MDUzLCAidmVyc2lvbiI6ICIzIiwgInNhbmRib3giOiAxLCAic2VydmVyX3VybCI6ICJodHRwOi8vMTI3LjAuMC4xOjgwMDAvcGF5LWNhbGxiYWNrLyIsICJwdWJsaWNfa2V5IjogInNhbmRib3hfaTE5MzE4MTU1MDQ3In0=",
    "signature": "dzLcUN1RyKgU5EmTtUwh/uGH7wk="
}
```

---

# Check Payment

Method: POST

Endpoint: /api/v1/pay-callback?data={payment_data}&signature={payment_signature}

### Query params:

`data -> int -> primary key id for tour`

`signature -> int -> primary key id for tour`

### Headers:

Accept-Language: uk / ru 

### Description:

Это второй ендпоинт, который нужно прокинуть при заказе. Он нужен для проверки статуса и подтверждения существования оплаты в Liqpay.  Если нет ошибок, то будет обновлена запись заказа в бд и на туре отнимется количество забронированных мест

### Response status:

**200** - *success*

404 - error:

- Неправильный запрос

402 - error:

- status = error
    
    ```json
    {
        "code": "payment_not_found",
        "err_code": "payment_not_found",
        "err_description": "Платеж не найден",
        "result": "error",
        "status": "error"
    }
    ```
    

500 - error :

- Attempt to retrieve data for payment from Liqpay failed - Если не вышло получить обьект об оплате от Liqpay
- Если не вышло обновить данные на ордере
- Если не вышло получить данные об ордере для респонса

### Response Fields:

Параметры, которые нужно передавать на страницу для оплаты через Liqpay

? - optional 

- token

### Response Example:

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmRlcl9wayI6MjcsImV4cCI6MTY5OTE4NjM2OH0.K6GU0N4AZbL4khLBHtEM7zKCfwpS1HunzcjzMtx4MOU"
}
```

---

# Get Payment Successful Order Info

Method: POST

Endpoint: /api/v1/pay-callback/successful/

### Headers:

Accept-Language: uk / ru 

`Barer Token: Token` 

### Description:

Это третий ендпоинт, который нужно прокинуть после проверки на то, что заказ успешный. Он нужен для того что бы секьюрно получать данные об оплаченном заказе.

### Response status:

**200** - *success*

404 - error:

- Invalid token. Order code is missing in the token. - После докодинга из токена не вышло получить код заказа
- Invalid token. Order not found. - За ордер кодом, зашифрованным в токене не вышло получить заказа, заказа с таким кодом не существует в бд.

403 - error:

- Invalid or expired token - Если время жизни токена уже истекло или указан некорректный токен.

500 - error:

- Can not get response info. - Произошла ошибка при попытки получения информации о заказе.

### Response Fields:

Параметры, которые нужно передавать на страницу для оплаты через Liqpay

? - optional 

- tour
    - id
    - name
    - date_start
    - date_end
    - price
    - free_places
    - season
    - ? images
- sumpaid
- order_code

### Response Example:

```json
{
    "tour": {
        "id": 4,
        "name": "Leeview",
        "date_start": "2023-10-04",
        "date_end": "2023-10-09",
        "price": 1376,
        "free_places": 12,
        "season": "Літо",
        "images": "https://images.unsplash.com/photo-1623785745260-e07bd6754e82?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGNhcnBhdGhpYW4lMjBtb3VudGFpbnxlbnwwfDB8MHx8fDI%3D&w=1000&q=80"
    },
    "sumpaid": 4128,
    "order_code": 909197
}
```

---

# Check Client Info Page Code

Method: POST

Endpoint:  /api/v1/order/client-info/{order_code}/check-code

### Body:

```json
{
    "code": 794647
}
```

### Headers:

Accept-Language: uk / ru - *может принимать, но нет смысла*

### Description:

Этот ендпоинт мы отправляем для проверки кода. Код проверяется для того пассажира заказа, который отмечен как *primary point of contact.* То есть есть только один подходящий код для каждого заказа. Если код для этого заказа правильный - будет возвращен токен, который нужен для получения информации об заказе. Токен живет 1 час с момента получения, спустя это время он сгорает и получить по нему информацию не выйдет, нужно получить новый токен и только после этого можно будет получить информацию о заказе

### Response status:

**200** - *success*

404 - error:

- Order not found - Если не существует ордера с таким кодом (каждый код уникальный)
- Неправильный запрос

400- error:

- Invalid verification code. - Если указанный код - неправильный

500 - error :

- Can not get verification code. - Если не для этого заказа не найдено пассажира, где `is_primary_contact=True` или у такого пассажира по какой-то причине не указан verification code в БД.

### Response Fields:

Параметры, которые нужно передавать на страницу для оплаты через Liqpay

? - optional 

- token

### Response Example:

```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcmRlcl9jb2RlIjoiMjU2NDM0IiwiZXhwIjoxNjk4OTY5MDU0fQ.-CQYS38GEzfMdWeKnS6F33A4iVbQ7WgNg-VCnPcp7s0"
}
```

---

# Get Client Order Info

Method: GET

Endpoint: /api/v1/order/client-info/

### Headers:

Accept-Language: uk / ru 

`Barer Token: Token` 

### Description:

Этот ендпоинт предназначен для получения информации об заказе, получить информацию можно только указав токен доступа. Больше ничего указывать не нужно, потому что в токен вшивается код заказа.

### Response status:

**200** - *success*

404 - error:

- Invalid token. Order code is missing in the token. - После докодинга из токена не вышло получить код заказа
- Invalid token. Order not found. - За ордер кодом, зашифрованным в токене не вышло получить заказа, заказа с таким кодом не существует в бд.

403 - error:

- Invalid or expired token - Если время жизни токена уже истекло или указан некорректный токен.

500 - error:

- Can not get response info. - Произошла ошибка при попытки получения информации о заказе.

### Response Fields:

Параметры, которые нужно передавать на страницу для оплаты через Liqpay

? - optional 

- tour
    - id
    - name
    - date_start
    - date_end
    - price
    - free_places
    - season
    - ? images
- sumpaid
- order_code

### Response Example:

```json
{
    "tour": {
        "id": 32,
        "name": "Південь Майкл",
        "date_start": "2023-10-06",
        "date_end": "2023-10-13",
        "price": 2915,
        "free_places": 9,
        "season": "Літо"
    },
    "sumpaid": 2915,
    "order_code": "256434",
    "passengers": [
        {
            "name": "gdfg",
            "surname": "dfgdfgdf",
            "phone": "+38 (444) 444 44 44",
            "place": 9
        }
    ]
}
```
