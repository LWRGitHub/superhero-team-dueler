import dog

my_dog = dog.Dog("Rex", "SuperDog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "SuperDog")
print(my_other_dog.name)

my_other_dog = dog.Dog("Tom", "golden")
print(my_other_dog.bark())

my_other_dog = dog.Dog("Annie", "poodle")
print(my_other_dog.sit())

my_other_dog = dog.Dog("Annie", "Finland")
print(my_other_dog.roll_over())