# ---------: Contact Management System :----------

import os 
import datetime 
import csv 

class CMS : 
    def __init__(self):
        self.contact_field = ['Name', 'Phone_number']
        self.contact_database = 'contacts.csv'
        self.contact_data = []

    def title(self):
        line_1 = '-------------------------------------------'
        line_2 = "        Contact Management System          "
        line_3 = '-------------------------------------------'
        print(line_1)
        print(line_2)
        print(line_3)

    def create(self):
        print('')
        print('Create Contact : ')
        print('-----------------')

        for i in self.contact_field :
            contact_details = input('Enter '+ i + ':')
            print('')
            self.contact_data.append(contact_details)

        Date = datetime.datetime.today()
        d = Date.strftime('%B %d %Y')
        self.contact_data.append(d)
        
        with open(self.contact_database, 'a' ) as file :
            write = csv.writer(file)
            write.writerows([self.contact_data])
        
        self.contact_data = []
        print('Contact is created Successfully !!!')
        print('\n')


    def view(self):
        print('')
        print('View Contacts : ')
        print('----------------')

        count = 0 
        with open(self.contact_database, 'r') as file :
            read = csv.reader(file)
            for data in read :
                if len(data) > 0 :
                    count += 1 
            print('Total Count : ', count)
        
        with open(self.contact_database, 'r') as file :
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0 :
                print('')
                print('contact book is empty, pleas enter contact Number')
            else:
                for fields in self.contact_field :
                    print('{0:<10}'.format(fields).center(10), end='\t\t')
                print('{0:<10}'.format('Date'))
                print('{:<10}\t\t{:10}\t\t{:<10}'.format('------','-----------','------'))
                print('')

                for data in read :
                    for item in data : 
                        print('{:10}'.format(item).center(10), end='\t\t')
                    print('')
        print('\n')
        input('\t Press enter key to continew...')
  

    def search(self):
        print('Searching Contact : ')
        print('--------------------')

        self.contact_match = 'false'
        search_views = input('Enter the Name : ')
        print('')

        for fields in self.contact_field :
            print('{0:<10}'.format(fields), end='\t\t')
        print('{0:<10}'.format('Date'))
        print('{:<10}\t\t{:10}\t\t{:<10}'.format('-----','------------','-----'))
        print('')

        with open(self.contact_database,'r') as file :
            read = csv.reader(file)
            for data in read:
                if len(data) > 0 :
                    if search_views == data[0] :
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:10}\t\t{:<10}'.format(data[0],data[1],data[2]))
        
        if self.contact_match == 'false' :       
            print('sorry there is no data by this name ')
        print('')

    def update(self):
        print('Update Contact : ')
        print('------------------')
        print('')

        self.contact_match = False
        update_name = input('Enter the Name : ')
        update_number = input('Enter the Phone Number : ')
        update_list = []

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if update_name == data[0]: 
                        self.contact_match = True
                        data[1] = update_number 
                update_list.append(data) 

        if self.contact_match:
            with open(self.contact_database, 'w', newline='') as file:
                write = csv.writer(file)
                write.writerows(update_list)
            print('')
            print('Contact is updated successfully ')
            print('')

        else:
            print('')
            print('Sorry, data not found ')
            print('')

    
    def delete(self):
        print('Delete Contact : ')
        print('------------------')
        print('')

        self.contact_match = 'false'
        delete_view = input('Enter the Name : ')
        update_list = []

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read :
                if len(data) > 0 :
                    if delete_view != data[0] :
                        update_list.append(data)
                    else:
                        self.contact_match = 'true'
        
        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print('')
                print('contact is delete successfully ')
                print('')

        if self.contact_match == 'false':
            print('')
            print('sorry data not found ')
            print('')
  
contact_class = CMS()

try:
    while True:
        contact_class.title()
        print('')
        print('1. Create contacts')
        print('2. view contacts')
        print('3. search contacts')
        print('4. update contacts')
        print('5. delete contacts')
        print('6. Exit')
        print('___________________________')
        option = int(input('Choose your option: '))

        if option == 1:
            while True :
                contact_class.create()
                ans = input('Do you want to create another contact number? [Y/N] :')
                if ans == 'Y' or ans == 'y':
                    continue
                else:
                    break
                
        elif option == 2:
            contact_class.view() 
                
        elif option == 3:
            while True : 
                contact_class.search()
                print('')
                ans = input('Do you want to search another contact number? [Y/N] :')
                if ans == 'Y' or ans == 'y':
                    continue
                else:
                    break   

        elif option == 4:
            while True :
                contact_class.update()
                ans = input('Do you want to search another contact number? [Y/N] :')
                if ans == 'Y' or ans == 'y' :
                    continue
                else:
                    break
        
        elif option == 5:
            while True :
                contact_class.delete()
                ans = input('Do you want to delete another contact number? [Y/N] :')
                if ans == 'Y' or ans == 'y':
                    continue
                else:
                    break
            
        elif option == 6:
            line_1 = '-------------------------------------------'
            line_2 = "    Thank you for using this software   "
            line_3 = '-------------------------------------------'
            print(line_1)
            print(line_2)
            print(line_3)
            break

        elif option > 6 or option < 1 :
            print('Invalid choice. please choose valide option ')
            print('\n')
            input('press enter key to continue...')
        
except Exception as e:
    print('Something went wrong.... please check your input....')

        