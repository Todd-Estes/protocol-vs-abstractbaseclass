from iot.message import MessageType

class HueLight:
  def connect(self) -> None:
    print("Connecting Hue Light")

  def disconnect(self) -> None:
    print("Disconnecting the Hue Light")

  def send_message(self, message_type: MessageType, data: str) -> None:
    print(
      f"Hue light handling message of type {message_type.name} with data [{data}]"
    )

  def status_update(self) -> str:
    return "hue_light_status_ok"

class SmartSpeaker:
  def connect(self) -> None:
    print("Connecting Smart Speaker")

  def disconnect(self) -> None:
    print("Disconnecting the Smart Speaker")

  def send_message(self, message_type: MessageType, data: str) -> None:
    print(
      f"Smart Speaker handling message of type {message_type.name} with data [{data}]"
    )

  def status_update(self) -> str:
    return "smart_speaker_status_ok"
  
class Curtains:
  def connect(self) -> None:
    print("Connecting Curtains")

  def disconnect(self) -> None:
    print("Disconnecting the Curtains")

  def send_message(self, message_type: MessageType, data: str) -> None:
    print(
      f"Curtains handling message of type {message_type.name} with data [{data}]"
    )

  def status_update(self) -> str:
    return "curtains_status_status_ok"