import pickle
from py_abac.exceptions import PolicyExistsError
from pandas import DataFrame

import socket
fp = open("/Users/pbchandra1/Documents/passdata/venv/shared.pkl","rb")
shared = pickle.load(fp)
print(shared)
def extract_ip():
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        st.connect(('10.255.255.255', 1))
        ip = st.getsockname()[0]
    except :
        ip = '127.0.0.1'
    finally:
        st.close()
    return ip

try:
    from pymongo import MongoClient
    from py_abac import PDP, Policy, Request
    from py_abac.storage.mongo import MongoStorage

    # Policy definition in JSON
    policy_json = {
        "uid": "1",
        "description": "Access to be allowed to get "
                       "resource only if the client IP matches and only if the role"
                       "is Human Resources.",
        "effect": "allow",
        "rules": {
            "subject": [{"$._id": {"condition": "RegexMatch", "value": ".*"}} and
                        {"$.employee_name": {"condition": "RegexMatch", "value": ".*"}} and
                        {"$.department": {"condition": "RegexMatch", "value": ".*"}} and
                        {"$.working_from_office": {"condition": "Equals", "value": "Yes"}} and
                        {"$.role": {"condition": "Equals", "value": "Human Resources"}}],
            "resource": {"$.name": {"condition": "RegexMatch", "value": ".*"}},
            "action": {"$.method": {"condition": "Equals", "value": "get"}},
            "context": [{"$.ip": {"condition": "CIDR", "value": "76.76.21.123"}},
                        {"$.ip": {"condition": "CIDR", "value": "192.168.1.224"}},
                        {"$.ip": {"condition": "CIDR", "value": "127.0.0.1"}}]
        },
        "targets": {},
        "priority": 0
    }
    # Parse JSON and create policy object
    policy = Policy.from_json(policy_json)
    # Setup policy storage

    client = MongoClient()
    storage = MongoStorage(client)
    # Add policy to storage
    storage.add(policy)

except PolicyExistsError:
    print("Policy already exists.")

details = {}

try:
    # Create policy decision point
    pdp = PDP(storage)
    # A sample access request JSON
    request_json = {
        "subject": {
            "id": "",
            "attributes": {"_id": shared[0], "employee_name": shared[1], "department": shared[2],
                           "working_from_office": shared[3], "role": shared[4]}
        },
        "resource": {
            "id": "",
            "attributes": {"name": "Confidential_Details"}
        },
        "action": {
            "id": "",
            "attributes": {"method": "get"}
        },
        "context": {
            "ip":extract_ip()
        }
    }
    # Parse JSON and create access request object
    request = Request.from_json(request_json)
    # Check if access request is allowed. Evaluates to True since
    # Max is allowed to get any resource when client IP matches.
    print(extract_ip())
    assert pdp.is_allowed(request)
    print("ACCESS GRANTED BASED ON CURRENT POLICY.\n")


    db = client.py_abac  # connect to database
    cursor = db.Confidential_Documents.find({})
    list_cur = list(cursor)
    df = DataFrame(list_cur)
    result=df.to_html()
    text_file = open("/Users/pbchandra1/Documents/passdata/templates/result.html", "w")
    text_file.write(result)
    text_file.close()


except AssertionError:
    print("ACCESS DENIED")