from decorators import consult_animal


@consult_animal
def consult_api(sound):
    print(sound)


consult_api('meow')
print('#'*30)
consult_api('woof')
