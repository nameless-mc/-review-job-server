# Database

## users

| param      | type        | option          |
| ---------- | ----------- | --------------- |
| id         | BIGINT      | pk              |
| name       | VARCHAR(45) | NOT NULL        |
| signin_id  | VARCHAR(45) | NOT NULL unique |
| pass       | VARCHAR(45) | NOT NULL        |

## groups

| param | type        | option          |
| ----- | ----------- | --------------- |
| id    | BIGINT      | pk              |
| name  | VARCHAR(45) | NOT NULL        |
| code  | VARCHAR(45) | NOT NULL unique |

## join

| param    | type   | option |
| -------- | ------ | ------ |
| user_id  | BIGINT | pk fk  |
| group_id | BIGINT | pk fk  |

## reviews

| param       | type          | option   |
| ----------- | ------------- | -------- |
| id          | BIGINT        | pk       |
| user_id     | BIGINT        | pk fk    |
| group_id    | BIGINT        | pk fk    |
| name        | VARCHAR(45)   | NOT NULL |
| note        | VARCHAR(1000) |          |
| category_id | BIGINT        | fk       |
| star        | BIGINT        | NOT NULL |

## categories

| param | type        | option   |
| ----- | ----------- | -------- |
| id    | BIGINT      | pk       |
| name  | VARCHAR(45) | NOT NULL |
