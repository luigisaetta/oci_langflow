"""
Custom integration with Langflow and OCI Chat Model
"""

from langflow.base.models.model import LCModelComponent
from langflow.field_typing import LanguageModel
from langchain_community.chat_models.oci_generative_ai import ChatOCIGenAI
from langflow.inputs import StrInput, DropdownInput, SecretStrInput


class OCIChatComponent(LCModelComponent):
    """
    This class integrates the OCI Chat Model with Langflow.

    Notes:
        * Security: for now API_KEY, set your key-pair in $HOME/.oci

    """

    display_name = "OCI Chat Model"
    description = "OCI's Generative AI Chat Model."

    inputs = [
        *LCModelComponent._base_inputs,
        DropdownInput(
            name="auth_type",
            display_name="auth_type",
            info="The type of auth_type to use for the chat model",
            advanced=True,
            options=[
                "API_KEY",
                "RESOURCE_PRINCIPAL",
            ],
            value="API_KEY",
        ),
        DropdownInput(
            name="model_id",
            display_name="model_id",
            info="The model_id to use for the chat model",
            advanced=True,
            options=[
                "meta.llama-3.1-70b-instruct",
                "cohere.command-r-plus-08-2024",
                "meta.llama-3.1-405b-instruct",
            ],
            value="meta.llama-3.1-70b-instruct",
        ),
        StrInput(
            name="service_endpoint",
            display_name="Service Endpoint",
            info="OCI Service Endpoint URL",
            value="https://inference.generativeai.eu-frankfurt-1.oci.oraclecloud.com",
        ),
        SecretStrInput(
            name="compartment_id",
            display_name="Compartment ID",
            info="OCI Compartment OCID",
        ),
        StrInput(name="test_id", display_name="test ID", info="test id"),
    ]

    def build_model(self) -> LanguageModel:
        chat_model = ChatOCIGenAI(
            auth_type=self.auth_type,
            model_id=self.model_id,
            service_endpoint=self.service_endpoint,
            compartment_id=self.compartment_id,
        )

        return chat_model
