
## 使用功能mysql引擎

```markdown
使用mysqlclient包连接mysql
```

```bash
celery -A application worker --loglevel=INFO -c 2 --pool=solo -Ofair
celery -A application worker --loglevel=INFO -c 2 --pool=eventlet -Ofair
```
