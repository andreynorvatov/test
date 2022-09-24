# http-sandbox

## Описание задания q09
1. Отправить POST запрос с телом в JSON формате на /q09p1 для отправки значения параметра на сервер.
   (в header указать application/json).
   Значения в JSON сообщении:
```sh
parameter = любая строка
```
2. Отправить PUT запрос с телом в JSON формате на /q09p2 для изменения значения параметра, отправленного на сервер в п.1.
   Значения в JSON сообщении:
```sh
parameter = новая любая строка
```
3. Отправить DELETE запрос с удаляемым параметром (параметр передать как в GET запросе) для удаления отправленного на сервер параметра.
```sh
parametertodelete = parameter
```
> Note: В случае получения необработанных ошибок от сервера, а так же при желании повторных прохождений, необходимо удалить cookies в Postman и повторить упражнение с п.1.

## Методы для задания q09
<details>
    <summary>POST метод для добавления параметра на сервер */q09p1*</summary>

*/q09p1*

Request:
```json
{
    "parameter" : "POST"
}
```
Response correct:
```json
{
    "timeEpoch": "1664053031",
    "timeISO": "2022-09-24T20:57:11.700270800",
    "message": "Новый параметр parameter успешно добавлен, значение: POST.",
    "clientIP": "0:0:0:0:0:0:0:1",
    "correct": true
}
```

</details>
<details>
    <summary>PUT метод для обновления заданного параметра на сервере</summary>

*/q09p2*

Request:
```json
{
   "parameter":"PUT"
}
```
Response:
```json
{
   "timeEpoch": "1664053292",
   "timeISO": "2022-09-24T21:01:32.926552500",
   "message": "Параметру parameter изменено значение с POST на PUT",
   "clientIP": "0:0:0:0:0:0:0:1",
   "correct": true
}
```
</details>
<details>
    <summary>DELETE метод для удаления заданного параметра на сервере, с проверкой на выполнение PUT</summary>

*/q09p3*

Request:
```sh
http://localhost:8080/q09p3?parametertoremove=parameter
```
Response:
```json
{
   "timeEpoch": "1664053352",
   "timeISO": "2022-09-24T21:02:32.670084100",
   "message": "Параметр parameter со значением PUT удален. Код для moodle NAAGPB11922SMR922",
   "clientIP": "0:0:0:0:0:0:0:1",
   "correct": true
}
```
</details>

## Дополнительные методы
- DELETE метод для удаления всех значений в HashMap q09ParamStorageCUID */q09_drop_param_storage_cuid*
- DELETE метод для удаления всех значений в HashMap q09ParamStoragePUID */q09_drop_param_storage_puid*
- GET метод для просмотра всех значений в HashMap q09ParamStorageCUID */q09_get_all_cuid*
- GET метод для просмотра всех значений в HashMap q09ParamStoragePUID */q09_get_all_puid*



