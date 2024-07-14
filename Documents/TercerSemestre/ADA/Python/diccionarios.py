# 
import itertools
# d ={}
# d = {'key': 'value'}

# d ={k:v for k, v in[('key','value')]}
# print(d)
# d['nbkey'] = 55
# d['dkey'] = {'nested_dict': 33}
# print(d)
# n = int(input('numeo de diccionarios que quieres llenar'))
# # La forma para llenar un diccionario de n 'claves'
# my_dict = {}
# for i in range(n):
#     stringt = i
#     # my_dict[stringt] = int(input('valor de tu valor en la clave i'))
# print(my_dict)

# # Para recorrer un diccionario a traves de las claves
# for key in my_dict:
#     print(key,'<-clave, valor->',my_dict[key])
# #----------------------------------------------------------------------------------------------------
# # Las conbinaciones que puedes hacer
# # usass ""------->> import itertools
# options = {
#     "x": ["a","b"],
#     "y" :[12,34]
# }
# keys = options.keys()
# values = (options[key] for key in keys)
# print(keys)
# values2 = [options[i] for i in keys]
# print(values2)
# print(list(zip(list(values2[0]),list(values2[1]))))
# combinaciones = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
# print(combinaciones)
d ={}
# numero = 1

# d[1] = numero
# num2 = d[1]
# numero = numero + num2

# d[1] = numero
print(d)


