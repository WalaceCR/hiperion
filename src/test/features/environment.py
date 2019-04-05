from src.test.util.Util import utilidades


def before_all(context):
    print("Executando antes de tudo")
    utilidades.start_browser()


def before_feature(context, feature):
    print("Executando antes da feature")


def before_scenario(context, scenario):
    print("Executando antes do cenário")


def after_scenario(context, scenario):
    print("Executando depois do cenário")


def after_feature(context, feature):
    print("Executando depois da feature")


def after_all(context):
    print("Executando depois de tudo")
    utilidades.finish_browser()
