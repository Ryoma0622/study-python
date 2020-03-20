name = 'これはテスト'
print(name)
print(1 < 2)

dictionary = { 'hoge': 'huga' }
print(dictionary)

for i in range(5):
   print(i)
print('テスト')

names = ['hoge', 'fuga', 'hige']
for i in range(len(names)):
  print(names[i])

for name in names:
  print(name + ' san')

val = 0
if val >= 1:
  print('if')
elif val == 0:
  print('elif')
else:
  print('else')

def say_hello(name):
  print('こんにちは' + name)

say_hello('hoge')
say_hello('fuga')
say_hello('hige')
say_hello('figa')

def add(a, b, c):
  return a + b + c

result = add(3, 5, 2)

print(result)

def abs(num):
  if num < 0:
    return -1 * num
  else:
    return num

print(abs(-1))