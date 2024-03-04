# Log.ic: Pytest Log Viewer

Log.ic is a Flask-based web application designed to simplify the viewing and analysis of logs generated by Pytest. It provides a user-friendly interface to explore and filter log entries, making it easier for developers and testers to understand the results of Pytest runs.

## Key Features

- **Log Filtering:** Filter logs based on log levels, such as INFO, DEBUG, and ERROR.
- **Request-Response Highlight:** Easily identify logs related to requests and responses with a distinct background color and the PT Mono font.
- **Responsive Design:** Clean and responsive interface for a seamless user experience.
- **Custom Styling:** Customize the appearance to suit your preferences.

## How to Use
**There are 3 different ways.**
 - Creating and Running docker container **(Check "Docker Way" section of this file)**
 - Running the python code **(Check Bottom of this file)**

   
 - directly pulling the docker image
   ```bash
    docker pull itachi9604/log.ic
   ```
   1. create a directory somewhere , preferably in Documents. Lets say directory name is **pytest_logs** .
   2. Navigate inside the directory using terminal. (Or open the directory in a terminal).
    ```bash
    docker run -p 8000:80 -v .:/app/logs itachi9604/log.ic 
    ```
   3. Now In your pycharm or framework, command should start like below and then rest of your parameters / arguments .
      ```bash
      pytest -o "log_file=/Users/tony.stark/Documents/pytest_logs/log_file.log"
      ```
   

## Docker Way
  - navigate to the cloned project and build the image.
    ```bash
    docker build -t log.ic .
    ```
  - Creating the container
    1. create a directory somewhere , preferably in Documents. Lets say directory name is **pytest_logs** .
    2. Navigate inside the directory using terminal. (Or open the directory in a terminal).
    ```bash
    docker run -p 8000:80 -v .:/app/logs  log.ic 
    ```
    You can replace **/Users/tony.stark/Documents/pytest_logs** with the directory where your log file will be generated.
    To generate log file to a particular destination, while running pytest, give below params in pytest.ini .
    Remember to add log_file.log in the end in pytest.
    ```bash
    pytest -o "log_file=/Users/tony.stark/Documents/pytest_logs/log_file.log"
    ```
    **Make Sure the -v path in your docker container command and -o path in your pytest argument are same**
    

### Prerequisites

- Python (3.11 recommended)
- Flask

### Getting Started
**Clone And Run the repository:**


   ```bash
   git clone https://github.com/your-username/Log.ic.git
   cd Log.ic
   pip install -r requirements.txt
   python app.py
   ```
**Access the application:**
  Open your web browser and go to http://localhost:5000.

## Explore and analyze your Pytest logs with ease!

### Contribution
Contributions are welcome! If you encounter any issues, have feature requests, or want to contribute improvements, please open an issue or submit a pull request.


