set obj=createobject("wscript.shell")
do
    obj.run "runSpider.bat"
    wscript.sleep 120000
    obj.run "userSpider.bat"
    wscript.sleep 800000
loop