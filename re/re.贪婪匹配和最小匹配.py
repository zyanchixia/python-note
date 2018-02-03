#贪婪匹配和最小匹配

>>> match = re.search(r'PY.*N','PYANBNCNDN') #.指的是单个，*指出现0到无限次
>>> match.group(0)
'PYANBNCNDN' #Re库默认采用贪婪匹配，即输出匹配最长的子串

>>> match  = re.search(r'PY.*?N','PYANBNCNDN')
>>> match.group(0)
'PYAN'  #在操作符后增加?变成小匹配



操作符说明
*? 前一个字符0次或无限次扩展，最小匹配
+? 前一个字符1次或无限次扩展，最小匹配
?? 前一个字符0次或1次扩展，最小匹配
{m,n}? 扩展前一个字符m至n次（含n），最小匹配
