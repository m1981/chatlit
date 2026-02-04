import time


class AIService:
    """
    Single Responsibility: Handle interactions with LLMs.
    """

    @staticmethod
    def generate_response(user_text, attachments):
        # Simulate API latency
        time.sleep(1)

        response = "Processed: " + user_text
        if attachments:
            response += f" (Received {len(attachments)} files)"

        return response