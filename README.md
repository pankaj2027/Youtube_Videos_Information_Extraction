# Youtube_Videos_Information_Extraction
Steps for running the program:

Step1: Install the redis server by following command: $ sudo apt-get update $ sudo apt-get install redis-server

start redis server:
	$ redis-server
Check If Redis is Working:
	$ redis-cli
Step2: Refer requirement.txt to install require libraries

Step3: Run the first script i.e request_queue.py by executing below command. python|python3 request_queue.py "youtube_url".

   ex:python3 request_queue.py "https://www.youtube.com/watch?v=94o73K5T0MQ"
   
Step4: According to my understanding there are 3 ways to execute request_process.py running indefinitely 1. On machine start request_process.py will execute automatically. 2. By executing the request_queue.py for the first time, it will call request_process.py to run indefinitely. 3. Execute request_process.py manually using command prompt until unless SIGTERM signal is received.

 	In this project 3 one is implimented.
Step5: request_save.py will run when the request_process.py complete its execution and found data to used by request_save.py and store the data in .csv file

Step 6: sending_sigterm_signal.py can be used to send the SIGTERM signal to terminate the request_process.py.
