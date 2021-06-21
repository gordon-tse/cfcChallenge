# CFC Insight Technical Challenge
Submitted by: Gordon Tse ([CV](https://drive.google.com/file/d/1Aygr-EMG8Fo79PxnYerItKkZAfXi3Tf7/view?usp=sharing)) \
LinkedIn: [https://www.linkedin.com/in/gordon-tse/](https://www.linkedin.com/in/gordon-tse/) \
Location: Bristol, United Kingdom (willing to relocate)


## Executing the program
1. Make sure you are connected to the internet. The internet access is essential for installing missing dependencies and to 
requesting to the web page as required. 
2. Install all the required dependencies.

   `$ pip install -r requirements.txt`

3. Execute the driver code `main.py`.

    `$ python main.py`
    
4. Find the output file `output.json` in the current directory.

## The output.json
It can be found in the working directory after executing `main.py` successfully. This is a single `.json` file containing arrays of externally hosted resources grouped by its html tag and a json object 
of all the word frequency counts.

Note: The word frequency counting is case-insensitive and includes visible texts in drop down menus, as required. It is 
displayed as `"[word]": [frequency]`

## Running unit tests
I have also created some unit tests for some core methods. These tests can be run as follow:


`$ python -m unittest <Test class name>`


## Possible checked errors
1. Fail to request the index page. The program will be exited at status code `1` following error message will be printed
to the screen: 

    `[HTTP Status Code]: Unsuccessful http request`

2. Cannot find the hyperlink to the Privacy policy. The program will be exited at status code `1` following error message will be printed
to the screen: 

    `Privacy policy not found`
    
3. Fail to open or write to the output file. The program will be exited at status code `1` following error message will be printed
to the screen: 

    `Cannot open or write to a file`

