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
สร้างเว็บไซต์ชื่อ alumnitu
```
heroku create alumnitu
```
ตั้งค่า heroku disable collect static

```
heroku config:set DISABLE_COLLECTSTATIC=1
```
ทำการเชื่อมต่อกับ PostgreSQL
```
heroku addons:create heroku-postgresql:hobby-dev
```
สร้าง git Repository บน Heroku และ push ไฟล์ทั้งหมดขึ้นไปบน Repository ที่สร้าง
```
git init
git add .
git commit -m "deploy"
git push heroku master
```

Migrate โครงสร้างฐานข้อมูล
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```
เปิดเว็บที่ Deploy
```
heroku open
```

## เข้าไปยัง Repository เพื่อแก้ไข หลังจากที่ Deploy แล้ว

เข้าไปยัง Remote Repository บน Heroku โดยที่ต้อง login ก่อน

```
heroku git:remote -a alumnitu
```
หากต้องการแก้ไขไฟล์ และเมื่อแก้ไขเสร็จให้ Push ไฟล์ ไปที่ Remote Repository
```
git add .
git commit -m "edit"
git push heroku master
```
หากมีการเปลี่ยแปลงโครงสร้างตารางให้ทำการ Migrate
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```
เปิดเว็บที่ Deploy
```
heroku open
```








  
  
