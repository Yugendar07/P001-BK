def success_response(message=None, status=None, details=None):
    if status == None:
        status = "Request processed Successfully"
    response = {}
    response["success"] = True
    response["status"] = status
    response["message"] = message
    if details != None:
        response["details"] = details
    return response


def failure_response(errors, error_message="Invalid Params", status_code=0, message_duration='S'):
    print(errors)
    response = {}
    response["success"] = False
    response["status"] = "Bad Request"
    
    response["status_code"] = status_code
    response["message_duration"] = message_duration
    
    response["error_message"] = error_message
    if errors != None:
        pass
        # print("serializer errors", errors)
        # response["errors"] = errors
    return response

