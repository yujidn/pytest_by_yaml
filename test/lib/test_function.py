from lib import function
import yaml
from dataclasses import dataclass
import typing
import pytest

def test_value():
    post_value = 1
    assert post_value == function.return_value(post_value)


##################################################################
## 本来はtest/__init__.pyに書く
@dataclass
class yaml_params:
    name: str
    api: str
    summary: str
    images: typing.List
    request_param: typing.List
    response_param: typing.List

def yaml_load(yaml_path):
    with open(yaml_path, "r") as f:
        y = yaml.safe_load(f)

    cases = y['cases']
    params = [yaml_params(**c) for c in cases]
    return params

def yaml_tester(param: yaml_params):
    print(param.summary)

    request_param = {}
    if param.images is not None:
        for img in param.images:
            request_param[img['key']] = img['path']   # ここcv2.imread()やb64読み込みに置き換え

    for rp in param.request_param:
        request_param[rp['key']] = rp['predict_value']

    ## ここを対象のapi呼び出しに置き換え
    res = function.return_value(request_param)

    print(res)
    for rp in param.response_param:
        ## yamlのresponse paramに==, !=, >, <, is, is notなどの演算子指定をつけてもいいかも
        ## 中間とかlen()とかも書こうと思うと大変
        assert rp['predict_value'] == res[rp['key']]

## 本来はtest/__init__.pyに書く
##################################################################

@pytest.mark.parametrize('param', yaml_load('test/yaml/function.yaml'))
def test_from_yaml(param: yaml_params):
    yaml_tester(param)

