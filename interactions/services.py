from django.contrib.auth.models import User
from django.db import transaction

from .models import Interaction, Audit

class InteractionService:

    @staticmethod
    @transaction.atomic
    def create_interaction(
        user: User,
        question: str,
        llm_response: str,
        llm_provider: str = "",
        model_name: str = ""
    ):

        interaction = Interaction.objects.create(
            user=user,
            question=question,
            llm_response=llm_response,
            llm_provider=llm_provider,
            model_name=model_name
        )

        audit = Audit.objects.create(
            interaction=interaction
        )

        return interaction, audit