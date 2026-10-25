# Item Management API - API Reference Manual
**Version:** `1.0.0`  
**Base URL:** `http://localhost:8000`

Generated API based on requirements: design a supermarket management api...

## Table of Contents
- [GET `/items`](#get-items)
- [POST `/items`](#post-items)
- [GET `/items/{item_id}`](#get-itemsitem_id)
- [DELETE `/items/{item_id}`](#delete-itemsitem_id)

---

### <a id="get-items"></a>GET `/items`
**Summary:** List all items  
**Description:** List all items  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `limit` | `query` | `False` | `integer` | Maximum number of records to return |
| `offset` | `query` | `False` | `integer` | Number of records to skip for pagination |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/ItemListResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/items" -H "Authorization: Bearer <TOKEN>"
```

### <a id="post-items"></a>POST `/items`
**Summary:** Create a new item  
**Description:** Create a new item  
🔒 **Authentication Required:** Bearer Token

#### Request Body (`application/json`):
Ref: `#/components/schemas/ItemCreate`

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `201` | Resource created successfully | `#/components/schemas/ItemResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X POST "http://localhost:8000/items" -H "Authorization: Bearer <TOKEN>" -H "Content-Type: application/json" -d '{}'
```

### <a id="get-itemsitem_id"></a>GET `/items/{item_id}`
**Summary:** Get item by ID  
**Description:** Get item by ID  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `item_id` | `path` | `True` | `string` | Unique identifier for item_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `200` | Successful operation | `#/components/schemas/ItemResponse` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X GET "http://localhost:8000/items/{item_id}" -H "Authorization: Bearer <TOKEN>"
```

### <a id="delete-itemsitem_id"></a>DELETE `/items/{item_id}`
**Summary:** Delete a item  
**Description:** Delete a item  
🔒 **Authentication Required:** Bearer Token

#### Parameters:
| Name | In | Required | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `item_id` | `path` | `True` | `string` | Unique identifier for item_id |

#### Responses:
| Status Code | Description | Schema |
| :--- | :--- | :--- |
| `204` | Resource deleted successfully | `None` |
| `400` | Bad Request / Validation Failure | `#/components/schemas/ErrorResponse` |
| `401` | Unauthorized / Missing Token | `#/components/schemas/ErrorResponse` |
| `404` | Resource Not Found | `#/components/schemas/ErrorResponse` |

#### Example cURL:
```bash
curl -X DELETE "http://localhost:8000/items/{item_id}" -H "Authorization: Bearer <TOKEN>"
```
