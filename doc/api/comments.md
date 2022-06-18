# comments API

## コメント一覧取得 API

```
GET /api/groups/{group_id}/comments
        ?q=&category=&sort_target=&order=
```

| param       | type   | description                                                  |
| ----------- | ------ | ------------------------------------------------------------ |
| q           | string | 検索文字列(完全一致)                                         |
| category    | number | カテゴリ ID                                                  |
| sort_target | string | ソート対象<br><br>以下から選択<br>- name<br>- star<br>- date |
| order       | string | ソート順<br><br>以下から選択<br>- asc<br>- desc              |

### レスポンス

#### 成功時

| param                    | type   | description |
| ------------------------ | ------ | ----------- |
| comments[].id            | number | レビュー ID |
| comments[].name          | string | 店舗名      |
| comments[].note          | string | 内容        |
| comments[].user_id       | number | ユーザー ID |
| comments[].user_name     | string | ユーザー名  |
| comments[].category_name | string | カテゴリ名  |
| comments[].category_id   | name   | カテゴリ ID |
| comments[].star          | number | スター数    |

```javascript
{
    "comments": [
        {
            "id": number,
            "name": string,
            "user_id": number,
            "user_name": string,
            "note": string,
            "category_name": string,
            "category_id": number,
            "star": number
        },
        ...
    ]
}
```

## コメント取得 API

```
GET /api/groups/{group_id}/comments/{comment_id}
```

### レスポンス

#### 成功時

| param         | type   | description |
| ------------- | ------ | ----------- |
| id            | number | レビュー ID |
| name          | string | 店舗名      |
| note          | string | 内容        |
| user_id       | number | ユーザー ID |
| user_name     | string | ユーザー名  |
| category_name | string | カテゴリ名  |
| category_id   | name   | カテゴリ ID |
| star          | number | スター数    |

```javascript
{
    "id": number,
    "name": string,
    "user_id": number,
    "user_name": string,
    "note": string,
    "category_name": string,
    "category_id": number,
    "star": number
}
```

## コメント投稿 API

```
POST /api/groups/{group_id}/comments
```

| param       | type   | description |
| ----------- | ------ | ----------- |
| name        | string | 店舗名      |
| note        | string | 内容        |
| category_id | name   | カテゴリ ID |
| star        | number | スター数    |

```javascript
{
    "name": string,
    "note": string,
    "category_id": number,
    "star": number
}
```

### レスポンス

#### 成功時

| param         | type   | description |
| ------------- | ------ | ----------- |
| id            | number | レビュー ID |
| name          | string | 店舗名      |
| note          | string | 内容        |
| user_id       | number | ユーザー ID |
| user_name     | string | ユーザー名  |
| category_name | string | カテゴリ名  |
| category_id   | name   | カテゴリ ID |
| star          | number | スター数    |

```javascript
{
    "id": number,
    "name": string,
    "user_id": number,
    "user_name": string,
    "note": string,
    "category_name": string,
    "category_id": number,
    "star": number
}
```

