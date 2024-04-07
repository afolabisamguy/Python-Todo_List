class MyClass:
    instances = []

    def __init__(self):
        self.name = None
        self.age = None
        self.__class__.instances.append(self)

    @classmethod
    def create_instance(cls):
        instance = cls()
        instance.name = input("Enter name: ")
        instance.age = int(input("Enter age: "))

    @classmethod
    def edit_instances(cls):
        for i, instance in enumerate(cls.instances, start=0):
            print(f"Instance {i}: Name: {instance.name}, Age: {instance.age}")
            choice = input("Do you want to edit this instance? (yes/no): ").lower()
            if choice == 'yes':
                instance.name = input("Enter new name: ")
                instance.age = int(input("Enter new age: "))
