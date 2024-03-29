class Student:
    students = 0 # this is a class attribute

    def __init__(self, name, staff):
        self.name = name # this is an instance attribute
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)


class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1


class MinList:
    """A list that can only pop the smallest element """
    def __init__(self):
        self.items = [] 
        self.size = 0

    def append(self, item):
        """Appends an item to the MinList 
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.items.append(item)
        self.size += 1

    def pop(self):
        """ Removes and returns the smallest item from the MinList 
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        if self.size == 0:
            pass
        else:
            smallest = min(self.items)
            idx = self.items.index(smallest)
            self.size -= 1
            return self.items.pop(idx)


class Email:
    """Every email object has 3 instance attributes: 
    the message, the sender name, and the recipient name.
    >>> gmail = Server()
    >>> jason = Client(gmail, 'Jason Wu')
    >>> emma = Client(gmail, 'Emma Watson')
    >>> gmail.register_client(jason, jason.name)
    >>> gmail.register_client(emma, emma.name)
    >>> jason.compose('Will you marry me?', 'Emma Watson')
    >>> emma.inbox[0].msg
    'Will you marry me?'
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, 
    which is a dictionary that associates client names with client objects.
    """
    def __init__(self):
        self.clients = {}
    
    def send(self, email):
        """Take an email and put it in the inbox of the 
        client it is addressed to.
        """
        recipient = self.clients[email.recipient_name]
        recipient.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name 
        and adds them to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is 
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and 
    inbox (a list of all emails the client has received). 
    """
    
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg 
        to the given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this client.
        """
        self.inbox.append(email)


