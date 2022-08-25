```
$ pytest
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.7.11, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/yujinunome/workspace/pytest_by_yaml
collected 4 items

test/lib/test_function.py ...F                                                                                                                                                                          [100%]

================================================================================================== FAILURES ===================================================================================================
___________________________________________________________________________________________ test_from_yaml[param2] ____________________________________________________________________________________________

param = yaml_params(name='valid_json_test', api='function', summary='ccc', images=[{'key': 'image', 'path': 'image_path'}, {'k...ype', 'predict_value': 2}], response_param=[{'key': 'value', 'predict_value': 1}, {'key': 'type', 'predict_value': 1}])

    @pytest.mark.parametrize('param', yaml_load('test/yaml/function.yaml'))
    def test_from_yaml(param: yaml_params):
>       yaml_tester(param)

test/lib/test_function.py:56:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

param = yaml_params(name='valid_json_test', api='function', summary='ccc', images=[{'key': 'image', 'path': 'image_path'}, {'k...ype', 'predict_value': 2}], response_param=[{'key': 'value', 'predict_value': 1}, {'key': 'type', 'predict_value': 1}])

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
>           assert rp['predict_value'] == res[rp['key']]
E           assert 1 == 2

test/lib/test_function.py:49: AssertionError
-------------------------------------------------------------------------------------------- Captured stdout call ---------------------------------------------------------------------------------------------
ccc
{'image': 'image_path', 'image2': 'image_path2', 'value': 1, 'type': 2}
=========================================================================================== short test summary info ===========================================================================================
FAILED test/lib/test_function.py::test_from_yaml[param2] - assert 1 == 2
========================================================================================= 1 failed, 3 passed in 0.16s =========================================================================================

```