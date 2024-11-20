language={}
print("enter dictionary:",language)
language={1:"PYTHON",2:"c++",3:"java"}
print("initial dictionary:",language)
language[4]="HTML"
language.update({200:'PASCAL',100:"C#.NET"})
print("updated dictionary:",language)
newlang=language.copy()
print("copy of language in newlang:",newlang)
