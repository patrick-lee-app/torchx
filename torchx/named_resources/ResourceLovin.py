#!/usr/bin/env python3

from torchx.specs import Resource
from kubernetes.client.models import V1Toleration

def test_gpu_node_selector() -> Resource:
    capabilities = {
        "node_selector": {
            "node_pool": "biddermlgpu-t4-node-pool"
        },
        "tolerations":[
            V1Toleration(
                effect="NoSchedule",
                key="nvidia.com/gpu",
                operator="Equal",
                value="present"
            ),
        ]
    }

    return Resource(cpu=2,  gpu=4, memMB=1000, capabilities=capabilities)
