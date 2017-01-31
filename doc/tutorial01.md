









## url 的参数
urls.py中的url()参数  
1，regex（正则表达式），以^开始，$结尾  
2，view，当django按正则表达式的规则匹配成功，就会请求view函数。  
3，kwargs，任意关键词参数可以在字典中传递到目标视图view。  
4，name， 命名你的URL可以在django的其他地方，特别是模板中引用他。  