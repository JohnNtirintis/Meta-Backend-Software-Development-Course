import json
from employee import employee_name, age, title, details

def create_dict(name, age, title):
    #Creates a dictionary that stores an employee's information
    employee_dict = {
        "first_name": name, 
        "age": int(age),
        "title": title
    }
    
    return employee_dict

def write_json_to_file(json_obj, output_file):
    # Write json string to file
    file1 = open(output_file, 'w')
    file1.write(json_obj)
    file1.close()

    return output_file

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()