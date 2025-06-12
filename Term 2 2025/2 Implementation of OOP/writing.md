1. Programmers use stubs as placeholders for functions so other functions can use while other functions aren't complete or are in development. One example of the use of stubs is in the case of parallel development, where multiple people are developing overlapping systems at the same time, which often results in the two systems being isolated while they are in development, but they still need to reference each other properly when the program is complete, so they use stubs, which allow programmers to program an isolated feature properly without having to rewrite it after.
2. Version control is important because it allows for parallel development to occur and for it to be controlled by the people using it. Version control allows for different versions to be saved, tracked and managed in an orderly way, the primary thing that allows programmers to use parallel development in their projects. One of the key examples of version control is Github, which allows for the saving of different versions and the ability to fork the main project, so that different functions can be improved in isolation to allow for features to be developed in parallel.
3. Code optimisation is the practice of changing the layout of code in order to improve its speed or how well it performs its purpose. This is done to improve the program as a whole, which is important when a piece of code is run repeatedly, so by optimising a frequently used piece of code, the program can be significantly improve the user experience.

4. 
    a. In this piece of code it handles message passing at one point. This point is when the attack function tells the other player inputted to take damage, where the other player runs the take_damage function\
    b. The two objects in this example pass messages at three points, the first being when the player runs open_chest which tells the chest to open, and then the chest tells the player to collect, the second message pass, then the player attempts to open the chest again, which doesn't send an additional message to the player object because it is empty
5. 
    a. 
    ``` python
        x = 5
        y = 7

        def add(x, y):
            print(x + y)

        add(x, y)
    ```
    b.
    ``` python
        name_list = ['Ali', 'Ben', 'Cat', 'Doge', 'Eggebert', 'Fred', 'Grod']
        for name in name_list:
            print(f'Welcome, {name}!')
    ```
    c.
    ```python
        class Animal:
            def __init__(self):
                self.sound = ""

            def make_sound(self):
                pass

        class Dog(Animal):
            def __init__(self):
                self.sound = "woof"

            def make_sound(self):
                print("Dog goes woof")

        class Cat(Animal):
            def __init__(self):
                self.sound = "meow"

            def make_sound(self):
                print("Cat goes meow")

        class Cow(Animal):
            def __init__(self):
                self.sound = "moo"

            def make_sound(self):
                print('Cow goes moo')


        animals = [Dog(), Cat(), Cow()]
        for a in animals:
            a.make_sound()
    ```
    d.
    ```python
        words = ["hello", "world", "!"]
        sentence = " ".join(words)

        print(sentence)
    ```
    e.
    ```python
        fruit_stock = ["apple", "banana", "cherry"]
        for fruit in range(len(fruit_stock)):
            print(fruit, fruit_stock[fruit])

