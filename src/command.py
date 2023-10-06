from typing import List
import re

PARAMS_PATTERN = '\${[a-zA-Z]+[0-9]*}'
TARGETS_PATTERN = '\${[0-9]+}'


def prepare_command(config: dict, targets: List[str]) -> str:
    cmd = config["command"]
    params = config["parameters"]
    cmd = _replace_params(cmd, params)
    cmd = _replace_targets(cmd, targets)
    return cmd


def _replace_params(cmd: str, params: dict) -> str:
    return _replace_entities(cmd, PARAMS_PATTERN, params, lambda p, k: p[k])


def _replace_targets(cmd: str, targets: List[str]):
    return _replace_entities(cmd, TARGETS_PATTERN, targets, lambda p, i: p[int(i)])


def _replace_entities(cmd: str, pattern: str, entities, replace_value_func) -> str:
    search_result = re.findall(pattern, cmd)
    # no params to be replaced
    if len(search_result) < 1:
        return cmd
    for i in range(0, len(search_result)):
        match = search_result[i]
        key = match.split("{")[1].split("}")[0]
        replace_value = replace_value_func(entities, key)
        cmd = cmd.replace(match, replace_value)
    return cmd
