# users API

## サインイン API

### リクエスト

```
POST /api/signin
```

```javascript
{
    "id": number,
    "pass": string
}
```

### レスポンス

#### 成功時

200 OK

※cokkie にログイン情報を埋め込み

#### 失敗時

400 BadRequest
| param | type | description |
| -- | -- | -- |
| code | string | エラーコード |

```javascript
{
    "code": InvalidParameter,
}
```

```
POST /api/signin
```

```javascript
{
    "id": number,
    "pass": string
}
```

### レスポンス

#### 成功時

200 OK

※cokkie にログイン情報を埋め込み

#### 失敗時

400 BadRequest
| param | type | description |
| -- | -- | -- |
| code | string | エラーコード |

```javascript
{
    "code": InvalidParameter,
}
```

## サインアップ API

### リクエスト

```
POST /api/signup
```

```javascript
{
    "id": number,
    "pass": string,
    "name": string
}
```

### レスポンス

#### 成功時

200 OK

※cokkie にログイン情報を埋め込み

#### 失敗時

400 BadRequest

| param | type   | description  |
| ----- | ------ | ------------ |
| code  | string | エラーコード |

```javascript
{
    "code": InvalidParameter,
}
```

```
POST /api/signin
```

```javascript
{
    "id": number,
    "pass": string
}
```

### レスポンス

#### 成功時

200 OK

※cokkie にログイン情報を埋め込み

#### 失敗時

400 BadRequest

| param | type   | description  |
| ----- | ------ | ------------ |
| code  | string | エラーコード |

```javascript
{
    "code": InvalidParameter,
}
```

## サインアウト API

### リクエスト

```
POST /api/signout
```

### レスポンス

#### 成功時

200 OK

※cokkie からログイン情報を削除
