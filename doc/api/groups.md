# groups API

## グループ一覧取得 API

```
GET /api/groups
```

### レスポンス

#### 成功時

| param         | type   | description |
| ------------- | ------ | ----------- |
| groups[].id   | number | グループ ID |
| groups[].name | string | グループ名  |
| groups[].code | string | 招待コード  |

```javascript
{
    "groups": [
        {
            "id": number,
            "name": string,
            "code": string
        },
        ...
    ]
}
```

## グループ取得 API

```
GET /api/groups/{group_id}
```

### レスポンス

#### 成功時

| param | type   | description |
| ----- | ------ | ----------- |
| id    | number | グループ ID |
| name  | string | グループ名  |
| code  | string | 招待コード  |

```javascript
{
    "id": number,
    "name": string,
    "code": string
}
```

## グループ作成 API

```
POST /api/groups
```

| param | type   | description |
| ----- | ------ | ----------- |
| name  | string | グループ名  |

```javascript
{
    "name": string
}
```

### レスポンス

#### 成功時

| param | type   | description |
| ----- | ------ | ----------- |
| id    | number | グループ ID |
| name  | string | グループ名  |
| code  | string | 招待コード  |

```javascript
{
    "id": number,
    "name": string,
    "code": string
}
```

## グループ参加 API

```
POST /api/join
```

| param | type   | description |
| ----- | ------ | ----------- |
| code  | string | 招待コード  |

```javascript
{
    "code": string
}
```

### レスポンス

200 OK
