from locust import HttpUser, between, constant, task
import json

class CalculatorUser(HttpUser):
    
    wait_time = between(2, 4)


    def on_start(self):
        pass

    @task(2)
    def add(self):
        add = {
            "operation": "add",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculator", catch_response=True, name='add', json=add, timeout=1) as response:
            if response.status_code == 200: 
                try:
                    response_data = json.loads(response.text)
                    #print("json decode worked")
                except json.JSONDecodeError as e:
                    response.failure(f"Failed to decode JSON response: {e}")
                if not response_data['result'] == 2:
                    response.failure(f"Expected result to be 2 but was {response_data['result']}")
            else:
                response.failure(f"Received non-200 status code: {response.status_code}")
                
    
    
    @task(1)
    def subtract(self):
        subtract = {
            "operation": "subtract",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculator", catch_response=True, name='subtract', json=subtract) as response:
            if response.status_code == 200: 
                try:
                    response_data = json.loads(response.text)
                except json.JSONDecodeError as e:
                    response.failure(f"Failed to decode JSON response: {e}")
                if not response_data['result'] == 0:
                    response.failure(f"Expected result to be 0 but was {response_data['result']}")
            else:
                response.failure(f"Received non-200 status code: {response.status_code}")
 
           
    @task(1)
    def multiply(self):
        multiply = {
            "operation": "multiply",
            "operand1": 1,
            "operand2": 1
        }
        with self.client.post("/calculator", catch_response=True, name='multiply', json=multiply) as response:
            if response.status_code == 200: 
                try:
                    response_data = json.loads(response.text)
                except json.JSONDecodeError as e:
                    response.failure(f"Failed to decode JSON response: {e}")
                if not response_data['result'] == 1:
                    response.failure(f"Expected result to be 1 but was {response_data['result']}")
            else:
                response.failure(f"Received non-200 status code: {response.status_code}")
                
          
    @task(1)
    def divide(self):
        divide = {
            "operation": "divide",
            "operand1": 10,
            "operand2": 5
        }
        with self.client.post("/calculator", catch_response=True, name='divide', json=divide) as response:
                if response.status_code == 200: 
                    try:
                        response_data = json.loads(response.text)
                    except json.JSONDecodeError as e:
                        response.failure(f"Failed to decode JSON response: {e}")
                    if not response_data['result'] == 2:
                        response.failure(f"Expected result to be 2 but was {response_data['result']}")
                else:
                    response.failure(f"Received non-200 status code: {response.status_code}")
                    
    
    

if __name__ == "__main__":
    from locust import run_single_user
    CalculatorUser.host = "http://127.0.0.1:5000"
    run_single_user(CalculatorUser)
    

