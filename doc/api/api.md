# API Document

## [users API](./users.md)

## [groups API](./groups.md)

## [members API](./members.md)

## [reviews API](./reviews.md)

## カテゴリ一覧取得 API

## グループ取得 API

```
GET /api/categories
```

### レスポンス

#### 成功時

| param             | type   | description |
| ----------------- | ------ | ----------- |
| categories[].id   | number | カテゴリ ID |
| categories[].name | string | カテゴリ名  |

```javascript
{
    "categories": [
        {
            "id": number,
            "name": string,
        }
    ]
}
```
