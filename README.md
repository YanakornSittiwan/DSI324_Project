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
  
Alum9 (CIS Alumni Service System) ระบบศิษย์เก่าวิทยาลัยสหวิทยาการ
คู่มือสำหรับติดตั้งระบบ Alum9 พร้อมวิธีการติดตั้ง Database โดยมีหัวข้อดังนี้

Prerequisite
Deploy with Heroku Git on CMD Prompt
Migrate Heroku PostgreSQL
Prerequisite
การ Deploy บน Heroku จำเป็นจะต้องมี

บัญชีสำหรับเข้าใช้งาน Heroku โดยสมัครได้ที่นี่ Heroku Signup
มีการ Create App ไว้บน Heroku แล้ว ขั้นตอนนี้เพียงแค่ Login เข้าไปในเว็บ Heroku และกดสร้างผ่านหน้า UI ได้ทันที
ติดตั้ง Heroku PostgreSQL บน App ที่สร้าง ติดตั้งที่นี่ Heroku PostgresSQL
ติดตั้ง Heroku CLI ดาวน์โหลดได้ที่นี่ Heroku CLI
เตรียมไฟล์ secretskey.txt ของตัวเองไว้ โดยใส่ไว้ในระดับเดียวกันกับพวก requirements.txt
Deploy with Heroku Git on CMD Prompt
สำหรับการ Deploy ด้วย Heroku Git บน Command Prompt นั้นจะมีคำสั่งดังนี้

cd [TO_YOUR_PROJECT_DIRECTORY]
[TO_YOUR_PROJECT_DIRECTORY] = Path ไปยังโฟลเดอร์ที่เก็บโปรเจค เช่น C:\cis_alumni

heroku login
heroku git:remote -a [YOUR_HEROKUAPP_NAME]
[YOUR_HEROKUAPP_NAME] = ชื่อแอปที่ตั้งไว้ตอนกด Create App บน Heroku เช่น alum9app

git add .
git commit -am "make it better"
git push heroku master
Heroku ก็จะทำการ Deploy ให้จนเสร็จสิ้น

Migrate Heroku PostgreSQL
ก่อนจะทำขั้นตอนนี้ ให้เข้าไปเปลี่ยน Database URL ในหน้า settings.py ให้เป็น Database URL ตามที่ได้สร้างใน Prerequisite ข้อ 3

heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
