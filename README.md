# DSI321/DSI324_Project
# Alumni Service System Project
## วัตถุประสงค์
  เพื่อให้มหาวิทยาลัยสามารถติดต่อกับศิษเก่าได่ และเพื่อให้เกิดการติดต่อสื่อสารระหว่างศฺษเก่าด้วยกันเอง
## วิธีใช้
  1)Admin ต้องอัพโหลดไฟล์ csv ของ User , Alumni , Course , Education , Company \
  2)User Alumni สามารถดู , แก้ไข, เพิ่ม ข้อมูลรางวัลและข้อมูลการทำงานได้ \
  3)มีการขอคำยินยอมให้นำข้อมูลการทำงานและข้อมูลการติดต่อเปิดเผยต่อผู้ใช้คนอื่น \
  4)สามารถเรียกดูข้อมูล การทำงานและการติดต่อกับผู้ใช้คนอื่น \
  5)ระบบสามารถแสดงกราฟภาพรวมการทำงาน และการศึกษาของศิษย์เก่า
  
## ขั้นตอนการ Deploy
เข้าไปยังโฟลเดอร์ของโปรเจค
```
cd AlumTU_proj
```
ลอคอิน Heroku
```
heroku login
```
```
heroku create alumapp
```

```
heroku config:set DISABLE_COLLECTSTATIC=1
```

```
heroku addons:create heroku-postgresql:hobby-dev
```

```
git add .
git commit -m "deploy"
git push heroku master
```


```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```

```
heroku open
```






  
  
