import os
import autogen
from autogen import UserProxyAgent, AssistantAgent
from prompts.prompts import coding_assistant_system_message_prompt, openai_specialized_system_message, langchain_specialized_system_message, autogen_specialized_system_message

openai_api_key = os.environ.get("OPENAI_API_KEY")

function_map = {

}


llm_config = {
    "api_key": openai_api_key,
    "seed": 42,
    "temperature": 0.1,
    "model": "gpt-4"
}

test_llm_config = {
    "api_key": openai_api_key,
    "seed": 42,
    "temperature": 0.1,
    "model": "gpt-3.5-turbo"
}

code_exe_config = {
    "use_docker": False,
}

user = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    code_execution_config=code_exe_config,
    max_consecutive_auto_reply=2,

)

general_coding_assistant = autogen.AssistantAgent(
    name="General_Coder",
    system_message=coding_assistant_system_message_prompt,
    llm_config=llm_config,
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    code_execution_config=code_exe_config,
)

openai_specialized_coding_assistant = autogen.AssistantAgent(
    name="OpenAI_Specialized_Coder",
    system_message=openai_specialized_system_message,
    llm_config=llm_config,
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    code_execution_config=code_exe_config,
)

langchain_specialized_coding_assistant = autogen.AssistantAgent(
    name="Langchain_Specialized_Coder",
    system_message=langchain_specialized_system_message,
    llm_config=llm_config,
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    code_execution_config=code_exe_config,
)

autogen_specialized_coding_assistant = autogen.AssistantAgent(
    name="Autogen_Specialized_Coder",
    system_message=autogen_specialized_system_message,
    llm_config=llm_config,
    max_consecutive_auto_reply=3,
    human_input_mode="NEVER",
    code_execution_config=code_exe_config,
)

agents = [user, general_coding_assistant, openai_specialized_coding_assistant,
          langchain_specialized_coding_assistant, autogen_specialized_coding_assistant]
coding_help_groupchat = autogen.GroupChat(
    agents=agents,
    messages=[],
    max_round=10,
    admin_name="user"
)

coding_group_manager = autogen.GroupChatManager(
    coding_help_groupchat, max_consecutive_auto_reply=5, human_input_mode="NEVER")


def main():
    message = input("Enter your message here\n> ")
    user.initiate_chat(coding_group_manager, True, False, message=message)

    return


if __name__ == "__main__":
    main()
