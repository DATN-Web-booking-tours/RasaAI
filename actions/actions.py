from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionSearchTourPrice(Action):

    def name(self) -> Text:
        return "action_ask_search_tour_price_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        low = tracker.get_slot('low')
        hight = tracker.get_slot('hight')

        if low is not None and hight is not None:
            response = f"Bạn muốn đặt tour có giá từ {low} đến {hight}."
        elif low is not None:
            response = f"Bạn muốn đặt tour có giá trên {low}."
        elif hight is not None:
            response = f"Bạn muốn đặt tour có giá dưới {hight}."
        else:
            response = "Bạn muốn đặt tour có giá như thế nào?"

        dispatcher.utter_message(text=response)

        return []
