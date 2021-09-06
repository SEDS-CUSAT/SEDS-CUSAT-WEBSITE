# SEDS-CUSAT-WEBSITE

Basic steps to run this code on the machine  
1. Install python  
    https://www.python.org/downloads/  
    
2. Install PyCharm ( prefarably )   
    https://www.jetbrains.com/pycharm/download/#section=windows  
 
3. Clone this repositiory  
 
4. Open terminal,  
  1.Install virtualenv  
    `pip install virtualenv`
  2. Create virtual env  
    `py -m venv env`
  3. Activate virtual env  
        In powershell  
        `.\env\Scripts\activate`  
        In bash  
        `source ./env/Scripts/activate`
  4. Install libraries inside requirement.txt  
    `cd ..`  
    `py install -r requirement.txt`
  5. run django migrate   
    `python manage.py migrate`    
  6. run django server  
    `python manage.py runserver`  
