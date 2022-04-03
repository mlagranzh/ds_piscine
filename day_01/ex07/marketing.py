import sys

def call_center(lists, recipients):
    print(set(lists).difference(set(recipients)))

def loyalty_program(lists, participants):
    print(set(lists).difference(set(participants)))

def potential_clients(lists, clients):
    print(set(lists).difference(set(clients)))

def marketing():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is', 'bill_gates@live.com',\
         'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
        'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    for i, param in enumerate(sys.argv):
        if (i != 0):
            if (len(sys.argv) > 2 or \
                (param != 'loyalty_program' and param != 'call_center' and param != 'potential_clients')):
                raise Exception('Argument error')
        lists = clients + participants + recipients
        if (param == 'call_center'):
            call_center(lists, recipients)
        if (param == 'loyalty_program'):
            loyalty_program(lists, participants)
        if (param == 'potential_clients'):
            potential_clients(lists, clients)

if __name__ == '__main__':
    marketing()