from client import AgentToAgentCapabilityHandshakeNegotiatorClient

def main():
    client = AgentToAgentCapabilityHandshakeNegotiatorClient()
    res = client.negotiate_a2a_capability_contract('agent_a', 'agent_b', 'EXECUTE_QUERY')
    print('A2A Capability Handshake: ' + res['handshake_contract_id'])
    print('Granted: ' + str(res['capability_granted']) + ' | SLA: ' + str(res['sla_latency_limit_ms']) + 'ms')
    print('Scopes: ' + ', '.join(res['authorized_scopes']))
    print('Contract URL: ' + res['contract_proof_url'])

if __name__ == '__main__':
    main()
