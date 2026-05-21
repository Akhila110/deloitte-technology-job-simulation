from datetime import datetime

def convert_iso_to_millis(timestamp):
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)

def convertFromFormat1(jsonObject):
    return {
        "deviceID": jsonObject["deviceID"],
        "deviceType": jsonObject["deviceType"],
        "timestamp": jsonObject["timestamp"],
        "location": jsonObject["location"],
        "operationStatus": jsonObject["operationStatus"],
        "temp": jsonObject["temp"]
    }

def convertFromFormat2(jsonObject):
    return {
        "deviceID": jsonObject["device"]["id"],
        "deviceType": jsonObject["device"]["type"],
        "timestamp": convert_iso_to_millis(jsonObject["timestamp"]),
        "location": jsonObject["location"],
        "operationStatus": jsonObject["status"],
        "temp": jsonObject["temp"]
    }
