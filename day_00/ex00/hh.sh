# /bin/sh
curl -G --data-urlencode "search_field=name"  --data-urlencode "text=data scientist" -X GET  https://api.hh.ru/vacancies | jq . > hh.json