import importlib.util

def regex_from_file(dataset_name):
    file_path = f"/home/andre-pereira/projects/aisolutions/dataset_version_control/backend/app/models/regex/pattern/{dataset_name}.py"
    spec = importlib.util.spec_from_file_location(dataset_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.regex()

licitacao_contrato = regex_from_file("licitacao_contrato")

vida_funcional = regex_from_file("vida_funcional")

if __name__ == "__main__":
    print("\n")
    
    print(licitacao_contrato)
    
    print("\n")

    print(vida_funcional)
    
    print("\n")
