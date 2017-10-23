#!/bin/bash
# 执行迁移,并在数据库中生成迁移表
python manage.py makemigrations
python manage.py migrate
