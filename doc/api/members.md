# members API

## メンバー一覧取得 API

```
GET /api/groups/{group_id}/members
```

### レスポンス

#### 成功時

| param                   | type   | description |
| ----------------------- | ------ | ----------- |
| members[].id            | number | グループ ID |
| members[].name          | string | グループ名  |
| members[].review_counts | number | 投稿件数    |

```javascript
{
    "members":[
        {
            "id": number,
            "name": string,
            "review_counts": number
        }
        ...
    ]
}
```

## メンバーの情報取得 API

```
GET /api/groups/{group_id}/members/{user_id}
```

### レスポンス

#### 成功時

| param                   | type   | description |
| ----------------------- | ------ | ----------- |
| user_id                 | number | ユーザー ID |
| user_name               | string | ユーザー名  |
| review_counts           | number | 投稿件数    |
| reviews[].id            | number | レビュー ID |
| reviews[].name          | string | 店舗名      |
| reviews[].note          | string | 内容        |
| reviews[].category_name | string | カテゴリ名  |
| reviews[].category_id   | name   | カテゴリ ID |
| reviews[].star          | number | スター数    |

```javascript
{
    "user_id": number,
    "user_name": string,
    "review_counts": number,
    "reviews": [
        {
            "id": number,
            "name": string,
            "note": string,
            "category_name": string,
            "category_id": number,
            "star": number
        },
        ...
    ]
}
```
