from PodSixNet.Connection import connection

# connect to the server - optionally pass hostname and port like: ("mccormick.cx", 31425)
connection.DoConnect()

connection.Send({"action": "myaction", "blah": 123, "things": [3, 4, 3, 4, 7]})

connection.Pump()
