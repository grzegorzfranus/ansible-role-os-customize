# Copyright (c) Grzegorz Franus
# SPDX-License-Identifier: Apache-2.0
"""Ansible filter plugins for Netplan configuration processing."""

from __future__ import annotations

import copy
from typing import Any


def os_customize_netplan_default_route_onlink(data: Any) -> Any:
    """Ensure IPv4 default routes under network.ethernets have on-link: true.

    Takes parsed YAML data of a Netplan configuration file and returns a deep
    copy where each route under network.ethernets.<id>.routes whose 'to' is
    'default' or '0.0.0.0/0' has 'on-link: true'. Other routes, IPv6 defaults,
    and existing keys remain untouched.
    """
    if not isinstance(data, dict):
        return data

    result = copy.deepcopy(data)
    network = result.get("network")
    if not isinstance(network, dict):
        return result

    ethernets = network.get("ethernets")
    if not isinstance(ethernets, dict):
        return result

    for _eth_id, eth_conf in ethernets.items():
        if not isinstance(eth_conf, dict):
            continue
        routes = eth_conf.get("routes")
        if not isinstance(routes, list):
            continue
        for route in routes:
            if not isinstance(route, dict):
                continue
            to_val = route.get("to")
            if to_val is not None and str(to_val).strip() in ("default", "0.0.0.0/0"):
                route["on-link"] = True

    return result


def os_customize_netplan_gateway4_ids(data: Any) -> list[str]:
    """Return Ethernet interface identifiers using deprecated gateway4.

    Takes parsed YAML data of a Netplan configuration file and returns a list
    of ethernet section keys that contain the deprecated 'gateway4' directive.
    """
    if not isinstance(data, dict):
        return []

    network = data.get("network")
    if not isinstance(network, dict):
        return []

    ethernets = network.get("ethernets")
    if not isinstance(ethernets, dict):
        return []

    gateway4_ids: list[str] = []
    for eth_id, eth_conf in ethernets.items():
        if isinstance(eth_conf, dict) and "gateway4" in eth_conf:
            gateway4_ids.append(str(eth_id))

    return gateway4_ids


class FilterModule:
    """Ansible Jinja2 filter plugins for Netplan configuration manipulation."""

    def filters(self) -> dict[str, Any]:
        """Return filter name to function mappings."""
        return {
            "os_customize_netplan_default_route_onlink": os_customize_netplan_default_route_onlink,
            "os_customize_netplan_gateway4_ids": os_customize_netplan_gateway4_ids,
        }
