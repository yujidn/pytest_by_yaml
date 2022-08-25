

```

$ pytest -s
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.7.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/yujinunome/workspace/pytest_by_yaml
collected 4 items

test/lib/test_function.py .aaa
{'value': 1}
.bbb
{'value': 1}
Fccc
{'image': 'image_path', 'image2': 'image_path2', 'value': 1}
.

================================================================================================== FAILURES ===================================================================================================
___________________________________________________________________________________________ test_from_yaml[param1] ____________________________________________________________________________________________

param = yaml_params(name='invalid test', api='function', summary='bbb', images=None, other_request_param={'value': 1}, response_param={'value': 2})

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
>           assert res[k] == v
E           assert 1 == 2

test/lib/test_function.py:47: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED test/lib/test_function.py::test_from_yaml[param1] - assert 1 == 2
========================================================================================= 1 failed, 3 passed in 0.13s =========================================================================================

```