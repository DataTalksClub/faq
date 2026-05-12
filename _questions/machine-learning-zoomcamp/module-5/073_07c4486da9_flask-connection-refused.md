---
id: 07c4486da9
question: ConnectionRefusedError [Errno 61/111] Connection refused when calling Flask from predict-test.py
sort_order: 73
---

The Flask server isn't reachable from where the test script runs. Checklist:

1. Is the Flask process actually running? Start it in a separate terminal and leave it running.
2. Is the port the same in the server and the client? Match `app.run(port=9696)` with the URL in `predict-test.py`.
3. Try `127.0.0.1` instead of `localhost`, or vice versa.
4. On Windows, check whether the port is taken or blocked: `netstat -aon | findstr :9696`.
5. Test with `curl http://127.0.0.1:9696/predict` first to isolate Python from networking.
