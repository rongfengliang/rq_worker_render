import json 
def report_success(job, connection, result, *args, **kwargs):
    print("job success",job.id,job.kwargs,result,args,kwargs)
    info = {
        "data": {
            "name":"dalong",
            "age":11,
            "job_id":job.id
        }
    }
    connection.publish('response', json.dumps(info))
