import os,sys,tempfile
d=tempfile.mkdtemp();os.environ["DB_PATH"]=d+"/db.sqlite";os.environ["BOT_TOKEN"]="1:x"
sys.path.insert(0,"/home/user/she-bot");os.chdir("/home/user/she-bot")
import app as A
A.webapp_user=lambda *a,**k: ({"id":777,"first_name":"Тест"}, None)
A.touch_user({"id":777});A.grant(777,"yaz")
A.app.run(port=5077)
