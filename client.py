from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def main():
    r1 = requests.get("http://vcm-3539.vm.duke.edu:5000/name")
    print(r1.text)

    r2 = requests.get("http://vcm-3539.vm.duke.edu:5000/hello/Rich")
    print(r2.text)

    r3 = requests.post("http://vcm-3539.vm.duke.edu:5000/distance", json={"a": [2, 5], "b": [2, 9]})
    sum_result = r3.json()
    print(sum_result)
    print("The response was {0}.".format(sum_result['result']))

if __name__ == "__main__":
    main()