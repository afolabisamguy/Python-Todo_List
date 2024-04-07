class Todo:
    instances = []

    def __init__(self):
        self.title = None
        self.description = None
        self.due_date = None
        self.priority = None
        self.status = None
        self.__class__.instances.append(self)

    @classmethod
    def create(cls, title, description, due_date, priority, status):
        # All this method was back when it was a CLI but now that its a GUI its no longer needed
        # Just Kept it here for reference purpose

        # print('Create your todo\'s')
        #
        # def set_title():
        #     # print('Enter The Title of your todo')
        #     # title = input()
        #     return title
        #
        # def set_description():
        #     # print('Enter The Description of your todo')
        #     # description = input()
        #     return description
        #
        # def set_due_date():
        #     # print('Enter The Due Date')
        #     # while True:
        #     #     try:
        #     #         due_date = int(input())
        #     return due_date
        #     #         break
        #     #     except ValueError:
        #     #         print('Invalid! Due Date has to be an integer')
        #
        # def set_priority():
        #     # print('Enter The Priority of your todo')
        #     # print('Note The piority stems from 1 to 5 with 1 been the highest priority')
        #     # while True:
        #     #     try:
        #     #         priority = int(input())
        #     #         if priority in (1, 2, 3, 4, 5):
        #     return priority
        #     #             break
        #     #         else:
        #     #             print('Invalid! The priority has to be in the range 1 through 5')
        #     #     except ValueError:
        #     #         print('Invalid! Priority has to be an integer')
        #
        # def set_status():
        #     # print('Enter The Status of your todo')
        #     # print('Note The status is either Completed or Pending')
        #     # while True:
        #     #     status = input()
        #     #     if status == 'Completed' or status == 'Pending':
        #     return status
        #     #         break
        #     #     else:
        #     #         print('Invalid! Status has to be Completed or pending')
        #
        #
        #
        #
        instance = cls()
        instance.title = title
        instance.description = description
        instance.due_date = due_date
        instance.priority = priority
        instance.status = status
        with open('todo.txt', 'a+') as file:
            for i, instance in enumerate(cls.instances, start=1):
                file.write(f"TODO {i}: {instance.title} - Status: {instance.status} \n")
                file.write(f"Description: {instance.description} \n")
                file.write(f"The Due Date is: {instance.due_date} \n")
                file.write(f"The Priority is: {instance.priority} \n")
                file.write("\n")
                file.write("\n")

    @classmethod
    def edit_instance(cls):
        for i, instance in enumerate(cls.instances, start=1):
            print(f"Instance {i}: {instance.title} - {instance.description}")
            choice = input("Do you want to edit this instance? (yes/no): ")
            if choice == 'yes':
                instance.title = input("Enter new title")
                instance.description = input("Enter new description")
                instance.due_date = input("Enter new due date")
                instance.priority = input("Enter new priority")
                instance.status = input("Enter new status")

    def viewers(self):
        viewer = []
        with open('todo.txt', 'r')as file:
            reader = False
            for line in file:
                if line.strip().startswith('TODO'):
                  viewer.append(line.strip())
                  reader = True
                elif reader:
                    reader = False
        return viewer

    @classmethod
    def view_instances(cls):
        with open('todo.txt', 'r') as files:
            for line in files:
                print(line)
        # sorted_instances = sorted(cls.instances, key=lambda x: x.priority)
        # print("Displaying Your Todo's in the order of priority")
        # for i, instance in enumerate(sorted_instances, start=1):
        #     print(f"TODO {i}: {instance.title} - Status: {instance.status}")
        #     print(f"Description: {instance.description}")
        #     print(f"The Due Date is: {instance.due_date}")
        #     print(f"The Priority is: {instance.priority}")
        #     print()
        #     print()

    @classmethod
    def delete_instance(cls):
        for i, instance in enumerate(cls.instances, start=1):
            print(f"Instance {i}: {instance.title} - {instance.description}")
            choice = input("Do you want to delete this instance? (yes/no): ")
            if choice == 'yes':
                cls.instances.remove(instance)

    @classmethod
    def my_delete(cls):
        for instance in cls.instances:
            cls.instances.remove(instance)

    # def printer(self):
    #     print(f"Title:  + {self.title}")
    #     print(f"Description: {self.description}")
    #     print(f"Due Date: {self.due_date}")
    #     print(f"Priority: {self.priority}")
    #     print(f"Status:   {self.status}")
