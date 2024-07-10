from typing import List
from twilio.rest.conversations import Conversations
from twilio.rest.conversations.v1.participant_conversation import ParticipantConversationInstance
from twilio.client import get_client

client = get_client()

def close_all_conversations(number: str):
    api: Conversations = client.conversations
    conversationList: List[ParticipantConversationInstance] = api.participant_conversations.list(
        address="whatsapp:+" + number,
    )

    for conversationItem in conversationList:
        api.conversations(conversationItem.conversation_sid).update(
            state="closed"
        ).delete()


# def close_all_task(number: str):
#     api: Conversations = client.conversations
#     taskList: List[ParticipantConversationInstance] = api.participant_conversations.list(
#         address="whatsapp:+" + number,
#     )

#     for taskItem in taskList:
#         api.tasks(taskItem.conversation_sid).update(
#             assignment_status="canceled"
#         ).delete()
