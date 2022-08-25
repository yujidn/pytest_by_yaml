from lib import function
import yaml
from dataclasses import dataclass
import typing
import pytest

def test_value():
    post_value = 1
    assert post_value == function.return_value(post_value)

## 本来はtest/__init__.pyに書く
@dataclass
class yaml_params:
    name: str
    api: str
    summary: str
    images: typing.Dict
    other_request_param: typing.Dict
    response_param: typing.Dict

def yaml_load(yaml_path):
    with open(yaml_path, "r") as f:
        y = yaml.safe_load(f)

    cases = y['cases']
    params = [yaml_params(**v, name=k) for k, v in cases.items()]
    return params

@pytest.mark.parametrize('param', yaml_load('test/yaml/function.yaml'))
def test_from_yaml(param: yaml_params):

    print(param.summary)

    request_param = {}
    if param.images is not None:
        for k, v in param.images.items():
            request_param[k] = v   # ここcv2.imread()やb64読み込みに置き換え

    request_param.update(param.other_request_param)

    ## ここを対象のapi呼び出しに置き換え
    res = function.return_value(request_param)


    print(res)
    for k, v in param.response_param.items():
        assert res[k] == v

