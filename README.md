# go-simple-chat-testing
## Automated tests in Python for the go-simple-chat repo

### To run these tests you need:
`python >3.10`

### Install Allure reports:
In Mac:
```
brew install allure
```
For other OSs, please refer to: 
[Allure](https://allurereport.org/docs/install/)

### Clone this repo
```
git clone https://github.com/aabuezo/go-simple-chat-testing.git
```
And cd into the folder:
```
cd go-simple-chat-testing
```

### Create a virtual environment
From the repo directory
```
python -m .venv venv
```
Activate it
```
source ./venv/bin/activate
```
And install requirements.txt
```
pip install -r requirements.txt
```

### Provide execution permissions to run_tests.sh script
```
chmod +x run_tests.sh
```

### From now on, you can run tests and generate reports with:
```
./run_tests.sh
```