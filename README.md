# DSI321/DSI324_Project
# Alumni Service System 
## วัตถุประสงค์
1) เพื่อให้มหาวิทยาลัยสามารถติดต่อกับศิษย์เก่าได่ และเพื่อให้เกิดการติดต่อสื่อสารระหว่างศิษย์เก่าด้วยกันเอง
2) เกิดเครื่อค่ายความสัมพันธ์ระหว่ามหาวิทยาลัยกับศิษย์เก่า และระหว่างศิษย์เก่ากับศิษย์เก่าด้วยกัน
## วิธีใช้
### แบ่งผู้ใช้เป็น 4 ระดับ
1) Admin 
    - Admin ต้องอัพโหลดไฟล์ csv ของ User , Alumni , Course , Education , Company
2) Alumni
    - login เพื่อเข้าระบบในฐานะศิษย์เก่าได้
    - สามารถดู , แก้ไข, เพิ่ม ข้อมูลรางวัลและข้อมูลการทำงานได้
    - สามารถดูข้อมูลการทำงานของศิษย์เก่าคนอื่น โดยที่ต้องได้รับการยินยอมจากศิษย์เก่าคนนั้นๆก่อน
    - สามารถดูข้อมูลภาพรวมการทำงานของศิษย์เก่าโดยแสดงผลออกมาเป็นรูปแบบกราฟ
3) Officer
    - login เพื่อเข้าระบบในฐานะเจ้าหน้าที่ฝ่ายวิชาการได้
    - สามารถดูข้อมูลศิษเก่า และข้อมูลการทำงานของศิษย์เก่าได้
    - สามารถแก้ไขข้อมูลการศึกษาของศิษย์เก่าได้
    - สามารถดูข้อมูลภาพรวมการทำงานของศิษย์เก่าโดยแสดงผลออกมาเป็นรูปแบบกราฟ
    
4) Dean
    - login เพื่อเข้าระบบในฐานะรองคณะบดีได้
    - สามารถข้อมูลการทำงานของศิษย์เก่าได้
    - สามารถดูข้อมูลภาพรวมการทำงานของศิษย์เก่าโดยแสดงผลออกมาเป็นรูปแบบกราฟ

## การ Deploy บน Heroku
### Requirement
1) ติดตั้ง Heroku CLI และมีบัญชี Heroku: [Heroku CLI Download](https://devcenter.heroku.com/articles/heroku-cli) , [Heroku Signup](https://signup.heroku.com/)
2) มีไฟล์ requirement.txt เพื่อบอกว่าจำเป็นต้องใช้ library ใดบ้าง
3) มี Procfile

### การ Deploy บน Heroku

1) เข้าไปยังโฟลเดอร์ของโปรเจค โดยในที่นี้จะใช้ชื่อโปรเจคว่า AlumTU_proj
```
cd AlumTU_proj
```
2) ลอคอิน Heroku
```
heroku login
```
3) สร้างเว็บไซต์บน Heroku ชื่อ alumnitu
```
heroku create alumnitu
```
4) ตั้งค่า heroku disable collect static
```
heroku config:set DISABLE_COLLECTSTATIC=1
```
5) ทำการเชื่อมต่อกับ [Heroku PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql)
```
heroku addons:create heroku-postgresql:hobby-dev
```
6) สร้าง git Repository บน Heroku และ push ไฟล์ทั้งหมดขึ้นไปบน Repository ที่สร้าง
```
git init
git add .
git commit -m "deploy"
git push heroku master
```
7) Migrate โครงสร้างฐานข้อมูล
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```
8) เปิดเว็บที่ Deploy 
  จะได้เว็บไซต์ดังนี้ https://alumnitu.herokuapp.com/
```
heroku open
```

### เข้าไปยัง Repository เพื่อแก้ไข หลังจากที่ Deploy แล้ว

1) เข้าไปยัง Remote Repository บน Heroku ที่ได้สรา้งไว้ในขั้นตอนก่อนหน้า โดยที่ต้อง login ก่อน

```
heroku git:remote -a alumnitu
```
2) หากต้องการแก้ไขไฟล์ และเมื่อแก้ไขเสร็จให้ Push ไฟล์ ไปที่ Remote Repository
```
git add .
git commit -m "edit"
git push heroku master
```
3) หากมีการเปลี่ยแปลงโครงสร้างตารางให้ทำการ Migrate
```
heroku run python manage.py makemigrations
heroku run python manage.py migrate
```
4) เปิดเว็บที่ Deploy
```
heroku open
```


