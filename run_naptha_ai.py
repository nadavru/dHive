import asyncio
from multiplayer_chat.schemas import InputSchema
from naptha_sdk.task import Task
from naptha_sdk.client.node import Node
from naptha_sdk.schemas import ModuleRun
from typing import Dict
import yaml
from multiplayer_chat.utils import get_logger

logger = get_logger(__name__)

async def run(inputs: InputSchema, worker_nodes, orchestrator_node, flow_run, cfg: Dict):

    # workflow = Workflow("Multiplayer Chat", job)
    task1 = Task(name="chat_initiator", fn="chat", worker_node=worker_nodes[0], orchestrator_node=orchestrator_node, flow_run=flow_run)
    task2 = Task(name="chat_receiver", fn="chat", worker_node=worker_nodes[1], orchestrator_node=orchestrator_node, flow_run=flow_run)

    def generate_prompt_with_data(investment_data, prompt):
        # Example: include user data and investment data in the prompt
        return f"{prompt}\n\nInvestment Data: {investment_data}"
    
    # for example:
    user_data_1 = "[{'timestamp': 1717757584, 'value': 0.67453072, 'symbol': 'USDC', 'name': ['Stablecoins']}, {'timestamp': 1716271142, 'value': 0.7895209, 'symbol': 'BTC', 'name': ['Tokenized', 'BTC']}, {'timestamp': 1715687848, 'value': 0.58119469, 'symbol': 'ETH', 'name': ['Tokenized', 'ETH']}]"
    user_data_2 = "[{'timestamp': 1718732852, 'value': 14129.04308858, 'symbol': 'WETH', 'name': ['Tokenized', 'ETH']}, {'timestamp': 1714588713, 'value': 10467.46273303, 'symbol': 'BTC', 'name': ['Tokenized', 'BTC']}, {'timestamp': 1714770774, 'value': 10669.54033199, 'symbol': 'BTC', 'name': ['Tokenized', 'BTC']}]"

    response = None

    for i in range(10):
        if response is None:
            response = inputs.prompt
        else:
            response = generate_prompt_with_data(user_data_1, response)
        response = await task1(prompt=response)
        response = generate_prompt_with_data(user_data_2, response)
        response = await task2(prompt=response)

    return response

if __name__ == "__main__":
    cfg_path = "multiplayer_chat/component.yaml"
    with open(cfg_path, "r") as file:
        cfg = yaml.load(file, Loader=yaml.FullLoader)
    args = {
        "prompt": "lets count up one number at a time. ill start. one.",
        "coworkers": "http://node.naptha.ai:7001,http://node1.naptha.ai:7001"
    }
    flow_run = {"consumer_id": "user:18837f9faec9a02744d308f935f1b05e8ff2fc355172e875c24366491625d932f36b34a4fa80bac58db635d5eddc87659c2b3fa700a1775eb4c43da6b0ec270d", "module_name": "multiplayer_chat", "module_type": "flow"}
    flow_run = ModuleRun(**flow_run)
    inputs = InputSchema(**args)
    orchestrator_node = Node("http://localhost:7001")
    worker_nodes = [Node(coworker) for coworker in args['coworkers'].split(',')]
    response = asyncio.run(run(inputs, worker_nodes, orchestrator_node, flow_run, cfg))
    print(response)
    print("Flow Run: ", flow_run)