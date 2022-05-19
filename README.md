
## 使用功能mysql引擎

```markdown
在windows中使用pymysql
链接：https://stackoverflow.com/questions/50970188/did-you-install-mysqlclient/54200666

# linux
sudo apt-get install libmysqlclient-dev
```

```python
# Then edit the init.py file in project root directory (where settings.py file located)
# 在windows pip install pymysql
import pymysql
pymysql.install_as_MySQLdb()
```
