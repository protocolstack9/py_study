print("---------------------------------------")
print(" Numbers ");
print("---------------------------------------")

x = 3
print(type(x))
y = 3.
print(type(y))

print(x)
print(x + 1)
print(x - 1)
print(x * 2)
print(x ** 2)
x += 1
print(x)
x *= 2
print(x)

z = 2.5
print(type(z))
print(z, z+1, z*2, z**2)

print(x, z, x//z) # 음의 무한대로 정수 내림


print("---------------------------------------")
print(" Boolean ");
print("---------------------------------------")

t = True
f = False
print(type(t))
print(t and f)
print(t or f)
print(not t)
print(t != f)



print("---------------------------------------")
print(" Strings ");
print("---------------------------------------")

hello = 'hello'
world = "World"
print(hello)
print(len(hello))
hw = hello + ' ' + world
print(hw)
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)

s= "hello"
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print("  world   ".strip() + "|\n")
