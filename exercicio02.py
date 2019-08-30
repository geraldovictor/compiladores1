from lark import Lark

json = Lark(r"""
start : array | object
object : "{" "}"
array : "[" _ws "]" | "[" value ("," value)* "]"
value : _ws atom _ws
atom : number | string | array | object | /true/ | /false/ | /null/
number : /[0-9]+/
string : /"[\w, ]+"/ 
_ws : (" " | "\n" | "\t" | "\r")*
""")


tree =json.parse('[42,null,true,false,"GHAGDG323424hello world again", "0", 45]')

print(tree.pretty())
