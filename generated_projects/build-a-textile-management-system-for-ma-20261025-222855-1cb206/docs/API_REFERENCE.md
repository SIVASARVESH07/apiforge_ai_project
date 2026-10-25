# User Management API - API Reference Manual
**Version:** `1.0.0`  
**Base URL:** `http://localhost:8000`

Generated API based on requirements: Build a textile management system for managing fabrics, yarn, inventory, suppliers, and customer ord...

## Table of Contents
- [GET `/users`](#get-users)
- [POST `/users`](#post-users)
- [GET `/users/{user_id}`](#get-usersuser_id)
- [DELETE `/users/{user_id}`](#delete-usersuser_id)
- [GET `/orders`](#get-orders)
- [POST `/orders`](#post-orders)
- [GET `/orders/{order_id}`](#get-ordersorder_id)
- [DELETE `/orders/{order_id}`](#delete-ordersorder_id)
- [GET `/products`](#get-products)
- [POST `/products`](#post-products)
- [GET `/products/{product_id}`](#get-productsproduct_id)
- [DELETE `/products/{product_id}`](#delete-productsproduct_id)
- [GET `/customers`](#get-customers)
- [POST `/customers`](#post-customers)
- [GET `/customers/{customer_id}`](#get-customerscustomer_id)
- [DELETE `/customers/{customer_id}`](#delete-customerscustomer_id)

---

### <a id="get-users"></a>GET `/users`
**Summary:** List all users  
**Description:** List all users  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `limit` | `query` | `False` | `integer` | Maximum number of records to return |
| `offset` | `query` | `False` | `integer` | Number of records to skip for pagination |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/UserListResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/users" -H "Authorization: Bearer <TOKEN>"
```

### <a id="post-users"></a>POST `/users`
**Summary:** Create a new user  
**Description:** Create a new user  
🔒 **Authentication Required:** Bearer Token

#### Request Body (`application/json`):
Ref: `#/components/schemas/UserCreate`

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `201` | Resource created successfully | `#/components/schemas/UserResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X POST "http://localhost:8000/users" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{}'
```

### <a id="get-usersuser_id"></a>GET `/users/{user_id}`
**Summary:** Get user by ID  
**Description:** Get user by ID  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `user_id` | `path` | `True` | `string` | Unique identifier for user_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/UserResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/users/{user_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="delete-usersuser_id"></a>DELETE `/users/{user_id}`
**Summary:** Delete a user  
**Description:** Delete a user  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `user_id` | `path` | `True` | `string` | Unique identifier for user_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `204` | Resource deleted successfully | `None` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X DELETE "http://localhost:8000/users/{user_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="get-orders"></a>GET `/orders`
**Summary:** List all orders  
**Description:** List all orders  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `limit` | `query` | `False` | `integer` | Maximum number of records to return |
| `offset` | `query` | `False` | `integer` | Number of records to skip for pagination |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/OrderListResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/orders" -H "Authorization: Bearer <TOKEN>"
```

### <a id="post-orders"></a>POST `/orders`
**Summary:** Create a new order  
**Description:** Create a new order  
🔒 **Authentication Required:** Bearer Token

#### Request Body (`application/json`):
Ref: `#/components/schemas/OrderCreate`

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `201` | Resource created successfully | `#/components/schemas/OrderResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X POST "http://localhost:8000/orders" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{}'
```

### <a id="get-ordersorder_id"></a>GET `/orders/{order_id}`
**Summary:** Get order by ID  
**Description:** Get order by ID  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `order_id` | `path` | `True` | `string` | Unique identifier for order_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/OrderResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/orders/{order_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="delete-ordersorder_id"></a>DELETE `/orders/{order_id}`
**Summary:** Delete a order  
**Description:** Delete a order  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `order_id` | `path` | `True` | `string` | Unique identifier for order_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `204` | Resource deleted successfully | `None` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X DELETE "http://localhost:8000/orders/{order_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="get-products"></a>GET `/products`
**Summary:** List all products  
**Description:** List all products  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `limit` | `query` | `False` | `integer` | Maximum number of records to return |
| `offset` | `query` | `False` | `integer` | Number of records to skip for pagination |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/ProductListResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/products" -H "Authorization: Bearer <TOKEN>"
```

### <a id="post-products"></a>POST `/products`
**Summary:** Create a new product  
**Description:** Create a new product  
🔒 **Authentication Required:** Bearer Token

#### Request Body (`application/json`):
Ref: `#/components/schemas/ProductCreate`

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `201` | Resource created successfully | `#/components/schemas/ProductResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X POST "http://localhost:8000/products" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{}'
```

### <a id="get-productsproduct_id"></a>GET `/products/{product_id}`
**Summary:** Get product by ID  
**Description:** Get product by ID  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `product_id` | `path` | `True` | `string` | Unique identifier for product_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/ProductResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/products/{product_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="delete-productsproduct_id"></a>DELETE `/products/{product_id}`
**Summary:** Delete a product  
**Description:** Delete a product  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `product_id` | `path` | `True` | `string` | Unique identifier for product_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `204` | Resource deleted successfully | `None` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X DELETE "http://localhost:8000/products/{product_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="get-customers"></a>GET `/customers`
**Summary:** List all customers  
**Description:** List all customers  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `limit` | `query` | `False` | `integer` | Maximum number of records to return |
| `offset` | `query` | `False` | `integer` | Number of records to skip for pagination |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/CustomerListResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/customers" -H "Authorization: Bearer <TOKEN>"
```

### <a id="post-customers"></a>POST `/customers`
**Summary:** Create a new customer  
**Description:** Create a new customer  
🔒 **Authentication Required:** Bearer Token

#### Request Body (`application/json`):
Ref: `#/components/schemas/CustomerCreate`

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `201` | Resource created successfully | `#/components/schemas/CustomerResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X POST "http://localhost:8000/customers" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{}'
```

### <a id="get-customerscustomer_id"></a>GET `/customers/{customer_id}`
**Summary:** Get customer by ID  
**Description:** Get customer by ID  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `path` | `True` | `string` | Unique identifier for customer_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/CustomerResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/customers/{customer_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="delete-customerscustomer_id"></a>DELETE `/customers/{customer_id}`
**Summary:** Delete a customer  
**Description:** Delete a customer  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `customer_id` | `path` | `True` | `string` | Unique identifier for customer_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `204` | Resource deleted successfully | `None` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X DELETE "http://localhost:8000/customers/{customer_id}" -H "Authorization: Bearer <TOKEN>"
```
