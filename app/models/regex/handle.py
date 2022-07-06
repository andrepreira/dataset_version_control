import importlib.util

def regex_from_file(dataset_name):
    file_path = f"/home/andre-pereira/projects/aisolutions/dataset_version_control/app/models/regex/pattern/{dataset_name}.py"
    spec = importlib.util.spec_from_file_location(dataset_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.regex()